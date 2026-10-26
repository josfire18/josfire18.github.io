"""
Builds the auto-managed cards in index.html's "Use it now" list.

A repo gets a card only if ALL of these are true:
  - you tagged it with the `lab` topic (the on/off switch)
  - it's public, owned by OWNER, and not a fork
  - GitHub Pages is turned on for it
Repos already linked by a hand-written card (href="/<repo>/" outside the auto block)
are skipped, so hand cards are never duplicated or touched.

Only the text between the AUTO markers is rewritten. Run with GITHUB_TOKEN set.
"""
import html
import json
import os
import re
import sys
import urllib.request

OWNER = os.environ.get("LAB_OWNER", "josfire18")
TOPIC = os.environ.get("LAB_TOPIC", "lab")
PAGE = os.environ.get("LAB_PAGE", "index.html")
START, END = "<!-- lab:auto:start -->", "<!-- lab:auto:end -->"


def api(path):
    req = urllib.request.Request("https://api.github.com" + path, headers={
        "Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}",
        "Accept": "application/vnd.github+json", "User-Agent": "lab-cards"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def title_of(name):
    return " ".join(w if w.isupper() else w.capitalize() for w in re.split(r"[-_]+", name))


def main():
    page = open(PAGE, encoding="utf-8").read()
    if START not in page or END not in page:
        sys.exit(f"{PAGE} is missing the {START} / {END} markers")
    before, rest = page.split(START, 1)
    _, after = rest.split(END, 1)
    hand = before + after                       # everything outside the auto block

    q = urllib.request.quote(f"topic:{TOPIC} user:{OWNER} fork:false is:public")
    repos = api(f"/search/repositories?q={q}&per_page=100").get("items", [])
    cards = []
    for r in sorted(repos, key=lambda r: r["name"].lower()):
        name = r["name"]
        if r["owner"]["login"] != OWNER or r["fork"] or r["private"] or not r.get("has_pages"):
            continue
        if f'href="/{name}/"' in hand:          # already has a hand-written card
            continue
        desc = html.escape(r.get("description") or "")
        cards.append(
            f'      <li><a href="/{html.escape(name)}/">\n'
            f'        <span class="path">/{html.escape(name)}</span>\n'
            f'        <b>{html.escape(title_of(name))}</b>\n'
            f'        <span>{desc}</span>\n'
            f'      </a></li>\n')

    block = START + "\n" + "".join(cards) + "      " + END
    new = before + block + after
    if new != page:
        open(PAGE, "w", encoding="utf-8").write(new)
        print(f"updated: {len(cards)} auto card(s)")
    else:
        print(f"no change ({len(cards)} auto card(s))")


if __name__ == "__main__":
    main()

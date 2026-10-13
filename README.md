# Lab

Hub page for small side projects, served by GitHub Pages at **https://lab.joeyrockwood.fyi**.

This is the account's user site (`josfire18.github.io`), so its custom domain also applies to every
project repo that has GitHub Pages turned on: repo `name` is served at `lab.joeyrockwood.fyi/name/`.

## Add a project

The page has two lists:

- **Use it now**: apps that run in the browser from this site. Anyone can click one and use it.
- **Projects**: things that aren't hosted here (bots, CLIs, things you run yourself). The card links to
  the GitHub repo, whose README is the project's page, and its label says what kind of thing it is.

For a **Use it now** app:

1. Create a public repo with an `index.html` at the root (plus a `.nojekyll` file).
2. Settings → Pages → Deploy from branch `main`, folder `/` (or `gh api -X POST repos/josfire18/NAME/pages -f "source[branch]=main" -f "source[path]=/"`).
3. Add a `<li>` for it under *Use it now* in `index.html` here.

For a **Project**: make the repo public, then add a `<li>` under *Projects* that links to the repo.

## Things to keep in mind

- All projects share one browser origin. Prefix every `localStorage`/IndexedDB key with the project
  name (e.g. `cube-solver-…`), and remember that a permission granted to one project (camera, etc.)
  applies to all of them.
- Static files only. Anything that needs a server (API keys, databases) goes on Netlify or Cloudflare
  under its own subdomain instead.

## DNS

One record at the DNS host: `CNAME lab → josfire18.github.io`.

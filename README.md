# Lab

Hub page for small side projects, served by GitHub Pages at **https://lab.joeyrockwood.fyi**.

This is the account's user site (`josfire18.github.io`), so its custom domain also applies to every
project repo that has GitHub Pages turned on: repo `name` is served at `lab.joeyrockwood.fyi/name/`.

## Add a project

1. Create a public repo with an `index.html` at the root (plus a `.nojekyll` file).
2. Settings → Pages → Deploy from branch `main`, folder `/` (or `gh api -X POST repos/josfire18/NAME/pages -f "source[branch]=main" -f "source[path]=/"`).
3. Add a `<li>` for it in `index.html` here.

## Things to keep in mind

- All projects share one browser origin. Prefix every `localStorage`/IndexedDB key with the project
  name (e.g. `cube-solver-…`), and remember that a permission granted to one project (camera, etc.)
  applies to all of them.
- Static files only. Anything that needs a server (API keys, databases) goes on Netlify or Cloudflare
  under its own subdomain instead.

## DNS

One record at the DNS host: `CNAME lab → josfire18.github.io`.

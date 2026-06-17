# 05 — Tech Stack & Tooling

Brochure + CMS + SEO + speed → static/SSG site.

## Tooling

| Tool | Choice |
| --- | --- |
| Editor | Cursor |
| VCS | Git + GitHub (private repo) |
| Package manager | pnpm (or npm) |
| Runtime | Node LTS |
| Design | Figma (optional, layout before code) |

## Framework

| Option | Notes |
| --- | --- |
| **Astro** (recommended) | Lightest, content-focused, best Core Web Vitals, ideal for brochure + blog |
| Next.js (App Router) | Bigger ecosystem; more than needed here |
| WordPress (alt) | TR-familiar admin, client-friendly, but heavier + security upkeep |

Recommendation: **Astro + Tailwind CSS**.

## CMS (client edits content)

| Option | Notes |
| --- | --- |
| Sanity | Free tier, structured, good editor UX |
| Decap CMS | Git-based, free, no DB |
| Strapi | Self-hosted, more ops |

Recommendation: **Sanity** (friendly admin) or **Decap** (zero-cost, Git-based).

## Content model (CMS schema sketch)

```
Lawyer      { name, title, sicilNo, baroNo, startDate, university, languages, photo, bio }
ActivityArea{ title (faaliyet alanı), slug, body }
Article     { title, slug, date, author(ref Lawyer), category, body }
LegalText   { key (kvkk|gizlilik|cerez), body }
SiteSettings{ buroName, address, phone, fax, email, kep, sicilNo }
```

## Forms

- Serverless function (host-provided) or form service
- Email delivery via Resend (or SMTP)
- Store consent flag + timestamp
- Spam protection (honeypot / hCaptcha)

## Styling

- Tailwind CSS
- Design tokens for palette + type

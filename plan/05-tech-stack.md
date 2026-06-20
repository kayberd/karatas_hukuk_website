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

**Astro + Tailwind CSS** (decided).

- Lightest, content-focused, best Core Web Vitals
- Ideal for brochure + blog
- Static/SSG output; islands only where interactivity needed (forms, menus)

## CMS (client edits content)

**Sanity** (decided).

- Free tier, structured content, friendly editor UX (Sanity Studio)
- Hosted dataset + GROQ queries; pull content into Astro at build time
- Use `@sanity/client` in Astro; webhook deploy on publish

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

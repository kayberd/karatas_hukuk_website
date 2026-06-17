# Karataş Hukuk — Website Blueprint

High-level blueprint for a single law-firm brochure website (Turkey). No code here — only plan.

## Scope (locked)

| Decision | Choice |
| --- | --- |
| Target | Single firm site (Karataş Hukuk) |
| Depth | Marketing/brochure (pages, articles, contact) |
| Language | Turkish only |
| Content editing | Non-technical client → needs CMS/admin panel |

## Guiding principle

The strongest constraint is **TBB Reklam Yasağı Yönetmeliği** (updated 09.08.2024), not design.
It dictates what content is allowed. Every feature is filtered through it first.
The site is an **information + trust** medium, NOT a lead-generation / advertising tool.

## Document index

| File | Topic |
| --- | --- |
| `01-legal-compliance.md` | TBB ban, Avukatlık Kanunu, KVKK, domain rules |
| `02-features.md` | Page inventory + feature list (build / don't build) |
| `03-content-strategy.md` | Sitemap, tone, content sourcing |
| `04-design-ux.md` | Visual identity, layout, accessibility, responsive |
| `05-tech-stack.md` | Tooling, framework, CMS, forms |
| `06-deploy-infra.md` | Domain (av.tr), hosting, DNS, SSL, CI/CD, backups |
| `07-seo-analytics.md` | Ban-safe SEO, schema, GBP, analytics |
| `08-ops-maintenance.md` | Monitoring, updates, content workflow, handover |

## Topic map

```
A. Legal / Compliance   -> 01
B. Strategy / Content   -> 03
C. Design / UX          -> 04
D. Tech / Tooling       -> 05
E. Infra / Deploy       -> 06
F. SEO / Performance    -> 07
G. Ops / Maintenance    -> 08
(Features span all)     -> 02
```

## Build order (suggested)

1. Lock legal content rules (`01`)
2. Finalize page inventory + content (`02`, `03`)
3. Design system (`04`)
4. Stack setup + CMS schema (`05`)
5. Build pages
6. Deploy on `av.tr` (`06`)
7. SEO + analytics wiring (`07`)
8. Handover + maintenance plan (`08`)

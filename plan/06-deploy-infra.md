# 06 — Deploy & Infrastructure

## Domain (critical)

- MUST be **`....av.tr`** (TBB rule, see `01`)
- Apply via nic.tr — av.tr requires lawyer/baro verification
- No `.com`/`.com.tr` as primary domain

## Hosting

| Option | Notes |
| --- | --- |
| Vercel | SSG-friendly, auto SSL, global CDN, free tier |
| Netlify | Similar, good for Astro + Decap |
| Cloudflare Pages | Fast CDN, free tier |

Any of these fit an SSG site. Pick one; document choice.

## Data residency (KVKK)

- Static content: no hard localization mandate
- Contact-form data: prefer storing in TR/EU; state location in aydınlatma metni

## DNS

- Point `av.tr` domain to host
- Configure apex + `www` redirect
- Set up email/KEP records separately if needed

## SSL

- Automatic via host (Let's Encrypt) — required (KVKK + trust)

## CI/CD

- Git push → auto build + deploy
- Branch previews for review before publish

## Backups

- Git = source backup
- CMS content: scheduled export (Sanity dataset export / Git history for Decap)
- Form submissions: backed up where stored

## Pre-launch infra checklist

- [ ] av.tr domain live
- [ ] SSL active
- [ ] DNS + redirects correct
- [ ] CI/CD deploying
- [ ] Backups configured
- [ ] Form data storage location documented

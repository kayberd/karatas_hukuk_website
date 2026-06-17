# 02 — Features & Page Inventory

Every feature filtered through `01-legal-compliance.md`.

## Core pages

| Page | Purpose | Notes |
| --- | --- | --- |
| Anasayfa | Entry, info-first | Minimal, no ad-style CTAs |
| Hakkımızda | Firm intro | Allowed fields only |
| Avukat Profilleri | Lawyer cards + detail | Repeatable; only allowed fields |
| Faaliyet Alanları (hub) | Tüm alanlar grid | Hub → tek tek alan sayfalarına link |
| Faaliyet Alanı (detay) | One page per area | Aile, ceza, ticaret, gayrimenkul, iş, icra, miras, tazminat, KVKK... → "faaliyet alanı" |
| Bilgi Bankası (hub) | Makale listesi | Anonymized, CMS-driven |
| Makale Kategorisi (arşiv) | Konu bazlı arşiv | ceza, aile, tazminat, genel-hukuk, hesaplama-araclari |
| Makale (detay) | Tek makale | title, date, lawyer-author, category |
| Hesaplama Araçları (ops.) | Bilgilendirme aracı | Disclaimer şart, CTA yok — bkz. priority "Could" |
| İletişim | Address, map, phone, form | KVKK consent required |
| KVKK Aydınlatma | Legal text | Linked from footer + form |
| Gizlilik / Çerez Politikası | Legal text | Linked from footer + cookie banner |

## Functional features

- CMS-managed articles + activity-area pages
- Article **categories** → category archive pages (CMS-driven taxonomy)
- Faaliyet alanları hub (grid) + repeatable area detail pages
- Repeatable lawyer profiles (name, title, sicil, university, languages, photo)
- Contact form: KVKK consent checkbox (unchecked default), spam protection, email/DB delivery
- Schema markup: `Attorney`, `LegalService`, `FAQPage`
- Cookie consent banner
- Article search/filter + category filter (optional)
- Map embed (office location)
- Responsive nav + footer with required identity info

## Explicitly NOT building

- Testimonials / "müvekkil yorumları"
- Case-result / "kazanılan davalar" showcase
- "Referanslar" section
- Live-chat lead capture
- Paid-ad landing funnels
- "Ücretsiz danışma" / discount CTAs
- Any banned-phrase marketing copy
- E-commerce (mağaza / sepet / ödeme) — referans sitede var, hukuk bürosu için dışarıda
- Author archive + theme-template URLs (header/footer/mega-menu) — sadece içerik route'ları

## Feature priority

| Priority | Items |
| --- | --- |
| Must (MVP) | Core pages, faaliyet hub + area pages, lawyer profiles, contact form + KVKK, cookie banner, articles |
| Should | Schema markup, map embed, article filter, article categories + archive pages |
| Could | On-site search, dark mode, tags, hesaplama araçları |
| Won't | Anything in "NOT building" list |

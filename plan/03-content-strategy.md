# 03 — Content Strategy

## Sitemap

Structure informed by a comparable Turkish law-firm site (Yoast sitemap pattern: pages + posts + categories), but trimmed to stay TBB-compliant. No shop/cart/checkout, no author archive, no theme-template URLs.

```
/
├── hakkimizda
├── avukatlar
│   └── [avukat-slug]
├── faaliyet-alanlari                     (hub: tüm alanlar grid)
│   └── [alan-slug]
│        aile · ceza · ticaret · gayrimenkul · is · icra-iflas
│        miras · idare · vergi · tuketici · sirketler · kvkk
│        tazminat · kira · sigorta · bilisim · fikri-mulkiyet ...
├── bilgi-bankasi                         (makale hub'ı)
│   ├── [kategori-slug]                    (ceza, aile, tazminat, genel-hukuk, hesaplama-araclari)
│   └── [makale-slug]                      (ör. tck-220-orgut-kurma, kasten-oldurme-sucu)
├── araclar                               (opsiyonel — bkz. not)
│   └── [arac-slug]                        (vekalet-ucreti, infaz-hesaplama, tazminat-hesaplama)
├── iletisim
├── kvkk-aydinlatma
├── gizlilik
└── cerez-politikasi
```

### Route notları (referans siteden çıkarım)

- **Faaliyet alanları** geniş tutuluyor — referans sitedeki ~25 hukuk dalı yerine firmanın gerçekten çalıştığı alanlar seçilir. Her alan ayrı sayfa + hub grid.
- **Bilgi bankası** referanstaki "blog + post" yapısını karşılar; makaleler **kategoriye** ayrılır (ceza, aile, tazminat, genel-hukuk). Kategori arşiv sayfaları SEO için ayrı route.
- Makale slug'ları konu-bazlı (suç/dava türü), tarih içermez.
- **Araçlar** (hesaplama): referans sitede var ("infaz hesaplama", "vekalet ücreti", "tazminat hesaplama"). Bilgilendirme aracı olarak TBB-uyumlu; reklam/CTA içermemeli. Opsiyonel — `02` "Could" önceliğinde.
- **Dahil EDİLMEYEN** referans route'ları: `magaza`, `sepet`, `odeme` (e-ticaret), `author/*`, `header/*`, `footer/*`, `ct-mega-menu/*` (tema şablonları), `404-error-page` (özel sayfa değil).

## Tone of voice

- Plain Turkish, jargon minimized ("anlaşmazlık" over "uyuşmazlık" where natural)
- Explain legal processes step by step
- No banned phrases (see `01`)
- Message frame: deneyim + faaliyet alanı + sürece dayalı yaklaşım
- FAQ-style: answer the questions clients actually ask

## Content sourcing

| Content | Source | Reviewer |
| --- | --- | --- |
| Lawyer profiles | Firm-provided official data | Lawyer |
| Activity-area pages | Drafted, lawyer-reviewed | Lawyer (compliance) |
| Articles (+ kategoriler) | Lawyer-authored / reviewed | Lawyer (must be anonymized) |
| Tools / hesaplama araçları | Public mevzuat formülleri | Lawyer (disclaimer şart) |
| Legal texts (KVKK/cookie) | Template + lawyer review | Lawyer |

## Article rules

- No client names, no identifying case detail
- Anonymized examples only
- No "uzman" claims; informational framing
- Each article: title, date, author (lawyer), body, **category** (ceza / aile / tazminat / genel-hukuk / hesaplama-araclari)
- Tools (hesaplama): yalnız bilgilendirme; "sonuç bağlayıcı değildir, avukata danışın" disclaimer'ı zorunlu, CTA yok

## Visual content

- Lawyer portraits (professional)
- Office photos
- Restrained iconography (terazi, kanun kitabı) — no flashy/ad-style graphics

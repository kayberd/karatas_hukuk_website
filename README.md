# Karataş Hukuk — Web Sitesi

TBB Reklam Yasağı Yönetmeliği'ne uygun, bilgi + güven odaklı hukuk bürosu broşür sitesi.
Astro + Tailwind CSS, statik (SSG) çıktı. İçerik Markdown content collections ile yönetilir.

## Teknoloji

- **Astro 5** (SSG) + **Tailwind CSS 4**
- İçerik: `src/content/` (Markdown + content collections)
- SEO: `@astrojs/sitemap`, JSON-LD şema, canonical
- Analitik: Plausible (cookieless, opsiyonel)

## Geliştirme

```bash
npm install
npm run dev        # http://localhost:4321
npm run build      # statik çıktı -> dist/
npm run preview
```

`.env` için `.env.example` dosyasını kopyalayın.

## İçerik yapısı

| Klasör | İçerik |
| --- | --- |
| `src/content/lawyers/` | Avukat profilleri (yalnızca mevzuata uygun alanlar) |
| `src/content/areas/` | Faaliyet alanları |
| `src/content/articles/` | Bilgi bankası yazıları (kategori + opsiyonel FAQ) |
| `src/content/legal/` | KVKK / gizlilik / çerez metinleri |
| `src/config/site.ts` | Büro bilgileri, menü, kategori etiketleri |

## Sayfalar

`/`, `/hakkimizda`, `/avukatlar` + `/avukatlar/[slug]`,
`/faaliyet-alanlari` + `/faaliyet-alanlari/[slug]`,
`/bilgi-bankasi` + `/bilgi-bankasi/[slug]` + `/bilgi-bankasi/kategori/[category]`,
`/iletisim`, `/kvkk-aydinlatma`, `/gizlilik`, `/cerez-politikasi`, `404`.

## Uyum (kritik)

- Yalnızca mevzuatın izin verdiği alanlar yayımlanır (bkz. `plan/01-legal-compliance.md`).
- Yasaklı ifadeler kullanılmaz ("en iyi", "uzman", "garanti", "ücretsiz danışma" vb.).
- Referans / müvekkil yorumu / dava sonucu yer almaz.
- Yayın domaini **`av.tr`** olmalıdır.
- İletişim formunda KVKK açık rıza onay kutusu (varsayılan işaretsiz) bulunur.

## Dağıtım

Vercel / Netlify / Cloudflare Pages (SSG). Git push → otomatik build + deploy.
İletişim formu için bir serverless fonksiyon veya form servisi (`PUBLIC_FORM_ENDPOINT`) bağlanmalıdır.

> İleride istemci tarafı içerik düzenleme için Sanity CMS entegre edilebilir
> (bkz. `plan/05-tech-stack.md`); mevcut sürüm Markdown tabanlıdır.

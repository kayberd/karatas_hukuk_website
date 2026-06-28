# Doğrulama Listesi — Karataş Hukuk Web Sitesi

Manuel sayfa sayfa kontrol. Her satır işaretle. `npm run dev` (http://localhost:4321) veya `npm run build && npm run preview` üzerinde test et.

> Local base: `http://localhost:4321` · Prod base: `https://rusenkaratas.av.tr`
> Aşağıdaki linkler local içindir, tıkla → kontrol et. Sitemap (`sitemap.xml`) ile birebir eşleşir: **27 URL** (+ `/404` sitemap'te yok).

---

## 0. Hazırlık / Global

- [ ] `npm install` hatasız
- [ ] `npm run dev` başlıyor, konsol temiz (uyarı/hata yok)
- [ ] `npm run build` hatasız, `dist/` üretiliyor
- [ ] `npm run preview` çalışıyor
- [ ] `.env` doğru dolduruldu (`.env.example` baz)
- [ ] `PUBLIC_FORM_ENDPOINT` set (iletişim formu)
- [ ] `sitemap-index.xml` üretiliyor + tüm sayfaları içeriyor
- [ ] `robots.txt` doğru
- [ ] `favicon` görünüyor (tüm sekmeler)
- [ ] 404 sayfası bilinmeyen URL'de geliyor (örn `/asdf`)

---

## 0.5. Sitemap Çapraz Kontrol (27 URL)

Sitemap'teki her URL tıkla → 200 dönüyor mu işaretle. Hızlı tarama bölümü.

| # | URL | OK |
| --- | --- | --- |
| 1 | http://localhost:4321/ | [ ] |
| 2 | http://localhost:4321/hakkimizda | [ ] |
| 3 | http://localhost:4321/iletisim | [ ] |
| 4 | http://localhost:4321/avukatlar | [ ] |
| 5 | http://localhost:4321/avukatlar/rusen-karatas | [ ] |
| 6 | http://localhost:4321/faaliyet-alanlari | [ ] |
| 7 | http://localhost:4321/faaliyet-alanlari/aile | [ ] |
| 8 | http://localhost:4321/faaliyet-alanlari/akademik | [ ] |
| 9 | http://localhost:4321/faaliyet-alanlari/ceza | [ ] |
| 10 | http://localhost:4321/faaliyet-alanlari/idari-yargi | [ ] |
| 11 | http://localhost:4321/faaliyet-alanlari/is | [ ] |
| 12 | http://localhost:4321/faaliyet-alanlari/tasinmaz | [ ] |
| 13 | http://localhost:4321/faaliyet-alanlari/yabancilar | [ ] |
| 14 | http://localhost:4321/blog | [ ] |
| 15 | http://localhost:4321/blog/anlasmali-bosanma-sureci | [ ] |
| 16 | http://localhost:4321/blog/pomem-saglik-raporu-sureci | [ ] |
| 17 | http://localhost:4321/blog/sorusturma-asamasinda-supheli-haklari | [ ] |
| 18 | http://localhost:4321/blog/trafik-kazasi-tazminat | [ ] |
| 19 | http://localhost:4321/blog/vekaletname-turleri | [ ] |
| 20 | http://localhost:4321/blog/kategori/aile | [ ] |
| 21 | http://localhost:4321/blog/kategori/ceza | [ ] |
| 22 | http://localhost:4321/blog/kategori/genel-hukuk | [ ] |
| 23 | http://localhost:4321/blog/kategori/idari-yargi | [ ] |
| 24 | http://localhost:4321/blog/kategori/tazminat | [ ] |
| 25 | http://localhost:4321/kvkk-aydinlatma | [ ] |
| 26 | http://localhost:4321/gizlilik | [ ] |
| 27 | http://localhost:4321/cerez-politikasi | [ ] |
| — | http://localhost:4321/asdf → 404 sayfası (sitemap'te yok) | [ ] |

---

## 1. Her Sayfada Ortak Kontroller (her sayfa için tekrar et)

Aşağıdaki blok HER sayfada geçerli:

- [ ] Sayfa 200 dönüyor, beyaz ekran yok
- [ ] `<title>` doğru + sayfaya özel
- [ ] Meta description dolu
- [ ] Canonical URL doğru (`av.tr` domain)
- [ ] OpenGraph / JSON-LD şema var, geçerli ([Rich Results Test](https://search.google.com/test/rich-results))
- [ ] Header menü görünüyor, tüm linkler çalışıyor
- [ ] Aktif menü öğesi vurgulanıyor
- [ ] Footer görünüyor, yasal linkler çalışıyor
- [ ] Logo tıkla → anasayfa
- [ ] Mobil (≤375px) bozulma yok, hamburger menü açılıp kapanıyor
- [ ] Tablet (768px) düzgün
- [ ] Desktop (≥1280px) düzgün
- [ ] Görseller yükleniyor, alt text var, kayma (CLS) yok
- [ ] Konsolda JS hatası yok
- [ ] Klavye ile gezinilebiliyor (Tab focus görünür)
- [ ] Çerez banner ilk ziyarette çıkıyor, kabul/ret çalışıyor, tekrar çıkmıyor

---

## 2. Statik Sayfalar

### `/` Anasayfa → http://localhost:4321/
- [ ] Hero metin + CTA doğru
- [ ] Faaliyet alanları önizleme kartları → doğru slug'a gidiyor
- [ ] Öne çıkan yazılar/bölümler doğru
- [ ] Tüm CTA butonları doğru hedefe gidiyor
- [ ] Ortak kontroller (bölüm 1) tamam

### `/hakkimizda` → http://localhost:4321/hakkimizda
- [ ] Büro bilgisi doğru (isim, baro, adres)
- [ ] Mevzuata aykırı ifade yok ("en iyi", "uzman", "garanti" vb.)
- [ ] Ortak kontroller tamam

### `/iletisim` → http://localhost:4321/iletisim
- [ ] Adres doğru: Kocatepe Mah. Mithatpaşa Cad. Ahenk Apt. No: 62/8, Çankaya/Ankara
- [ ] Telefon doğru: +90 507 533 82 02, tıkla→arama (`tel:`)
- [ ] E-posta doğru: avrusenkaratas@gmail.com, tıkla→`mailto:`
- [ ] Google Maps embed doğru konum gösteriyor
- [ ] Form alanları çalışıyor (ad, e-posta, mesaj)
- [ ] KVKK açık rıza kutusu VAR + varsayılan İŞARETSİZ
- [ ] Kutu işaretsizken gönderim engelleniyor
- [ ] Form gönderimi `PUBLIC_FORM_ENDPOINT`'e ulaşıyor
- [ ] Başarı + hata mesajı gösteriliyor
- [ ] Boş/geçersiz alan validasyonu çalışıyor
- [ ] Ortak kontroller tamam

---

## 3. Avukatlar

### `/avukatlar` (liste) → http://localhost:4321/avukatlar
- [ ] Avukat kartı listeleniyor
- [ ] Kart → doğru profil slug'ına gidiyor
- [ ] Ortak kontroller tamam

### `/avukatlar/rusen-karatas` (profil) → http://localhost:4321/avukatlar/rusen-karatas
- [ ] İsim, ünvan doğru
- [ ] Yalnız mevzuata uygun alanlar (sicil/baro no, üniversite, dil)
- [ ] Fotoğraf yükleniyor (varsa)
- [ ] Yasaklı içerik yok (referans, dava sonucu, yorum)
- [ ] Ortak kontroller tamam

---

## 4. Faaliyet Alanları

### `/faaliyet-alanlari` (liste) → http://localhost:4321/faaliyet-alanlari
- [ ] Tüm alan kartları görünüyor (7 adet)
- [ ] Her kart doğru slug'a gidiyor
- [ ] İkonlar yükleniyor
- [ ] Ortak kontroller tamam

### Alan detayları — her biri açılıyor, içerik+başlık doğru:
- [ ] Akademik Hukuk ve Danışmanlık → http://localhost:4321/faaliyet-alanlari/akademik
- [ ] Yabancılar Hukuku → http://localhost:4321/faaliyet-alanlari/yabancilar
- [ ] İdari Yargı → http://localhost:4321/faaliyet-alanlari/idari-yargi
- [ ] Aile Hukuku → http://localhost:4321/faaliyet-alanlari/aile
- [ ] Ceza Hukuku → http://localhost:4321/faaliyet-alanlari/ceza
- [ ] İş Hukuku → http://localhost:4321/faaliyet-alanlari/is
- [ ] Taşınmaz Hukuku → http://localhost:4321/faaliyet-alanlari/tasinmaz
- [ ] Geçersiz slug → http://localhost:4321/faaliyet-alanlari/xxx → 404

---

## 5. Blog

### `/blog` (liste) → http://localhost:4321/blog
- [ ] Tüm yazı kartları görünüyor (5 adet)
- [ ] Tarih, kategori, başlık doğru
- [ ] Kart → doğru yazı slug'ına gidiyor
- [ ] Kategori filtre/etiket linkleri çalışıyor
- [ ] Ortak kontroller tamam

### Yazı detayları — açılıyor, içerik+FAQ+tarih+yazar doğru:
- [ ] Trafik kazası tazminat (tazminat) → http://localhost:4321/blog/trafik-kazasi-tazminat
- [ ] Soruşturmada şüpheli hakları (ceza) → http://localhost:4321/blog/sorusturma-asamasinda-supheli-haklari
- [ ] Anlaşmalı boşanma süreci (aile) → http://localhost:4321/blog/anlasmali-bosanma-sureci
- [ ] POMEM sağlık raporu (idari-yargi) → http://localhost:4321/blog/pomem-saglik-raporu-sureci
- [ ] Vekaletname türleri (genel-hukuk) → http://localhost:4321/blog/vekaletname-turleri
- [ ] FAQ varsa açılır/şema (FAQPage JSON-LD) doğru
- [ ] Geçersiz slug → http://localhost:4321/blog/xxx → 404

### Kategori sayfaları — açılıyor, sadece o kategori yazıları:
- [ ] Tazminat Hukuku → http://localhost:4321/blog/kategori/tazminat
- [ ] Ceza Hukuku → http://localhost:4321/blog/kategori/ceza
- [ ] Aile Hukuku → http://localhost:4321/blog/kategori/aile
- [ ] İdari Yargı → http://localhost:4321/blog/kategori/idari-yargi
- [ ] Genel Hukuk → http://localhost:4321/blog/kategori/genel-hukuk
- [ ] Genel Hukuk tek yazı içeriyor (doğru filtre)
- [ ] Geçersiz kategori → http://localhost:4321/blog/kategori/xxx → 404

---

## 6. Yasal Sayfalar

- [ ] KVKK Aydınlatma — metin tam, tarih doğru → http://localhost:4321/kvkk-aydinlatma
- [ ] Gizlilik — metin tam → http://localhost:4321/gizlilik
- [ ] Çerez Politikası — metin tam, banner ile tutarlı → http://localhost:4321/cerez-politikasi
- [ ] Footer linkleri bu 3 sayfaya doğru gidiyor

---

## 7. Mevzuat Uyum (TBB Reklam Yasağı) — KRİTİK

Tüm site genelinde kontrol:

- [ ] Yasaklı ifade YOK: "en iyi", "uzman", "garanti", "ücretsiz danışma", "%100", "kazandırırız"
- [ ] Referans / müvekkil yorumu YOK
- [ ] Dava sonucu / başarı oranı YOK
- [ ] Fiyat / ücret reklamı YOK
- [ ] Sadece izin verilen avukat bilgileri yayında
- [ ] İletişim formu KVKK rıza kutusu varsayılan işaretsiz
- [ ] Domain `av.tr`

---

## 8. SEO & Performans (opsiyonel ama önerilen)

- [ ] Lighthouse — her ana sayfa Performance/SEO/Best-Practices/Accessibility yeşil
- [ ] Tüm sayfalarda tekil `<h1>`
- [ ] Kırık link yok (tüm iç linkler test)
- [ ] Görsel boyut optimize (lazyload)
- [ ] Plausible analitik (opsiyonel) yükleniyor, çerezsiz
- [ ] `sitemap` tüm rotaları içeriyor

---

## 9. Dağıtım Sonrası (prod)

- [ ] `https://rusenkaratas.av.tr` açılıyor, HTTPS geçerli
- [ ] `www` → ana domain yönleniyor
- [ ] Git push → otomatik build + deploy çalışıyor
- [ ] Prod'da iletişim formu gerçek gönderim test
- [ ] Tüm sayfalar prod URL ile tekrar hızlı tarama (bölüm 2-6)

---

### Sayfa Sayısı Özeti (sitemap = 27 URL)
- Statik (sitemap): 9 (`/`, hakkimizda, iletisim, avukatlar, faaliyet-alanlari, blog, kvkk-aydinlatma, gizlilik, cerez-politikasi)
- Avukat profili: 1
- Faaliyet alanı detay: 7
- Blog yazı: 5
- Kategori: 5
- **Sitemap toplam: 27** (+ `/404` sitemap dışı)

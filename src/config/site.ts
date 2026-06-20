export const site = {
  buroName: "Karataş Hukuk Bürosu",
  shortName: "Karataş Hukuk",
  legalIdentity: "Av. ... Karataş Hukuk Bürosu",
  baro: "Ankara Barosu",
  sicilNo: "00000",
  address: "Örnek Mah. Örnek Cad. No: 0/0, Çankaya / Ankara",
  phone: "+90 312 000 00 00",
  phoneHref: "+903120000000",
  fax: "+90 312 000 00 01",
  email: "info@karatashukuk.av.tr",
  kep: "karatashukuk@hs01.kep.tr",
  mapEmbed:
    "https://www.google.com/maps?q=Ankara+Adliyesi&output=embed",
  url: "https://karatashukuk.av.tr",
} as const;

export const nav = [
  { label: "Anasayfa", href: "/" },
  { label: "Hakkımızda", href: "/hakkimizda" },
  { label: "Avukatlar", href: "/avukatlar" },
  { label: "Faaliyet Alanları", href: "/faaliyet-alanlari" },
  { label: "Bilgi Bankası", href: "/bilgi-bankasi" },
  { label: "İletişim", href: "/iletisim" },
] as const;

export const categoryLabels: Record<string, string> = {
  ceza: "Ceza Hukuku",
  aile: "Aile Hukuku",
  tazminat: "Tazminat Hukuku",
  "genel-hukuk": "Genel Hukuk",
};

export const footerLegalLinks = [
  { label: "KVKK Aydınlatma Metni", href: "/kvkk-aydinlatma" },
  { label: "Gizlilik Politikası", href: "/gizlilik" },
  { label: "Çerez Politikası", href: "/cerez-politikasi" },
] as const;

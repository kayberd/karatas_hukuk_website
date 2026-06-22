export const site = {
  buroName: "Karataş Hukuk ve Danışmanlık",
  shortName: "Karataş Hukuk",
  legalIdentity: "Av. M. Ruşen Karataş",
  baro: "Ankara Barosu",
  address:
    "Kocatepe Mah. Mithatpaşa Cad. Ahenk Apt. No: 62/8, Çankaya / Ankara",
  phone: "+90 507 533 82 02",
  phoneHref: "+905075338202",
  email: "avrusenkaratas@gmail.com",
  mapEmbed:
    "https://www.google.com/maps?q=Kocatepe+Mah.+Mithatpa%C5%9Fa+Cad.+%C3%87ankaya+Ankara&output=embed",
  url: "https://rusenkaratas.av.tr",
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
  "idari-yargi": "İdari Yargı",
  "genel-hukuk": "Genel Hukuk",
};

export const footerLegalLinks = [
  { label: "KVKK Aydınlatma Metni", href: "/kvkk-aydinlatma" },
  { label: "Gizlilik Politikası", href: "/gizlilik" },
  { label: "Çerez Politikası", href: "/cerez-politikasi" },
] as const;

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
    "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3059.9954069934533!2d32.85680577727907!3d39.919118985773515!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x14d34f077b32ee37%3A0x1f1446ae8005903b!2zS2FyYXRhxZ8gSHVrdWsgdmUgRGFuxLHFn21hbmzEsWsgfCBBdnVrYXQgTS4gUnXFn2VuIEtBUkFUQcWe!5e0!3m2!1str!2sus!4v1782634539474!5m2!1str!2sus",
  mapLink:
    "https://www.google.com/maps/search/?api=1&query=39.9191149%2C32.8593807&query_place_id=ChIJN-4ye3dP01ARO5AAgK5GFB8",
  url: "https://rusenkaratas.av.tr",
} as const;

export const nav = [
  { label: "Anasayfa", href: "/" },
  { label: "Hakkımızda", href: "/hakkimizda" },
  { label: "Avukatlar", href: "/avukatlar" },
  { label: "Faaliyet Alanları", href: "/faaliyet-alanlari" },
  { label: "Blog", href: "/blog" },
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

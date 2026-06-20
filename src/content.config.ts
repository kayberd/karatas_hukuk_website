import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";

const lawyers = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/lawyers" }),
  schema: ({ image }) =>
    z.object({
      name: z.string(),
      title: z.string().optional(),
      slug: z.string(),
      sicilNo: z.string().optional(),
      baroNo: z.string().optional(),
      baro: z.string().optional(),
      startDate: z.string().optional(),
      university: z.string().optional(),
      languages: z.array(z.string()).default([]),
      photo: image().optional(),
      order: z.number().default(99),
    }),
});

const areas = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/areas" }),
  schema: z.object({
    title: z.string(),
    slug: z.string(),
    summary: z.string(),
    icon: z.string().default("scale"),
    order: z.number().default(99),
  }),
});

const articleCategories = [
  "ceza",
  "aile",
  "tazminat",
  "genel-hukuk",
] as const;

const articles = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/articles" }),
  schema: z.object({
    title: z.string(),
    slug: z.string(),
    description: z.string(),
    date: z.coerce.date(),
    author: z.string(),
    category: z.enum(articleCategories),
    faq: z
      .array(z.object({ q: z.string(), a: z.string() }))
      .default([]),
  }),
});

const legal = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/legal" }),
  schema: z.object({
    title: z.string(),
    key: z.enum(["kvkk-aydinlatma", "gizlilik", "cerez-politikasi"]),
    updated: z.coerce.date().optional(),
  }),
});

export const collections = { lawyers, areas, articles, legal };
export { articleCategories };

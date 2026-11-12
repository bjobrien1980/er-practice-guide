import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";

const modules = defineCollection({
  loader: glob({ pattern: "**/*.mdx", base: "./src/content/modules" }),
  schema: z.object({
    id: z.number(),
    slug: z.string(),
    title: z.string(),
    tier: z.number().min(1).max(4),
    provisions: z.array(z.string()),
    version: z.string(),
    last_updated: z.string(),
    law_current_as_at: z.string().nullable(),
    law_sources: z.array(z.string()),
    reading_minutes: z.number(),
    related: z.array(z.number()),
  }),
});

export const collections = { modules };

import { getCollection } from "astro:content";

export type NavModule = { id: number; title: string; slug: string };
export type NavTier = { title: string; modules: NavModule[] };

// Tier names are the only navigation text kept here. Module ids, titles and slugs come from
// each module's own front matter, so the sidebar, home page and page heading cannot drift apart.
const TIER_TITLES = [
  "Tier 1: Foundations",
  "Tier 2: The s.387 test",
  "Tier 3: Situations",
  "Tier 4: Running a matter",
  "Tier 5: General protections in depth",
];

export async function getTiers(): Promise<NavTier[]> {
  const modules = (await getCollection("modules")).map((m) => m.data).sort((a, b) => a.id - b.id);
  return TIER_TITLES.map((title, i) => ({
    title,
    modules: modules
      .filter((m) => m.tier === i + 1)
      .map(({ id, title, slug }) => ({ id, title, slug })),
  }));
}

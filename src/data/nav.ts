export type NavModule = { id: number; title: string; slug?: string };
export type NavTier = { title: string; modules: NavModule[] };

export const TIERS: NavTier[] = [
  {
    title: "Tier 1: Foundations",
    modules: [
      { id: 1, title: "Who can claim", slug: "who-can-claim" },
      { id: 2, title: "General protections", slug: "general-protections" },
      { id: 3, title: "Agreements and policies", slug: "agreements-and-policies" },
      { id: 4, title: "Notice and summary dismissal", slug: "notice-and-summary-dismissal" },
    ],
  },
  {
    title: "Tier 2: The s.387 test",
    modules: [
      { id: 5, title: "Valid reason", slug: "valid-reason" },
      { id: 6, title: "Notification and response", slug: "notification-and-response" },
      { id: 7, title: "Support persons", slug: "support-persons" },
      { id: 8, title: "Performance warnings", slug: "performance-warnings" },
      { id: 9, title: "Other relevant matters", slug: "other-relevant-matters" },
    ],
  },
  {
    title: "Tier 3: Situations",
    modules: [
      { id: 10, title: "Drug and alcohol", slug: "drug-and-alcohol" },
      { id: 11, title: "Safety breaches", slug: "safety-breaches" },
      { id: 12, title: "Bullying, harassment and sexual harassment", slug: "bullying-and-harassment" },
      { id: 13, title: "Medical capacity and inherent requirements", slug: "medical-capacity" },
      { id: 14, title: "Absenteeism and abandonment", slug: "absenteeism-and-abandonment" },
      { id: 15, title: "Social media and out-of-hours conduct", slug: "social-media-and-out-of-hours" },
      { id: 16, title: "Dishonesty and falsified records", slug: "dishonesty-and-falsified-records" },
    ],
  },
  {
    title: "Tier 4: Running a matter",
    modules: [
      { id: 17, title: "Investigations", slug: "investigations" },
      { id: 18, title: "Stand-down and suspension", slug: "stand-down-and-suspension" },
      { id: 19, title: "Records that stand up", slug: "records-that-stand-up" },
      { id: 20, title: "Commission proceedings", slug: "commission-proceedings" },
      { id: 21, title: "Remedies and risk", slug: "remedies-and-risk" },
      { id: 22, title: "Escalation", slug: "escalation" },
    ],
  },
];

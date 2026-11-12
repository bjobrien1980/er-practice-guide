export type GlossaryTerm = {
  id: string;
  term: string;
  definition: string;
  /** Regular-expression sources for the wording that should link to this entry from module text. */
  match?: string[];
};

export const GLOSSARY: GlossaryTerm[] = [
  { id: "adverse-action", term: "Adverse action", definition: "Action by an employer that disadvantages an employee, including dismissal, for a prohibited reason under the general protections provisions.", match: ["adverse action"] },
  { id: "workplace-right", term: "Workplace right", definition: "A right or entitlement arising under a workplace law, instrument or process, or the ability to make a complaint or inquiry about employment.", match: ["workplace rights?"] },
  { id: "reverse-onus", term: "Reverse onus", definition: "An evidentiary rule in general protections proceedings. Once the relevant statutory facts are in issue, the decision-maker may presume the prohibited reason unless the employer proves otherwise.", match: ["reverse onus"] },
  { id: "minimum-employment-period", term: "Minimum employment period", definition: "The statutory period relevant to eligibility for an unfair dismissal application. It is not the same question as whether a dismissal was fair.", match: ["minimum employment period"] },
  { id: "high-income-threshold", term: "High-income threshold", definition: "A statutory threshold that may affect unfair dismissal coverage, subject to the applicable award or enterprise agreement and the law current at the relevant time.", match: ["high[- ]income threshold"] },
  { id: "genuine-redundancy", term: "Genuine redundancy", definition: "A statutory concept with specific elements. Calling a decision a restructure does not itself establish genuine redundancy.", match: ["genuine redundancy"] },
  { id: "serious-misconduct", term: "Serious misconduct", definition: "Conduct that may justify summary dismissal under the applicable law, instrument, contract or policy. The label does not replace analysis of the facts and process.", match: ["serious misconduct"] },
  { id: "summary-dismissal", term: "Summary dismissal", definition: "Dismissal without notice where the employer relies on a lawful basis to do so. The source of the power and the facts supporting it must be checked.", match: ["summary dismissals?", "summarily dismiss(?:ed|al)?"] },
  { id: "support-person", term: "Support person", definition: "A person who attends a disciplinary or dismissal meeting to provide support. Their role and the employee's opportunity to have one may also be governed by an instrument, contract, policy or established process.", match: ["support persons?"] },
  { id: "representation", term: "Representation", definition: "Advocacy or assistance in a workplace process or proceeding. Whether a person may be represented, and by whom, depends on the applicable source and forum." },
  { id: "briginshaw", term: "Briginshaw considerations", definition: "The practical caution that serious allegations require evidence commensurate with their gravity before a fact is found on the balance of probabilities.", match: ["Briginshaw"] },
  { id: "reinstatement", term: "Reinstatement", definition: "Returning an unfairly dismissed employee to employment. It has statutory primacy among remedies, but whether it is appropriate depends on the facts.", match: ["reinstatement"] },
  { id: "mitigation", term: "Mitigation", definition: "Steps taken by a dismissed employee to reduce loss, usually relevant to compensation. It does not retrospectively make a dismissal fair.", match: ["mitigation"] },
  { id: "repudiation", term: "Repudiation", definition: "Conduct showing an intention not to be bound by an employment relationship or a fundamental term. The question is objective and fact-dependent.", match: ["repudiation"] },
  { id: "pip", term: "PIP", definition: "Performance improvement plan. A PIP is a possible management tool, not a universal legal precondition to dismissal.", match: ["PIPs?", "performance improvement plans?"] },
  { id: "ea", term: "EA", definition: "Enterprise agreement." },
  { id: "fwa", term: "FWA", definition: "Fair Work Act 2009 (Cth)." },
  { id: "fwc", term: "FWC", definition: "Fair Work Commission." },
];

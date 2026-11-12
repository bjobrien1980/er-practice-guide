import { GLOSSARY } from "../data/glossary";

// Links the first use of each glossary term in a module's rendered HTML to its glossary entry.
// Works on the HTML string so it is independent of the Markdown processor in use.

const VOID = new Set(["area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"]);
// Text inside these is left alone: existing links, headings, form controls, citations and tools.
const SKIP_TAGS = new Set(["a", "h1", "h2", "h3", "h4", "button", "label", "textarea", "script", "style", "code", "summary"]);
const SKIP_CLASSES = /\b(cite|statute|tag|tool|telemetry|scenario-note)\b/;

const escapeAttr = (s: string) => s.replace(/&/g, "&amp;").replace(/"/g, "&quot;").replace(/</g, "&lt;");

export function linkGlossaryTerms(html: string): string {
  const pending = GLOSSARY.filter((g) => g.match?.length).map((g) => ({
    entry: g,
    pattern: new RegExp(`(?<![\\w-])(?:${g.match!.join("|")})(?![\\w-])`, "i"),
  }));
  const stack: boolean[] = []; // one entry per open element: true if its text must be skipped
  let skipDepth = 0;

  return html
    .split(/(<(?:"[^"]*"|'[^']*'|[^>"'])+>)/)
    .map((part) => {
      if (part.startsWith("<")) {
        const tag = /^<(\/?)([a-zA-Z][\w-]*)/.exec(part);
        if (!tag) return part; // comment or doctype
        const name = tag[2].toLowerCase();
        if (tag[1]) {
          if (stack.pop()) skipDepth--;
        } else if (!VOID.has(name) && !part.endsWith("/>")) {
          const skip = SKIP_TAGS.has(name) || SKIP_CLASSES.test(/\bclass="([^"]*)"/.exec(part)?.[1] ?? "");
          stack.push(skip);
          if (skip) skipDepth++;
        }
        return part;
      }
      if (skipDepth > 0 || !part.trim()) return part;

      // Find the earliest remaining term in this text run, link it, and carry on after it.
      let out = "";
      let rest = part;
      while (pending.length) {
        let best: { index: number; length: number; at: number } | undefined;
        pending.forEach((p, at) => {
          const m = p.pattern.exec(rest);
          if (m && (!best || m.index < best.index || (m.index === best.index && m[0].length > best.length))) {
            best = { index: m.index, length: m[0].length, at };
          }
        });
        if (!best) break;
        const { entry } = pending.splice(best.at, 1)[0];
        const text = rest.slice(best.index, best.index + best.length);
        out += `${rest.slice(0, best.index)}<a class="term" href="/glossary#${entry.id}" title="${escapeAttr(entry.definition)}">${text}</a>`;
        rest = rest.slice(best.index + best.length);
      }
      return out + rest;
    })
    .join("");
}

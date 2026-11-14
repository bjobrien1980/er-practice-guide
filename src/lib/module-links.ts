type ModuleRef = { id: number; title: string; slug: string };

const VOID = new Set(["area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"]);
const SKIP_TAGS = new Set(["a", "h1", "h2", "h3", "h4", "button", "label", "textarea", "script", "style", "code", "summary"]);
const SKIP_CLASSES = /\b(cite|statute|tag|tool|telemetry|scenario-note)\b/;
const escapeAttr = (s: string) => s.replace(/&/g, "&amp;").replace(/"/g, "&quot;").replace(/</g, "&lt;");

/** Link plain "Module N" references in rendered module prose, without touching existing links or headings. */
export function linkModuleReferences(html: string, modules: ModuleRef[]): string {
  const byId = new Map(modules.map((m) => [m.id, m]));
  const pattern = /\bModule\s+(\d+)\b/g;
  const stack: boolean[] = [];
  let skipDepth = 0;

  return html.split(/(<(?:"[^"]*"|'[^']*'|[^>"'])+>)/).map((part) => {
    if (part.startsWith("<")) {
      const tag = /^(<)(\/)?([a-zA-Z][\w-]*)/.exec(part);
      if (!tag) return part;
      const name = tag[3].toLowerCase();
      if (tag[2]) {
        if (stack.pop()) skipDepth--;
      } else if (!VOID.has(name) && !part.endsWith("/>")) {
        const skip = SKIP_TAGS.has(name) || SKIP_CLASSES.test(/\bclass="([^"]*)"/.exec(part)?.[1] ?? "");
        stack.push(skip);
        if (skip) skipDepth++;
      }
      return part;
    }
    if (skipDepth > 0 || !part.trim()) return part;

    return part.replace(pattern, (whole, idText: string) => {
      const module = byId.get(Number(idText));
      if (!module) return whole;
      return `<a class="module-ref" href="/modules/${module.slug}" title="${escapeAttr(module.title)}">${whole}</a>`;
    });
  }).join("");
}

// Post-render step: figure and example numbers follow the lecture number.
// Quarto numbers chapters across the whole book. The Basic lectures are
// chapters 1 to 10 (tutorials, sheets and mocks are unnumbered), so the
// Intermediate lectures come out as 11 to 16. This script maps them back to
// 1 to 6 in the Intermediate pages and in the search index. Numbers below 11
// are left alone, so running the script twice changes nothing.
const OFFSET = 10;
const out = Deno.env.get("QUARTO_PROJECT_OUTPUT_DIR") ?? "docs";
const re = /\b(Figure|Example|Table|Definition|Exercise|Equation)(&nbsp;| | )(\d+)\.(\d+)/g;
const fix = (s: string) =>
  s.replace(re, (m, w, sp, ch, n) => {
    const c = parseInt(ch, 10);
    return c > OFFSET ? `${w}${sp}${c - OFFSET}.${n}` : m;
  });

const dir = `${out}/intermediate`;
for (const e of Deno.readDirSync(dir)) {
  if (!e.isFile || !e.name.endsWith(".html")) continue;
  const p = `${dir}/${e.name}`;
  const t = Deno.readTextFileSync(p);
  const u = fix(t);
  if (u !== t) Deno.writeTextFileSync(p, u);
}

const sp = `${out}/search.json`;
try {
  const items = JSON.parse(Deno.readTextFileSync(sp));
  for (const it of items) {
    if (typeof it.href === "string" && it.href.startsWith("intermediate/")) {
      for (const k of Object.keys(it)) {
        if (typeof it[k] === "string") it[k] = fix(it[k]);
      }
    }
  }
  Deno.writeTextFileSync(sp, JSON.stringify(items));
} catch (_e) {
  // no search index: nothing to do
}

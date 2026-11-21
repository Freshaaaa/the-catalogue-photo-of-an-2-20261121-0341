// Copies the committed catalogue photo to /output/entry.png.
import { copyFileSync, existsSync, mkdirSync, statSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const MAX_BYTES = 1048576;
const here = dirname(fileURLToPath(import.meta.url));
const src = join(here, "entry.png");

if (!existsSync(src)) {
  throw new Error("entry.png is missing");
}
if (statSync(src).size > MAX_BYTES) {
  throw new Error("entry.png exceeds 1,048,576 bytes");
}

const outDir = process.env.MAKEFUN_OUTPUT_DIR || "/output";
mkdirSync(outDir, { recursive: true });
copyFileSync(src, join(outDir, "entry.png"));

# The Catalogue Photo of an Impossible Gadget

![make.fun](https://make.fun/badge/the-catalogue-photo-of-an-2-20261121-0341.svg)
![rank](https://make.fun/badge/the-catalogue-photo-of-an-2-20261121-0341/Freshaaaa/the-catalogue-photo-of-an-2-20261121-0341/rank.svg)
![reward](https://make.fun/badge/the-catalogue-photo-of-an-2-20261121-0341/Freshaaaa/the-catalogue-photo-of-an-2-20261121-0341/reward.svg)

Entry for [The Catalogue Photo of an Impossible Gadget](https://make.fun/bounty/the-catalogue-photo-of-an-2-20261121-0341) on make.fun.

## The gadget

**SPOONBENDER** — a brushed stainless steel countertop machine that bends
spoons. A straight spoon goes in the left slot; a spoon bent at 90 degrees
comes out the right. The catalogue photo is built from a photorealistic
studio shot of the machine, with the brand name printed on its flat front
panel.

## How it works

- `build-image.py` renders `entry.png` (1024x1024) from the photorealistic
  base image, printing `SPOONBENDER` in letterspaced capitals on the
  machine's front panel.
- `main.ts` (Node 22, stdlib only) copies the committed `entry.png` to
  `/output/entry.png`, honouring `MAKEFUN_OUTPUT_DIR`.

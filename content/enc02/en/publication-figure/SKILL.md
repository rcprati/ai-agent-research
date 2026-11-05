---
name: publication-figure
description: Use when creating a figure (plot) from data for a scientific paper, report, or presentation with matplotlib. Produces a vector figure (PDF), with no title inside the plot, fonts that are legible at the final size, axis labels with units, and distinguishable colors, ready to be placed in a paper.
---

# Publication figure

## Before drawing

1. Set the **final width**: one column ≈ 8.6 cm (3.4 in), two columns ≈ 17.8 cm (7 in). If the journal specifies
   another size, follow it. Create the figure **at the final size** (`figsize` in inches); do not resize afterwards.
2. Load the skill's style: `plt.style.use("<skill-folder>/scripts/pubstyle.mplstyle")`.

## Rules

- **Vector format:** save as **PDF** (and SVG if requested). PNG only as a preview, never as the final file.
- **No title inside the plot.** The title and description go in the figure caption, in the paper text.
- **Larger fonts:** axis labels and tick numbers at least 8–9 pt **at the final size**.
- **Axis labels** with quantity, symbol, and unit, for example `a (Å)` and `E (eV/atom)`.
- **Distinguishable series** by color **and** marker or line style (colorblind-safe palette, readable in black and white).
- **Legend** without a frame and not covering data. No heavy grid or extra borders.
- **Measured points** as markers; fits and curves as lines. Do not connect with a line what should not be interpolated.
- **Reproducible:** read the data from the file (never type values), use a descriptive file name, and save the **script** next to the figure.

## Before saying you are done

- **Run** the script and open the generated file. Check: no title in the plot, legible text, units present, free legend.
- Report the files generated, the size in cm, and what was **not** verified (for example, journal-specific requirements).

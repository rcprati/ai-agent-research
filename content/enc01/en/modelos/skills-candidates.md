# Candidate skills for the group

Working list, organized by need. Names and descriptions come from the repositories' READMEs;
**no skill has been tested or audited**. Before installing any of them, read the
`SKILL.md` and the scripts (skills run code on your machine). Check each skill's license.

Priority legend for Meeting 2: ★ = start here.

## 1. Verification and rigor (aligned with the group's theme)

From [K-Dense scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills):
- ★ **Uncertainty & Units**: measurement uncertainty and unit checks (directly targets the "mixed units" failure)
- ★ **Statistical Analysis**: statistical analysis workflows
- **Exploratory Data Analysis**: bounded EDA
- **Experimental Design** and **Statistical Power**: planning, randomization, sample size
- **Scientific Critical Thinking**: critical analysis
- **statsmodels**, **scikit-learn**, **PyMC** (Bayesian), **scikit-survival**, **SHAP** (interpretability)

Others:
- ★ [AI-research-feedback](https://www.sourcepulse.org/projects/27605239) (claesbackman): `review-paper-code` links claims in a LaTeX paper to the analysis code (Stata, R, Python) to check reproducibility
- [Claude-Code-Scientist, peer-review](https://openskillindex.com/skills/rhowardstone-claude-code-scientist-peer-review): three simulated reviewers (methodology, statistics, impact); the statistics reviewer checks effect size, confidence intervals, and multiple-testing correction
- Anthropic use case, ["verify statistics from raw data"](https://claude.com/resources/use-case/verify-statistics-from-raw-data): extracts every statistical claim from the text and reruns the analysis (a prompt example, not a package)

## 2. Scientific writing and LaTeX

- **Scientific Writing**, **Venue Templates**, **Citation Management**, **Peer Review** (K-Dense)
- **Scientific Slides**, **LaTeX Posters**, **PPTX Posters** (K-Dense)
- [phd](https://github.com/kylymo/phd) (kylymo): paper editing, claim compression, structure audit, "red team" review, bibliography validation, LaTeX finalization. Editing skills only run when invoked
- [claude-code-my-workflow](https://claudecodeguides.com/claude-code-academic-workflow-guide-2026/) (Pedro Sant'Anna): LaTeX + R + academic project management (28 skills, 14 agents, 24 rules)
- academic-paper and academic-paper-reviewer (imbad0202, academic-research-skills repository): writing pipeline and simulated review panel, output in LaTeX, DOCX, or PDF
- **Research Grants** (K-Dense) and `review-grant` (AI-research-feedback): grant writing and simulated review panel

## 3. Literature and references

- **Paper Lookup**, **Literature Review**, **Research Lookup**, **Exa Search**, **Paperclip** (full text with line-pinned citations), **BGPT Paper Search** (K-Dense)
- **pyzotero**: access to a Zotero library (K-Dense)
- **LiteParse** and **MarkItDown**: convert PDFs and documents to text for the agent to read
- [systematic-literature-review](https://claudemarketplaces.com/skills/huangwb8/chineseresearchlatex/systematic-literature-review) (huangwb8): systematic review pipeline with LaTeX/BibTeX output
- Warning: made-up citations are a classic silent failure. Test any literature skill by checking every reference by hand

## 4. Data and figures

- **Scientific Visualization**, **Matplotlib**, **Seaborn**, **Infographics**, **Scientific Schematics** (K-Dense)
- [figures4papers](https://github.com/ChenLiu-1996/figures4papers): `scientific-figure-making` skill (license to be confirmed)
- **Polars**, **Dask**, **Vaex**: large data
- **GeoPandas**, **GeoMaster**: geospatial and remote sensing
- **NetworkX**: networks
- **SymPy**: symbolic math (good for checking calculations)

## 5. Domain-specific (for those interested)

| Area | Skills |
|---|---|
| Chemistry and materials | RDKit, Datamol, DeepChem, pymatgen, Cantera, OpenMM + MDAnalysis, nmrglue; and the 35 skills of [computational-chemistry-agent-skills](https://github.com/jinzhezenggroup/computational-chemistry-agent-skills) (VASP, CP2K, Quantum ESPRESSO, xTB, LAMMPS, DeePMD) |
| Physics and astronomy | Astropy, QuTiP, Qiskit, Cirq, PennyLane |
| Biology and bioinformatics | BioPython, Scanpy, PyDESeq2, scikit-bio, pysam, QIIME 2, Phylogenetics |
| Neuroscience | BIDS, NWB, NeuroKit2, Neuropixels-Analysis |
| Imaging and microscopy | pydicom, CellProfiler, histolab |
| Engineering and simulation | SimPy, FluidSim, PyBaMM, OpenPIV, MATLAB/GNU Octave |
| Machine learning | PyTorch Lightning, Transformers, Torch Geometric, aeon, TimesFM, UMAP-learn |

## 6. Infrastructure and reproducibility

- **DataLad**: data versioning and provenance
- **Nextflow**: reproducible workflows
- **LaminDB**: data management
- **Get Available Resources**: detects local CPU/GPU/memory
- **Autoskill**: mines your work history to draft new skills (useful for the group's goal of building its own skills)
- Lab: **protocols.io**, **Benchling**, **LabArchives**, **Opentrons**

## 7. Collections to explore (catalogs, not individual skills)

- [anthropics/skills](https://github.com/anthropics/skills): official examples; `docx`, `pdf`, `pptx`, and `xlsx` are *source-available*, not open source
- [qinyan-academic-skills](https://www.sourcepulse.org/projects/31899587) (LeonChaoX): 183 academic skills
- [research-plugins](https://www.sourcepulse.org/projects/32841255) (wentorai): 433 skills and 34 tools, integrated with academic databases
- [Awesome-Scientific-Skills](https://www.sourcepulse.org/projects/26791144) (InternScience): curation of official and community registries
- [Awesome-Agent-Skills-for-Empirical-Research](https://openskillindex.com/skills/brycewang-stanford-awesome-agent-skills-for-empirical-research-methodology-skill) (brycewang-stanford): 13 methodology skills
- Star counts on aggregators differ widely; check the last commit date on GitHub

## 8. Skills the group could write (gaps)

Nothing above directly covers the "silent failures" theme. Candidates for our own skills,
good for Meeting 2 or 3:

1. **validate-against-reference**: run the method on a case with a known answer and report the deviation
2. **data-accounting**: every analysis ends by listing rows read, discarded, converted, and why
3. **check-units-and-missing**: scans the data for mixed units and missing-data codes (-999, NA, 9999)
4. **independent-reviewer**: reviews a result without seeing the reasoning of whoever produced it
5. **audit-citations**: checks that each reference exists and says what the text claims
6. **reproducibility-report**: records versions, seeds, commands, and outputs

## To do

- Audit 2 or 3 third-party skills (one per category) with the group's checklist
- Check each skill's license before redistributing
- Ask the group which domain areas are represented, to prune section 5

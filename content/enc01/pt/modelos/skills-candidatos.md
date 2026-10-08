# Skills candidatos para o grupo

Lista de trabalho, organizada por necessidade. Os nomes e as descrições vêm dos READMEs dos
repositórios; **nenhum skill foi testado ou auditado**. Antes de instalar qualquer um, ler o
`SKILL.md` e os scripts (skills executam código na máquina). Conferir licença de cada skill.

Legenda de prioridade para o Encontro 2: ★ = começar por aqui.

## 1. Verificação e rigor (alinhado ao tema do grupo)

Do [K-Dense scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills):
- ★ **Uncertainty & Units**: incerteza de medida e checagem de unidades (ataca direto a falha "unidades trocadas")
- ★ **Statistical Analysis**: fluxos de análise estatística
- **Exploratory Data Analysis**: EDA delimitada
- **Experimental Design** e **Statistical Power**: planejamento, randomização, tamanho de amostra
- **Scientific Critical Thinking**: análise crítica
- **statsmodels**, **scikit-learn**, **PyMC** (bayesiano), **scikit-survival**, **SHAP** (interpretabilidade)

Outros:
- ★ [AI-research-feedback](https://www.sourcepulse.org/projects/27605239) (claesbackman): `review-paper-code` liga afirmações do artigo LaTeX ao código de análise (Stata, R, Python) para checar reprodutibilidade
- [Claude-Code-Scientist, peer-review](https://openskillindex.com/skills/rhowardstone-claude-code-scientist-peer-review): três revisores simulados (metodologia, estatística, impacto); o revisor de estatística checa tamanho de efeito, IC e correção para múltiplos testes
- Caso de uso da Anthropic, ["verificar estatísticas a partir dos dados brutos"](https://claude.com/resources/use-case/verify-statistics-from-raw-data): extrai cada afirmação estatística do texto e reexecuta a análise (é um exemplo de prompt, não um pacote)

## 2. Escrita científica e LaTeX

- **Scientific Writing**, **Venue Templates**, **Citation Management**, **Peer Review** (K-Dense)
- **Scientific Slides**, **LaTeX Posters**, **PPTX Posters** (K-Dense)
- [phd](https://github.com/kylymo/phd) (kylymo): edição de artigos, compressão de claims, auditoria de estrutura, revisão "red team", validação de bibliografia, finalização em LaTeX. Skills de edição só rodam quando chamados
- [claude-code-my-workflow](https://claudecodeguides.com/claude-code-academic-workflow-guide-2026/) (Pedro Sant'Anna): LaTeX + R + gestão de projeto acadêmico (28 skills, 14 agentes, 24 regras)
- academic-paper e academic-paper-reviewer (imbad0202, repositório academic-research-skills): pipeline de redação e painel de revisão simulado, saída em LaTeX, DOCX ou PDF
- **Research Grants** (K-Dense) e `review-grant` (AI-research-feedback): redação e simulação de painel de edital

## 3. Literatura e referências

- **Paper Lookup**, **Literature Review**, **Research Lookup**, **Exa Search**, **Paperclip** (texto completo com citações ancoradas em linhas), **BGPT Paper Search** (K-Dense)
- **pyzotero**: acesso à biblioteca do Zotero (K-Dense)
- **LiteParse** e **MarkItDown**: converter PDF e documentos em texto para o agente ler
- [systematic-literature-review](https://claudemarketplaces.com/skills/huangwb8/chineseresearchlatex/systematic-literature-review) (huangwb8): pipeline de revisão sistemática com saída LaTeX/BibTeX
- Atenção: citações inventadas são uma falha silenciosa clássica. Qualquer skill de literatura deve ser testado conferindo cada referência à mão

## 4. Dados e figuras

- **Scientific Visualization**, **Matplotlib**, **Seaborn**, **Infographics**, **Scientific Schematics** (K-Dense)
- [figures4papers](https://github.com/ChenLiu-1996/figures4papers): skill `scientific-figure-making` (licença a confirmar)
- **Polars**, **Dask**, **Vaex**: dados grandes
- **GeoPandas**, **GeoMaster**: geoespacial e sensoriamento remoto
- **NetworkX**: redes
- **SymPy**: matemática simbólica (bom para conferir contas)

## 5. Específicos de domínio (para quem tiver interesse)

| Área | Skills |
|---|---|
| Química e materiais | RDKit, Datamol, DeepChem, pymatgen, Cantera, OpenMM + MDAnalysis, nmrglue; e os 35 skills do [computational-chemistry-agent-skills](https://github.com/jinzhezenggroup/computational-chemistry-agent-skills) (VASP, CP2K, Quantum ESPRESSO, xTB, LAMMPS, DeePMD) |
| Física e astronomia | Astropy, QuTiP, Qiskit, Cirq, PennyLane |
| Biologia e bioinformática | BioPython, Scanpy, PyDESeq2, scikit-bio, pysam, QIIME 2, Phylogenetics |
| Neurociência | BIDS, NWB, NeuroKit2, Neuropixels-Analysis |
| Imagem e microscopia | pydicom, CellProfiler, histolab |
| Engenharia e simulação | SimPy, FluidSim, PyBaMM, OpenPIV, MATLAB/GNU Octave |
| Aprendizado de máquina | PyTorch Lightning, Transformers, Torch Geometric, aeon, TimesFM, UMAP-learn |

## 6. Infraestrutura e reprodutibilidade

- **DataLad**: versionamento e proveniência de dados
- **Nextflow**: fluxos de trabalho reprodutíveis
- **LaminDB**: gestão de dados
- **Get Available Resources**: detecta CPU/GPU/memória locais
- **Autoskill**: minera o seu histórico de trabalho para rascunhar novos skills (útil para a meta do grupo de criar skills próprios)
- Laboratório: **protocols.io**, **Benchling**, **LabArchives**, **Opentrons**

## 7. Coleções para explorar (catálogos, não skills individuais)

- [anthropics/skills](https://github.com/anthropics/skills): exemplos oficiais; `docx`, `pdf`, `pptx` e `xlsx` são *source-available*, não open source
- [qinyan-academic-skills](https://www.sourcepulse.org/projects/31899587) (LeonChaoX): 183 skills acadêmicos
- [research-plugins](https://www.sourcepulse.org/projects/32841255) (wentorai): 433 skills e 34 ferramentas, com integração a bases acadêmicas
- [Awesome-Scientific-Skills](https://www.sourcepulse.org/projects/26791144) (InternScience): curadoria de registros oficiais e da comunidade
- [Awesome-Agent-Skills-for-Empirical-Research](https://openskillindex.com/skills/brycewang-stanford-awesome-agent-skills-for-empirical-research-methodology-skill) (brycewang-stanford): 13 skills de metodologia
- Números de estrelas em agregadores divergem muito entre si; conferir no GitHub a data do último commit

## 8. Skills que o grupo poderia escrever (lacunas)

Nada acima cobre diretamente o tema "falhas silenciosas". Candidatos a skills próprios,
bons para o Encontro 2 ou 3:

1. **validar-contra-referência**: rodar o método em um caso com resposta conhecida e reportar o desvio
2. **contabilidade-de-dados**: toda análise termina listando linhas lidas, descartadas, convertidas e por quê
3. **checar-unidades-e-faltantes**: varre o dado por unidades mistas e códigos de faltante (-999, NA, 9999)
4. **revisor-independente**: revisa um resultado sem ver o raciocínio de quem o produziu
5. **auditar-citações**: confere se cada referência existe e diz o que o texto afirma
6. **relatório-de-reprodutibilidade**: registra versões, sementes, comandos e saídas

## Pendências

- Auditar 2 ou 3 skills de terceiros (um por categoria) com o checklist do grupo
- Conferir a licença de cada skill antes de redistribuir
- Perguntar ao grupo quais áreas de domínio estão representadas, para podar a seção 5

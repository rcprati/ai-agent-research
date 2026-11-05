# Leitura de três skills do K-Dense (sem instalar nem executar)

Repositório: [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) (MIT; cada skill declara a sua licença, as três leem `MIT`).
Lidos na íntegra: o `SKILL.md` de `exploratory-data-analysis` (311 linhas) e a primeira metade do de `uncertainty-and-units` (415 linhas).
Lidos em parte: `statistical-analysis` (453 linhas; cabeçalhos, descrição e buscas por termos), o script `missingness_leakage_audit.py` e, por busca de termos, `_tabular.py`.
**Não lidos:** as pastas `references/` e a maior parte dos scripts. Nada foi instalado nem rodado.

## Estrutura e tamanho

| Skill | SKILL.md | Scripts | References |
|---|---|---|---|
| exploratory-data-analysis | 311 linhas | 13 arquivos Python (~130 KB) | 6 arquivos de formatos + 1 template de relatório |
| statistical-analysis | 453 linhas | 1 (`assumption_checks.py`) | 5 arquivos |
| uncertainty-and-units | 415 linhas | 7 arquivos Python (~150 KB) | 7 arquivos |

Padrão comum: frontmatter (`name`, `description` longa, `license`, `compatibility`, `allowed-tools`, `metadata`), corpo com escopo,
regras, exemplos de comandos, e detalhes empurrados para `references/` e `scripts/` (carregados só quando preciso).

## O que chama atenção

- **Descrições longas, no formato "use quando…"**: servem para o agente decidir se carrega o skill. A do *uncertainty-and-units* lista uma dúzia de gatilhos e até frases típicas ("is this number physically reasonable").
- **Regras do tipo "não faça"**: o EDA proíbe apagar outliers, imputar, normalizar ou sobrescrever dados brutos automaticamente, e exige manter distintos "faltante", "não detectado", "abaixo do limite" e "zero verdadeiro".
- **Muita segurança**: trata todo conteúdo de arquivo como dado não confiável, limita tamanho e caminhos, sem rede. Útil, mas faz o skill pesado.
- **Barreira de entrada**: exige Python 3.12+ e, em alguns casos, `uv` e bibliotecas fixadas por versão. Para quem não é da computação, é uma dificuldade real.
- **Um skill pode dar instruções ao agente além da tarefa.** O EDA tem uma seção final mandando o agente citar o artigo do K-Dense em manuscritos que o usaram e, havendo rede, consultar o arXiv. É um bom exemplo para o grupo: ler o `SKILL.md` mostra tudo o que o agente passa a fazer.

## O que ele pegaria nos nossos casos (leitura, não teste)

| Nosso caso | O que a leitura sugere |
|---|---|
| 1 · ORCA (log não convergido, método diferente) | Nenhum dos três trata saídas de química quântica. O EDA só encaminha para uma `reference` de química (não lida). |
| 2 · VASP (ENCUT, relaxação incompleta) | Idem: fora do escopo dos três. |
| 3A · coluna vazada do alvo | A "auditoria de vazamento" do EDA checa **sobreposição de entidades, grupos, linhas idênticas e tempo entre divisões treino/teste**. Não procura uma coluna derivada do alvo (busca no código: nada sobre isso). Mas o EDA exige, antes de interpretar, um **dicionário de dados com derivações e procedência**: seguindo isso, o agente teria de ler o nosso `dicionario_dados.txt`. |
| 3B · escalas diferentes no K-means | O EDA fala em registrar transformações e ajustar parâmetros só no treino, mas não diz "padronize antes de K-means". Há `distribution_sensitivity.py` por coluna, que não resolve isso. |
| Código de faltante (-999) | O EDA cobre: aceita `--missing-token`, mantém faltante separado de zero, não imputa automaticamente. |
| Unidades misturadas numa tabela | O *uncertainty-and-units* audita **código Python** com unidades removidas e usa `pint`; não olha colunas de unidade num CSV. |

Conclusão provisória: os três são bons para **ler e discutir**, e o ponto mais útil para os nossos casos é a exigência do dicionário de dados no EDA.
Para as falhas que mostramos, falta um skill menor e mais específico, o que reforça a ideia de escrever o nosso.

## Para a discussão no encontro

- Quanto de cada skill um agente carrega por vez? (o corpo do `SKILL.md`; `references/` e `scripts/` só se necessário)
- A descrição diz quando usar? O corpo manda **executar e verificar**, ou só descreve?
- O que o skill proíbe? O que ele deixa de fora? Quem o auditou?
- Vale instalar, ou basta copiar as ideias para o nosso `AGENTS.md`?

## Limites desta leitura

Baseada nos arquivos do repositório em 2026-10-08 (HEAD). Os skills são atualizados com frequência, e os números de linhas e tamanhos mudam.
Não confirmei se os scripts fazem o que a descrição afirma.

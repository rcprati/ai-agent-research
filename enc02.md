---
theme: seriph
title: Skills na prática — Aula 2
info: |
  Ferramentas de IA para código na pesquisa.
  Aula 2: ler, construir e testar um skill.
class: text-center
highlighter: shiki
drawings:
  persist: false
transition: slide-left
mdc: true
colorSchema: light
fonts:
  sans: 'Inter'
---

# Skills na prática

### Aula 2 · Ler, construir e testar um skill

<div class="pt-10 opacity-70 text-sm">
Ferramentas de IA para código na pesquisa
</div>

<!--
Boas-vindas. Perguntar: quem fez a tarefa de casa (analisar um skill da lista)? O que viram?
-->

---

# Roteiro de hoje

<div class="mt-6 text-lg leading-10">

1. **Recapitulando** a Aula 1
2. Um **skill por dentro**
3. **Lendo** skills reais
4. **Construindo** o nosso: `verificar-entradas`
5. **Testando:** sem skill × com skill
6. **Mãos à obra:** o seu skill
7. Combinados para a próxima aula

</div>

---

# Recapitulando a Aula 1

<div class="mt-2 text-base leading-8">

- Pedido **restrito** ("…usando `resumo.csv`") → o agente leu **só o que foi apontado** → saída limpa, **sem aviso**
  <br><span class="text-sm opacity-70">ORCA, VASP, regressão e clustering: o mesmo padrão nos quatro casos</span>
- Com um **`AGENTS.md`**, o agente passou a abrir os arquivos de origem e a ler o dicionário
- Mas o arquivo **não garante**: no caso 2 ele reportou o valor **sem executar** o script
- Um `AGENTS.md` com regras demais vira texto longo que o agente lê **sempre**

</div>

<div class="mt-6 p-4 rounded-xl bg-blue-50 border border-blue-200 text-center text-lg">
E se a checagem fosse <b>uma receita reutilizável</b>, carregada só quando a tarefa aparece?
</div>

---

# Um skill por dentro

<div class="grid grid-cols-2 gap-6 mt-2 text-base">
<div>

```text
verificar-entradas/
├── SKILL.md        ← nome, descrição, passos
├── scripts/
│   └── scan.py     ← código de apoio (opcional)
└── references/     ← detalhes (opcional)
```

</div>
<div class="leading-7">

**Três camadas de carregamento**
1. **Sempre:** `name` e `description` (poucas linhas)
2. **Quando o pedido combina:** o corpo do `SKILL.md`
3. **Só se necessário:** `scripts/` e `references/`

O nome da pasta deve ser igual ao `name`.

</div>
</div>

<div class="mt-2 text-xs leading-5">

**Onde instalar** (projeto · global; cada skill em uma subpasta `<nome>/`)
- **Claude Code:** `.claude/skills/` · `~/.claude/skills/`
- **Antigravity:** `.agents/skills/` · `~/.gemini/config/skills/` (app e IDE) ou `~/.gemini/antigravity-cli/skills/` (CLI)
- **OpenCode:** `.opencode/skills/` · `~/.config/opencode/skills/` (nativo); também lê `.claude/skills/` e `.agents/skills/`, no projeto e no global

<span class="opacity-70">Dica: um skill em `.agents/skills/` serve ao Antigravity **e** ao OpenCode.</span>

</div>

<!--
Mostrar a pasta real em materiais/ (zip "Skill verificar-entradas"). Caminhos do Antigravity e do OpenCode informados por quem vai apresentar (OpenCode: seis locais, nativo + compatíveis com Claude Code e com o padrão Agent Skills). Conferir nas versões instaladas antes da aula.
-->

---

# Lendo skills reais (K-Dense)

<div class="text-sm">

| Skill | `SKILL.md` | Scripts | Referências |
|---|---|---|---|
| exploratory-data-analysis | 311 linhas | 13 arquivos Python (~130 KB) | 6 + 1 modelo |
| statistical-analysis | 453 linhas | 1 | 5 |
| uncertainty-and-units | 415 linhas | 7 arquivos Python (~150 KB) | 7 |

</div>

<div class="mt-3 text-base leading-7">

- Descrições longas, no formato **"use quando…"**
- Muitas regras **"não faça"**: não apagar outliers, não imputar sozinho, não sobrescrever dado bruto
- Exigem Python 3.12+ e bibliotecas fixadas: **barreira** para quem não é da computação
- Um skill pode instruir o agente **além da tarefa** (o de EDA manda citar o artigo do K-Dense e consultar o arXiv)

</div>

<div class="mt-2 text-xs opacity-60">
Lidos sem instalar: <code>SKILL.md</code> do EDA, parte do <i>uncertainty-and-units</i> e cabeçalhos do <i>statistical-analysis</i>. Nenhum foi executado.
</div>

---

# O que eles pegariam nos nossos casos?

<div class="text-sm">

| Caso | O que a leitura sugere |
|---|---|
| 1 · ORCA · 2 · VASP | Fora do escopo dos três |
| 3A · coluna vazada | A "auditoria de vazamento" olha **sobreposição treino/teste**, não uma coluna derivada do alvo. Mas o EDA exige um **dicionário de dados** com derivações |
| 3B · escala no K-means | Fala em registrar transformações; não diz para padronizar antes de distância |
| Faltante (-999) | Coberto no EDA: código explícito, sem imputar sozinho |
| Unidades numa tabela | O *uncertainty-and-units* audita **código Python**, não colunas de um CSV |

</div>

<div class="mt-3 text-center text-lg">
Leitura, não teste. Faltou um skill <b>pequeno e específico</b> para as nossas falhas.
</div>

---

# O que faz uma boa descrição

<div class="grid grid-cols-2 gap-5 mt-2 text-sm">
<div class="p-3 rounded-xl bg-red-50">

**Vaga**
```yaml
description: Ajuda a analisar dados.
```
O agente não sabe **quando** carregar, nem o que esperar.

</div>
<div class="p-3 rounded-xl bg-green-50 border border-green-200">

**Específica, com gatilhos**
```yaml
description: Use antes de calcular um
  resultado a partir de arquivos de
  dados ou saídas de cálculo (CSV, logs
  de DFT, resultados de ML). Confere
  unidades, faltantes, convergência...
```

</div>
</div>

<div class="mt-4 text-base leading-8">

- Diga **quando usar** (tipos de arquivo, palavras do pedido)
- Diga **o que ele faz** e o que entrega ao final
- Descrições curtas demais não disparam; longas demais gastam contexto

</div>

---

# Construindo o nosso: `verificar-entradas`

<div class="text-sm leading-6">

Uma página (35 linhas) com seis blocos:

1. **Documentação:** ler todo README e dicionário antes de usar os dados
2. **Tabela-resumo:** abrir o arquivo de origem de cada linha; nunca confiar só na tabela
3. **Cálculos (DFT):** só corridas convergidas; mesmo método, ENCUT e ISPIN; a **última** energia
4. **Tabelas:** unidade de cada coluna; faltantes (-999, NA) tratados como ausentes
5. **Machine learning:** origem de cada coluna (nada derivado do alvo); padronizar antes de distância
6. **Antes de dizer "pronto":** **executar** o script, mostrar a saída real, listar usados, descartados e **não verificados**

</div>

<div class="mt-3 p-3 rounded-xl bg-slate-100 text-sm">
Cada passo vem de uma falha que <b>vimos</b> na Aula 1. Arquivo completo no zip do material.
</div>

<!--
Mostrar o SKILL.md real (materiais/verificar-entradas/SKILL.md) e a versão em inglês check-inputs.
-->

---

# O script de apoio: `scan.py`

<div class="grid grid-cols-2 gap-5 mt-1 text-xs leading-5">
<div>

**Faz a parte mecânica**, só com a biblioteca padrão do Python (não altera nada, não usa rede):

- lista a documentação da pasta
- procura `NOT CONVERGED` e relaxações sem `reached required accuracy`
- compara método, ENCUT e ISPIN entre arquivos
- conta energias por arquivo (vale a última)
- acha códigos de faltante, unidades misturadas, valores negativos em colunas de grandeza positiva
- compara escalas e colunas quase idênticas
- avisa quando uma **tabela-resumo aponta para um arquivo com problema**

</div>
<div>

```text
$ python3 scripts/scan.py caso-2-vasp/

Pontos de atenção:
 ⚠ COslab_run1.OUTCAR: relaxação sem a
   linha 'reached required accuracy'
 ⚠ resumo.csv: a linha 'CO_slab' aponta
   para COslab_run1.OUTCAR, que tem
   problema. Não confie na tabela-resumo
 ⚠ Parâmetro 'ENCUT' difere entre
   arquivos: CO_gas.OUTCAR=520.0;
   CO_gas_ecut400.OUTCAR=400.0; ...
```

</div>
</div>

<div class="mt-3 text-sm opacity-70">
Ele só <b>sinaliza</b>. Quem decide o que usar continua sendo o agente (e você).
</div>

---

# A varredura nos nossos quatro casos

<div class="text-sm">

| Caso | O que o `scan.py` sinaliza |
|---|---|
| 1 · ORCA | `HF_run1.log` **não convergiu**; o resumo aponta para ele; o log PBE usa outro método |
| 2 · VASP | **ENCUT 400** × 520; `COslab_run1` **incompleto**; o resumo aponta para ele; várias energias por arquivo |
| 3A · regressão | `energia` e `energia_calc_anterior` **quase idênticas** (\|r\| = 0,999) |
| 3B · clustering | **Escalas** muito diferentes (~1 × ~1700); 10 valores negativos em `raio_A` |

</div>

<div class="mt-3 text-base leading-7">

- Achou **tudo** o que tínhamos escondido (rodamos os quatro, com os mesmos dados da Aula 1)
- Falso alarme: marca todo arquivo com várias energias, mesmo nos corretos
- Um skill **não obriga** o agente a obedecer: precisa ser testado

</div>

---

# Outro skill: figura para publicação

<div class="grid grid-cols-2 gap-5 mt-1 text-sm leading-6">
<div>

O **mesmo pedido** nos dois casos:

> Crie um script em python que faça uma figura da energia versus o parâmetro de rede, com os dois funcionais, a partir de `dados_eos.csv`, com os rótulos em inglês

**O skill manda:**
- formato **vetorial** (PDF), PNG só de prévia
- **sem título** dentro do gráfico (vai na legenda do artigo)
- fontes **≥ 8–9 pt no tamanho final**
- rótulos com **símbolo e unidade**
- **cor e marcador** (seguro para daltônicos)
- script **reprodutível**, lendo os dados do arquivo

</div>
<div>

```text
figura-publicacao/
├── SKILL.md
└── scripts/
    └── pubstyle.mplstyle
```

<div class="text-xs opacity-70 leading-5">
O arquivo <code>pubstyle.mplstyle</code> fixa tamanho de uma coluna (8,6 cm), fontes, paleta e PDF com fonte incorporada. O agente só precisa carregá-lo.
</div>

</div>
</div>

---

# A mesma figura, sem e com o skill

<div class="grid grid-cols-2 gap-6 mt-1">
<div class="text-center">

<img src="/fig-sem-skill.png" style="height:230px;margin:0 auto" />

<div class="text-xs leading-5 mt-1"><b>Sem skill</b> · PNG 1800 × 1350 px · fonte padrão 10 pt (≈ 5,7 pt numa coluna) · grade e legenda com moldura</div>

</div>
<div class="text-center">

<img src="/fig-com-skill.png" style="height:230px;margin:0 auto" />

<div class="text-xs leading-5 mt-1"><b>Com skill</b> · PDF vetorial · Arial incorporada · 9–10 pt · 8,4 × 6,3 cm · sem grade nem moldura</div>

</div>
</div>

<div class="mt-2 text-xs opacity-70 leading-5">
Ambas à mesma escala (largura de uma coluna). Duas execuções do Claude, com o mesmo pedido; a sem skill não abriu a imagem para conferir. Neste caso o agente sem skill não pôs título no gráfico, mas as outras regras não vieram sozinhas.
</div>

<!--
Figuras reais geradas por duas execuções isoladas do Claude (subagentes) a partir de dados_eos.csv (dados sintéticos), com o pedido de rótulos em inglês nas duas. Numa primeira rodada (rótulos em português) o agente sem skill tinha posto título no gráfico; nesta, não. O script e as figuras estão no zip "Exemplo de figura". No Antigravity/OpenCode, repetir o teste ao vivo: mesmo pedido, sem e com o skill instalado.
-->

---

# Testando: sem skill × com skill

<div class="mt-1 text-sm opacity-70">Mesmos pedidos restritos da Aula 1 · sessão nova, pasta só com os dados · o skill instalado na ferramenta</div>

<div class="text-sm">

| Caso | Sem skill (Aula 1) | Com o skill |
|---|---|---|
| 1 · ORCA | −18,80 ✗ | |
| 2 · VASP | −1,515 ✗ | |
| 3A · regressão | R² 0,9982 ✗ | |
| 3B · clustering | 88/70/42 ✗ | |
| 4 · Figura | PNG, fonte pequena | |

</div>

<div class="mt-3 text-sm leading-6">

Anote em cada execução: o agente **carregou** o skill? Rodou o `scan.py`? Abriu os arquivos de origem? **Executou** o script? Qual foi o resultado?

</div>

<!--
Tabela a preencher ao vivo (coluna "Com o skill"). Se a ferramenta não carregar o skill automaticamente, pedir explicitamente para usá-lo e anotar isso. Uma execução por célula não é estatística.
-->

---

# Mãos à obra: o seu skill

<div class="grid grid-cols-2 gap-5 mt-2 text-sm">
<div class="leading-7">

Escolha uma tarefa que **se repete** no seu laboratório e rascunhe:

1. **Nome** da pasta (minúsculas, hifens)
2. **Quando usar** (a descrição)
3. **4 a 6 passos**
4. **O que reportar** ao final
5. **Um caso com resposta conhecida** para testar

</div>
<div class="p-3 rounded-xl bg-slate-100 text-xs leading-5">

```markdown
---
name: meu-skill
description: Use quando ... Faz ... e entrega ...
---

# Título

## Passos
1. ...
2. ...

## Antes de dizer que terminou
- Execute e mostre a saída real
- Liste usado, descartado, não verificado
```

</div>
</div>

---

# Checklist de um bom skill

<div class="mt-2 text-lg leading-9">

☐ A descrição diz **quando** usar?<br>
☐ Os passos são **curtos e verificáveis**, não genéricos?<br>
☐ Manda **executar e mostrar a saída real**?<br>
☐ Diz o que **não** fazer (não apagar, não inventar)?<br>
☐ Foi **testado** em pelo menos um caso com resposta conhecida?<br>
☐ Quem não programa consegue **ler e entender** o `SKILL.md`?

</div>

---

# Cuidados com skills de terceiros

<div class="mt-2 text-base leading-8">

- Skills **executam código** na sua máquina: leia o `SKILL.md` **e os scripts** antes de instalar
- **Licença** de cada skill (o repositório pode ser MIT e o skill, não)
- Podem carregar **instruções embutidas** (citar artigos, acessar a rede): o que ele pede ao agente?
- Teste numa **pasta isolada**, com dados que não são sensíveis
- Fixe a **versão** que testou: skills mudam

</div>

<div class="mt-4 p-3 rounded-xl bg-amber-50 border border-amber-200 text-sm text-center">
Quando não for instalar, <b>ler o SKILL.md</b> já ensina muito sobre o que o agente vai fazer.
</div>

---

# Para a próxima aula

<div class="mt-4 text-lg leading-9">

- **Testar** o seu skill em um caso real e anotar o que mudou
- **Compartilhar** um skill (ou o rascunho) no repositório compartilhado
- **Trazer** um caso em que o skill **não** ajudou

</div>

<div class="mt-6 text-sm opacity-70">
Possíveis temas: dados sensíveis e privacidade · limites de uso e custo · tarefas longas e reprodutibilidade
</div>

---

# Referências

- Learn Harness Engineering (walkinglabs, MIT): <https://github.com/walkinglabs/learn-harness-engineering>
- Scientific Agent Skills (K-Dense-AI, MIT, licença por skill): <https://github.com/K-Dense-AI/scientific-agent-skills>

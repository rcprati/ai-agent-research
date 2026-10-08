---
theme: seriph
title: Agentes de IA para código na pesquisa — Encontro 1
info: |
  Grupo de estudo sobre ferramentas de IA para código (Claude Code, Antigravity).
  Encontro 1: o que são, onde falham em silêncio e como verificar.
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

# IA que escreve código<br>na sua pesquisa

### Encontro 1 · O que funciona, onde falha em silêncio e como verificar

<div class="pt-10 opacity-70 text-sm">
Grupo de estudo · CMD · sexta, 16/10 · não é preciso saber programar
</div>

<!--
[~0:00] Boas-vindas. Combinar o formato: quinzenal, aberto a todos os níveis, troca de prompts, configurações e skills.
Perguntar quem já usou Claude Code, quem já usou Antigravity, quem nunca usou.
-->

---

# Roteiro de hoje (1h30)

<div class="mt-6 text-lg leading-10">

1. O que é um **agente de código** (e o que não é)
2. **Casos reais:** o agente diz "pronto"
3. **Falhas silenciosas** em código de pesquisa
4. A regra principal: **não confie, verifique**
5. **Arquivo de instruções** do projeto e **skills**
6. **Checklist** e combinados para o próximo encontro

</div>

---

# Chat × agente de código

<div class="grid grid-cols-2 gap-8 mt-6">
<div class="p-5 rounded-xl bg-slate-100">

### Chat (ChatGPT, Claude.ai)
- Você cola um trecho e recebe texto
- Você copia, roda, volta com o erro
- **Você** executa tudo
</div>
<div class="p-5 rounded-xl bg-blue-50 border border-blue-200">

### Agente de código
- Lê os arquivos da sua pasta
- **Roda comandos**, cria e edita arquivos
- Tenta de novo sozinho quando dá erro
- **Diz quando acha que terminou**
</div>
</div>

<div class="mt-8 text-center text-lg">
Mais autonomia = mais produtividade <b>e</b> mais lugares para um erro passar despercebido.
</div>

<!--
[~0:10] Ponto central: o agente age sobre a sua pasta. Isso é útil, mas muda o seu papel: de quem escreve para quem revisa.
-->

---

# Claude Code e Antigravity: a mesma ideia

| | Claude Code | Google Antigravity |
|---|---|---|
| Onde roda | Terminal, app desktop, extensões de IDE | Editor próprio (IDE) e CLI |
| Faz | Lê, edita, executa comandos | Idem, com painel de agentes |
| Arquivo de instruções | `CLAUDE.md` | `AGENTS.md` / `GEMINI.md` |
| Skills reutilizáveis | Sim | Sim |

<div class="mt-6 text-sm opacity-70">
Tudo o que veremos hoje vale para as duas. O que muda é onde clicar e o nome do arquivo de instruções.
</div>

<!--
Verificar antes da reunião: nomes e caminhos do Antigravity mudam entre versões (IDE × CLI). Fontes de terceiros indicam que o IDE passou a ler AGENTS.md a partir da v1.20.x (março/2026); confirmar na documentação oficial.
-->

---

# Caso 1: o pedido (DFT, ORCA)

<div class="mt-2 text-sm opacity-70">Antigravity · Gemini 3.1 Pro (low) · pasta com 5 logs de DFT e um <code>resumo.csv</code> (dados sintéticos)</div>

<div class="mt-6 p-5 rounded-xl bg-slate-100 text-lg leading-8">

> Crie um script em python que calcule a energia de reação de **H2 + F2 → 2 HF** em kcal/mol usando `resumo.csv`

</div>

<div class="mt-6 text-lg text-center">
Um pedido comum: alguém passa uma planilha-resumo e pede a análise.<br>
<b>O que pode dar errado?</b>
</div>

<!--
[~0:20] Pedir 2 ou 3 palpites à plateia antes de mostrar a resposta. Dados e gabarito: materiais/demo e materiais/gabaritos/00-demo.md. Roteiro e variações: materiais/roteiro-demo.md.
Atenção: o modelo foi o Gemini 3.1 Pro (low) no Antigravity; confirmar antes da reunião.
-->

---

# A resposta do agente

```text
=== Cálculo de Energia de Reação ===
Reação: H2 + F2 -> 2 HF
E(H2):    -1.173525 Hartree
E(F2):  -199.343845 Hartree
E(HF):  -100.273666 Hartree
------------------------------------
ΔE (Hartree):     -0.029962
ΔE (kcal/mol):   -18.801425
```

<div class="mt-4 p-4 rounded-xl bg-green-50 border border-green-200">
"A energia final de reação calculada é de <b>-18.80 kcal/mol</b>. O script já está pronto no seu diretório."
</div>

<div class="mt-4 text-center text-lg">
Rodou sem erro. Sinal e ordem de grandeza razoáveis. <b>Vocês confiariam?</b>
</div>

---

# O que estava por trás

<div class="grid grid-cols-2 gap-6 mt-2 text-sm">
<div>

### `resumo.csv`
```text
molecula,arquivo,energia
H2,H2.log,-1.173525
F2,F2.log,-199.343845
HF,HF_run1.log,-100.273666
```

### `HF_run1.log`
```text
*   ERROR: SCF NOT CONVERGED AFTER 2 CYCLES  *
Total Energy (ultimo ciclo)  -100.273665650111 Eh
****ORCA finished by error termination****
```

</div>
<div class="text-base leading-8">

- A linha do HF veio de um cálculo que **não convergiu**
- Existia um `HF_run2.log` **convergido**, que a tabela não citava
- O agente leu **só a tabela**, como pedido, e **não avisou** de nada

<div class="mt-4 p-3 rounded-xl bg-amber-50 border border-amber-200 text-center">
Resultado correto: <b>−118,6 kcal/mol</b><br>
<span class="text-sm opacity-70">o agente deu −18,8: errado por um fator de 6, e ainda exotérmico</span>
</div>

</div>
</div>

---

# Mesmo pedido, resultados diferentes

| Execução | Pedido | Resultado |
|---|---|---|
| Antigravity · Gemini 3.1 Pro (low) | "…usando `resumo.csv`" | **−18,80** (errado) |
| Antigravity | "…usando os arquivos desta pasta; diga quais usou e por quê" | −118,57 (certo) |
| Claude (6 agentes isolados) | os dois pedidos, 3 execuções cada | **−118,57** (6 de 6 certos) |

<div class="mt-4 text-base leading-8">

- Os agentes que acertaram **abriram os logs por conta própria**; o que errou, não
- **Poucas execuções:** isto não é um ranking de ferramentas. Mostra que o resultado **varia**
- Com a resposta certa conhecida o erro é fácil de ver. **E se você não a conhecesse?**

</div>

<!--
Honestidade metodológica: os "agentes isolados do Claude" foram subagentes, não o Claude Code interativo; 6 execuções, só neste problema. Os mesmos não acertam sempre em outros problemas. O ponto é variabilidade e a necessidade de verificar, não qual ferramenta é melhor.
Obs.: três subagentes descreveram o erro "que sairia" pelo CSV com números inventados (-55, -56, -80); o valor real é -18,80.
-->

---

# Caso 2: energia de adsorção (VASP, dados fictícios)

<div class="mt-1 text-sm opacity-70">Antigravity · mesmo tipo de pedido · cinco <code>OUTCAR</code> e um <code>resumo.csv</code></div>

<div class="grid grid-cols-2 gap-5 mt-3 text-sm">
<div>

> Crie um script em python que calcule a energia de adsorção do CO em Pt(111) em eV, E_ads = E(CO/slab) − E(slab) − E(CO gás), usando `resumo.csv`

```text
Cálculo da Energia de Adsorção
E(CO/slab) :   -361.150 eV
E(slab)    :   -345.123 eV
E(CO gás)  :    -14.512 eV
E_ads      :     -1.515 eV
```

</div>
<div class="leading-7">

**O que estava por trás**
- CO gás: o resumo usa um cálculo com **ENCUT = 400 eV**; os outros usam **520**
- CO/slab: relaxação que **parou por limite de passos** (sem `reached required accuracy`)
- O agente **não abriu nenhum OUTCAR**

<div class="mt-3 p-3 rounded-xl bg-amber-50 border border-amber-200 text-center">
Correto: <b>−1,697 eV</b> · agente: <b>−1,515 eV</b><br>
<span class="text-xs opacity-70">sinal e ordem de grandeza certos, errado em 0,18 eV</span>
</div>

</div>
</div>

<!--
Dados fictícios (arquivos simplificados no estilo VASP, não saída real). Gabarito: materiais/gabaritos/caso2-vasp.md. Confirmar o modelo usado nesta execução.
-->

---

# Caso 3: machine learning (dados sintéticos)

<div class="mt-1 text-sm opacity-70">Antigravity · dois CSVs e um <code>dicionario_dados.txt</code> que ele <b>não leu</b></div>

<div class="grid grid-cols-2 gap-5 mt-3 text-sm">
<div>

**A) Regressão linear**
> …prever `energia` usando `dados_regressao.csv` e reportar o R² em dados de teste

R² = **0,9982** (divisão 80/20 escolhida pelo agente)

**B) K-means com 3 clusters**
> …agrupar `dados_clustering.csv` em 3 clusters e mostrar o tamanho de cada um

Cluster 0: **88** · Cluster 1: **70** · Cluster 2: **42**

</div>
<div class="leading-7">

**O que dizia o dicionário**
```text
energia_calc_anterior  ... obtida a partir do
  próprio alvo; NÃO é um descritor
raio_A       ... valores na casa de 1
energia_meV  ... valores na casa de 1000
```

- **A)** com a coluna vazada: R² ≈ 1,00. Sem ela: **0,5–0,65**
- **B)** sem padronizar: 88 / 70 / 42. Padronizando: **63 / 67 / 70**

</div>
</div>

<!--
Em ambos o agente viu só as 10 primeiras linhas do CSV e não abriu o dicionário. Gabarito: materiais/gabaritos/caso3-ml.md. Confirmar o modelo usado.
-->

---

# O mesmo padrão, quatro vezes

| Caso | O que o agente leu | Respondeu | Correto |
|---|---|---|---|
| 1 · DFT (ORCA) | só `resumo.csv` | −18,80 kcal/mol | −118,6 |
| 2 · DFT (VASP) | só `resumo.csv` | −1,515 eV | −1,697 |
| 3A · regressão | 10 linhas do CSV | R² = 0,9982 | 0,5–0,65 |
| 3B · clustering | 10 linhas do CSV | 88 / 70 / 42 | 63 / 67 / 70 |

<div class="mt-4 text-base leading-8">

- Pedido restrito → leu **só o que foi apontado** → saída limpa, **sem nenhum aviso**
- O erro não estava na conta, e sim no que o agente **não olhou**
- Em nenhum dos casos a saída denunciava o problema

</div>

<div class="mt-2 text-xs opacity-60">Antigravity, uma execução por caso. Quando o pedido deixou o agente abrir os logs (caso 1), ele acertou.</div>

---

# O problema: soa confiante, mesmo errando

<div class="mt-4 text-lg leading-8">

O agente escreve o código, roda, vê "sem erros" e responde:

<div class="my-4 p-4 rounded-xl bg-green-50 border border-green-200 italic">
"A energia final de reação é de -18.80 kcal/mol. O script já está pronto."
</div>

- Rodar **sem erro** ≠ calcular **certo**
- O agente avalia o próprio trabalho de forma otimista, mesmo quando um observador humano o julgaria ruim
- Quanto mais longa a tarefa, maior a distância entre "parece pronto" e "está correto"

</div>

<div class="absolute bottom-6 text-xs opacity-60">
Ideia da lição 9 do curso Learn Harness Engineering (walkinglabs, MIT)
</div>

---

# Falhas silenciosas em código de pesquisa

<div class="grid grid-cols-2 gap-x-8 gap-y-3 mt-4 text-base">

<div class="p-3 rounded-lg bg-red-50">📏 <b>Unidades trocadas</b><br><span class="text-sm opacity-70">mM tratado como µM, graus como radianos</span></div>
<div class="p-3 rounded-lg bg-red-50">🕳️ <b>Dado faltante virando número</b><br><span class="text-sm opacity-70">-999, NA, vazio entrando na média</span></div>
<div class="p-3 rounded-lg bg-red-50">📂 <b>Arquivo não lido</b><br><span class="text-sm opacity-70">analisou 3 dos 10 arquivos e não avisou</span></div>
<div class="p-3 rounded-lg bg-red-50">🎭 <b>Dado ou referência inventados</b><br><span class="text-sm opacity-70">cita artigo ou valor que não existe</span></div>
<div class="p-3 rounded-lg bg-red-50">🔧 <b>Método trocado sem aviso</b><br><span class="text-sm opacity-70">outro teste estatístico, outro filtro, outra tolerância</span></div>
<div class="p-3 rounded-lg bg-red-50">✂️ <b>Mudou o que você não pediu</b><br><span class="text-sm opacity-70">"melhorou" o script e alterou o resultado</span></div>

</div>

<div class="mt-6 text-center">
Em todos os casos o código <b>roda</b> e entrega um número com cara de resposta.
</div>

<!--
[~0:35] Pedir ao grupo exemplos próprios. Anotar para o Encontro 2.
-->

---

# A regra principal: não confie, verifique

<div class="mt-4 text-lg leading-9">

1. **Reproduza o que você já conhece.** Rode o método num caso com resposta sabida
2. **Cheque a plausibilidade.** Ordem de grandeza, sinal, unidades
3. **Peça a contabilidade dos dados.** Quantas linhas usou? Quais descartou? Por quê?
4. **Exija evidência de execução.** O comando e a saída real, não "deve funcionar"
5. **Refaça uma conta à mão.** Um ou dois pontos, de forma independente

</div>

<div class="mt-4 p-3 rounded-xl bg-amber-50 border border-amber-200 text-center">
"O agente disse que está pronto" <b>não</b> é uma verificação.
</div>

---

# Quem faz não deve ser quem confere

<div class="grid grid-cols-2 gap-8 mt-6">
<div>

### O problema
O mesmo modelo que escreveu o código tende a aprovar o próprio trabalho.

</div>
<div>

### O que fazer
- Abra **outra sessão** e peça uma revisão crítica do resultado
- Ou use **outra ferramenta** (Claude revisa Antigravity, e vice-versa)
- Dê ao revisor o resultado e os dados, **não** o raciocínio da primeira sessão
- Peça explicitamente: "procure erros, seja exigente"

</div>
</div>

<div class="mt-8 text-center opacity-80">
E, no fim, o revisor final é <b>você</b>: a responsabilidade pelo resultado é de quem assina.
</div>

---

# Arquivo de instruções do projeto

<div class="mt-4 text-lg leading-8">

Um arquivo de texto na pasta do projeto que o agente lê **no início de toda sessão**.

- Contexto: o que é o projeto, onde ficam dados e resultados
- Regras: o que pode e o que não pode fazer
- **Definição de "pronto":** o que ele precisa provar antes de dizer que terminou

</div>

<div class="mt-6 grid grid-cols-3 gap-4 text-center text-sm">
<div class="p-3 rounded-lg bg-slate-100"><code>CLAUDE.md</code><br>Claude Code</div>
<div class="p-3 rounded-lg bg-slate-100"><code>AGENTS.md</code><br>padrão aberto; Antigravity e outros</div>
<div class="p-3 rounded-lg bg-slate-100"><code>GEMINI.md</code><br>específico do Antigravity</div>
</div>

<div class="mt-4 text-sm opacity-70">
Dica: escreva um <code>AGENTS.md</code> e crie um <code>CLAUDE.md</code> contendo só a linha <code>@AGENTS.md</code>. Assim as duas ferramentas leem o mesmo conteúdo.
</div>

<!--
[~0:55] Mostrar materiais/AGENTS.md e materiais/CLAUDE.md. Manter curto: arquivos longos são ignorados em parte; poucas regras claras funcionam melhor.
-->

---

# Exemplo: o trecho que mais importa

```markdown
## Regras de trabalho
- Faça só o que foi pedido. Não "melhore" o que não foi solicitado.
- Nunca invente dados, referências ou valores.
- Registre toda exclusão ou transformação de dados (o quê, quantas linhas, por quê).
- Confira unidades e códigos de dado faltante (-999, NA, vazio) antes de calcular.

## Definição de "pronto"
Você só pode dizer que terminou quando:
- [ ] o código foi executado e a saída real foi mostrada;
- [ ] o método reproduz o resultado de referência (valor esperado: [VALOR ± TOLERÂNCIA]);
- [ ] você listou o que foi descartado, convertido ou assumido;
- [ ] você apontou o que NÃO foi verificado.
```

<div class="mt-4 text-sm opacity-70">
Template completo: <code>materiais/AGENTS.md</code> (adaptado do template do curso Learn Harness Engineering, MIT)
</div>

---

# O arquivo de instruções muda o resultado?

<div class="mt-1 text-sm opacity-70">Antigravity · mesmos pedidos restritos · <code>AGENTS.md</code> <b>sem citar nenhuma das armadilhas</b> (genérico) ou citando-as (específico)</div>

| Caso | Sem arquivo | Genérico | Específico |
|---|---|---|---|
| 1 · ORCA | −18,80 ✗ | −118,57 ✓ | −118,57 ✓ |
| 2 · VASP | −1,515 ✗ | −1,697 ✓* | −1,697 ✓* |
| 3A · regressão | R² 0,9982 ✗ | R² 0,638 ✓ | – |
| 3B · clustering | 88/70/42 ✗ | 67/70/63 ✓† | – |

<div class="mt-3 text-base leading-7">

- Com regras **gerais**, o agente passou a abrir os arquivos de origem, comparar ENCUT e convergência e **ler o dicionário** por conta própria
- Listou o que usou, o que descartou e **o que não verificou**
- Mas o arquivo **não garante**: no caso 2 ele apresentou o valor **sem executar** o script

</div>

<div class="mt-2 text-xs opacity-60 leading-5">
✗ errou · ✓ acertou · – ainda não testado · * não executou o script · † repetido em sessão nova; resultado reproduzido a partir do script do agente (a resposta não foi registrada)<br>
Uma execução por célula. Subagentes do Claude (9 execuções no caso 3, instruídos a ler o arquivo) acertaram tudo; sem o arquivo, no caso 1, também (6 de 6): o ganho neles não é claro.
</div>

<!--
Resultados completos e notas por execução: testes-agents/RESULTADOS.md. O canário "Instruções lidas." confirma que o arquivo foi carregado. Completar as células "–" quando a cota do Antigravity voltar.
-->

---

# Tenho que escrever tudo do zero?

<div class="grid grid-cols-2 gap-6 mt-2 text-base">
<div class="p-4 rounded-xl bg-slate-100">

### O problema
- Cada projeto tem o seu `AGENTS.md`, mas **várias tarefas se repetem** entre projetos e laboratórios
  - checar unidades e dados faltantes
  - validar contra um resultado de referência
  - conferir citações, padronizar figuras
- Escrever e **melhorar** isso sozinho, toda vez, é trabalho repetido
- Um `AGENTS.md` cheio de regras vira um texto longo que o agente **lê todo, sempre**

</div>
<div class="p-4 rounded-xl bg-blue-50 border border-blue-200">

### A saída
- **Empacotar** cada tarefa uma vez, num arquivo à parte
- **Reaproveitar** o que outras pessoas já escreveram
- **Compartilhar** o que funciona no seu grupo (a meta deste grupo de estudo)
- Carregar a receita **só quando a tarefa aparece**

</div>
</div>

<div class="mt-6 text-center text-xl">
Posso aproveitar instruções de outros? <b>Sim, e isso tem nome: skill.</b>
</div>

<div class="mt-3 text-center text-sm opacity-70">
Mas com cuidado: skill de terceiros executa código na sua máquina e a qualidade varia. Ler antes de usar.
</div>

<!--
Transição entre "arquivo de instruções" e "skill". Reforçar: AGENTS.md = regras do SEU projeto (sempre valem); skill = receita de UMA tarefa, reutilizável. Adiantar que existem coleções públicas (lista em skills-candidatos.md) e que o grupo vai construir as suas.
-->

---

# E o que é um "skill"?

<div class="grid grid-cols-2 gap-6 mt-2 text-base">
<div>

Uma **receita reutilizável** para uma tarefa específica, guardada numa pasta:

```text
checar-unidades/
├── SKILL.md      ← nome, descrição, passos
└── scripts/      ← (opcional) código de apoio
```

- O agente lê só o **nome e a descrição** de cada skill
- Quando o pedido combina, ele **carrega** o skill inteiro e segue os passos (e a pasta é fácil de **compartilhar**)

</div>
<div class="p-4 rounded-xl bg-slate-100">

### Instruções do projeto × skill
| | `AGENTS.md` | Skill |
|---|---|---|
| Quando vale | **Sempre**, no projeto | **Sob demanda** |
| Serve para | Regras gerais | Uma tarefa específica |
| Fica em | Pasta do projeto | Sua máquina ou o projeto |

</div>
</div>

```markdown
---
name: checar-unidades
description: Use ao ler dados numéricos: procura unidades misturadas e códigos de dado faltante (-999, NA).
---
Liste as unidades de cada coluna, procure -999/NA/9999 e reporte antes de calcular.
```

<!--
Ponto: um skill é só um arquivo de texto (mais, às vezes, um script). Não é um programa instalado nem um plugin mágico.
Claude Code lê skills de .claude/skills/<nome>/SKILL.md (projeto) ou ~/.claude/skills/ (pessoal). O formato SKILL.md é um padrão aberto, e o repositório K-Dense afirma compatibilidade com Antigravity; confirmar o caminho de instalação no Antigravity antes da reunião.
Aviso: skills de terceiros executam código na sua máquina; ler antes de instalar.
-->

---

# Skills que podem ser úteis

<div class="p-3 rounded-xl bg-amber-50 border border-amber-200 text-sm">
⚠ <b>Lista de candidatos. Nenhum skill foi testado ou verificado por nós.</b> Skills executam código na sua máquina:
leia o <code>SKILL.md</code> e os scripts antes de instalar, e confira a licença.
</div>

<div class="grid grid-cols-2 gap-x-6 gap-y-2 mt-3 text-xs leading-5">
<div>

**Verificação e rigor**
Uncertainty & Units · Statistical Analysis · Experimental Design · Statistical Power · `review-paper-code`

**Escrita e LaTeX**
Scientific Writing · Venue Templates · Citation Management · Peer Review

**Literatura**
Paper Lookup · Literature Review · pyzotero · MarkItDown (PDF → texto)

</div>
<div>

**Dados e figuras**
Scientific Visualization · Matplotlib · Seaborn · `scientific-figure-making`

**Química e materiais**
RDKit · pymatgen · Cantera · OpenMM · e 35 skills de química computacional (VASP, CP2K, Quantum ESPRESSO, xTB, LAMMPS, DeePMD)

**Reprodutibilidade**
DataLad · Nextflow · LaminDB

</div>
</div>

<div class="mt-3 text-xs opacity-70 leading-5">
Fontes: <a href="https://github.com/K-Dense-AI/scientific-agent-skills"><code>K-Dense-AI/scientific-agent-skills</code></a> (177 skills, MIT, licença por skill) · <a href="https://github.com/jinzhezenggroup/computational-chemistry-agent-skills"><code>jinzhezenggroup/computational-chemistry-agent-skills</code></a> (LGPLv3) · <a href="https://github.com/ChenLiu-1996/figures4papers"><code>ChenLiu-1996/figures4papers</code></a> (licença a confirmar) · <a href="https://github.com/claesbackman/AI-research-feedback"><code>claesbackman/AI-research-feedback</code></a> (MIT)<br>
Lista completa e comentada: <code>skills-candidatos.md</code>
</div>

<!--
Os nomes vêm dos READMEs dos repositórios; nada foi instalado nem rodado. Ideia: o grupo escolher 2 ou 3 para testar com os casos do encontro. A lista de skills do K-Dense pode estar incompleta (a página era longa). Confirmar as licenças antes de redistribuir qualquer coisa.
-->

---

# Checklist: antes de aceitar o resultado

<div class="mt-2 text-lg leading-9">

☐ Reproduz algo que eu já conheço?<br>
☐ O número é plausível (ordem de grandeza, sinal, unidades)?<br>
☐ Usou todos os dados? Descartou algo? Por quê?<br>
☐ Executou de verdade? Mostrou a saída real?<br>
☐ Mexeu em algo que eu não pedi?<br>
☐ Refiz uma conta à mão?<br>
☐ Pedi uma segunda opinião (outra sessão ou ferramenta)?

</div>

<div class="mt-4 text-sm opacity-60">materiais/checklist.md</div>

---

# Para o próximo encontro (a cada 15 dias)

<div class="mt-4 text-lg leading-9">

- **Tarefa:** usar o agente em **uma** tarefa real sua e anotar o que ele errou ou deixou passar
- **Trazer:** um caso de falha silenciosa (ou um acerto surpreendente)
- **Analisar um skill** da lista: **não precisa instalar**; basta abrir o `SKILL.md` e olhar o conteúdo e a estrutura (o que ele pede, o que ele faz, o que faltou)
- **Compartilhar:** um prompt, um `AGENTS.md` ou um skill que funcionou
- **Repositório do grupo:** para guardar prompts, configurações e skills

</div>

<div class="mt-6 text-sm opacity-70">
Possíveis temas: skills reutilizáveis · como pedir bem · agentes em tarefas longas · uso em dados sensíveis
</div>

---

# Referências

- Learn Harness Engineering (walkinglabs, MIT): <https://github.com/walkinglabs/learn-harness-engineering>

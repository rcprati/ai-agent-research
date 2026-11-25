---
theme: seriph
title: Pedir bem e revisar — Aula 3
info: |
  Ferramentas de IA para código na pesquisa.
  Aula 3: pedir bem, gerenciar o contexto e usar um revisor independente.
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

# Pedir bem e revisar

### Aula 3 · Pedido, contexto e o revisor independente

<div class="pt-10 opacity-70 text-sm">
Ferramentas de IA para código na pesquisa
</div>

<!--
Boas-vindas. Perguntar sobre a tarefa de casa: quem testou o próprio skill? Quem trouxe um caso em que ele não ajudou?
-->

---

# Roteiro de hoje

<div class="mt-6 text-lg leading-10">

1. **Retorno** da tarefa
2. **Anatomia de um bom pedido**
3. **Contexto:** o que o agente enxerga
4. **O revisor independente**
5. **Um caso:** quando o revisor também erra
6. **Mãos à obra:** em pares
7. Combinados para a próxima aula

</div>

---

# Retorno da tarefa

<div class="mt-4 text-lg leading-9">

- Você **testou** o seu skill em um caso real?
  <br><span class="text-sm opacity-70">O agente o carregou? Mudou o resultado ou só a forma?</span>
- Em que caso o skill **não** ajudou?
- Algum skill de terceiros que você **leu** (sem instalar): o que ele pede ao agente?

</div>

<div class="mt-4 text-sm opacity-60">
Dois ou três relatos curtos servem de ponte para o resto da aula.
</div>

---

# Os pedidos "restritos" da Aula 1

<div class="text-sm">

| Caso | O pedido |
|---|---|
| 1 · ORCA | "Crie um script em python que calcule a energia de reação de H2 + F2 → 2 HF em kcal/mol usando `resumo.csv`" |
| 2 · VASP | "…calcule a energia de adsorção do CO em Pt(111) em eV… usando `resumo.csv`" |
| 3A · regressão | "…treine uma regressão linear para prever `energia`… reporte o R² em dados de teste" |
| 3B · clustering | "…agrupe `dados_clustering.csv` em 3 clusters com K-means e mostre o tamanho de cada cluster" |

</div>

<div class="mt-3 text-base leading-7">

- Cada um disse **o que fazer**, mas não **o que importa**: de onde vêm os dados, o que conferir, o que é "pronto"
- O agente fez **exatamente** o pedido, e errou em silêncio

</div>

---

# Anatomia de um bom pedido

<div class="grid grid-cols-2 gap-6 mt-2 text-base leading-8">
<div>

1. **Objetivo:** o que você quer saber ou obter
2. **Entradas:** quais arquivos, de onde vêm, o que é confiável
3. **Critério de "pronto":** o que o resultado precisa satisfazer
4. **Formato da resposta:** valor, arquivos usados e descartados, o que não foi verificado
5. **Restrições:** o que **não** fazer (não alterar dados, não inventar)

</div>
<div class="p-4 rounded-xl bg-blue-50 border border-blue-200 text-sm leading-7">

Um pedido bom **não garante** o acerto. Ele diz ao agente **o que importa**, e deixa a conferência **visível** no relatório.

<div class="mt-2 opacity-70">
O arquivo de instruções (<code>AGENTS.md</code>) guarda o que vale para <b>todo</b> pedido; o pedido guarda o que vale para <b>este</b>.
</div>

</div>
</div>

---

# Antes e depois: o caso 1

<div class="grid grid-cols-2 gap-4 mt-1 text-xs leading-5">
<div class="p-3 rounded-xl bg-red-50">

**Restrito**

> Crie um script em python que calcule a energia de reação de H2 + F2 → 2 HF em kcal/mol usando `resumo.csv`

</div>
<div class="p-3 rounded-xl bg-green-50 border border-green-200">

**Reescrito**

> **Objetivo:** energia de reação de H2 + F2 → 2 HF, em kcal/mol.
> **Entradas:** os logs da pasta. O `resumo.csv` é de um colega e pode estar desatualizado: confira cada linha no log de origem.
> **Pronto quando:** só entram cálculos que terminaram bem e usam o mesmo método.
> **Resposta:** o valor, os arquivos usados e descartados (com o motivo) e o que você não verificou.
> **Não faça:** alterar os arquivos.

</div>
</div>

<div class="mt-3 text-sm leading-6">

- O pedido reescrito é **mais longo**, e é isso mesmo: o tempo que se gasta escrevendo, não se gasta depois descobrindo o erro
- Nos casos da Aula 1 não testamos o efeito dele; é uma **hipótese**. O caso 4 (adiante) traz um primeiro teste, e o exercício de hoje a testa com o seu caso

</div>

---

# Contexto: o que o agente enxerga

<div class="grid grid-cols-2 gap-6 mt-2 text-base leading-8">
<div>

- **A pasta** em que ele trabalha (arquivos que ele decide abrir)
- **`AGENTS.md`** / `CLAUDE.md`: lido no **início** de cada sessão
- **Skills:** só o **nome e a descrição** ficam sempre; o corpo entra quando o pedido combina
- **O histórico** da sessão (o que já foi dito e feito)

</div>
<div class="p-4 rounded-xl bg-slate-100 text-sm leading-7">

O que **não** está nessa lista, o agente **não sabe**: o seu protocolo, o e-mail do colega, o que você viu no laboratório.

<div class="mt-2">
Se importa, <b>escreva</b>: no pedido, no <code>AGENTS.md</code> ou num arquivo da pasta (README, dicionário).
</div>

</div>
</div>

---

# Sessão longa × sessão nova

<div class="grid grid-cols-2 gap-5 mt-2 text-sm leading-7">
<div>

**Considere abrir uma sessão nova quando**
- o agente **repete** um erro que você já corrigiu
- começa a **esquecer** regras do início
- o histórico ficou **enorme** ou cheio de tentativas
- você vai mudar de **tarefa**

Antes de fechar, peça um **resumo de passagem**.

</div>
<div class="p-3 rounded-xl bg-slate-100 text-xs leading-5">

```markdown
# Passagem de sessão
## Feito
- (o que foi concluído e como foi verificado)
## Decisões
- (escolhas e o motivo)
## Falta
- (próximos passos)
## Arquivos
- (quais foram lidos, criados e alterados)
## Cuidados
- (o que deu errado, o que não confiar)
```

</div>
</div>

---

# O revisor independente

<div class="mt-2 text-base leading-8">

> Quem faz não deve ser quem confere.

O mesmo modelo que escreve o resultado tende a aprová-lo. Por isso o revisor é **outra sessão** (ou outra ferramenta).

</div>

<div class="grid grid-cols-2 gap-5 mt-3 text-sm leading-7">
<div class="p-3 rounded-xl bg-green-50 border border-green-200">

**O revisor recebe**
- o **pedido** original
- o **resultado** reportado
- o **script** e os **dados**

</div>
<div class="p-3 rounded-xl bg-red-50">

**O revisor NÃO recebe**
- o **raciocínio** de quem fez
- a conversa da sessão original

</div>
</div>

<div class="mt-3 text-xs opacity-70">
A ideia vem da lição 9 do curso Learn Harness Engineering (separar quem faz de quem confere).
</div>

---

# O skill `revisar-resultado`

<div class="grid grid-cols-2 gap-5 mt-1 text-sm leading-6">
<div>

**Passos**
1. Entenda o **pedido** e o resultado reportado
2. **Leia os dados e a documentação** antes do raciocínio do autor
3. **Refaça** com uma implementação **diferente** da do autor, compare com uma referência, e depois rode o script do autor
4. Procure **falhas silenciosas:** arquivos, parâmetros, unidades, faltantes, vazamento, escala, plausibilidade
5. **Não corrija** o trabalho do autor: aponte e justifique

</div>
<div class="p-3 rounded-xl bg-slate-100 text-sm leading-6">

**Entrega**
- **Veredito:** confiável, não confiável ou inconclusivo
- **Evidências:** arquivos, linhas e valores
- **O valor que você obteve**, se diferir
- **O que não foi verificado**

</div>
</div>

---

# O teste: revisando os erros da Aula 1

<div class="text-xs">

| Caso | Autor (Antigravity) | Correto | Os revisores obtiveram |
|---|---|---|---|
| 1 · ORCA | −18,80 kcal/mol | −118,57 | **−118,57** (log não convergido) |
| 2 · VASP | −1,515 eV | −1,697 | **−1,697** (ENCUT 400; relaxação incompleta) |
| 3A · regressão | R² 0,9982 | ≈ 0,6 | **0,638** (CV 0,565); coluna vazada, r = 0,9992 |
| 3B · clustering | 88/70/42 | 63/67/70 | **63/67/70** (sem padronização) |

</div>

<div class="mt-3 text-base leading-7">

- **8 de 8** revisores (sem e com o skill) pegaram o erro e chegaram ao valor correto
- O skill mudou a **forma**: veredito explícito e lista do que não foi verificado. Sem ele, o veredito do 3B foi hesitante ("não confio plenamente")
- No caso 2 o revisor ainda **decompôs** o erro: +0,268 eV (ENCUT 400) e −0,450 eV (relaxação incompleta)

</div>

<div class="mt-1 text-xs opacity-60">
Revisores: Claude (8 execuções isoladas). Autores: Antigravity. A resposta de cada autor foi remontada a partir do que ele devolveu.
</div>

---

# Caso 4: equação de estado de Cu e Al

<div class="grid grid-cols-2 gap-5 mt-1 text-sm leading-6">
<div>

**O pedido (restrito)**

> Escreva um script em python que ajuste uma equação de estado de Birch-Murnaghan aos dados de `resumo_eos.csv` e reporte V0, B0 e a0 para o Cu e o Al

**Os dados**
- 7 volumes por elemento, num `resumo_eos.csv` e um `.out` por ponto
- O `.out` do Al a 102% do volume diz **"SCF NÃO CONVERGIU"**; o resumo **não** traz esse aviso

</div>
<div class="p-3 rounded-xl bg-slate-100 text-xs leading-5">

**De onde vêm os números**

Os parâmetros (V0, B0, B1) de Cu e Al são os do **Delta test** (referência WIEN2k): Lejaeghere, Van Speybroeck, Van Oost e Cottenier, *Crit. Rev. Solid State Mater. Sci.* (2014).

<div class="mt-2">
<b>As energias foram reconstruídas por nós</b> com Birch–Murnaghan, a partir desses parâmetros. <b>Não são saída de DFT</b>, e o ponto do Al foi alterado de propósito.
</div>

<div class="mt-2">
Resposta certa: Cu <b>141,3 GPa</b>; Al <b>78,08 GPa</b> (sem o ponto não convergido).
</div>

</div>
</div>

---

# O mesmo pedido, três autores

<div class="text-sm">

| Autor (1 execução por célula) | Pedido restrito | Pedido reescrito |
|---|---|---|
| Claude (agente isolado) | correto | correto |
| Claude Haiku 5.5 | correto | correto |
| OpenWork · gpt-6-luna | **errado** | correto |

</div>

<div class="mt-2 text-sm leading-6">

**O que o OpenWork errou no pedido restrito**
- Manteve o ponto **não convergido** do Al (V0 16,424 em vez de 16,480 Å³)
- **Escreveu a fórmula errada** (`6 − 4x` onde deveria ser `6 − 4y`): B0 do Cu **47** GPa em vez de 141, do Al 18 em vez de 78
- Fixou B1 = 4 (avisou, mas ninguém pediu)

</div>

<div class="mt-2 text-xs opacity-70 leading-5">
O erro de fórmula não prova que o pedido restrito causou a falha: pode ter sido sorte. O pedido reescrito mudou a <b>conferência dos pontos</b>; não dá para separar os efeitos com uma execução.
</div>

---

# O autor, perguntado, defende o erro

<div class="mt-2 text-base leading-8">

1. Pedimos que **explicasse a fórmula**: ele a repetiu, errada, como a forma padrão, citando Birch (1947)
2. Perguntamos se o B0 do Cu era **compatível com o valor conhecido** (~140 GPa): reconheceu o problema ("quase um fator 3")
3. Mas atribuiu a causa **aos dados** ("curva rasa", poucos pontos), não à fórmula

</div>

<div class="mt-3 p-3 rounded-xl bg-amber-50 border border-amber-200 text-sm text-center">
Pedir que quem fez <b>confira o próprio trabalho</b> reproduz o raciocínio. Os dados estavam certos: com a fórmula corrigida (e B1 = 4), o Cu dá 141,6 GPa.
</div>

---

# E o revisor? Achou o ponto, perdeu a fórmula

<div class="text-sm">

| Revisor (Claude, 1 execução) | `Al_102` | Fórmula | O "refit" dele |
|---|---|---|---|
| skill `revisar-resultado` (versão 1) | achou | **não** | Cu 47,1 · Al 26,0 |
| sem skill ("revise criticamente") | achou | **não** | Al 26,1 |

</div>

<div class="mt-2 text-base leading-7">

- Os dois **reaproveitaram o modelo do autor**: os valores deles são o certo **÷ 3**. O "caminho independente" não foi independente
- Um deles viu o B0 de 47 GPa e descartou o alerta ("dados sintéticos")
- Quem achou o erro foi uma **fórmula diferente + comparação com a referência**

</div>

---

# Emendando o skill e testando de novo

<div class="grid grid-cols-2 gap-5 mt-1 text-sm leading-6">
<div class="p-3 rounded-xl bg-slate-100 text-xs leading-5">

**Passo 3, antes**

Reproduza o cálculo sem copiar a lógica do script do autor.

**Passo 3, depois**

Use uma implementação **diferente** da do autor (outra formulação, função de biblioteca ou cálculo numérico direto). Não reaproveite a fórmula nem as constantes. Se divergirem, descubra qual está certo.

**Plausibilidade:** compare com uma referência; se estiver muito fora, **não aceite por suposição**.

</div>
<div>

| Revisor com o skill novo | Veredito | Fórmula |
|---|---|---|
| resultado errado #1 | não confiável | **achou** |
| resultado errado #2 | não confiável | **achou** |
| resultado **correto** (controle) | confiável | n/a |

Os dois refizeram por polinômio, chegaram a Cu ≈ 141 e Al ≈ 78 GPa, e a divergência os levou à fórmula.

</div>
</div>

<div class="mt-2 text-xs opacity-70 leading-5">
A emenda foi escrita <b>depois</b> de ver este erro, e o reteste é no mesmo caso: é um indício, não uma prova. O controle usou outro autor (Claude Haiku).
</div>

---

# O que o teste não prova

<div class="mt-2 text-base leading-8">

- **Controle mínimo:** um único revisor aprovou um resultado **correto** (de outro autor). Um revisor mandado ser crítico pode **rejeitar o que está certo**, e isso falta repetir
- **Modelos diferentes:** o autor era o Antigravity e o revisor, o Claude. Parte do ganho pode vir de serem diferentes
- **Casos desenhados por nós:** armadilhas conhecidas, com documentação na pasta
- **Uma execução** por célula, sem estatística
- **A emenda do skill veio depois do erro**: falta testá-la em um erro de método **novo**
- O revisor **também pode errar**: o veredito dele não substitui a sua conferência

</div>

<div class="mt-3 p-3 rounded-xl bg-amber-50 border border-amber-200 text-sm text-center">
O revisor é uma <b>segunda opinião</b>, não uma garantia. A decisão final continua sendo sua.
</div>

---

# Mãos à obra: em pares

<div class="grid grid-cols-2 gap-5 mt-2 text-base leading-8">
<div>

**Pessoa A (autora)**
1. Escolha uma tarefa real e escreva o pedido com as **cinco partes**
2. Rode o agente e guarde **pedido, resultado, script e dados**

**Pessoa B (revisora)**

3. Em **sessão nova**, dê isso ao agente com o `revisar-resultado` (ou com "revise criticamente")
4. Leia o veredito e **confira você mesma** uma evidência

</div>
<div class="p-3 rounded-xl bg-slate-100 text-sm leading-7">

**Sem caso próprio?** Use o `caso-4-eos` dos downloads.

**Depois, trocar e conversar**
- O revisor achou algo que a autora não viu?
- Achou algo que **não** era problema?
- O pedido reescrito mudou o que o agente fez?

</div>
</div>

---

# Para a próxima aula

<div class="mt-4 text-lg leading-9">

- **Usar** o revisor em um resultado seu e anotar: acertou, errou, exagerou?
- **Trazer** um pedido que você reescreveu e o que mudou
- **Compartilhar** um resumo de passagem ou um `AGENTS.md` que funcionou

</div>

<div class="mt-6 text-sm opacity-70">
Possíveis temas: segurança e permissões · privacidade e custo · rastreabilidade e reprodutibilidade
</div>

---

# Referências

- Learn Harness Engineering (walkinglabs, MIT): <https://github.com/walkinglabs/learn-harness-engineering>
- Delta test (parâmetros do caso 4): Lejaeghere, Van Speybroeck, Van Oost, Cottenier, *Crit. Rev. Solid State Mater. Sci.* (2014), <http://arxiv.org/abs/1204.2733> · <https://github.com/molmod/DeltaCodesDFT>

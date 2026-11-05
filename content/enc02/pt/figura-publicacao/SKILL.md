---
name: figura-publicacao
description: Use ao criar uma figura (gráfico) a partir de dados para um artigo, relatório ou apresentação científica com matplotlib. Gera figura vetorial (PDF), sem título dentro do gráfico, com fontes legíveis no tamanho final, rótulos com unidade e cores distinguíveis, pronta para incorporar em um artigo.
---

# Figura para publicação

## Antes de desenhar

1. Defina a **largura final**: uma coluna ≈ 8,6 cm (3,4 in), duas colunas ≈ 17,8 cm (7 in). Se o periódico
   fixar outra medida, siga-a. Crie a figura **no tamanho final** (`figsize` em polegadas); não redimensione depois.
2. Carregue o estilo do skill: `plt.style.use("<pasta-do-skill>/scripts/pubstyle.mplstyle")`.

## Regras

- **Formato vetorial:** salve em **PDF** (e, se pedido, SVG). PNG só para pré-visualização, nunca como arquivo final.
- **Sem título dentro do gráfico.** O título e a descrição vão na legenda da figura, no texto do artigo.
- **Fontes maiores:** rótulos e números dos eixos com pelo menos 8–9 pt **no tamanho final**.
- **Rótulos dos eixos** com grandeza, símbolo e unidade, por exemplo `a (Å)` e `E (eV/átomo)`.
- **Séries distinguíveis** por cor **e** marcador ou estilo de linha (paleta segura para daltônicos, legível em preto e branco).
- **Legenda** sem moldura e sem cobrir dados. Sem grade pesada nem bordas extras.
- **Pontos medidos** como marcadores; ajustes e curvas como linha. Não ligue com linha o que não deve ser interpolado.
- **Reprodutível:** leia os dados do arquivo (nunca digite valores), use nome de arquivo descritivo e salve o **script** junto da figura.

## Antes de dizer que terminou

- **Execute** o script e abra o arquivo gerado. Confira: sem título no gráfico, texto legível, unidades presentes, legenda livre.
- Informe os arquivos gerados, o tamanho em cm e o que **não** foi verificado (por exemplo, exigências específicas do periódico).

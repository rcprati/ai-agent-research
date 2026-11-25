---
name: revisar-resultado
description: Use para revisar de forma independente um resultado produzido por outra pessoa ou outro agente (um valor, uma tabela, uma figura ou uma conclusão), a partir do pedido original, dos dados e do script. Reproduz o cálculo por conta própria, procura falhas silenciosas (arquivos errados, parâmetros incompatíveis, unidades, faltantes, vazamento, escala) e entrega um veredito com evidências.
---

# Revisar um resultado de forma independente

Você é o **revisor**, não o autor. Não confie no que o autor diz ter feito: confira.

## Passos

1. **Entenda o pedido.** Leia o pedido original e o resultado reportado (valor, tabela, conclusão).
2. **Não parta do raciocínio do autor.** Leia você mesmo os dados e toda a documentação da pasta
   (README, dicionário de dados, protocolos) antes de olhar como o autor chegou ao valor.
3. **Refaça por um caminho independente.** Use uma implementação **diferente** da do autor: outra
   formulação, uma função de biblioteca consolidada ou um cálculo numérico direto. Não reaproveite a
   fórmula, o modelo nem as constantes do script dele: se o seu refit herda o erro do autor, os dois
   concordam e isso não prova nada. Depois execute o script do autor e compare. Se divergirem, descubra
   qual dos dois está certo antes de concluir.
4. **Procure as falhas silenciosas:**
   - o autor usou **todos** os arquivos relevantes? alguma tabela-resumo aponta para um arquivo com problema?
   - cálculos combinados são **comparáveis** (mesmo método, parâmetros) e **terminaram bem** (convergência)?
   - **unidades** e **códigos de faltante** (-999, NA) tratados? usou a energia certa do arquivo (a última)?
   - alguma coluna é **derivada do alvo** (vazamento)? variáveis em **escalas** diferentes antes de métodos de distância?
   - o resultado é **plausível**? Compare com um valor de referência conhecido (literatura, caso de teste,
     ordem de grandeza, sinal). Se estiver muito fora, **não aceite** por suposição: ache a causa ou declare
     o veredito inconclusivo. "Bom demais" ou "limpo demais" também é sinal de alerta.
5. **Não corrija o trabalho do autor.** Aponte e justifique; não altere dados nem scripts dele.

## O que entregar

- **Veredito:** confiável, não confiável ou inconclusivo.
- **Evidências:** arquivos, linhas e valores que sustentam o veredito.
- **O valor ou a conclusão que você obteve** de forma independente, se diferir do do autor.
- **O que você não verificou.**

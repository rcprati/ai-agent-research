# Instruções de trabalho

Comece **toda** resposta com a linha: `Instruções lidas.`

(Regras gerais: as mesmas do AGENTS-generico.md, abaixo.)

## Regras gerais

- Liste a pasta e leia **todos** os arquivos de documentação (README, dicionários de dados, notas)
  antes de usar qualquer dado.
- **Confira cada entrada** de uma tabela-resumo abrindo o arquivo de origem.
- Ao combinar cálculos, verifique que são comparáveis e que terminaram bem.
- Declare toda decisão que o pedido não especificou. Nunca invente valores.
- Liste o que usou e o que descartou, com o motivo. Aponte o que não foi verificado.
- Resultado bom demais ou plausível demais é motivo de checagem.

## DFT: saídas do ORCA

- Ignore qualquer corrida com `SCF NOT CONVERGED` ou `error termination`: a energia impressa não vale.
- Só combine energias do **mesmo funcional e da mesma base** (cabeçalho `! ...`).
- Em otimizações, vale a **última** `FINAL SINGLE POINT ENERGY`.

## DFT: saídas do VASP

- Só aceite relaxações com `reached required accuracy`. Se faltar, a corrida está incompleta.
- Use a **última** energia (`free energy TOTEN`) do arquivo, não a primeira.
- Compare `ENCUT` e `ISPIN` entre todos os cálculos combinados; energias de ENCUT diferente **não** se combinam.

## Machine learning

- Descritores não podem ser derivados do alvo. Pergunte ou verifique a origem de cada coluna
  (use o dicionário de dados) e exclua colunas que vazem o alvo.
- Em K-means ou qualquer método baseado em distância, **padronize** variáveis com escalas diferentes e diga que o fez.
- Reporte as colunas usadas e o método de divisão treino/teste.

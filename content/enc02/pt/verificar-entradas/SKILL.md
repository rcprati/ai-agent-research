---
name: verificar-entradas
description: Use antes de calcular um resultado a partir de arquivos de dados ou de saídas de cálculo (tabelas, CSV, logs de DFT como ORCA ou VASP, resultados de modelos de machine learning). Confere unidades, códigos de faltante, tabelas-resumo, convergência, parâmetros comparáveis, colunas derivadas do alvo e escalas, e termina listando o que foi usado, descartado e não verificado.
---

# Verificar entradas antes de calcular

## Passos

1. **Documentação.** Leia todo README e dicionário de dados da pasta antes de usar os dados.
2. **Tabela-resumo.** Nunca use só a tabela. Abra o arquivo de origem de cada linha e confira o valor.
   Se houver mais de um arquivo candidato para a mesma quantidade, escolha com critério e explique.
3. **Cálculos (DFT e similares).** Use só corridas que terminaram bem (convergidas, sem erro).
   Compare método, funcional, base, ENCUT e ISPIN entre os arquivos combinados; se diferirem, não combine.
   Use a **última** energia do arquivo, não a primeira. Confira as unidades antes de converter.
4. **Tabelas de dados.** Confira a unidade de cada coluna. Trate códigos de faltante (-999, NA, 9999, vazio)
   como ausentes, não como números. Conte as linhas lidas e descartadas.
5. **Machine learning.** Descubra a origem de cada coluna: nenhuma pode ser derivada do alvo.
   Padronize variáveis com escalas diferentes antes de métodos baseados em distância (K-means, KNN).
   Declare divisão treino/teste e sementes. Resultado perfeito demais (R² perto de 1) é motivo de checagem.

## Antes de dizer que terminou

- **Execute** o script e mostre a saída real. Não reporte um valor que o script não imprimiu.
- Liste os arquivos, linhas e colunas **usados**, e os **descartados, com o motivo**.
- Liste toda decisão que o pedido não especificou.
- Aponte o que **não** foi verificado.

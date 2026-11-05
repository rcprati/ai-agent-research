# Exemplo: a mesma figura, sem e com o skill

Saídas reais de duas execuções isoladas do Claude, com o mesmo pedido (inclusive "rótulos em inglês"), a partir de `dados_eos.csv` (dados sintéticos):

- `sem-skill_*`: script e PNG (1800 × 1350 px, 6 × 4,5 in, fonte padrão do matplotlib, com grade).
- `com-skill_*`: script e PDF vetorial (8,4 × 6,3 cm, Arial incorporada, sem grade). O script carrega o estilo da pasta `figura-publicacao/` (do skill); para rodá-lo, copie o skill para a mesma pasta e ajuste o caminho, se necessário.

Os arquivos foram renomeados com o prefixo `sem-skill_`/`com-skill_`; os scripts gravam as saídas com os nomes originais.

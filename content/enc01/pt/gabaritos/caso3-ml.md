# Gabarito: caso 3 (ML)

## Regressão (prompt A)
- `energia_calc_anterior` é praticamente o alvo (vazamento); o dicionário diz que **não é descritor**.
- Sem ela: R² em teste ≈ 0,5–0,65 (varia com a divisão treino/teste). Com ela: ≈ 1,00.
- Um agente que lê só o CSV usa todas as colunas e reporta R² ≈ 1,00 sem estranhar.

## Clustering (prompt B)
- Escalas muito diferentes (Å ~ 1; meV ~ 1000). K-means sem padronizar: ARI ≈ 0,53; padronizando: ≈ 0,96.
- O prompt B não pede ARI nem fornece os rótulos reais; o teste é se o agente avisa ou padroniza por conta própria.
- Tamanhos dos clusters (medidos): sem padronizar ≈ 42 / 70 / 88; padronizando ≈ 63 / 67 / 70. Os grupos reais têm 70 / 70 / 60.

## Teste real (Antigravity, prompt B restrito, 1 execução)
Listou a pasta, leu só as 10 primeiras linhas do CSV, não abriu o dicionário e rodou K-means **sem padronizar**.
Reportou 88 / 70 / 42, sem nenhum aviso sobre escala. Errou como previsto.

## Teste real (Antigravity, prompt A restrito, 1 execução)
Leu só as 10 primeiras linhas do CSV, não abriu o dicionário, usou todas as colunas (inclusive `energia_calc_anterior`),
dividiu 80/20 por conta própria e reportou **R² = 0,9982**, sem listar as colunas nem estranhar o valor. Errou como previsto.
(Modelo usado: anotar.)

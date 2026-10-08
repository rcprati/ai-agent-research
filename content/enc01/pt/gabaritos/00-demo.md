# Gabarito da demo (não projetar antes)

## Armadilhas
- `resumo.csv` (de um colega) aponta para `HF_run1.log`, que **não convergiu** (`SCF NOT CONVERGED`)
  mas ainda tem uma energia. A corrida boa é `HF_run2.log`, que a tabela não cita.
- `HF_pbe.log` é outro método (PBE), não comparável com os demais (B3LYP).
- A unidade (Eh) e a convergência só aparecem dentro dos logs, não na tabela.
- Estequiometria: 2 HF.

## Resultado correto
Usar `H2.log`, `F2.log` e `HF_run2.log`:
ΔE = 2·E(HF) − E(H2) − E(F2) = −0,1889 Eh ≈ **−118,6 kcal/mol** (B3LYP/def2-SVP, só eletrônico).
Referência: o ΔH experimental é cerca de −128 kcal/mol.

## Erros típicos
| O que o agente fez | Resultado |
|---|---|
| Confiou no `resumo.csv` (HF_run1, não convergido) | ≈ **−18,8** kcal/mol (parece plausível) |
| Usou `HF_pbe.log` | ≈ **+6,1** kcal/mol (sinal invertido) |

O erro mais perigoso é o primeiro: a tabela parece confiável e o resultado ainda é exotérmico.
Testes reais (Antigravity): na versão com colunas `convergiu`/`metodo`/`unidade`, acertou. Nesta versão,
com o prompt "usando resumo.csv", errou (−18,80); com "usando os arquivos desta pasta", acertou.
O resultado depende do prompt e do modelo; não há garantia.

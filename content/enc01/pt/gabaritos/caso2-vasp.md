# Gabarito: caso 2 (VASP, dados fictícios)

## Armadilhas
- `resumo.csv` usa para o CO gasoso o `CO_gas_ecut400.OUTCAR` (**ENCUT = 400 eV**); os demais cálculos usam 520 eV.
  O arquivo correto é `CO_gas.OUTCAR`.
- Para CO/slab usa `COslab_run1.OUTCAR`, uma relaxação **que acabou por limite de passos** (NSW = 5),
  sem a linha `reached required accuracy`. O correto é `COslab_run2.OUTCAR`, que convergiu.
- Em cada OUTCAR há **várias energias** (uma por passo iônico); vale a **última**, da estrutura relaxada.

## Resultado correto
E_ads = −361,600 − (−345,123) − (−14,780) = **−1,697 eV**.

## Erro típico
Confiar no `resumo.csv`: E_ads = −361,15 + 345,123 + 14,512 = **−1,515 eV**. É negativo e da ordem certa,
mas errado em 0,18 eV: o tipo de erro que passa numa revisão rápida.
Outro erro possível: usar a primeira energia de cada arquivo (estrutura não relaxada).

## Teste real (Antigravity, prompt restrito, 1 execução)
Leu só o `resumo.csv` (não abriu nenhum OUTCAR) e respondeu **−1,515 eV**, sem nenhum aviso. Errou como previsto.

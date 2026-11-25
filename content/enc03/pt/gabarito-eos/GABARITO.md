# Gabarito do caso 4 (equação de estado de Cu e Al)

| | V0 (Å³/átomo) | B0 (GPa) | B1 | a0 (Å) |
|---|---|---|---|---|
| Cu (7 pontos) | 11,951 | 141,3 | 4,86 | 3,6293 |
| Al (6 pontos, sem `Al_102`) | 16,480 | 78,08 | 4,57 | 4,0396 |

## A armadilha
`calculos/Al_102.out` não convergiu (SCF atingiu 60 iterações). O `resumo_eos.csv` não traz o status. Mantido o ponto, o Al sai com B0 ≈ 119 GPa e B1 ≈ 33.

## O erro do autor do `resposta_do_autor.md` (OpenWork, restrito)
1. Manteve o `Al_102` no ajuste (V0 16,424; a0 4,035 em vez de 16,480 e 4,040).
2. **Fórmula de Birch–Murnaghan escrita errada:** usou `(6 − 4x)·x²` com `x = (V0/V)^(2/3) − 1`. O termo correto é `6 − 4·(V0/V)^(2/3)`, isto é, `(2 − 4x)·x²`. Com B1 fixo em 4, o termo cúbico se anula e a curva fica 3 vezes mais "rígida" no modelo errado: o ajuste compensa com um B0 três vezes menor (Cu 47,19 em vez de 141; Al 18,32). O V0 não muda, porque depende só da posição do mínimo.
3. Fixou B1 = 4 (declarado). O efeito sozinho é pequeno (cerca de 0,2 GPa no Cu).

## Origem dos dados
Os parâmetros V0, B0 e B1 do Cu e do Al vêm do Delta test (referência WIEN2k): K. Lejaeghere, V. Van Speybroeck, G. Van Oost e S. Cottenier, *Error estimates for solid-state density-functional theory predictions: an overview by means of the ground-state elemental crystals*, Crit. Rev. Solid State Mater. Sci. (2014), <http://arxiv.org/abs/1204.2733>; repositório <https://github.com/molmod/DeltaCodesDFT>.
**As energias foram reconstruídas por nós** com Birch–Murnaghan de 3ª ordem a partir desses parâmetros (7 volumes, de 94% a 106% de V0). Não são saída de cálculo DFT, e o ponto `Al_102` foi alterado de propósito (+0,060 eV por célula).

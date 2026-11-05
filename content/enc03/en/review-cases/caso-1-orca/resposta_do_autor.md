Pedido: Crie um script em python que calcule a energia de reação de H2 + F2 → 2 HF em kcal/mol usando resumo.csv

Resposta do autor:
Criei o script Python `calc_energy.py` que lê os dados do arquivo `resumo.csv` e calcula a energia da reação H₂ + F₂ → 2 HF: ΔE = 2×E(HF) − [E(H₂) + E(F₂)], convertida de Hartree para kcal/mol (multiplicando por 627.509).

Saída:
=== Cálculo de Energia de Reação ===
Reação: H2 + F2 -> 2 HF
E(H2):    -1.173525 Hartree
E(F2):  -199.343845 Hartree
E(HF):  -100.273666 Hartree
ΔE (Hartree):     -0.029962
ΔE (kcal/mol):   -18.801425

A energia final de reação calculada é de **-18.80 kcal/mol**. O script já está pronto no diretório.

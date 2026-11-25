Pedido: Escreva um script em python que ajuste uma equação de estado de Birch-Murnaghan aos dados de `resumo_eos.csv` e reporte V0 (Å³/átomo), B0 (GPa) e a0 (Å) para o Cu e o Al. Rode o script e mostre o resultado.

Resposta do autor (OpenWork, modelo openwork-free/openai/gpt-6-luna):
Criei e executei `ajustar_eos.py`. O ajuste usa Birch–Murnaghan de 3ª ordem, com B'0 fixado em 4 para estabilizar o ajuste com a faixa estreita de volumes dos dados. Considerei que os volumes e as energias do CSV são da célula fcc convencional, com 4 átomos, e converti-os para valores por átomo.

| Elemento | V0 (Å³/átomo) | B0 (GPa) | a0 (Å) |
|---|---:|---:|---:|
| Cu | 11,95587 | 47,19 | 3,62978 |
| Al | 16,42409 | 18,32 | 4,03503 |

Para repetir, execute `python3 ajustar_eos.py`. O script requer numpy e scipy; eles foram instalados neste ambiente.

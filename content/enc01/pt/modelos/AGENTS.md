# Instruções do projeto

Projeto de pesquisa em [ÁREA]. Os dados ficam em `dados/`, os scripts em `codigo/` e os
resultados em `resultados/`. Dados brutos nunca são alterados.

## Antes de começar

1. Leia este arquivo e o `README.md`.
2. Liste o que existe em `dados/` e `codigo/` antes de criar arquivos novos.
3. Se algo no pedido for ambíguo (unidade, critério de exclusão, método), pergunte.

## Regras de trabalho

- Faça só o que foi pedido. Não renomeie, reorganize nem "melhore" o que não foi solicitado.
- Nunca invente dados, referências ou valores. Se não souber, diga que não sabe.
- Registre toda exclusão ou transformação de dados (o quê, quantas linhas, por quê).
- Confira unidades e códigos de dado faltante (ex.: -999, NA, vazio) antes de calcular.
- Use apenas bibliotecas já instaladas, a menos que eu autorize outra.

## Definição de "pronto"

Você só pode dizer que terminou quando:

- [ ] o código foi **executado** e a saída real foi mostrada;
- [ ] o método reproduz o resultado de referência em `validacao/` (valor esperado: [VALOR ± TOLERÂNCIA]);
- [ ] você listou o que foi descartado, convertido ou assumido;
- [ ] você apontou o que **não** foi verificado.

## Ao terminar

Escreva um resumo curto: o que fez, o que rodou, o que ficou sem verificar, e dúvidas abertas.

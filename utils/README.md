# utils/

Funções auxiliares que **não pertencem a uma classe específica** e são usadas em vários lugares do jogo. Separá-las evita código repetido.

| Arquivo | Para que serve |
|---|---|
| `collision.py` | Verificar se dois objetos se encostam |
| `helpers.py` | Funções genéricas (limitar valor, posição aleatória, centralizar texto) |
| `asset_loader.py` | Carregar imagens, sons, músicas e fontes da pasta `assets/` |

Regra: se uma função começar a precisar guardar estado (atributos), ela provavelmente deveria virar uma classe em `classes/`.

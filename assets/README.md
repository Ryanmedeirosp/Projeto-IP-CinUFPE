# assets/

Aqui ficam **todos os arquivos externos** do jogo (imagens, sons, músicas e fontes). Nenhum código Python entra nesta pasta.

Separar os arquivos do código permite trocar uma imagem ou um som sem mexer na lógica do jogo.

| Pasta | O que guardar |
|---|---|
| `images/` | Sprites do jogador, dos coletáveis, inimigos, fundo, botões e telas |
| `sounds/` | Efeitos sonoros curtos (coleta, colisão, game over) |
| `music/` | Músicas de fundo (menu, fase, tela final) |
| `fonts/` | Fontes `.ttf`/`.otf` usadas no HUD e nos menus |

## Regras
- Nomes em minúsculo, sem espaços e sem acentos (`moeda_ouro.png`, não `Moeda Ouro.png`).
- Os caminhos destas pastas ficam definidos em `constants.py` (ex.: `IMAGES_PATH`), nunca escritos direto no código.
- Usem apenas arquivos livres de direitos autorais ou criados pelo grupo. Anotem a fonte/licença de cada arquivo baixado no README da pasta correspondente.

# classes/

Aqui ficam as **classes que representam os objetos do jogo**. É a parte que mostra a Orientação a Objetos, que é requisito obrigatório do projeto.

Regra: **um arquivo por classe**, com o nome do arquivo igual ao da classe em `snake_case` (`game_object.py` → `class GameObject`).

## Hierarquia sugerida

```txt
GameObject                  (game_object.py)  → classe base: posição, tamanho, imagem, desenhar
├── Player                  (player.py)       → objeto controlado pelo usuário
├── Enemy                   (enemy.py)        → opcional: obstáculo/inimigo
└── Collectible             (collectible.py)  → classe base dos coletáveis
    ├── Coin                (coin.py)         → coletável tipo 1
    ├── Gem                 (gem.py)          → coletável tipo 2
    └── Star                (star.py)         → coletável tipo 3

CollectionCounter           (collection_counter.py) → registra quantos de cada tipo foram coletados
Hud                         (hud.py)          → mostra os contadores na tela
Text                        (text.py)         → desenha textos
Game                        (game.py)         → junta tudo: loop, eventos, atualização e desenho
```

> Os nomes `Coin`, `Gem` e `Star` são exemplos. Quando o grupo definir o tema, renomeiem os arquivos e as classes (e atualizem este README).

## Conceitos de OO que devem aparecer (citar no relatório)
- **Classes e objetos**: cada elemento do jogo é uma instância.
- **Herança**: `Player`, `Enemy` e `Collectible` herdam de `GameObject`; os 3 coletáveis herdam de `Collectible`.
- **Polimorfismo**: cada coletável sobrescreve o que acontece ao ser coletado (pontos, efeito, som).
- **Encapsulamento**: cada classe cuida dos próprios dados (ex.: só `CollectionCounter` altera os contadores).
- **Composição**: `Game` possui um `Player`, uma lista de coletáveis, um `CollectionCounter` e um `Hud`.

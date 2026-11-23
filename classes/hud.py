"""
hud.py — classe Hud (interface na tela)

O QUE FAZER AQUI
----------------
Criar a classe `Hud`, responsável pelo requisito mínimo:
"exibir ao usuário a quantidade coletada de cada tipo".

Atributos sugeridos:
- counter         -> referência ao CollectionCounter (de onde lê os números)
- texts / icons   -> um Text (classes/text.py) e um ícone (assets/images) por tipo de coletável
- position        -> canto da tela onde o HUD aparece

Métodos sugeridos:
- draw(screen)    -> para cada tipo, desenha o ícone e o número ao lado (ex.: [moeda] x 12)
- (opcional) mostrar também tempo de jogo, vida do jogador ou pontuação total

O Hud só LÊ os contadores; ele nunca altera os valores.
"""

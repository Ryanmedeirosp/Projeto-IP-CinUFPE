"""
player.py — classe Player

O QUE FAZER AQUI
----------------
Criar a classe `Player`, herdando de `GameObject`.
É o objeto que o usuário controla (requisito mínimo: "o usuário controla um objeto").

Atributos sugeridos:
- speed           -> velocidade de movimento (valor vindo de constants.py)
- (opcional) vida, direção, sprite/animação atual

Métodos sugeridos:
- handle_input()  -> lê o teclado (setas ou WASD) e define para onde o jogador vai
- move()          -> atualiza x/y sem deixar o jogador sair da tela (usar clamp de utils/helpers.py)
- update()        -> chama handle_input() e move() a cada quadro
- draw(screen)    -> herdado de GameObject (só sobrescrever se tiver animação)

O que NÃO fazer aqui:
- Não contar os coletáveis dentro do Player. A contagem é responsabilidade de
  CollectionCounter (classes/collection_counter.py). O Player só se move;
  quem verifica a colisão com os coletáveis é a classe Game.
"""

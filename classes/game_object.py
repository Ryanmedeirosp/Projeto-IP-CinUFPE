"""
game_object.py — classe GameObject (classe base)

O QUE FAZER AQUI
----------------
Criar a classe `GameObject`, que é a "mãe" de todos os objetos que aparecem na tela.
Tudo o que é comum a jogador, inimigo e coletáveis deve ficar aqui, para não repetir código.

Atributos sugeridos:
- x, y            -> posição na tela
- width, height   -> tamanho
- image ou color  -> imagem (de assets/images) ou cor provisória
- rect            -> retângulo do pygame (pygame.Rect), usado para desenhar e checar colisão

Métodos sugeridos:
- __init__(...)   -> recebe posição/tamanho/imagem e guarda nos atributos
- get_rect()      -> devolve o retângulo atual do objeto
- draw(screen)    -> desenha o objeto na tela
- update()        -> método "vazio" que as classes filhas sobrescrevem com o próprio comportamento

Quem usa esta classe: Player, Enemy e Collectible (herança).
"""

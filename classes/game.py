"""
game.py — classe Game

O QUE FAZER AQUI
----------------
Criar a classe `Game`, que organiza a partida inteira. Assim o main.py fica
pequeno e toda a lógica fica dentro de uma classe (Orientação a Objetos).

Atributos sugeridos:
- screen          -> janela do pygame
- clock           -> controla o FPS (constants.py)
- player          -> instância de Player
- collectibles    -> lista com coletáveis dos 3 tipos espalhados pela tela
- enemies         -> lista de Enemy (opcional)
- counter         -> instância de CollectionCounter
- hud             -> instância de Hud
- running         -> True enquanto o jogo estiver aberto
- (opcional) state -> "menu", "playing", "game_over"

Métodos sugeridos:
- __init__()           -> inicializa o pygame, cria a janela e os objetos
- spawn_collectibles() -> cria os coletáveis em posições na tela (aleatórias ou fixas)
- handle_events()      -> trata eventos (fechar janela, pausar, teclas de menu)
- update()             -> atualiza o jogador/inimigos e verifica colisões:
                          se o jogador encostar num coletável -> coletavel.on_collect()
                          + counter.add(coletavel.kind) + remover da lista
- draw()               -> limpa a tela, desenha fundo, coletáveis, jogador, inimigos e o HUD
- run()                -> loop principal: handle_events -> update -> draw, até running = False
"""

"""
collision.py — funções de colisão

O QUE FAZER AQUI
----------------
Criar funções que verificam se objetos estão se encostando.

Funções sugeridas:
- check_collision(object_a, object_b)
    -> devolve True se os retângulos dos dois objetos se sobrepõem
       (usar get_rect() de GameObject e colliderect do pygame)
- check_collision_list(obj, objects)
    -> devolve a lista de objetos de `objects` que estão encostando em `obj`
       (útil para checar o jogador contra todos os coletáveis de uma vez)

Quem usa: a classe Game, no update(), para saber quando o jogador pegou um
coletável ou encostou num inimigo.
"""

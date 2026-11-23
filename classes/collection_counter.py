"""
collection_counter.py — classe CollectionCounter

O QUE FAZER AQUI
----------------
Criar a classe `CollectionCounter`, responsável pelo requisito mínimo:
"manter um registro da quantidade de objetos coletados para cada tipo".

Atributos sugeridos:
- counts          -> dicionário {tipo: quantidade}, começando com todos os tipos em 0
                     (ex.: {"coin": 0, "gem": 0, "star": 0})

Métodos sugeridos:
- add(kind)       -> soma 1 no contador do tipo recebido (chamado quando um coletável é pego)
- get(kind)       -> devolve a quantidade de um tipo
- get_all()       -> devolve todos os contadores (usado pelo Hud para mostrar na tela)
- total()         -> soma de todos os tipos (opcional, ex.: para pontuação ou condição de vitória)
- reset()         -> zera tudo (para reiniciar a partida)

Encapsulamento: só esta classe deve alterar os contadores. As outras classes
apenas pedem para somar (add) ou leem os valores (get/get_all).
"""

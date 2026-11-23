"""
collectible.py — classe Collectible (classe base dos coletáveis)

O QUE FAZER AQUI
----------------
Criar a classe `Collectible`, herdando de `GameObject`.
Ela reúne o que é comum aos 3 tipos de coletáveis (requisito mínimo:
"no mínimo três tipos distintos de objetos coletáveis").

Atributos sugeridos:
- kind            -> nome do tipo (ex.: "coin", "gem", "star"); é a chave usada no CollectionCounter
- value           -> quantos pontos vale (opcional)
- collected       -> True/False, indica se já foi pego

Métodos sugeridos:
- on_collect()    -> o que acontece ao ser coletado. Na classe base marca `collected = True`;
                     cada tipo filho SOBRESCREVE este método (polimorfismo) para ter um efeito
                     próprio (tocar um som diferente, dar mais pontos, aumentar a velocidade...).
- draw(screen)    -> herdado de GameObject; só desenhar se ainda não foi coletado

Classes filhas (uma por arquivo):
- coin.py  -> Coin
- gem.py   -> Gem
- star.py  -> Star
"""

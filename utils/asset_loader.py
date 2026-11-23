"""
asset_loader.py — carregamento de arquivos da pasta assets/

O QUE FAZER AQUI
----------------
Centralizar o carregamento de imagens, sons, músicas e fontes, montando o
caminho com as constantes de constants.py (IMAGES_PATH, SOUNDS_PATH...).

Funções sugeridas:
- load_image(name, size=None) -> carrega assets/images/<name> e, se pedido, redimensiona
- load_sound(name)            -> carrega assets/sounds/<name>
- play_music(name, loop=True) -> toca assets/music/<name> em loop
- load_font(name, size)       -> carrega assets/fonts/<name>

Dicas:
- Montar os caminhos com os.path.join (funciona no Windows, Linux e Mac).
- Carregar cada arquivo UMA vez (no início), não a cada quadro do loop,
  senão o jogo fica lento.
"""

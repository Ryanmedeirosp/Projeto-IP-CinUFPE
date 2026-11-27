import os

# Tela
TITULO_JOGO = 'Arena PvP - Projeto IP'
ALTURA = 640
LARGURA = 480
FPS = 60

# Atributos do jogador
VELOCIDADE_JOGADOR = 5
TAMANHO_JOGADOR = 32

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)

# Caminhos de arquivos
DIRETORIO_PRINCIPAL = os.path.dirname(__file__)
PASTA_ASSETS = os.path.join(DIRETORIO_PRINCIPAL, "assets")
PASTA_IMAGENS = os.path.join(PASTA_ASSETS, "images")
PASTA_SONS = os.path.join(PASTA_ASSETS, "sounds")
PASTA_MUSICAS = os.path.join(PASTA_ASSETS, "music")
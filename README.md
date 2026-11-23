# Nome do Jogo _(definir)_

Projeto da disciplina de **Introdução à Programação — CIn/UFPE (2026.2)**.

> Este README é o **relatório do projeto** (o enunciado permite entregar o relatório aqui em vez de PDF).
> Cada seção abaixo explica o que deve ser preenchido. Substituam os textos em _itálico_ pelo conteúdo real.

---

## 🎯 Sobre o projeto

_Descrever em poucas linhas a ideia do jogo e o objetivo do jogador._

### Requisitos mínimos (obrigatórios)
- [ ] Sistema interativo em ambiente **2D**.
- [ ] O usuário **controla um objeto** para coletar outros objetos na tela.
- [ ] No mínimo **três tipos distintos de coletáveis**.
- [ ] Registro da **quantidade coletada de cada tipo**, exibida ao usuário.
- [ ] Código estruturado com **Orientação a Objetos**.
- [ ] Desenvolvido exclusivamente em **Python**.

> ⚠️ Implementem primeiro os requisitos mínimos. Só depois os extras.

---

## 👥 Equipe

| Nome | GitHub | E-mail / login CIn |
|---|---|---|
| | | |
| | | |
| | | |
| | | |
| | | |

---

## ▶️ Como executar

1. Ter o **Python 3** instalado.
2. Clonar o repositório:
   ```bash
   git clone https://github.com/Ryanmedeirosp/Projeto-IP-CinUFPE.git
   cd Projeto-IP-CinUFPE
   ```
3. (Opcional) Criar e ativar um ambiente virtual:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate      # Windows
   source .venv/bin/activate   # Linux / Mac
   ```
4. Instalar as dependências:
   ```bash
   pip install -r requirements.txt
   ```
5. Rodar o jogo:
   ```bash
   python main.py
   ```

### Controles
| Tecla | Ação |
|---|---|
| _Setas / WASD_ | _Mover o jogador_ |
| _ESC_ | _Pausar / sair_ |

---

## 📸 Capturas de tela

_Adicionar aqui os prints do jogo funcionando (ficam em [`docs/screenshots/`](docs/screenshots/)). Eles também vão para a galeria de projetos._

<!-- Exemplo:
![Gameplay](docs/screenshots/02_gameplay.png)
-->

---

## 🏗️ Arquitetura do projeto

_Explicar como o código foi organizado. Atualizar a árvore abaixo se a estrutura mudar._

```txt
Projeto-IP-CinUFPE/
├── assets/              # arquivos externos (sem código)
│   ├── images/          # sprites, fundo, ícones
│   ├── sounds/          # efeitos sonoros
│   ├── music/           # músicas de fundo
│   └── fonts/           # fontes do HUD/menus
├── classes/             # classes do jogo (Orientação a Objetos)
│   ├── game_object.py   # classe base de tudo que aparece na tela
│   ├── player.py        # objeto controlado pelo usuário
│   ├── enemy.py         # inimigo/obstáculo (opcional)
│   ├── collectible.py   # classe base dos coletáveis
│   ├── coin.py          # coletável tipo 1
│   ├── gem.py           # coletável tipo 2
│   ├── star.py          # coletável tipo 3
│   ├── collection_counter.py  # contagem por tipo de coletável
│   ├── hud.py           # exibe os contadores na tela
│   ├── text.py          # desenha textos
│   └── game.py          # loop principal e regras da partida
├── utils/               # funções auxiliares
│   ├── collision.py     # verificação de colisões
│   ├── helpers.py       # funções genéricas
│   └── asset_loader.py  # carregamento de imagens/sons/fontes
├── docs/                # documentação (checkpoints, tarefas, apresentação, prints)
├── constants.py         # valores fixos (tela, velocidades, caminhos)
├── main.py              # ponto de entrada
├── requirements.txt     # dependências
└── README.md            # este relatório
```

Cada pasta tem um `README.md` e cada arquivo `.py` começa com um comentário explicando o que deve ser implementado nele.

### Diagrama de classes
_Descrever (ou colocar uma imagem) da hierarquia: `GameObject` → `Player`, `Enemy`, `Collectible` → `Coin`, `Gem`, `Star`; `Game` possui `Player`, coletáveis, `CollectionCounter` e `Hud`._

---

## 🧰 Ferramentas, bibliotecas e frameworks

_Listar tudo o que foi usado e **justificar** cada escolha (exigido no enunciado)._

| Ferramenta | Para que foi usada | Por que escolhemos |
|---|---|---|
| Python 3 | Linguagem do projeto | Obrigatória na disciplina |
| PyGame | _Janela, desenho, teclado, sons_ | _..._ |
| Git / GitHub | Versionamento e entrega | Uso obrigatório |
| _Trello / Notion / GitHub Projects_ | _Gerenciar tarefas_ | _..._ |
| _Discord / WhatsApp_ | _Comunicação do grupo_ | _..._ |

---

## 🧑‍🤝‍🧑 Divisão de trabalho

_Quem fez o quê. Detalhes em [`docs/divisao_tarefas.md`](docs/divisao_tarefas.md)._

| Integrante | Contribuições |
|---|---|
| | |

---

## 📚 Conceitos da disciplina utilizados

_Indicar cada conceito e **onde** ele aparece no código._

| Conceito | Onde foi usado |
|---|---|
| Classes e objetos | _ex.: `classes/player.py`_ |
| Herança | _ex.: `Coin(Collectible)`_ |
| Polimorfismo | _ex.: `on_collect()` em cada coletável_ |
| Encapsulamento | _ex.: `CollectionCounter`_ |
| Laços de repetição | _ex.: loop principal em `Game.run()`_ |
| Condicionais | _ex.: verificação de colisões_ |
| Listas | _ex.: lista de coletáveis_ |
| Dicionários | _ex.: contadores por tipo_ |
| Funções | _ex.: `utils/`_ |
| Módulos / imports | _ex.: separação em pastas_ |

---

## 🧗 Desafios, erros e lições aprendidas

**Qual foi o maior erro cometido durante o projeto? Como vocês lidaram com ele?**
_Resposta._

**Qual foi o maior desafio enfrentado durante o projeto? Como vocês lidaram com ele?**
_Resposta._

**Quais as lições aprendidas durante o projeto?**
_Resposta._

---

## 📦 Entregas

Até a data da apresentação, preencher na planilha da disciplina:
- [ ] Link deste repositório no GitHub
- [ ] Link do relatório (este README)
- [ ] Link dos slides da apresentação (ver [`docs/apresentacao.md`](docs/apresentacao.md))
- [ ] Aba "Checkpoints" atualizada antes de cada checkpoint (ver [`docs/checkpoints.md`](docs/checkpoints.md))

# Fluxo de trabalho com Git

O repositório no GitHub é **obrigatório** na entrega, e o histórico de commits mostra a evolução do projeto (critério de avaliação). Sugestão do enunciado: **uma branch para cada feature, pull requests e reuniões de merge**.

## Branches
- `main`: só código que funciona. Ninguém faz commit direto nela.
- Uma branch por tarefa, criada a partir da `main` atualizada:
  - `feature/player-movimento`
  - `feature/coletaveis`
  - `feature/hud-contador`
  - `fix/colisao-borda`
  - `docs/relatorio`

## Passo a passo de uma tarefa
1. Atualizar a main: `git checkout main` e `git pull`
2. Criar a branch: `git checkout -b feature/nome-da-tarefa`
3. Fazer commits pequenos enquanto trabalha.
4. Enviar: `git push -u origin feature/nome-da-tarefa`
5. Abrir um **Pull Request** no GitHub para a `main`.
6. Outro integrante revisa e testa; depois faz o merge.

## Mensagens de commit
Formato: `tipo: descrição curta no imperativo`

| Tipo | Quando usar |
|---|---|
| `feat` | Nova funcionalidade (`feat: adiciona coletável Gem`) |
| `fix` | Correção de bug (`fix: impede jogador de sair da tela`) |
| `docs` | Documentação (`docs: adiciona prints ao README`) |
| `refactor` | Reorganização sem mudar comportamento |
| `chore` | Configuração, dependências, `.gitignore` |
| `assets` | Imagens, sons e músicas |

## Padrão de nomes no código
- Arquivos e funções: `snake_case` (`collection_counter.py`, `check_collision`).
- Classes: `PascalCase` (`CollectionCounter`).
- Constantes: `MAIUSCULAS` (`SCREEN_WIDTH`).
- Sem espaços nem acentos em nomes de arquivo.

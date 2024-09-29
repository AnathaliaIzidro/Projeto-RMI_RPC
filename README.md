# Resta Um

Jogo de estratégia para dois jogadores.

## Como jogar

1. O jogo começa com 32 peças no tabuleiro, deixando o espaço do centro vazio.
2. O jogador escolhe uma peça para começar, a peça escolhida deve saltar sobre outra peça, fazendo movimentos na horizontal ou na vertical, e deve chegar a um espaço vazio.
3. A peça que foi pulada sai do jogo.
4. Só é possível retirar uma peça por vez.
5. Os jogadores se revezam, jogando um de cada vez.
6. O jogo termina quando restar somente uma peça ou não for possível fazer movimentos.

## Funcionalidades

* Controle de turno, com definição de quem inicia a partida
* Movimentação das peças nos tabuleiros
* Desistência
* Chat para comunicação durante toda a partida
* Indicação de vencedor

## Tecnologias

* Frontend: HTML, CSS, JavaScript
* Backend: Python utilizando Flask e Pyro4

## Como executar

1. Clone o repositório.
2. Instale as dependências necessárias com `pip install -r requirements.txt`.
3. Execute o servidor Pyro4 com `python app.py`.
4. Acesse o jogo em `http://localhost:5000`.
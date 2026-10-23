
import tkinter as tk


# Armazena as perguntas, alternativas e respostas corretas.
# O índice 0 representa a primeira alternativa, 1 a segunda e 2 a terceira.
perguntas = [
    {
        "pergunta": "O que é Python?",
        "alternativas": [
            "Uma linguagem de programação",
            "Um sistema operacional",
            "Um navegador de internet",
        ],
        "correta": 0,
    },
    {
        "pergunta": "Qual símbolo usamos para comentários em Python?",
        "alternativas": ["//", "#", "<!-- -->"],
        "correta": 1,
    },
    {
        "pergunta": "Qual comando exibe uma mensagem na tela?",
        "alternativas": ["input()", "print()", "int()"],
        "correta": 1,
    },
]

# Inicializa a pontuação e o índice da pergunta atual.
pontuacao = 0
indice_pergunta = 0


# Atualiza a pergunta e as alternativas exibidas na janela.
def carregar_pergunta():
    pergunta_atual = perguntas[indice_pergunta]

    pergunta.config(text=pergunta_atual["pergunta"])

    botao1.config(text=pergunta_atual["alternativas"][0])
    botao2.config(text=pergunta_atual["alternativas"][1])
    botao3.config(text=pergunta_atual["alternativas"][2])


# Verifica a resposta escolhida e atualiza a pontuação.
# Depois, avança para a próxima pergunta ou encerra o quiz.
def verificar_resposta(indice_alternativa):
    global pontuacao, indice_pergunta

    # Recupera os dados da pergunta atual.
    pergunta_atual = perguntas[indice_pergunta]

    # Compara a alternativa escolhida com a resposta correta.
    if indice_alternativa == pergunta_atual["correta"]:
        pontuacao += 1
        resultado.config(
            text=f"Resposta correta! Pontuação: {pontuacao}"
        )
    else:
        resultado.config(
            text=f"Resposta incorreta! Pontuação: {pontuacao}"
        )

    # Avança para a próxima pergunta.
    indice_pergunta += 1

    # Verifica se ainda existem perguntas.
    if indice_pergunta < len(perguntas):
        carregar_pergunta()
    else:
        # Exibe o resultado final do quiz.
        pergunta.config(text="Quiz finalizado!")
        resultado.config(
            text=f"Você acertou {pontuacao} de {len(perguntas)} perguntas!"
        )

        # Desativa os botões de resposta ao finalizar o jogo.
        botao1.config(state="disabled")
        botao2.config(state="disabled")
        botao3.config(state="disabled")


# Reinicia a pontuação e retorna à primeira pergunta.
def reiniciar_quiz():
    global pontuacao, indice_pergunta

    pontuacao = 0
    indice_pergunta = 0

    # Reativa os botões para permitir uma nova partida.
    botao1.config(state="normal")
    botao2.config(state="normal")
    botao3.config(state="normal")

    # Restaura o texto inicial da pontuação.
    resultado.config(text="Pontuação: 0")

    # Carrega novamente a primeira pergunta.
    carregar_pergunta()


# Cria e configura a janela principal.
janela = tk.Tk()
janela.title("Quiz de Python")
janela.geometry("500x350")
janela.resizable(False, False)


# Exibe o título do jogo.
titulo = tk.Label(
    janela,
    text="Quiz de Python",
    font=("Arial", 20, "bold")
)
titulo.pack(pady=20)


# Exibe a pergunta atual.
pergunta = tk.Label(
    janela,
    text="",
    font=("Arial", 14)
)
pergunta.pack(pady=15)


# Cria os botões das alternativas.
# O lambda permite executar a função somente quando houver um clique.
botao1 = tk.Button(
    janela,
    text="",
    command=lambda: verificar_resposta(0)
)
botao1.pack(pady=5)

botao2 = tk.Button(
    janela,
    text="",
    command=lambda: verificar_resposta(1)
)
botao2.pack(pady=5)

botao3 = tk.Button(
    janela,
    text="",
    command=lambda: verificar_resposta(2)
)
botao3.pack(pady=5)


# Cria o elemento que exibirá o feedback e a pontuação.
# Ele será posicionado abaixo das alternativas.
resultado = tk.Label(
    janela,
    text="Pontuação: 0",
    font=("Arial", 11)
)

# Posiciona o feedback e a pontuação acima do botão de reinício.
resultado.pack(pady=5)


# Cria o botão para iniciar uma nova partida.
botao_reiniciar = tk.Button(
    janela,
    text="Jogar novamente",
    command=reiniciar_quiz
)
botao_reiniciar.pack(pady=15)


# Carrega a primeira pergunta e mantém a janela aberta.
carregar_pergunta()
janela.mainloop()

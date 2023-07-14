from tkinter import *
from random import choice

letras = []
lista_tracos = []
letras_erradas = []
letras_escolhidas = []
dificuldade = []
lista_conferencia = []
interface_dificuldade = None
interface_forca = None
caracter = None
caracters_anteriores = None
caracter_vazio = None
entrada_dados = None


def escolha_dificuldade():
    global interface_dificuldade
    interface_dificuldade = Tk()
    interface_dificuldade.title("Escolha a Dificuldade")

    label_titulo = Label(interface_dificuldade, text='Escolha sua dificuldade: ', font=('georgia', 16), fg='black')
    label_titulo.pack(pady=20)

    frame_botoes = Frame(interface_dificuldade)
    frame_botoes.pack()

    button_facil = Button(frame_botoes, text='Fácil - 10 erros permitidos', font=('arial', 12),
                          fg='black', command=escolha_dificuldade_facil)
    button_facil.pack(side=LEFT, padx=10)

    button_medio = Button(frame_botoes, text='Médio - 8 erros permitidos', font=('arial', 12),
                          fg='black', command=escolha_dificuldade_medio)
    button_medio.pack(side=LEFT, padx=10)

    button_dificil = Button(frame_botoes, text='Difícil - 6 erros permitidos', font=('arial', 12),
                            fg='black', command=escolha_dificuldade_dificil)
    button_dificil.pack(side=LEFT, padx=10)

    interface_dificuldade.mainloop()


def escolha_dificuldade_facil():
    global interface_dificuldade
    dificuldade.append(10)
    interface_dificuldade.destroy()
    iniciar_jogo()


def escolha_dificuldade_medio():
    global interface_dificuldade
    dificuldade.append(8)
    interface_dificuldade.destroy()
    iniciar_jogo()


def escolha_dificuldade_dificil():
    global interface_dificuldade
    dificuldade.append(6)
    interface_dificuldade.destroy()
    iniciar_jogo()


def forca(event):
    global interface_forca
    global caracter
    global caracters_anteriores
    global caracter_vazio
    global entrada_dados

    cabeca = interface_forca.create_oval
    corpo = interface_forca.create_line
    boca = interface_forca.create_arc

    try:
        char = caracter.get().upper()[0]
    except IndexError:
        pass
    else:
        try:
            int(char)
        except ValueError:
            if char not in letras_escolhidas:
                letras_escolhidas.append(char)
                for indice in range(len(letras)):
                    if char == letras[indice]:
                        lista_tracos[indice] = letras[indice]
                        caracter_vazio['text'] = ' '.join(lista_tracos)
                        lista_conferencia.append(char)
                if char not in letras:
                    letras_erradas.append(char)
                    caracters_anteriores['text'] = ' '.join(letras_erradas)
            if len(lista_conferencia) == len(letras):
                mensagem_final['text'] = 'Parabéns! Jogo ganho!'
                mensagem_final['fg'] = 'green'
                caracter.destroy()
                button_finalizar = Button(interface, text='Finalizar', font=('georgia', 15), fg='red',
                                          command=quit_game)
                button_finalizar.pack(pady=10)
            if len(letras_erradas) == dificuldade[0]:
                palavra_perdida = ' '.join(letras)
                mensagem_final['text'] = f'Erros máximos atingidos, você perdeu!\nA palavra era: {palavra_perdida}'
                mensagem_final['fg'] = 'red'
                caracter.destroy()
                button_finalizar = Button(interface, text='Finalizar', font=('georgia', 15), fg='red',
                                          command=quit_game)
                button_finalizar.pack(pady=10)
            # boneco:
            if len(letras_erradas) == 1:
                cabeca(165, 95, 215, 140, fill='grey', outline='black')  # cabeça
            elif len(letras_erradas) == 2:
                corpo(190, 140, 190, 235)  # corpo
            elif len(letras_erradas) == 3:
                corpo(190, 140, 130, 190)  # braço esquerdo
            elif len(letras_erradas) == 4:
                corpo(190, 140, 250, 190)  # braço direito
            elif len(letras_erradas) == 5:
                corpo(190, 235, 125, 300)  # perna esquerda
            elif len(letras_erradas) == 6:
                corpo(190, 235, 250, 300)  # perna direita
            elif len(letras_erradas) == 7:
                cabeca(175, 105, 185, 115, fill='white', outline='black')  # olho esquerdo
            elif len(letras_erradas) == 8:
                cabeca(195, 105, 205, 115, fill='white', outline='black')  # olho direito
            elif len(letras_erradas) == 9:
                cabeca(187.5, 117.5, 192, 122.5, fill='white', outline='black')  # nariz
            elif len(letras_erradas) == 10:
                boca(165, 125, 205, 130, fill='red')  # boca
    entrada_dados.set('')


def quit_game():
    interface.destroy()


def iniciar_jogo():
    with open('palavras.txt') as palavras:
        leitura = palavras.readlines()
        palavra = choice(leitura).strip().upper()

    for indice in range(len(palavra)):
        letras.append(palavra[indice])
        lista_tracos.append('(___)')

    global interface
    global interface_forca
    global caracter
    global caracters_anteriores
    global caracter_vazio
    global mensagem_final
    global entrada_dados

    interface = Tk()
    interface.title("Hangman Game")
    label_titulo = Label(interface, text="Hangman Game", font=("georgia", 20), fg="black")
    label_titulo.pack(pady=20)

    interface_frame = Frame(interface)
    interface_frame.pack(padx=20, pady=10)

    interface_forca = Canvas(interface_frame, width=400, height=400)
    interface_forca.pack(side=LEFT, padx=20)

    interface_texto = Frame(interface_frame)
    interface_texto.pack(side=RIGHT, padx=20)

    interface_forca.create_rectangle(10, 400, 400, 390, fill='green')
    interface_forca.create_rectangle(10, 400, 30, 30, fill='brown')
    interface_forca.create_rectangle(10, 30, 200, 40, fill='brown')
    interface_forca.create_rectangle(180, 40, 200, 50, fill='yellow')
    interface_forca.create_rectangle(187.5, 50, 192.5, 90, fill='black')
    interface_forca.create_oval(160, 90, 220, 145, fill='black')
    interface_forca.create_oval(165, 95, 215, 140, fill='white')

    label_letra = Label(interface_texto, text='Digite sua letra abaixo:', font=('arial', 12), fg='black')
    label_letra.pack(pady=10)

    entrada_dados = StringVar()
    caracter = Entry(interface_texto, textvariable=entrada_dados, font=('arial', 12))
    caracter.pack()

    caracter.bind('<Return>', forca)

    caracter_vazio = Label(interface_texto, text=' '.join(lista_tracos), font=('arial', 12))
    caracter_vazio.pack(pady=10)

    label_letras_erradas = Label(interface_texto, text='Letras Erradas:', font=('arial', 12), fg='black')
    label_letras_erradas.pack()

    caracters_anteriores = Label(interface_texto, text=' '.join(letras_erradas), font=('arial', 12))
    caracters_anteriores.pack(pady=10)

    mensagem_final = Label(interface_texto, text='', font=('arial', 12), fg='black')
    mensagem_final.pack()

    interface.mainloop()


escolha_dificuldade()

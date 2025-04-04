""" Faça um jogo da Forca utilizando listas. Dada uma palavra, dê algumas
chances para o usuário acertar.
"""

palavras = "banana"

palavra = palavras[0]

resultado=["_" for _ in palavra[0]]

boneco = ["\\","\\O", "\\O/"]

while True:
    palpite = input("digite uma letra: ").lower

    if palpite not in palavra:
        print(boneco.pop(0))

    for i, letra in enumerate(palavra):
        if palpite == letra:
            resultado[i] = letra
        
    for letra in resultado:
        print(f"{letra}", end="")

    print()

    if resultado == list(palavra):
        print("você acertou!")
        break
    if len(boneco)==0:
        print("tente novamente")
        break

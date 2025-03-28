import random
help(random)

num_secreto =  random.randint(1,100)
tentativas = 0

print("tente adivinhar o número de 1 a 100:")

while True:
    palpite = int(input("digite um número:"))
    tentativas+=1

    if palpite == num_secreto:
        print("parabéns, você acertou!")
        break
    elif palpite > num_secreto:
        print("palpite alto!")
    elif palpite < num_secreto:
        print("palpite baixo!")

    if tentativas==10:
        break


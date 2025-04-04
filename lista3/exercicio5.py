""" Represente polinômios como dicionários, onde as chaves são os expoentes
e os valores são os coeficientes. Por exemplo, o polinômio é
representado por 2 3, 1 2, 0 1.
Crie uma função que multiplique dois polinômios e retorne o polinômio
resultante, também como dicionário.
"""

p1 = {2:3,1:2,0:1} #3x^2 + 2x +1
p2 = {1:1,0:4} #x+4

#(3x^2 + 2x +1) * (x+4) = 3x^3 + 12x^2 + 2x^2 + 8x + x + 4 = 3x^3 + 14x^2 + 9x + 4

p_result={}

for exp1, coef1 in p1.items():
    for exp2, coef2 in p2.items():

        p_result[exp1+exp2] = p_result.get(exp1+exp2,0) + coef1*coef2


for chave, valor in p1.items():
    print(f"{valor}x^{chave}", end="")
    if chave != 0:
        print("+",end="")

print()

for chave, valor in p2.items():
    print(f"{valor}x^{chave}", end="")
    if chave != 0:
        print("+",end="")
print()

for chave, valor in p_result.items():
    print(f"{valor}x^{chave}", end="")
    if chave != 0:
        print("+",end="")
print(p_result)

"""
 Dada uma lista de palavras, agrupe-as em um dicionário onde a chave seja
uma forma canônica (por exemplo, os caracteres ordenados) e o valor seja
a lista de palavras que são anagramas entre si. Essa técnica pode ser
utilizada para identificar grupos de palavras com os mesmos caracteres,
independentemente da ordem.
Entrada:
["amor", "roma", "mora", "carro", "orça", "orca", "arco"]
Saída:
('a', 'm', 'o', 'r'): ['amor', 'roma', 'mora']
('c', 'o', 'r', 'r'): ['carro']
('a', 'c', 'o', 'r'): ['orça', 'orca', 'arco']"""

def agrupar_anagramas(palavras):
    grupos = {}
    
    for palavra in palavras:
        chave = tuple(sorted(palavra))  # Cria a chave canônica
        if chave not in grupos:
            grupos[chave] = []  # Cria a lista se não existir
        grupos[chave].append(palavra)
    
    return grupos

# Exemplo de entrada
entrada = ["amor", "roma", "mora", "carro", "orça", "orca", "arco"]

# Agrupar as palavras
grupos = agrupar_anagramas(entrada)

# Exibir os grupos de anagramas
for chave, grupo in grupos.items():
    print(f"{chave}: {grupo}")

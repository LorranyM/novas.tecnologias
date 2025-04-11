def sequencia(n, memo={}):
    if n==0:
        return 0
    if n==1:
        return 1
    if n in memo:
        resultado = memo[n]
    else:
       resultado = sequencia(n-1,memo)+2*sequencia(n-2,memo)
       memo[n]=resultado

    print(memo)

    return resultado

calc = lambda n: sequencia(n)

n = int(input("Entre com a posicao desejada:"))

print(f"T{(n)} = {sequencia(n)}")
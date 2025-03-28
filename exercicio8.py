n = int(input("qual é a sequência de Fibonacci:"))

if n <= 0:
    print("o número deve ser maior que zero.")
elif n==1:
    print("1")
else:
    fib=[0,1]
    while len(fib)<n:
        fib.append(fib[-1]+fib[-2])
    print("sequencia: ", fib)


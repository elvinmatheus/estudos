x = input().split()
y = input().split()

valor = int(x[1]) * float(x[2]) + int(y[1]) * float(y[2])

print("VALOR A PAGAR: R$ %.2f" %valor)
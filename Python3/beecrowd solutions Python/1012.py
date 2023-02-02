x = input().split()
x = list(map(float, x))

triangulo = (x[0] * x[2]) / 2
circulo = 3.14159 * x[2] ** 2
trapezio = ((x[0] + x[1]) * x[2]) / 2
quadrado = x[1] ** 2
retangulo = x[0] * x[1]

print("""TRIANGULO: {:.3f}
CIRCULO: {:.3f}
TRAPEZIO: {:.3f}
QUADRADO: {:.3f}
RETANGULO: {:.3f}""".format(triangulo, circulo, trapezio, quadrado, retangulo))
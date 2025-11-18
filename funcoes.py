import math

# Fórmula simbólica da equação do segundo grau (apenas para exibir)
FormulaPadrao = "f(x) = a*x**2 + b*x + c"

sen30 = 0.5
cos30 = math.sqrt(3) / 2
tg30 = sen30 / cos30

print(sen30)
print(cos30)
print(tg30)


def calcular_delta(a, b, c):
    """Calcula o valor do discriminante (Delta)."""
    return b**2 - 4 * a * c


def calcular_raizes(a, b, c):
    """Calcula as duas raízes reais da equação do segundo grau (se existirem)."""
    if a == 0:
        print("❌ O valor de 'a' não pode ser zero em uma equação do segundo grau.")
        return None, None

    delta = calcular_delta(a, b, c)
    print(f"Δ = {delta}")

    if delta < 0:
        print('''\nSe o delta (Δ) for negativo:
        Dentro da fórmula há √Δ → não existe raiz quadrada real de número negativo.
        Isso quer dizer que não há interseção com o eixo X, ou seja, nenhuma raiz real.\n''')
        return None, None

    raiz_delta = math.sqrt(delta)
    x1 = (-b + raiz_delta) / (2 * a)
    x2 = (-b - raiz_delta) / (2 * a)

    print(f"x1 = {x1}")
    print(f"x2 = {x2}")

    return x1, x2


def derivada(a, b):
    """Retorna a derivada da função f(x) = a*x² + b*x + c."""
    return f"f'(x) = {2*a}x + {b}"


def vertice(a, b, c):
    """Calcula o vértice e identifica se é ponto máximo ou mínimo."""
    if a == 0:
        print("❌ O valor de 'a' não pode ser zero em uma equação do segundo grau.")
        return None, None, None

    xv = -b / (2 * a)
    yv = a * xv**2 + b * xv + c

    tipo = "ponto mínimo" if a > 0 else "ponto máximo"

    print(f"xv = {xv}")
    print(f"yv = {yv}")
    print(f"Esse é um {tipo}.")

    return xv, yv, tipo
def plotar_grafico(a, b, c):
    """Plota o gráfico da função quadrática."""
    import matplotlib.pyplot as plt
    import numpy as np

    # Gera valores de x
    x = np.linspace(-10, 10, 400)
    # Calcula os valores correspondentes de y
    y = a * x**2 + b * x + c

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f'f(x) = {a}x² + {b}x + {c}')
    plt.title('Gráfico da Função Quadrática')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.axhline(0, color='black',linewidth=0.5, ls='--')
    plt.axvline(0, color='black',linewidth=0.5, ls='--')
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.legend()
    plt.show()
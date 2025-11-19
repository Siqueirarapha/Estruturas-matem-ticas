import matplotlib
matplotlib.use('TkAgg') # Tenta forçar o uso do backend Tkinter
# Se o TkAgg não funcionar, tente 'Qt5Agg' ou 'Agg' (este último não abre janela, mas salva)

import math
import numpy as np
import matplotlib.pyplot as plt
# ... restante do seu código ...
# Fórmula simbólica da equação do segundo grau (apenas para exibir)
FormulaPadrao = "f(x) = a*x**2 + b*x + c"

sen30 = 0.5
cos30 = math.sqrt(3) / 2
tg30 = sen30 / cos30


def calcular_delta(a, b, c):
    """Calcula o valor do discriminante (Delta)."""
    return b**2 - 4 * a * c


def calcular_raizes(a, b, c):
    """Calcula as duas raízes reais da equação do segundo grau (se existirem)."""
    if a == 0:
        return None, None

    delta = calcular_delta(a, b, c)

    if delta < 0:
        # Retorna None, None para indicar que não há raízes reais
        return None, None

    raiz_delta = math.sqrt(delta)
    x1 = (-b + raiz_delta) / (2 * a)
    x2 = (-b - raiz_delta) / (2 * a)

    # Apenas retorna os valores
    return x1, x2


def derivada(a, b):
    """Retorna a derivada da função f(x) = a*x² + b*x + c."""
    return f"f'(x) = {2*a}x + {b}"


def vertice(a, b, c):
    """Calcula o vértice e identifica se é ponto máximo ou mínimo."""
    if a == 0:
        return None, None, None

    xv = -b / (2 * a)
    yv = a * xv**2 + b * xv + c

    tipo = "ponto mínimo" if a > 0 else "ponto máximo"

    # Apenas retorna os valores e o tipo
    return xv, yv, tipo


def plotar_grafico(a, b, c, x1=None, x2=None, xv=None, yv=None):
    """
    Plota o gráfico da função quadrática, incluindo as raízes (x1, x2) e o vértice (xv, yv).
    """
    
    # 1. AJUSTE DINÂMICO DO EIXO X PARA GARANTIR VISIBILIDADE
    min_x = -5
    max_x = 5
    if xv is not None:
        min_x = min(min_x, xv - 3)
        max_x = max(max_x, xv + 3)
    if x1 is not None:
        min_x = min(min_x, x1 - 1)
        max_x = max(max_x, x1 + 1)
    if x2 is not None:
        min_x = min(min_x, x2 - 1)
        max_x = max(max_x, x2 + 1)
        
    x = np.linspace(min_x - 1, max_x + 1, 400)
    y = a * x**2 + b * x + c

    # 2. CONFIGURAÇÃO BÁSICA DO GRÁFICO
    plt.figure(figsize=(9, 6)) 
    
    plt.plot(x, y, label=f'f(x) = {a}x² + {b}x + {c}', color='blue') 

    # Linhas de Referência (Eixos)
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
    plt.grid(color='gray', linestyle=':', linewidth=0.5, alpha=0.6)
    plt.title('Gráfico da Função Quadrática')
    plt.xlabel('x')
    plt.ylabel('f(x)')

    # 3. PLOTAGEM DO VÉRTICE
    if xv is not None and yv is not None:
        tipo = "Mínimo" if a > 0 else "Máximo"
        cor_v = 'darkorange' if a > 0 else 'purple'
        
        plt.plot(xv, yv, 's', color=cor_v, markersize=8, label=f'Vértice ({tipo}) ({xv:.4f}, {yv:.4f})')
        plt.axvline(xv, color=cor_v, linestyle=':', linewidth=0.7)
        plt.axhline(yv, color=cor_v, linestyle=':', linewidth=0.7)
        
    # 4. PLOTAGEM DAS RAÍZES
    if x1 is not None:
        plt.plot(x1, 0, 'ro', markersize=7, label=f'Raiz x1 ({x1:.4f}, 0)')
        
        if x2 is not None and abs(x1 - x2) > 1e-4: # Usa tolerância para evitar duplicar raízes muito próximas
            plt.plot(x2, 0, 'go', markersize=7, label=f'Raiz x2 ({x2:.4f}, 0)')

    # 5. FINALIZAÇÃO
    plt.legend()
    plt.show()
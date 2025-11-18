import os
import funcoes

os.system('cls')


print("BEM-VINDO AO SISTEMA DE PLANO CARTESIANO COM DERIVADAS")
input("Aperte ENTER para continuar...")
os.system('cls')

print(f"A fórmula geral é: {funcoes.FormulaPadrao}")

while True:
    try:
        a = float(input("Digite o valor de a: "))
        b = float(input("Digite o valor de b: "))
        c = float(input("Digite o valor de c: "))

        if a == 0:
            print("❌ O valor de 'a' não pode ser zero em uma equação do segundo grau.")
            continue

        # Cálculos principais
        delta = funcoes.calcular_delta(a, b, c)
        x1, x2 = funcoes.calcular_raizes(a, b, c)
        xv, yv, tipo = funcoes.vertice(a, b, c)

        # Exibição de resultados
        print(f"\nΔ (Delta) = {delta}")
        print(f"Raízes: x1 = {x1}, x2 = {x2}")
        print(f"Vértice: ({xv}, {yv}) → {tipo}")
        print(f"Derivada: {funcoes.derivada(a, b)}")

        # Exibe gráfico (caso tenha a função em funcoes.py)
        if hasattr(funcoes, "plotar_grafico"):
            funcoes.plotar_grafico(a, b, c)

        input("\nAperte ENTER para continuar ou feche o programa para sair...")
        os.system('cls')

    except ValueError:
        print("⚠️ Por favor, insira apenas números válidos.")
    except KeyboardInterrupt:
        print("\nEncerrando programa...")
        break

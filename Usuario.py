import os
import funcoes
import math # Adicionado para garantir o math.sqrt caso alguma função precise

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

        # -----------------------------------------------------------------
        # Exibição de resultados (AGORA CENTRALIZADA E FORMATADA)
        # -----------------------------------------------------------------
        print("\n--- Resultados ---\n")
        print(f"Δ (Delta) = {delta:.4f}")
        
        # Exibe Raízes de forma condicional
        if x1 is not None:
            # Garante que x1 e x2 sejam exibidos apenas com 4 casas decimais
            print(f"Raízes: x1 = {x1:.4f}, x2 = {x2:.4f}")
        else:
            print("Raízes: Não existem raízes reais (Δ < 0).")
            
        # Exibe Vértice
        if xv is not None:
            # Exibe o vértice e o tipo (máximo ou mínimo)
            print(f"Vértice: ({xv:.4f}, {yv:.4f}) → {tipo}")
        
        print(f"Derivada: {funcoes.derivada(a, b)}")

        # Exibe gráfico
        if hasattr(funcoes, "plotar_grafico"):
            funcoes.plotar_grafico(a, b, c, x1=x1, x2=x2, xv=xv, yv=yv)

            input("\nAperte ENTER para continuar ou feche o programa para sair...")
            os.system('cls')
            
        break # Sai do loop após o processamento bem-sucedido

    except ValueError:
        print("⚠️ Por favor, insira apenas números válidos.")
    except KeyboardInterrupt:
        print("\nEncerrando programa...")
        break
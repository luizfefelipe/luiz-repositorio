print("######SEJA BEM VINDO AO PROGRAMA DE VENDAS DE FRUTA [MELANCIA]")

def calcular_valor_venda(peso, preco_por_kg):
    """Função para calcular o valor total da venda de melancia."""
    return peso * preco_por_kg

def main():
    print("Bem-vindo ao sistema de vendas de melancia!")

    # Definindo o preço por quilo da melancia
    preco_por_kg = 5.00  # Por exemplo, 5 reais por quilo

    # Entrada de dados
    peso = float(input("Digite o peso da melancia (em kg): "))
    
    # Calcular o valor da venda
    valor_total = calcular_valor_venda(peso, preco_por_kg)
    
    # Exibir o valor da venda
    print(f"O valor total da venda é: R$ {valor_total:.2f}")
    
    # Perguntar se deseja realizar outra venda
    continuar = input("Deseja registrar outra venda? (s/n): ").lower()
    if continuar == 's':
        main()
    else:
        print("Obrigado por usar o sistema de vendas de melancia!")

if __name__ == "__main__":
    main()
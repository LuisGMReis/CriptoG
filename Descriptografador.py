def binToTxt(data):
    # Dicionário inverso para mapear números de volta às letras do alfabeto
    alfabeto_inverso = {
        1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F",
        7: "G", 8: "H", 9: "I", 10: "J", 11: "K", 12: "L",
        13: "M", 14: "N", 15: "O", 16: "P", 17: "Q", 18: "R",
        19: "S", 20: "T", 21: "U", 22: "V", 23: "W", 24: "X",
        25: "Y", 26: "Z"
    }
    
    result = ""  # Inicializa a variável para armazenar o texto decifrado
    
    for item in data:
        # Verifica se o item é uma string binária (composta apenas por '0' e '1')
        if isinstance(item, str) and all(c in '01' for c in item):
            num = int(item, 2)  # Converte o binário para decimal
        else:
            num = int(item)  # Caso contrário, converte diretamente para número decimal

        # Adiciona a letra correspondente ao resultado ou "?" se o número for inválido
        result += alfabeto_inverso.get(num, "?")
    return result

# Fluxo principal do programa
formato = input("O texto está no formato binário ou numérico? (Digite 'bin' ou 'num'): ").strip().lower()

# Verifica se o formato escolhido pelo usuário é válido
if formato not in ['bin', 'num']:
    print("Formato inválido. Escolha 'bin' para binário ou 'num' para numérico.")
else:
    # Solicita ao usuário os dados a serem decifrados
    entrada = input(f"Digite os dados separados por espaço ({'binários' if formato == 'bin' else 'números'}): ")
    dados = entrada.split()  # Divide os dados em uma lista
    
    if formato == "bin":
        # Valida se todos os itens são binários
        if not all(all(c in '01' for c in item) for item in dados):
            print("Entrada inválida. Certifique-se de que os dados são binários.")
        else:
            resultado = binToTxt(dados)  # Processa a entrada binária
            print(f"Texto decifrado: {resultado}")
    elif formato == "num":
        # Valida se todos os itens são números
        if not all(item.isdigit() for item in dados):
            print("Entrada inválida. Certifique-se de que os dados são números.")
        else:
            resultado = binToTxt(dados)  # Processa a entrada numérica
            print(f"Texto decifrado: {resultado}")

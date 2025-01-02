def txtForBin(txt, numero):
    
    alfabeto = {
        "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6,
        "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,
        "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18,
        "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24,
        "Y": 25, "Z": 26
    }

    txt = txt.upper()

    numbers = [alfabeto[letra] for letra in txt if letra in alfabeto]

    if numero % 2 == 0:
        result = [bin(num)[2:] for num in numbers]
    else:
        result = numbers

    return result

txt = input("Digite um texto: ")
numero = int(input("Digite um número de 1 a 30: "))

if 1 <= numero <= 30:
    resultado = txtForBin(txt, numero)
    print(f"Texto: {txt}")
    print(f"Resultado: {resultado}")
else:
    print("O número deve estar entre 1 e 30.")

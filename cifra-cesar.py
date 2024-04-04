import string

letras = list(string.ascii_lowercase)
frase = input("Digite a frase para aplicar a criptografia: ").lower()
valorValido = False

while valorValido is not True:
    try:
        chave = int(input("Valor da chave K para deslocamento: "))
        if chave < 26 and chave >= 0:
            valorValido = True      
            continue  

        print("O valor da chave deve estar entre 0 e 26.")
        valorValido = False

    except ValueError:
        print("Valor inválido.")

fraseCriptografada = ''

for letra in frase:
    if letra == " ":
        fraseCriptografada += " "
        continue

    posicao = letras.index(letra) + chave

    if posicao >= len(letras):
        posicao = posicao - len(letras)

    fraseCriptografada += letras[posicao]

print(f"Frase criptografada = {fraseCriptografada}")
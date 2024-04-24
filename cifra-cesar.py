import string

letras = list(string.ascii_lowercase)
frase = input("Digite a frase para aplicar a criptografia: ").lower()
valorValido = False

while valorValido is not True:
    try:
        chave = int(input("Valor da chave K para deslocamento: "))

        # Verifica a validade da chave de entrada.
        if chave < 26 and chave >= 0:
            valorValido = True      
            continue  

        print("O valor da chave deve estar entre 0 e 26.")
        valorValido = False

    except ValueError:
        print("Valor inválido.")

fraseCriptografada = ''

# Realiza a troca das letras de acordo com a chave.
for letra in frase:
    if letra == " ":
        fraseCriptografada += " "
        continue

    posicao = letras.index(letra) + chave

    if posicao >= len(letras):
        posicao = posicao - len(letras)

    fraseCriptografada += letras[posicao]

print(f"Frase criptografada = {fraseCriptografada}")

# Contabiliza a frequencia da letra no texto.
def calcularFrequencia(texto):
    frequencia = {}
    totalCaracteres = len(texto)
    
    for letra in texto:
        if letra.isalpha():
            letra = letra.lower()  # Converte para minúsculas
            if letra in frequencia:
                frequencia[letra] += 1
            else:
                frequencia[letra] = 1

    for letra in frequencia:
        frequencia[letra] /= totalCaracteres

    return frequencia

def criptoanalise(texto):

    # Frequência de letras no alfabeto português.
    frequenciaEsperada = {'a': 0.1463, 'b': 0.0104, 'c': 0.0388, 'd': 0.0499, 'e': 0.1257, 'f': 0.0102,
                           'g': 0.0130, 'h': 0.0128, 'i': 0.0618, 'j': 0.0040, 'k': 0.0002, 'l': 0.0278,
                           'm': 0.0474, 'n': 0.0505, 'o': 0.1073, 'p': 0.0252, 'q': 0.0120, 'r': 0.0653,
                           's': 0.0781, 't': 0.0434, 'u': 0.0463, 'v': 0.0167, 'w': 0.0001, 'x': 0.0021,
                           'y': 0.0001, 'z': 0.0047}
    
    frequenciaTextoCriptografado = calcularFrequencia(texto)

    menorDiferenca = float('inf')
    melhorChave = None

    for chave in range(26):
        diferencaTotal = 0
        
        # Calcula a soma das diferenças entre as frequências observadas e esperadas para cada letra.
        for letra in frequenciaTextoCriptografado:
            letraDeslocada = chr(((ord(letra) - ord('a') + chave) % 26) + ord('a'))
            frequenciaObservada = frequenciaTextoCriptografado[letra]
            frequenciaEsperadaLetra = frequenciaEsperada[letraDeslocada]
            diferencaTotal += abs(frequenciaObservada - frequenciaEsperadaLetra)
        
        # Verifica se a soma das diferenças é menor que a menor diferença encontrada até agora.
        if diferencaTotal < menorDiferenca:
            menorDiferenca = diferencaTotal
            melhorChave = chave
    
    return melhorChave

chave_criptoanalise = criptoanalise(fraseCriptografada)
print("Chave de deslocamento prevista com base na frequência:", chave_criptoanalise)
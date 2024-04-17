# Breno Lino Prado
# 202265013AC

# Convertendo texto para binário.
def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

# Convertendo binário para texto.
def binary_to_text(binary):
    text_chars = []
    
    for i in range(0, len(binary), 8):
        # Obtém um byte de caracteres binários (8 bits).
        byte = binary[i:i+8]

        # Converte o byte binário em um número inteiro.
        byte_int = int(byte, 2)
        
        # Converte o número inteiro em um caractere correspondente.
        char = chr(byte_int)
        
        # Adiciona o caractere convertido à lista de caracteres.
        text_chars.append(char)
    
    # Retorna a string.
    return ''.join(text_chars)

# Cifra de Feistel.
def alg_feistel(block, subkeys):
    size = len(block)//2

    # Divide o bloco recebido pela metade.
    left, right = block[:size], block[size:]

    for subkey in subkeys:
        # É aplicado a função F no lado direito e em seguida feita a operação XOR com o esquerdo.
        new_right = xor(left, function_F(right, subkey))

        # E então é feito a troca do direito pelo esquerdo e vice-versa.
        left = right
        right = new_right

    ciphed_block = left + right

    # É retornado o bloco criptografado.
    return ciphed_block

# Para decriptar, é feito o oposto da criptografia.
def dec_alg_feistel(ciphertext, subkeys):
    size = len(ciphertext)//2
    left, right = ciphertext[:size], ciphertext[size:]

    for subkey in subkeys:
        new_left = xor(right, function_F(left, subkey))
        right = left
        left = new_left

    plaintext = left + right
    return plaintext

# Função F utilizando uma S-BOX 4x4 para a substituição.
def function_F(right_half, subkey):
    S_BOX_4X4 = [
        [0x7, 0xC, 0x3, 0x8],
        [0xE, 0xA, 0xF, 0xB],
        [0x0, 0x5, 0x2, 0x9],
        [0x6, 0xD, 0x4, 0x1]
    ]

    xor_result = xor(right_half, subkey)
    substituted_value_binary = ''

    for i in range(0, len(xor_result), 4):
        nibble = xor_result[i:i+4]
        row = int(nibble[0] + nibble[3], 2)
        column = int(nibble[1:3], 2)
        substituted_value = S_BOX_4X4[row][column]
        substituted_value_binary += format(substituted_value, '04b')

    return substituted_value_binary

def xor(block1, block2):
    result = ''
    max_length = max(len(block1), len(block2))
    block1 = block1.zfill(max_length)
    block2 = block2.zfill(max_length)

    # Se bit1 == bit2, então o resultado é 0.
    # Se bit1 != bit2, então o resultado é 1.
    for bit1, bit2 in zip(block1, block2):
        result += '1' if bit1 != bit2 else '0'
    
    return result

def generate_subkeys(master_key):
    subkeys = []
    chunk_size = len(master_key) // 16

    # Gera as subchaves para criptografia e descriptografia.
    for i in range(16):
        subkey = master_key[i * chunk_size: (i + 1) * chunk_size]
        subkeys.append(subkey)

    # Para descriptografia, inverte a ordem das subchaves.
    subkeys_reverse = subkeys[::-1]

    return subkeys, subkeys_reverse

# Execução com chave aleatória de 48 bits.
master_key = "0101011101101111011100100110110001100100"
subkeys, subkeys_reverse = generate_subkeys(master_key)

# Entrada do texto a ser criptografado pela Cifra de Faiestel.
plaintext = input("Digite o texto para ser criptografado: ")
plaintext_binary = text_to_binary(plaintext)

# Cifragem do texto original
ciphertext = alg_feistel(plaintext_binary, subkeys)
print("Texto cifrado:", binary_to_text(ciphertext))

# Decifragem do texto cifrado
deciphertext = dec_alg_feistel(ciphertext, subkeys_reverse)
decrypted_text = binary_to_text(deciphertext)
print("Texto decifrado:", decrypted_text)
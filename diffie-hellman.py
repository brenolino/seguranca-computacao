p = 30851  # Número primo escolhido.
g = 2  # Raiz primitiva módulo p.

alice_number = 16943  # Número aleatório escolhido por Alice.
a_alice = (g ** alice_number) % p  # Cálculo de A pela Alice.
print("A calculado por Alice:", a_alice)

bob_number = 23090  # Número aleatório escolhido por Bob.
b_bob = (g ** bob_number) % p  # Cálculo de B pelo Bob.
print("B calculado por Bob:", b_bob)

# Alice calcula a chave compartilhada usando o B do Bob e seu próprio número aleatório.
s_alice = (b_bob ** alice_number) % p

# Bob calcula a chave compartilhada usando o A da Alice e seu próprio número aleatório.
s_bob = (a_alice ** bob_number) % p

print("Chave compartilhada pela Alice:", s_alice)
print("Chave compartilhada pelo Bob:", s_bob)

# Como esperado, agora tanto Alice quanto Bob possuem o mesmo valor de chave compartilhada
# e podem realizar a troca de informações.
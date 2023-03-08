lista_de_palavras = ["azul", "banana", "casamento", "distopia", "expurgo", "financiamento", "garganta", "horta", "incorporado", "jovem"]

import random
palavra_escolhida = lista_de_palavras[random.randint(0, len(lista_de_palavras) - 1)]
# palavra_escolhida = random.choice(lista_de_palavras)

#print(f'Teste - palavra escolhida: {palavra_escolhida}')

display = []
for letra in palavra_escolhida:
    display.append('_')
#print(f'A palavra tem {len(palavra_escolhida)} letras - {display}')

print (' '.join(display))

chute = input("Chuta uma letra ai, meu chapa: ").lower()

i = 0
for letra in palavra_escolhida:
    if chute == letra:
        display[i] = chute
        i += 1
    else:
        i += 1

print(' '.join(display))
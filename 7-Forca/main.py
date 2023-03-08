lista_de_palavras = ["azul", "banana", "casamento", "distopia", "expurgo", "financiamento", "garganta", "horta", "incorporado", "jovem"]

import random
# palavra_escolhida = lista_de_palavras[random.randint(0, len(lista_de_palavras) - 1)]
palavra_escolhida = random.choice(lista_de_palavras)

print(f'Teste - palavra escolhida: {palavra_escolhida}')

display = ""
for letra in palavra_escolhida:
    display += "_"
print(f'A palavra tem {len(palavra_escolhida)} letras - {display}')

chute = input("Chuta uma letra ai: ").lower()

i = 0
for letra in palavra_escolhida:
    if letra == chute:
        display[i] = str(letra)
    #else:
    #    print("errooooou!") 
    i += 1

print(display)
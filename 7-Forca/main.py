import random

lista_de_palavras = ["azul", "banana", "casamento", "distopia", "expurgo", "financiamento", "garganta", "horta", "incorporado", "jovem"]

palavra_escolhida = lista_de_palavras[random.randint(0, len(lista_de_palavras) - 1)]
tamanho = len(palavra_escolhida)
# palavra_escolhida = random.choice(lista_de_palavras)

#print(f'Teste - palavra escolhida: {palavra_escolhida}')

display = []
for letra in palavra_escolhida:
    display.append('_')
#print(f'A palavra tem {len(palavra_escolhida)} letras - {display}')

print (' '.join(display))

tentativas = tamanho
while tentativas > 0:

    chute = input("Chuta uma letra ai, meu chapa: ").lower()
    
    for posicao in range(tamanho):

        letra = palavra_escolhida[posicao]

        if chute == letra:
            display[posicao] = chute
        
    tentativas -= 1

    print(' '.join(display))
    
    if tentativas >= 2:
        print(f'você tem {tentativas} tentativas restantes, otário!')
    else: 
        print(f'você tem {tentativas} tentativa restante, otário!')

    
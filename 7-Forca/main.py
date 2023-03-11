import random
import palavras
import artes

lista_de_palavras = palavras.lista_de_palavras
palavra_escolhida = lista_de_palavras[random.randint(0, len(lista_de_palavras) - 1)]
tamanho = len(palavra_escolhida)
# palavra_escolhida = random.choice(lista_de_palavras)
#print(f'Teste - palavra escolhida: {palavra_escolhida}')
display = []
fim_do_jogo = False
vidas = 6
contador_auxiliar_com_nome_generico = tamanho
logo_jogo = artes.logo
letras_usadas = []
forca = artes.forca

print(logo_jogo)

for letra in palavra_escolhida:
    display.append('_')
#print(f'A palavra tem {len(palavra_escolhida)} letras - {display}')

print(f"Tenta acerta a palavra aí ó: {' '.join(display)}")
print(f"Ah, tem só {vidas} tentativas...")

while not fim_do_jogo:
    
    chute = input("Chuta uma letra ai, meu chapa: ").lower()
    
    while chute in letras_usadas:
        print(f"Meu bom, ta de sacanagem, tu já falou a letra {chute}.")
        chute = input("Chuta outra letra ai, meu irmão...: ").lower()

    letras_usadas.append(chute)

    for posicao in range(tamanho):

        letra = palavra_escolhida[posicao]

        if chute == letra:
            display[posicao] = chute

    if chute not in palavra_escolhida:
      print("Errooooou!")
      vidas -= 1
      if vidas == 0:
          fim_do_jogo = True
          print("Você perdeu, otário!")        
    print(f"{' '.join(display)}")

    if "_" not in display:
        fim_do_jogo = True
        print("você ganhou o jogo, mas perdeu um tempo de vida que nunca mais vai recuperar")
    
    print(forca[vidas])
    
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

opcao = input("Digite 'c' para criptografar e 'd' para descriptografar: ")
texto = list(input("Digite a mensagem: ").lower())
deslocamento = int(input("Digite o número de deslocamentos: "))


def criptografar(texto, deslocamento):
    texto_cifrado = []
    texto_plano = list(texto)
    for letra in texto_plano:
        if alfabeto.index(letra) + deslocamento > len(alfabeto):
            deslocamento -=  alfabeto.index(letra) + len(alfabeto)
        texto_cifrado += alfabeto[alfabeto.index(letra) + deslocamento]
    print(texto_cifrado)

if opcao == "c":
    criptografar(texto, deslocamento)
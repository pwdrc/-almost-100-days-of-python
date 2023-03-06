import random
import string

alfabeto = list(string.ascii_letters)
numeros = list(range(0,10))
especiais = ['!','@','#','$','%','&']

numero_letras = int(input("Quantidade de letras:"))
numero_numeros = int(input("Quantidade de números:"))
numero_especiais = int(input("Quantidade de caracteres especiais ('!','@','#','$','%','&'):"))

total = numero_letras + numero_numeros + numero_especiais
password = ""
cl = cn = ce = 0

for i in range(0, total + 1):
    factor = random.randint(0,3)
    if (factor == 0 and cl <= numero_letras):
        password += str(alfabeto[random.randint(0, len(alfabeto))])
        cl = cl + 1
    elif (factor == 1 and cn <= numero_numeros):
        password += str(numeros[random.randint(0, len(numeros))])
        cn = cn + 1
    elif (factor == 2 and ce <= numero_especiais):
        password += str(especiais[random.randint(0, len(especiais))])
        ce = ce + 1
    else:
        i = i - 1

print(password)

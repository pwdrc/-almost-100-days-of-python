import random
import string
from random import sample

alfabeto = list(string.ascii_letters)
numeros = list(range(0,10))
especiais = ['!','@','#','$','%','&']

numero_letras = int(input("Quantidade de letras:"))
numero_numeros = int(input("Quantidade de números:"))
numero_especiais = int(input("Quantidade de caracteres especiais:"))

password = ""

for i in range(0,numero_letras):
    password += str(alfabeto[random.randint(0,len(alfabeto)-1)])

for i in range(0,numero_numeros):
    password += str(numeros[random.randint(0,len(numeros)-1)])

for i in range(0,numero_especiais):
    password += str(especiais[random.randint(0,len(especiais)-1)])

password = sample(password,len(password))

pwd = ''
for i in range(len(password)):
    pwd += str(password[i])

print(pwd)

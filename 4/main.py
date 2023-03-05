import random

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

user_select = input("Pedra (0), papel (1) ou tesoura (2)?")
comp_select = random.randint(0,3)

if user_select == '0':
    print(pedra)
elif user_select == '1':
    print(papel)
else:
    print(tesoura)

print("O computador jogou:")
if comp_select == 0:
    print(pedra)
elif comp_select == 1:
    print(papel)
else:
    print(tesoura)

user_select = int(user_select)
if user_select == comp_select:
    print("empate!")
elif (user_select == 0 and comp_select == 2) or (user_select == 1 and comp_select == 0) or (user_select == 2 and comp_select == 1):
    print("ganhou")
else:
    print("perdeu")


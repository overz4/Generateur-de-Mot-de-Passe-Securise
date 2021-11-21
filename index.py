import random
lower ="abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBER = "0123456789"
Symbol = "[]{}#()*;._-¨^$£µù%§!:/?,"

all=lower + upper + NUMBER + Symbol
length = 9
password = "".join(random.sample(all,length))
print("Le mot de passe que vous avez généré est :",password)
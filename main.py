import random

low = "abcdefghijklmnopqrstuvwxyz"
up = "ABCDEFGHIJKLMOPQRSTUVWXYZ"
num = "0123456789"
symbols = ",-'.{}[]*;()"

luns = low + up + num + symbols

pass_length = input('''Type in your password length that you want to generate : ''')
length = int(pass_length)

password = "".join(random.sample(luns, int(pass_length)))
print(password)

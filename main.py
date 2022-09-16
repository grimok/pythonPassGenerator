import random

lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

symbols = ['@', '#','!','~','$','%','^',
                '&','*','(',',','-','+','/',
                ':','.',',','<','>','?','|']

password = random.choice(lowercase)

for i in range(1,12):
  if(i < 8):
    t = random.randint(1,2)
    if(t == 2):
      password += random.choice(lowercase)
    else:
      password += random.choice(uppercase)
  else:
    password += random.choice(symbols)

for x in range(1,6):
  password += str(random.randint(1,9))

#print(password)

l = [*password]
random.shuffle(l)
password = ''

for x in l:
  password += x

print(password)
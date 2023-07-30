nombre = int(input("Veuillez rentrer un nombre : "))
divisible = False

for i in range(2,nombre):
    if (nombre % i)==0:
            divisible=True
            break

if divisible:
      print(f"{nombre} n'est pas un nombre premier")
else:
      print(f'{nombre} est un nombre premier')
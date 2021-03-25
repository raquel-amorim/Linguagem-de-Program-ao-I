with open("100inteiros.txt", "w") as numeros:
    for i in range(0, 101):
        numeros.write(f"{i}\n")

with open("pares.txt", "w") as pares:
    with open("100inteiros.txt") as numeros:
        for i in numeros.readlines():
            if int(i) % 2 == 0:
                pares.write(f"{i}")

with open("multiplos5.txt", "w") as multiplos5:
    with open("100inteiros.txt") as numeros:
        for i in numeros.readlines():
            if int(i) % 5 == 0:
                multiplos5.write(f"{i}")
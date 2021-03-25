with open("pares2.txt", "w") as pares:
        for n in range(2, 101):
            if n % 2 == 0:
                pares.write(f"{n}\n")
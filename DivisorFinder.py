
n = int(input("Veuillez entrer un entier positif non nul : "))
i = 1


while i <= n:
    if n % i == 0:
        print(i)
    i += 1

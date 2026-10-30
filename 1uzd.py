
N = int(input("Ievadi skaitli N: "))
summa = 0
print("Pāra skaitļi no 1 līdz", N, ":")
for i in range(2, N + 1, 2):
    print(i)
    summa += i
print("Pāra skaitļu summa ir:", summa)
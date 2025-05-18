n=int(input('Введите число:'))
for i in range(n,0,-1):
    print(i)

n=float(input('Введите число:'))
for i in range(1, 11):
    result = n / i
    print(f"{n} / {i} = {result:.2f}")
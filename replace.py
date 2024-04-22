import math

a, b, c = map(float, input("Введите переменные в столбик без знаков: ").split())

discr = b ** 2 - 4 * a * c

if discr < 0:
    print("Решения нет")
else:
    if discr == 0:
        x1 = -b / (2 * a)
        x2 = x1
    else:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)

    s = x1 * x2 * (210 / 7 - 35)
    print(f"s = {s:.0f}")

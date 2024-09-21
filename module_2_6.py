# Переменная a может быть только от 3 и более.
a = 3
b = 20

def required_password(n):
    if n > b or n < a:
        result = f"Нет, надо от {a} до {b}"
        print(result)
        print()
    else:

        for i in range(3, b + 1):
            result = []
            for j in range(1, b // 2):
                for k in range(2, b):
                    if i % (j + k) == 0 and j < k:
                        result.extend([j, k])

            if i == n:
                print(i, ' - ', *result, sep='')
                print()


for n in range(5):
    required_password(int(input(f"Введите число от {a} до {b}: ")))

first_numbers = range(3, 21)

for first_number in first_numbers:
    result = ''
    for i in range(1, 20):
        for j in range(i + 1, 20):
            if first_number % (i + j) == 0:
                result += str(i) + str(j)
    print(f'{first_number} - {result}')

number =int(input('Enter a number to see its multiplication table: '))

i = 1

for i in range(1,11):
    product = number * i
    print(number, '*', i, '=', product)

    i -= 1

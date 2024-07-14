afe_divide(numerator, denominator):

    try:
        numerator1 = float(numerator)
        denominator1 = float(denominator)

        division = numerator1 / denominator1
        return print('The result of the division is', division)

    except ZeroDivisionError:
        return('Error: Cannot divide by zero.')
        

    except ValueError:
            return('Error: Please enter numeric values only.')

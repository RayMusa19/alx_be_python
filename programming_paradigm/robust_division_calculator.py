def safe_divide(numerator, denominator):

    try:
        numerator1 = float(numerator)
        denominator1 = float(denominator)

        division = numerator1 / denominator1
        return division

    except ZeroDivisionError:
        return('Error: Cannot divide by zero.')
        

    except ValueError:
        if isinstance(float(numerator), (float)) and isinstance(float(denominator), (float)):
            division = (float(numerator) / float(denominator))
            return ('The result of the division is',division)

        else:
            print('Error: Please enter numeric values only.')
            return
    


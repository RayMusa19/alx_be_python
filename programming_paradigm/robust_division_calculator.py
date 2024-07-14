def safe_divide(numerator, denominator):
    
    try:
        numerator1 = float(numerator)
        denominator1 = float(denominator)

        division = numerator1 / denominator1

    except ZeroDivisionError:
        division = print('Cannot bivide by 0')

    except ValueError:
        if isinstance(float(numerator, denominator), (float)):
            division = (float(numerator) / float(denominator))
        else:
            division = print('Enter an integer')

    return division

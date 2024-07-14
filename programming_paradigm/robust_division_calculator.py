def safe_divide(numerator, denominator):
    try: division = numerator / denominator

    except ZeroDivisionError:
        division = print('Cannot bivide by 0')

    except ValueError:
        if isinstance(str(denominator), (int, float)):
            division = numerator / float(denominator)
        else:
            division = print('Enter an integer')

    return division

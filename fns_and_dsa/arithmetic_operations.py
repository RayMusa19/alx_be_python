def perform_operation(num1, num2, operation):
    if num2!=0:
        match operation:
            case 'add': result = num1 + num2
            case 'subtract': result = num1 - num2
            case 'multiply': result = num1 * num2
            case 'divide': result = num1 / num2
        return result
    else:
        return 'Not divisible by 0'

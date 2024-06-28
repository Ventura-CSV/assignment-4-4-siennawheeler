def main():

    numbers = []
    """
    ########################################
    Code Your Program here
    ########################################
    """

    num1 = int(input('First number: '))
    numbers.append(num1)
    num2 = int(input('Second number: '))
    numbers.append(num2)
    num3 = int(input('Third number: '))
    numbers.append(num3)
    num4 = int(input('Fourth number: '))
    numbers.append(num4)
    num5 = int(input('Fifth number: '))
    numbers.append(num5)

    if num1 > num2:
        maxval = num1
        minval = num2
    else:
        maxval = num2
        minval = num1
    for n in range(2, 5):
        if numbers[n] < minval:
            minval = numbers[n]
        if numbers[n] > maxval:
            maxval = numbers[n]
    

    print(*numbers)
    print(maxval, minval)
    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, maxval, minval


if __name__ == '__main__':
    main()

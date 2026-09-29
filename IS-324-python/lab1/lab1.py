import math


def program1():
    n = input('enter value of n: ')
    nn = n * 2
    nnn = n * 3
    result = int(n) + int(nn) + int(nnn)
    print('the result is:', result)


def program2():
    tax_percentage = 0.15
    total_purchase = float(input('enter the amount of purchase: '))
    sales_tax = tax_percentage * total_purchase
    total = total_purchase + sales_tax
    print(f'total purchase = {total_purchase} SR')
    print(f'sales tax = {sales_tax} SR')
    print(f'total = {total} SR')


def program3():
    x = int(input('enter the value of x: '))
    y = int(input('enter the value of y: '))

    result = x * x * y + x * y + x * y * y
    print(f'the computed value is: {result}')


def program4():
    total = 0
    counter = 0

    n = int(input('Enter numbers to calculate their sum and average. Enter 0 to exit:'))

    while n != 0:
        counter += 1
        total += n
        avg = total / counter
        print(f'Sum = {total} , Average = {avg}')
        n = int(input('Enter numbers to calculate their sum and average. Enter 0 to exit:'))


def program5():
    mb = int(input('Enter the size of data in MBs: '))
    dig = int(input('How many digits to show after the decimal point? '))
    gb = mb / 1024

    result = format(gb, f'.{dig}f')
    print(f'Size in GB : {result}')


def program6():
    n = int(input('Enter number: '))
    isprime = True

    if n < 2:
        isprime = False
    else:
        for x in range(2, n):
            if n % x == 0:
                isprime = False
                break

    if isprime:
        factorial_result = math.factorial(n)
        print(f'{n} is prime.')
        print(f'its factorial : {factorial_result}')
    else:
        print(f'{n} is not prime.')


def program7():
    star = '*'
    for x in range(3):
        print(star * x)
        print()
# im not sure if this is the correct way to approach 
# if im wrong please correct me with a note id appreciate it 


def program8():
    number = 5
    guess = None
    failed_attempts = 0
    total_attempts = 0
    print('Guess the number!')

    while guess != number and failed_attempts < 10:
        guess = int(input('Is it... '))
        total_attempts += 1

        if guess == number:
            print('Wow! You guessed it right!')
            if total_attempts <= 3:
                print('You are an amazing guesser!')
            break
        elif guess < number:
            failed_attempts += 1
            print("Opps, It's bigger...")
        elif guess > number:
            failed_attempts += 1
            print("Opps, It's not so big.")

    if failed_attempts >= 10 and guess != number:
        print('Sorry, you ran out of attempts :( ')

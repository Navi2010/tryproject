try:
    age = int(input('enter your age: '))
    if age%2==0:
        print('your age is an even number.')
    else:
        print('your age is an odd number.')
except ValueError as e:
    print('you must have not entered your age number... pls try again.')
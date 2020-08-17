def ran_check(num,low,high):
    if num in range(low,high+1):
        print(f'{num} is in range')
    else:
        print('Not in range')
n = int(input('Enter the number '))
low = int(input('Enter minimum range '))
high = int(input('Enter maximum range '))
ran_check(n,low,high)
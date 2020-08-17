def up_low(s):
    lowercase = 0
    uppercase = 0
    for char in s:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
        else:
            pass
    print(f'Original string : {s}')
    print(f'Lowercase count : {lowercase}')
    print(f'Uppercase count : {uppercase}')
up_low("A Rabbit Eats Carrots And Runs Rapidly")
day = 32

try:
    if day > 31:
        raise ValueError('Invalid day Number')
except ValueError as msg:
    print(msg)
finally:
    print('But today is a beautiful day')

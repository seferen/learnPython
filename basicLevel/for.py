chars = ['A', 'B', 'C']
fruit = ['Apple', 'Banana', 'Cherry']
dict = {'name': 'Mike', 'ref': 'Python', 'sys': 'Win'}
print('\nElements: ', end=' ')
for item in chars:
    print(item, end=' ')
print('\nEnumerated: ', end=' ')
for item in enumerate(chars):
    print(item, end=' ')
print('\nZipped: ', end=' ')
for item in zip(chars, fruit):
    print(item, end=' ')
print('\nPaired: ')
for key, value in dict.items():
    print(key,'=',value)

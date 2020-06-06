dict = {'name': 'Bob', 'ref': 'Python', 'Sys': 'Win'}
print('\nReference: ', dict['ref'])
print('\nKets: ', dict.keys())
del dict['name']
dict['user'] = 'Tom'
print('\nDictionary: ', dict)
print('\nIs there a name key? ', 'name' in dict)

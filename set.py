zoo = ('Kangaroo', 'Leopard', 'Moose')
print('Tuple: ', zoo, '\tLength: ', len(zoo))
print(type(zoo))
bag = {'Red', 'Green', 'Blue'}
bag.add('Yellow')
print('\nSet: ', bag, '\tLength: ', len(bag))
print(type(bag))
print('\nIs Green in bag Set: ', 'Green' in bag)
print('\nIs Orange in bag Set: ', 'Orange' in bag)
box = {'Red', 'Purple', 'Yellow'}
print('\nSet: ', box, '\tLength: ', len(box))
print('Common to both Sets: ', bag.intersection(box))
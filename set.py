my_set = set('hola')
my_orther_set = {}

print(my_set)
print(type(my_set))
print(type(my_orther_set))

my_orther_set = {'jose', 'medina', 26}
print(type(my_orther_set))
print(len(my_orther_set))
print(my_orther_set)
my_orther_set.add('jairo')
print(my_orther_set)

print('jarez' in  my_orther_set)


print('jairo' in  my_orther_set)
my_orther_set.clear()
print(my_orther_set)
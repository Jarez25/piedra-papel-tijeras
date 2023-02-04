set_paise = {'Col', 'Nic', 'Hod'}

size = len(set_paise)  
print(size)

print('Col' in set_paise)

print('Per' in set_paise)

#añadir set

set_paise.add('Pe')
print(set_paise)

#actualizar set

set_paise.update({'Arg', 'Can', 'Egt', 'Pe'})
print(set_paise)

#borrar set

set_paise.remove('Arg')
print(set_paise)

#set_paise.remove('Ar')
set_paise.discard('Ar')
print(set_paise)
set_paise.add('Gua')
print(set_paise)
set_paise.clear()
print(set_paise)
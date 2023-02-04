set_paiseUno = {'Col', 'Mex', 'Bol'}
set_paiseDos = {'Pe', 'Nic', 'Bol'}

set_paiseFull = set_paiseUno.union(set_paiseDos)
print(set_paiseFull)

set_paiseFull = set_paiseUno.intersection(set_paiseDos)
print(set_paiseFull)
print(set_paiseUno & set_paiseDos)

set_paiseFull = set_paiseUno.difference(set_paiseDos)
print(set_paiseUno - set_paiseDos)
print(set_paiseFull)


set_paiseFull.symmetric_difference(set_paiseUno)
print(set_paiseFull)
print(set_paiseUno ^ set_paiseDos)
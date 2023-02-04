items = [
  {
    'product': 'camisa',
    'precio': 100,
  },
  {
    'product': 'pantalones',
    'precio': 300
  },
  {
    'product': 'pantalones 2',
    'precio': 200
  }
]

precio = list(map(lambda item : item['precio'], items))
print(precio)

def iva(item):
    item['impuesto'] = item['precio'] * .20
    return item

newItems = list(map(iva, items))
print(newItems)

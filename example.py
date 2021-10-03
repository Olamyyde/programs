from shirt import Shirt

shirt1 = Shirt('red', 'M', 'long_sleeved', 43)
shirt2 = Shirt('orange', 'S', 'short_sleeved', 30)


print(shirt1.price)
print(shirt2.color)
print(shirt2.style)

shirt2.change_price(45)

print(shirt2.price)



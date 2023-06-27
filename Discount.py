product = str(input('The product which the discount will be applied: '))
productPrice = float(input('Product original price: '))
discount = float(input('How much discount will be applied in (%): '))

finalPrice = (productPrice / 100) * (100 - discount)

print(product)
print('Discount Applied!')
print('Total discount: ', discount,'%')
print(product, 'with discount: ', '$',finalPrice)
resp = str(input('Run again? (s/n)'))
if resp == 'n':
    print("App closing, thx.")
while resp == "s":
    product = str(input('The product which the discount will be applied: '))
    productPrice = float(input('Product original price: '))
    discount = float(input('How much discount will be applied in (%): '))

    finalPrice = (productPrice / 100) * (100 - discount)

    print(product)
    print('Discount Applied!')
    print('Total discount: ', discount, '%')
    print(product, 'with discount: ', '$', finalPrice)
    resp = str(input('Run again? (s/n)'))

    if resp == 'n':
        print("App closing, thx.")


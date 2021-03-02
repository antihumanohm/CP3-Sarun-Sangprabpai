def vatcalculate(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result

totle = int(input("ราคาสินค้า : "))
print(vatcalculate(totle))
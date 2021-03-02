def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return showMenu()
    else:
        print("คุณกรอก user password ไม่ถูกต้อง")
        return login()
def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    print("3. exit")
    return menuSelect()
def menuSelect():
    userSelected = int(input("เลือกเมูทำรายการ : "))
    if userSelected == 1:
        pricevat = int(input("กรอกราคาสินค้า : "))
        print("ราคาสินค้ารวม Vat7% = ",vatCalculator(pricevat))
        return menuSelect()
    elif userSelected == 2:
        print("ราคาสินค้ารวม Vat7% = ",priceCalculator())
    elif userSelected == 3:
        return exit()
    else:
        print("กรุณาเลือกเมนูทำรายการตามหมายเลข")
        return menuSelect()
def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result
def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    sum = price1 + price2
    print("ราคาสินค้าไม่รวม Vat7% = ",sum)
    return vatCalculator(price1 + price2)

login()
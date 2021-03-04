menulist = []
pricelist = []
def showbill():
    print("----My Food----")
    totalprice = 0
    for number in range(len(menulist)):
        print(menulist[number],pricelist[number])
        totalprice += int(pricelist[number])
    print("ราคารวมสินค้า: ",totalprice)
while True:
    menuname = input("กรอกรายชื่อสินค้า : ")
    if (menuname.lower() == "exit"):
        break
    else:
        menuprice = int(input("กรอกราคาสินค้า : "))
        menulist.append(menuname)
        pricelist.append(menuprice)
print(menulist,pricelist)
print(showbill())
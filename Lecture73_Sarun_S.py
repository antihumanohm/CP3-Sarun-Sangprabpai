menulist = []
def showbill():
    print("----My Food----")
    totalprice = 0
    for number in range(len(menulist)):
        totalprice+= int(menulist[number][1])
        print(menulist[number][0],"ราคา",menulist[number][1])
    print("รวมราคาสินค้า : ",totalprice)

while True:
    menuname = input("กรอกรายชื่อสินค้า : ")
    if (menuname.lower() == "exit"):
        break
    else:
        menuprice = int(input("กรอกราคาสินค้า : "))
        menulist.append([menuname,menuprice])

(showbill())
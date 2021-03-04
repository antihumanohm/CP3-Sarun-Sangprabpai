systemmenu = {"ข้าวหมกไก่":45,"ข้าวมันไก่":50,"ข้าวไข่เจียว":35,"ข้าวหน้าไก่":45}
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
        menulist.append([menuname,systemmenu[menuname]])

(showbill())
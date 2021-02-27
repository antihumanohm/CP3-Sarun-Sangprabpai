user = input("Username : ")
pas = input("Password : ")
if user == "admin" and pas == "1234":
    print("----ยินดีต้อนรับสู่ร้านขายน้ำ----")
    print("----กรุณาเลือกรายการสินค้าโดยพิมหมายเลข----")
    print("1.อิชิตัน 20THB")
    print("2.ชเวปส์ 15THB")
    print("3.แฟนต้า 18THB")
    print("4.โค้ก 18THB")
    print("5.เป๊ปซี่ 18THB")
    water = int(input("เลือกสินค้าหมายเลข :"))
    if water == 1:
        amount = int(input("กรุณาระบุจำนวน : "))
        print("อิชิตัน",amount,"ขวด","ราคา",amount*20)
    if water == 2:
        amount = int(input("กรุณาระบุจำนวน : "))
        print("ชเวปส์",amount,"ขวด","ราคา",amount*15)
    if water == 3:
        amount = int(input("กรุณาระบุจำนวน : "))
        print("แฟนต้า",amount,"ขวด","ราคา",amount*18)
    if water == 4:
        amount = int(input("กรุณาระบุจำนวน : "))
        print("โค้ก",amount,"ขวด","ราคา",amount*18)
    if water == 5:
        amount = int(input("กรุณาระบุจำนวน : "))
        print("เป๊ปซี่",amount,"ขวด","ราคา",amount*18)
else:
    print("คุณกรอก Username&Password ไม่ถูกต้อง")
print("ออกจากโปรแกรม")




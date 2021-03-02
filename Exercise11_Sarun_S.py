number = int(input("กรอกตัวเลข : "))
print("จำนวน",number,"แถว")
for i in range(number):
    print(" "*(number-i),"*"*(((i+1)*2)-1))
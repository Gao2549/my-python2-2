def rectangle(width,long):
    area = width*long
    return area

w = int(input("กว้าง: "))
l = int(input("ยาว: "))
print("พื้นที่สี่เหลี่ยมผืนผ้า %d " % rectangle(w,l))
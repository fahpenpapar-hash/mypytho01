#กรณี 1 print() มีข้อมูลหลายประเภท ใช้ 4 วิธี
#วิธี 1ใช้ (โดยการแสดงผลที่ตรงจุด , จะเป็นการเว้น 1 spacce)
print('Hello',500,'weeb' ,789, 'AHHHHHH' ,35+10,10.235)
#วิธีที่ 2 ใช้ + (ข้อมูลไหนที่ไม่ใช่ string ต้องทำให้เป็น srting ใช้ฟังก์ชั่น str())

print('Hello' + str(500) + 'weeb' + str(789) + str(True) + 'AHHHHHH' + str(35+10) + str(10.235))
print('Hello' + " "+str(500) + 'weeb' str(789) +" " + str(True) +'AHHHHHH' + str(35+10)+" " + str(10.235))

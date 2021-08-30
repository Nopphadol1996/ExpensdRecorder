#GUI Basic  2 EP3 Expense.py

# EP4 https://www.youtube.com/watch?v=yNIgU2QF9fc

from tkinter import ttk
from tkinter import * # ttk is them of Tk
from datetime import datetime
import csv


GUI = Tk()

GUI.title('โปรแกรมบันทึกค่าใช้จ่าย')
GUI.geometry('500x350+500+200')


# B1 = Button(GUI,text='Hello1')
# B1.pack(ipadx=50,ipady=100) # ติดปุ่มเข้ากับ GUI หลัก ipadx=50 ตามแนวแกนx , ipady=100 ตามแนวแกน y

F1 = Frame(GUI)     # สร้าง Frame เปรียบเสมือนฟิวเจอร์บอร์ด
F1.place(x=100,y=50)

days = {'Mon':'จันทร์',
		'Tue':'อังคาร์',
		'Wed':'พุธ',
		'Thu':'พฤหัสบดี',
		'Fri':'ศุกร์',
		'Sat':'เสาร์',
		'Sun':'อาทิตย์'}

def Save(even=None):
         expense = v_expense.get() # .get ดึงค่ามาจาก v_expense = StringVarผป
         price = v_price.get() # .get ดึงค่ามาจาก v_expense = StringVar
         quantity = v_quantity.get() # .get ดึงค่ามาจาก v_expense = StringVar
         total = int(price)	* int(quantity)
         print('รายการ: {} ราคา: {} บาท' .format(expense,price))
         print('จำนวน:{} ชิ้น รวมทั้งหมด {} บาท '.format(quantity,total))

         # Clear ข้อมูลเก่า
         v_expense.set('')
         v_price.set('')
         v_quantity.set('')


         # บันทึกข้อมูลลง csv
         today = datetime.now().strftime('%a') # เรียก %a คือวันที่ เป็น format สามารถดูได้ใน google https://strftime.org/

         dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
         dt = days[today] + '-' + dt # แล้วเอา dictionaryมาบวกกับ days[today] ที่ get จาก datetime มา กับ - บวก dt
         with open('savedata.csv','a',encoding='utf-8',newline='') as f:

         	# with คือ คำสั่งเปิดไฟล์แล้วปิดอัตโนมัติ
         	# 'a' คือ การบันทึกไปเรื่อยๆ เพิ่มข้อมูลจากข้อมูลเก่า แต่ถ้า w  เคลียค่าเก่าแล้วบันทึกใหม่
         	# newline='' คือการทำให้ข้อมูลไม่มีบรรทัดว่าง

         	fw = csv.writer(f) # สร้างฟังก์ชั่นสำหรับเขียนข้อมูล
         	data = [dt,expense,price,quantity,total]
         	fw.writerow(data)
         # ทำให้เคอร์เซอร์กลับไปตำแหน่งช่องกรอก E1
         E1.focus()

######## ทำให้สามารถกด Enter ได้ ###############


GUI.bind('<Return>',Save) # ต้องเพิ่มใน def Save(event=None)

#############################################

#-------text1--------------
FONT1 = (None,20) # None เปลี่ยนเป็น 'Angsana New'

L1 = ttk.Label(F1,text='รายการค่าใช้จ่าย',font=FONT1).pack()
v_expense = StringVar() # String() คือตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E1 = ttk.Entry(F1,textvariable=v_expense,font=FONT1)
E1.pack()

#-------text1--------------


#-------text2--------------

L2 = ttk.Label(F1,text='ราคา (บาท)',font=FONT1).pack()
v_price = StringVar() # String() คือตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E2 = ttk.Entry(F1,textvariable=v_price,font=FONT1) # Entry คือ ช่องกรอกรับข้อมูลจาก User
E2.pack()

#-------text2-------------

#-------text3--------------

L3 = ttk.Label(F1,text='จำนวน (ชิ้น)',font=FONT1).pack()
v_quantity = StringVar() # String() คือตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E3 = ttk.Entry(F1,textvariable=v_quantity,font=FONT1) # Entry คือ ช่องกรอกรับข้อมูลจาก User
E3.pack()

#-------text3--------------


B2 = ttk.Button(F1,text='Save',command=Save)
B2.pack(ipadx=50,ipady=20) # ติดปุ่มเข้ากับ GUI หลัก

         

GUI.mainloop()

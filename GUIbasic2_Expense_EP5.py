#GUI Basic  2 EP3 Expense.py

from tkinter import ttk,messagebox
from tkinter import * # ttk is them of Tk
from datetime import datetime
import csv

GUI = Tk()

GUI.title('โปรแกรมบันทึกค่าใช้จ่าย V 1.0 ')
GUI.geometry('580x670+500+10')

# B1 = Button(GUI,text='Hello1')
# B1.pack(ipadx=50,ipady=100) # ติดปุ่มเข้ากับ GUI หลัก ipadx=50 ตามแนวแกนx , ipady=100 ตามแนวแกน y

########## สร้าง TAb ###############

Tab = ttk.Notebook(GUI)
T1 = Frame(Tab)#,width=400,height=400
T2 = Frame(Tab)
Tab.pack(fill=BOTH,expand=1) # BOTH ขยายทั้งหมด แกนX,Y

########## สร้าง TAb ###############

########## ดึงข้อมูลรูปภาพ .png ##############

icon_t1 = PhotoImage(file='T1_expens.png') # .subsample(2) ย่อขนาดลง2เท่าใช้ได้กับรูป png เท่านั้น
icon_t2 = PhotoImage(file='T2_expens.png')
icon_b1 = PhotoImage(file='button_save.png')

########## ดึงข้อมูลรูปภาพ .png ##############

#### เอารูปภาพมาใส่ในช่อง TAB, compound = 'left' ,top บน ,right = ขวา
Tab.add(T1,text=f'{"ค่าใช้จ่าย":^{30}}',image=icon_t1,compound='top') #ใช้ f-string มากำลังหนดระยะข้อความให้เท่ากัน ^ คือเริ่มจาก CENtor <คือ ซ้าย > ขวาสุด
Tab.add(T2,text=f'{"ค่าใช้จ่ายทั้งหมด":^{30}}',image=icon_t2,compound='top')	

F1 = Frame(T1)     # สร้าง Frame เปรียบเสมือนฟิวเจอร์บอร์ด  เอา TABมาใส่ใน Fram
#F1.place(x=100,y=50) # control ระยะ
F1.pack() # ขยายตามหน้าจอวางจากบนจากบนลงล่าง

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
	if expense == '':
		messagebox.showwarning('ERROR','กรุณากรอกรายการค่าใช้จ่าย')
		
		return

	elif price =='':

		messagebox.showwarning('ERROR','กรุณากรอกราคา')
		print('กรุณาใส่ราคา')
		return

	elif quantity =='':

		quantity = 1 #กำหนดค่า Default = 1 ถ้าหาก User ไม่ใส่ 
		#messagebox.showwarning('ERROR','กรุณากรอกจำนวน')
		#return

	try:
		total = float(price)	* float(quantity)
		print('รายการ: {} ราคา: {} บาท' .format(expense,price))
		print('จำนวน:{} ชิ้น รวมทั้งหมด {} บาท '.format(quantity,total))

		########## แสดงผลออกทาง GUI ################
		text = 'รายการ: {} ราคา: {} บาท\n'.format(expense,price)
		text = text + 'จำนวน:{} ชิ้น รวมทั้งหมด {} บาท '.format(quantity,total)
		v_result.set(text)

		########## แสดงผลออกทาง GUI ################

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


	except:
		print('ERROR')
		#messagebox.showerror('ERROR','กรุณากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')
		messagebox.showwarning('ERROR','กรุณากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')
		#messagebox.showinfo('ERROR','กรุณากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')

		# Clear ข้อมูลเก่า
		v_expense.set('')
		v_price.set('')
		v_quantity.set('')
		E1.focus()


######## ทำให้สามารถกด Enter ได้ ###############


GUI.bind('<Return>',Save) # ต้องเพิ่มใน def Save(event=None)

#############################################

#-------text1--------------
FONT1 = (None,20) # None เปลี่ยนเป็น 'Angsana New'

############## image ############
Main_icon = PhotoImage(file='icon_money.png')


Mainicon = Label(F1,image=Main_icon)
Mainicon.pack()



############## image ############

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


B2 = ttk.Button(F1,text=f'{"Save":>{10}}',image=icon_b1,compound='left',command=Save)
B2.pack(ipadx=50,ipady=20,pady=20) # ติดปุ่มเข้ากับ GUI หลัก


################# แสดงผลลัพธฺ์ออกทางหน้าจอ ##################
v_result = StringVar()
v_result.set('--------ผลลัพธ์--------')
result = ttk.Label(F1,textvariable=v_result,font=FONT1,foreground='green')
# result = Label(F1,textvariable=v_result,font=FONT1,fg='green') ของ Mac os จะใช้รูปแบบนี้
result.pack(pady=20)

################# แสดงผลลัพธฺ์ออกทางหน้าจอ ##################
         
GUI.bind('<Tab>',lambda x:E2.focus())
GUI.mainloop()

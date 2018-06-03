from tkinter import *
from tkinter import messagebox as msgbox

root = Tk()
#设置标题
root.title("绩点计算工具")
#设置窗口尺寸
root.geometry('400x400')
root.resizable(width=False, height=False) #宽不可变, 高可变,默认为True

grade = []
credit = []
count = 0

def calculate():
	credit_all = 0
	grade_all = 0.0
	for i in range(count):
		credit_all = credit_all + float(credit[i-1])
		grade_all = grade_all + float(grade[i-1])*float(credit[i-1])

	GPA = grade_all/credit_all
	var_b.set(round(GPA,3))
	print(round(GPA,3))

def add():
	global count
	credit_temp = round(float(var_t.get()),3)
	grade_temp = round(float(var_c.get()),3)
	print(count+1,end='  \t')
	print(credit_temp,end='\t\t')
	print(grade_temp)
	if credit_temp==0:
		msgbox.showinfo("info","请输入学分！")
		return
	if (grade_temp>=60 and grade_temp<=100):
		grade.append(grade_temp/10-5)
	elif (grade_temp>100 or grade_temp<0):
		msgbox.showinfo("info","输入错误！")
		root.mainloop()
	else:
		grade.append(0)
	credit.append(credit_temp)
	count += 1
	# print(count,end='  \t')
	# print(credit[count-1],end='\t\t')
	# print(grade[count-1])

def clean():
	global count
	global grade
	global credit
	count = 0
	grade = []
	credit = []
	print("clean")
	mainloop()


#上
frm_t = Frame(root)
Label(frm_t, text='学分', font=('Arial', 15)).pack()
var_t = StringVar()
var_t.set(0)
text_t = Entry(frm_t,textvariable=var_t).pack()
frm_t.pack(pady=20)

#中
frm_c = Frame(root)
Label(frm_c, text='分数', font=('Arial', 15)).pack()
var_c = StringVar()
var_c.set(0)
text_c = Entry(frm_c,textvariable=var_c).pack()
frm_c.pack()

#下
frm_b = Frame(root)
Label(frm_b, text='总绩点', font=('Arial', 15)).pack()
var_b = StringVar()
text_b = Entry(frm_b,textvariable=var_b).pack()
frm_b.pack(pady=20)

bt1 = Button(root, text="确认", command = add,activebackground='grey',width=15)
bt1.pack()

bt2 = Button(root, text="清零", command = clean,activebackground='grey',width=15)
bt2.pack(pady=10)

bt3 = Button(root, text="计算", command = calculate,activebackground='grey',width=15)
bt3.pack(fill=Y)

#开始主循环
root.mainloop()
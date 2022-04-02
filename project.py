from tkinter import * 
from tkinter.messagebox import * 
from datetime import * 
from tkinter.scrolledtext import *
import requests 
import bs4 
from sqlite3 import *
import matplotlib.pyplot as plt

mw = Tk()
mw.title("E.M.S")
mw.geometry("1000x600+300+50")
mw.configure(bg = 'cyan')

wa ="https://www.brainyquote.com/quote_of_the_day"
res = requests.get(wa)
data = bs4.BeautifulSoup(res.text , "html.parser")
info = data.find("img" , {"class" , "p-qotd"})
quote= info["alt"]

def f1():
	aw.deiconify()
	mw.withdraw()
def f2():
	mw.deiconify()
	aw.withdraw()
def f3():
	vw_data.delete( 1.0,END)
	mw.withdraw()
	vw.deiconify()
	info = ""
	con = None
	try:
		con = connect('pro.db')
		cursor = con.cursor()
		sql = "select * from emp"
		cursor.execute(sql)
		data = cursor.fetchall()
		for d in data:
			info = info + " ID = " + str(d[0]) + '\t' + " Name = " + str(d[1]) + '\t' + " Salary = " + str(d[2]) + '\t' + '\n\n'
		vw_data.insert(INSERT, info)
		con.commit()
	except Exception as e:
		showerror('Issue',e)
		con.rollback()
	finally:
		if con is not None:
			con.close()
def  f4():
	mw.deiconify()
	vw.withdraw()

def f5() :
	uw.deiconify()
	mw.withdraw()
def f6():
	mw.deiconify()
	uw.withdraw()
def f7() :
	dw.deiconify()
	mw.withdraw()
def f8():
	mw.deiconify()
	dw.withdraw()

def s1():
	con = None
	try:
		con = connect('pro.db')
		cursor = con.cursor()
		sql = "insert into emp values(?,?,?)"
		id = int(aw_entid.get())
		name = aw_entname.get()
		salary =int(aw_entsal.get())
		cursor.execute(sql ,(id ,name ,salary))
		if  id == "":
			showwarning('Fill ID','ID SHOULD NOT BE EMPTY ')
			con.rollback()
			aw_entid.delete(0,END)
			aw_entid.focus()
		elif id <= 0 or len(str(id)) > 4 : 
			showwarning('Wrong input','Enter positive numbers only and length of ID should not be more than 4 also it should not be empty')
			con.rollback()
			aw_entid.delete(0,END)
			aw_entid.focus()	 
			
		elif name == "" :
			showwarning('Wrong input','Name should not be empty')
			con.rollback()
			aw_entname.delete(0,END)
			aw_entname.focus()  
			
		elif len(name) < 2 or name.isalpha() == False:
			showwarning('Wrong input','Name should only have alphabets and the length of name should not be less than 2')
			con.rollback()
			aw_entname.delete(0,END)
			aw_entname.focus()
				
		elif  salary == ""  or salary < 8000 :
			showwarning('Wrong input','salary should be atleast 8000Rs')
			con.rollback()
			aw_entsal.delete(0,END)
			aw_entsal.focus()
				
		else:
			con.commit()
			showinfo('Success','Record Created')
			aw_entid.delete(0,END)
			aw_entname.delete(0,END)
			aw_entsal.delete(0,END)
			aw_entid.focus()
	
	except ValueError:
		d = "Enter Integer Values"
		showwarning('Failure',d)
		aw_entid.delete(0,END)
		aw_entsal.delete(0,END)
		con.rollback()

	except Exception as e:
		showerror('Issue','emp with same id already exists')
		con.rollback()
	finally:
		if con is not None:
			con.close()
def s2():
	con = None
	try:
		con = connect("pro.db")
		cursor = con.cursor()
		sql = "update emp set name = ?, salary= ? where id = ? "
		id = int(uw_entid.get())
		name = uw_entname.get()
		salary = int(uw_entsal.get())
		param =(name , salary , id)
		cursor.execute(sql,param) 
		if  id == "":
			showwarning('Wrong input','id. should only be integers and id. should not be empty')
			con.rollback()
			uw_entid.delete(0,END)
			uw_entid.focus()
		elif id <= 0 or len(str(id)) > 4 : 
			showwarning('Wrong input','Enter positive numbers only and length of id should not be more than 4')
			con.rollback()
			uw_entid.delete(0,END)
			uw_entid.focus()
		elif name == "" :
			showwarning('Wrong input','Name should not be empty')
			con.rollback()
			uw_entname.delete(0,END)
			uw_entname.focus()  
			
		elif len(name) < 2 or name.isalpha() == False:
			showwarning('Wrong input','Name should only have alphabets and the length of name should not be less than 2')
			con.rollback()
			uw_entname.delete(0,END)
			uw_entname.focus()
				
		elif  salary == "" or salary<8000 :
			showwarning('Wrong input','salary should not be less than 8000 and it should not be empty')
			con.rollback()
			uw_entsal.delete(0,END)
			uw_entsal.focus()
		else: 
			if cursor.rowcount > 0:		
				showinfo('Success',"Record Updated")
				con.commit()
				uw_entid.delete(0,END)
				uw_entname.delete(0,END)
				uw_entsal.delete(0,END)
				uw_entid.focus()
			else:
				showerror('issue',"Record Does Not Exist")
				uw_entid.delete(0,END)
				uw_entname.delete(0,END)
				uw_entsal.delete(0,END)
				uw_entid.focus()

	except ValueError:
		d = "Enter Integer Values"
		showwarning('Failure',d)
		uw_entid.delete(0,END)
		uw_entsal.delete(0,END)
		con.rollback()
		
	except Exception as e:
		showerror('Issue',e)
		con.rollback()
	finally:
		if con is not None:
			con.close()
				


def s3():
	con = None
	try:
		con = connect("pro.db")
		cursor = con.cursor()
		sql = "delete from  emp where id = ?"
		id = dw_entid.get()
		parameters = (id,)
		cursor.execute(sql,parameters)
		if id.isalpha() or id == "" :
			showwarning('Wrong input','id should only be integers and id should not be empty')
			con.rollback()
			dw_entid.delete(0,END)
			dw_entid.focus()
		
		elif id <= str(0) or len(str(id)) > 4 : 
			showwarning('Wrong input','Enter positive numbers only and length of id should not be more than 4')
			con.rollback()
			dw_entid.delete(0,END)
			dw_entid.focus()	 
		else:
			if cursor.rowcount > 0:		
				con.commit()
				showinfo('success','Record Deleted')
				dw_entid.focus()
			else:
				showerror('error','Record does not exist')					
				dw_entid.focus()
				dw_entid.delete(0,END)
	except Exception as e:
		showerror('Issue',e)
		con.rollback()
	finally:
		if con is not None:
			con.close()
def s4():
	con = None
	try:
		con = connect('pro.db')
		cursor = con.cursor()
		def graph():
			cursor.execute("SELECT name , salary FROM emp ORDER BY salary DESC LIMIT 5")
			data = cursor.fetchall()
			employee = []
			salary = []
			for d in data:
				employee.append(d[0])
				salary.append(d[1])
			plt.bar(employee,salary,color = ['orange','powderblue', 'green' , 'red' , 'black'],)
			plt.xlabel("employee")
			plt.ylabel("salary")
			plt.title('OUR HIGEST EARNERS')
			plt.show()
			con.commit()
		graph()
	except Exception as e:
		showerror('Issue',e)
		
	finally:
		if con is not None:
			con.close()

f = ("calibri" , 20 , "bold")
btn_add = Button( mw , text="Add" , font = f , command = f1  )
btn_add.pack(pady = 10)
btn_view = Button( mw , text="View" , font = f , command = f3 )
btn_view.pack(pady = 10)
btn_update = Button( mw , text="Update" , font = f , command = f5 )
btn_update.pack(pady = 10)
btn_delete = Button( mw , text="Delete" , font = f , command = f7  )
btn_delete.pack(pady = 10)
btn_charts = Button( mw , text="Charts" , font = f , command = s4 )
btn_charts.pack(pady = 10)
mw_lab = Label(mw , text ="QOTD : " , font = f )
mw_lab.pack(pady=10)

g = ("Algerian" , 15 )
mw_qotd = Label(mw , text = quote , font= g , borderwidth = 3 , justify = LEFT )
mw_qotd.pack(padx=10 ,pady=10)
# add window UI creation

aw = Toplevel(mw)
aw.title("Add Emp")
aw.geometry("700x600+300+50")
aw.configure(bg = 'cyan')
aw_id = Label(aw , text = "enter id: " , font = f )
aw_id.pack(pady = 5)
aw_entid = Entry(aw , font = f , bd = 6 )
aw_entid.pack(pady = 5)
aw_name = Label(aw , text = "enter name : " , font = f)
aw_name.pack(pady = 5)
aw_entname = Entry(aw , font = f , bd = 6)
aw_entname.pack(pady = 5)
aw_sal = Label(aw , text = "enter salary : " , font = f)
aw_sal.pack(pady = 5)
aw_entsal = Entry(aw , font = f , bd = 6 )
aw_entsal.pack(pady = 5)
aw_btn_save = Button(aw , text = "Save" , font = f , bd =5 , command = s1 )
aw_btn_back = Button(aw ,  text = "Back", font = f , bd = 5 , command = f2)
aw_btn_save.pack(pady = 5)
aw_btn_back.pack(pady = 5)
aw.withdraw()

#view window ui creation 

vw = Toplevel(mw)
vw.title("View Emp")
vw.geometry("700x600+300+50")
vw.configure(bg = 'cyan')

vw_data = ScrolledText(vw , width = 50 , height = 13 , font = f)
vw_data.pack(pady = 5)
vw_back = Button(vw , text = "Back" , font = f , command = f4)
vw_back.pack(pady = 5 )



# update window ui creation 

uw = Toplevel(mw)
uw.title("Update Emp")
uw.geometry("700x600+300+50")
uw.configure(bg = 'cyan')
uw_id = Label(uw , text = "enter id: " , font = f )
uw_id.pack(pady = 5)
uw_entid = Entry(uw , font = f , bd = 6 )
uw_entid.pack(pady = 5)
uw_name = Label(uw , text = "enter name : " , font = f)
uw_name.pack(pady = 5)
uw_entname = Entry(uw , font = f , bd = 6)
uw_entname.pack(pady = 5)
uw_sal = Label(uw , text = "enter salary : " , font = f)
uw_sal.pack(pady = 5)
uw_entsal = Entry(uw , font = f , bd = 6 )
uw_entsal.pack(pady = 5)
uw_btn_save = Button(uw , text = "Save" , font = f , bd =5 ,  command= s2 )
uw_btn_back = Button(uw ,  text = "Back", font = f , bd = 5 , command = f6)
uw_btn_save.pack(pady = 5)
uw_btn_back.pack(pady = 5)
uw.withdraw()

# delete window ui creation 

dw = Toplevel(mw)
dw.title("Delete Emp")
dw.geometry("700x600+300+50")
dw.configure(bg = 'cyan')
dw_id = Label(dw , text = "enter id " , font = f )
dw_id.pack(pady = 5)
dw_entid = Entry(dw , font = f , bd = 6 )
dw_entid.pack(pady = 5)
dw_btn_save = Button(dw , text = "Delete" , font = f , bd =5 , command=s3  )
dw_btn_back = Button(dw ,  text = "Back", font = f , bd = 5 , command = f8)
dw_btn_save.pack(pady = 5)
dw_btn_back.pack(pady = 5)
dw.withdraw()

mw.mainloop()

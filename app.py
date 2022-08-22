import mysql
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
import mysql.connector
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib import colors, fonts
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import numpy as np
import matplotlib.pyplot as plt
import pyautogui

window=Tk()

# window.resizable(False,False)
window.title("Result Checker")
window.geometry("600x800")
window.configure(background='white')

mystring = tk.StringVar(window)

def find():
    global entry
    global rolln
    global name
    global rollno
    global gender
    global s1,sn1,m1,g1
    global s2,sn2,m2,g2
    global s3,sn3,m3,g3
    global s4,sn4,m4,g4
    global s5,sn5,m5,g5
    global s6,sn6,m6,g6
    
    print(mystring.get())
    rolln = mystring.get()
    mysqldb = mysql.connector.connect(host="boqu686i3arvqfcd306c-mysql.services.clever-cloud.com", user="uj21uhyj8bu3xhp5", password="it9aUM7o8ohnY5FBtgEd", database="boqu686i3arvqfcd306c")
    mycursor = mysqldb.cursor()
    sql = 'SELECT * FROM result12 where Roll ='+rolln+';'
    mycursor.execute(sql)
    results = mycursor.fetchall()
    for result in results:
        print("Name: "+result[2])
        print(type(result[2]))
        name = result[2]
        print("Gender: "+result[1])
        gender = result[1]
        print("Roll no: "+str(result[0]))
        rollno = str(result[0])
        print("SUB CODE: "+str(result[3])+" Marks: "+ str(result[4])+" GRADE: "+result[5])
        s1 = result[3]
        m1 = result[4]
        g1 = result[5]
        print("SUB CODE: "+str(result[6])+" Marks: "+ str(result[7])+" GRADE: "+result[8])
        s2 = result[6]
        m2 = result[7]
        g2 = result[8]
        print("SUB CODE: "+str(result[9])+" Marks: "+ str(result[10])+" GRADE: "+result[11])
        s3 = result[9]
        m3 = result[10]
        g3 = result[11]
        print("SUB CODE: "+str(result[12])+" Marks: "+ str(result[13])+" GRADE: "+result[14])
        s4 = result[12]
        m4 = result[13]
        g4 = result[14]
        print("SUB CODE: "+str(result[15])+" Marks: "+ str(result[16])+" GRADE: "+result[17])
        s5 = result[15]
        m5 = result[16]
        g5 = result[17]
        print("SUB CODE: "+str(result[18])+" Marks: "+ str(result[19])+" GRADE: "+result[20])
        s6 = result[18]
        m6 = result[19]
        g6 = result[20]
        print("Result: " + result[21])
        res = result[21]
        sn1 = result[22]
        sn2 = result[23]
        sn3 = result[24]
        sn4 = result[25]
        sn5 = result[26]
        sn6 = result[27]
             
    Label(window, text="Name: "+name, justify=LEFT, bg='white').grid(row=5, columnspan=3)
    Label(window, text="Roll No: "+rollno, justify=LEFT, bg='white').grid(row=6, columnspan=3)
    Label(window, text="Gender: "+gender, justify=LEFT, bg='white').grid(row=7, columnspan=3)
    s = ttk.Style()
    s.theme_use('clam')
    s.configure('Treeview.Heading', background='#004540', foreground='white', font=('bold'))
    Tableframe = Frame(window).grid(row=8,columnspan=3)
    Table = ttk.Treeview(Tableframe)

    Table['columns'] = ('SUB CODE', 'SUBJECT','MARKS', 'GRADE')

    Table.column('#0', width=0, stretch=NO)
    Table.column('SUB CODE', anchor=CENTER, width=100)
    Table.column('SUBJECT', anchor=CENTER, width=180)
    Table.column('MARKS', anchor=CENTER, width=100)
    Table.column('GRADE', anchor=CENTER, width=100)

    Table.heading('#0',anchor=CENTER)
    Table.heading('SUB CODE', text='SUB CODE', anchor=CENTER)
    Table.heading('SUBJECT', text='SUBJECT', anchor=CENTER)
    Table.heading('MARKS', text='MARKS', anchor=CENTER)
    Table.heading('GRADE', text='GRADE', anchor=CENTER)

    Table.insert(parent='', index='end', iid=0, text='', values=(s1,sn1,m1,g1))
    Table.insert(parent='', index='end', iid=1, text='', values=(s2,sn2,m2,g2))
    Table.insert(parent='', index='end', iid=2, text='', values=(s3,sn3,m3,g3))
    Table.insert(parent='', index='end', iid=3, text='', values=(s4,sn4,m4,g4))
    Table.insert(parent='', index='end', iid=4, text='', values=(s5,sn5,m5,g5))
    Table.insert(parent='', index='end', iid=5, text='', values=(s6,sn6,m6,g6))
    Table.grid(row=8, columnspan=3)
    Label(window, text="Result: "+res, background='#004540', fg='#23ded1', padx=235, pady=10, font=('Helvetica 12 bold')).grid(row=9, columnspan=3)

    Button(window, text="Download", command=download).grid(row=10, column=0)
    Button(window, text="Show Marks in Graph", command=graph).grid(row=10, column=1)

def graph():
    data ={str(sn1):m1,str(sn2):m2,str(sn3):m3,str(sn4):m4,str(sn5):m5,str(sn6):m6}
    sub = list(data.keys())
    values = list(data.values())
    fig = plt.figure(figsize=(10,5))
    plt.bar(sub, values, color='maroon', width=0.4)
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.title("Graphical Representation of Marks")
    plt.show()        
    
def download():
    #PDF generation
    global pdf, flow_obj
    styles = getSampleStyleSheet()
    
    parastyle = ParagraphStyle('pstyle',
    fontName = 'Times-Roman',
    fontSize = 30,
    leading =30,
    alignment =1,
    spaceAfter = 20,
    borderPadding = (20,20,20)
                               )
    title = "Marksheet"
    pageinfo = "PYTHON MYSQL MARKSHEET GENERATOR"
    print("Downloading")
    messagebox.showinfo("File Downloaded", "Saved in same folder where this app is...")
    pdf = SimpleDocTemplate("Result.pdf")
    flow_obj = []
    td = [
        ["SUB CODE","SUBJECT", "MARKS", "GRADE"],
        [s1,sn1,m1,g1],
        [s2,sn2,m2,g2],
        [s3,sn3,m3,g3],
        [s4,sn4,m4,g4],
        [s5,sn5,m5,g5],
        [s6,sn6,m6,g6]
    ]
    para = Paragraph('''Marksheet''', parastyle)
    
    # para.drawOn(pdf, height=10, width=10)
    
    table = Table(td, colWidths=120, rowHeights=40)
    print(table)
    ts = TableStyle([("GRID",(0,0),(-1,-1),2, colors.black),
                     ("ALIGN", (0,0),(-1,-1),"CENTER"),
                     ("VALIGN", (0,0),(-1,-1),"MIDDLE")
                     ])
    table.setStyle(ts)
    flow_obj.append(para)
    flow_obj.append(table)
    pdf.build(flow_obj)

Label(window, text="Check Your Result!", font=('Times New Roman', 30, 'bold'), background='#004540', fg='white', padx=87, pady=20).grid(row=1, columnspan=3)
Label(window, text="Enter Your Roll no", background='#004540', fg='#23ded1', padx=43, font=('Helvetica 12 bold')).grid(row=2)
Label(window, text=" [13631236 - 13631441]", background='#004540', fg='#23ded1', padx=191, pady=10, font=('Helvetica 12 bold')).grid(row=3, columnspan=3)

entry = tk.Entry(window, textvariable = mystring, borderwidth=2, relief="solid", width=30).grid(row=2,column=1)

Button(window, text="🔍", command=find, borderwidth=2, relief="solid", padx=30).grid(row=2,column=2)

window.mainloop()
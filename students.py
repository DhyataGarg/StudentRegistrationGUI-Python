from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo
from tkinter.filedialog import *
from tkinter.scrolledtext import ScrolledText

root=Tk()
root.geometry('600x400')
root.title('STUDENT PERSONAL DETAILS')

##**************Functions start****************
def mysave():
    di={}
    d={}
    d['Name']=nameentry.get()
    d['Student ID']=rollnoentry.get()
    d['Gender']=gender.get()
    d['DOB']=(dateentry.get(),monthentry.get(),yearentry.get())
    d['Father\'s Name']=Fnameentry.get()
    d['Mother\'s Name']=Mnameentry.get()
    d['State']=statevar.get()
    d['H.no']=Hnoentry.get()
    d['Locality']=Localityentry.get()
    d['City']=cityentry.get()
    d['Mobile no.']=mobileentry.get()
    d['Batch']=batchvar.get()
    with open('Student.json','a') as f:
        f.write(str(d))
    nameentry.delete('0',END),rollnoentry.delete('0',END),dateentry.delete('0',END),monthentry.delete('0',END),yearentry.delete('0',END),Fnameentry.delete('0',END),Mnameentry.delete('0',END),Hnoentry.delete('0',END),Localityentry.delete('0',END),mobileentry.delete('0',END)
    messagebox.showinfo('showinfo','Your record has been saved')  
    return

def myopen():
    return 
##**************Functions end******************

## *************Frames start*******************
titleframe=Frame(root,width='600',height='50',bg='black')
titleframe.grid(row=0,column=0,sticky='nsew')

mainframe=Frame(root,width='600',height='300',bg='violet')
mainframe.grid(row=1,column=0,sticky='nsew')

for i in range(3):
    mainframe.columnconfigure(i,weight=1)
    
iframe1=Frame(mainframe,width='100',height='300',bg='green') 
iframe1.grid(row=0,column=0,sticky='nsew')

iframe2=Frame(mainframe,width='400',height='300',bg='violet') 
iframe2.grid(row=0,column=1,sticky='nsew')

iframe3=Frame(mainframe,width='40',height='300',bg='green') 
iframe3.grid(row=0,column=2,sticky='nsew')

for i in range(3):
    iframe1.columnconfigure(i,weight=1)
    
for i in range(3):
    iframe2.columnconfigure(i,weight=1)

lastframe=Frame(root,width='600',height='50',bg='black')
lastframe.grid(row=2,column=0)
##****************Frames end*********************

##****************Labels start*******************
mainlabel=Label(titleframe,text='STUDENT\'S RECORD',font=('Algerian',29),bg='black',fg='white').pack()
namelabel=Label(iframe2,text='Name:',font=('Times New Roman',12),bg='violet',fg='black').grid(row=0,column=0,sticky='w')
rollolabel=Label(iframe2,text='Student ID:',font=('Times New Roman',12),bg='violet',fg='black').grid(row=1,column=0,sticky='w')
genderlabel=Label(iframe2,text='Gender:',font=('Times New Roman',12),bg='violet',fg='black').grid(row=2,column=0,sticky='w')
doblabel=Label(iframe2,text='DOB:',font=('Times New Roman',12),bg='violet',fg='black').grid(row=3,column=0,sticky='w')
Fnamelabel=Label(iframe2,text='Father\'s Name:',font=('Times New Roman',12),bg='violet',fg='black').grid(row=4,column=0,sticky='w')
Mnamelabel=Label(iframe2,text='Mother\'s Name:',font=('Times New Roman',12),bg='violet',fg='black').grid(row=5,column=0,sticky='w')
Stateabel=Label(iframe2,text='State:',font=('Times New Roman',12),bg='violet',fg='black').grid(row=6,column=0,sticky='w')
Localitylabel=Label(iframe2,text='Locality:',font=('Times New Roman',12),bg='violet',fg='black').grid(row=8,column=0,sticky='w')
Hnolabel=Label(iframe2,text='H.no:',font=('Times New Roman',12),bg='violet',fg='black').grid(row=7,column=0,sticky='w')
citylabel=Label(iframe2,text='City:',font=('Times New Roman',12),bg='violet',fg='black').grid(row=9,column=0,sticky='w')
mobilelabel=Label(iframe2,text='Mobile no.:',font=('Times New Roman',12),bg='violet',fg='black').grid(row=10,column=0,sticky='w')
Batchlabel=Label(iframe2,text='Batch:',font=('Times New Roman',12),bg='violet',fg='black').grid(row=11,column=0,sticky='w')
##****************Labels end*********************

##***************Entry boxes start***************
nameentry=Entry(iframe2,width='47')
nameentry.grid(row=0,column=1,sticky='ew')
rollnoentry=Entry(iframe2,width='30')
rollnoentry.grid(row=1,column=1,sticky='ew')
dateentry=Entry(iframe2,width='10')
dateentry.grid(row=3,column=1,sticky='w')
monthentry=Entry(iframe2,width='10')
monthentry.grid(row=3,column=1)
yearentry=Entry(iframe2,width='10')
yearentry.grid(row=3,column=1,sticky='e')
Fnameentry=Entry(iframe2,width='30')
Fnameentry.grid(row=4,column=1,sticky='ew')
Mnameentry=Entry(iframe2,width='30')
Mnameentry.grid(row=5,column=1,sticky='ew')
Hnoentry=Entry(iframe2,width='30')
Hnoentry.grid(row=7,column=1,sticky='ew')
Localityentry=Entry(iframe2,width='30')
Localityentry.grid(row=8,column=1,sticky='ew')
cityentry=Entry(iframe2,width='30')
cityentry.grid(row=9,column=1,sticky='ew')
mobileentry=Entry(iframe2,width='30')
mobileentry.grid(row=10,column=1,sticky='ew')
##**************Entry boxes end******************

##****************Buttons start******************
savebutton=Button(iframe1,text='Save',command=mysave,width='5').grid(row=0,column=1,sticky='ns')
openbutton=Button(iframe1,text='Open',command=myopen,width='5').grid(row=1,column=1)
gender=StringVar()
gendermale=Radiobutton(iframe2,text='Male',value='Male',variable=gender).grid(row=2,column=1,sticky='w')
genderfemale=Radiobutton(iframe2,text='Female',value='Female',variable=gender).grid(row=2,column=1,sticky='e')
##****************Buttons end********************

##***************Combobox start***************
statevar=StringVar()
statevar.set('Select')
statemenu=ttk.Combobox(iframe2,width=27,textvariable =statevar)
statemenu['values']=('Andaman and Nicobar Islands','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chandigarh','Chhattisgarh','Dadra and Nagar Haveli and Daman and Diu','Delhi','Goa','Gujarat','Haryana','Himachal Pradesh','Jammu and Kashmir','Jharkhand','Karnataka','Kerela','Ladakh','Lakshadweep','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal')
statemenu.grid(row=6,column=1,sticky='ew')

batchvar=StringVar()
batchvar.set('Select')
batchmenu=ttk.Combobox(iframe2,width=27,textvariable=batchvar)
batchmenu['values']=('Batch 1','Batch 2','Batch 3')
batchmenu.grid(row=11,column=1,sticky='ew')
##***************Combobox end*****************
root.mainloop()
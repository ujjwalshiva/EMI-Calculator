import tkinter as t
from tkinter import BOTH
from tkinter.constants import *

# EMI Formula
# EMI = [P x R x (1+R)^M]/[(1+R)^(M-1)]

# Define Window
root=t.Tk()
root.title('EMI Calculator')
root.geometry('800x500')
root.config(bg='#009688')
root.resizable(0,0)
#root.iconbitmap(r"D:\UJJWAL\Python Files\Python Projects\Loan EMI App\cash.ico")

# Functions
def emicalc():
    p=int(loan.get())
    r=float(interest.get())/12/100
    m=int(months.get())
    emi=int(p*r*(((1+r)**m))/(((1+r)**(m))-1))
    print(emi)
    totalamount = emi*m
    emioutput = t.Label(root,text=f'EMI Amount: {emi}',font=('Open Sans',20, 'bold'),bg='#00796B', fg='white').grid(row=4, column=1,columnspan=2,sticky=W)
    finalamount = t.Label(root,text=f'Total Amount: {totalamount}',font=('Open Sans',20, 'bold'),bg='#00796B', fg='white').grid(row=5, column=1,columnspan=3,sticky=W)
    endingcomment.grid(pady='35px')
    


# Define Labels

heading=t.Label(root,text='EMI Calculator', font=('Raleway',20, 'bold'),bg='#00796B', fg='white',width=30)
heading.grid(ipadx='110px',columnspan=3,ipady='10px')

loanlabel=t.Label(root,text='Loan Amount: ',bg='#009688', fg='white',font=('Raleway',15, 'bold'))
loanlabel.grid(row=1,column=0,sticky=W,padx=('10px',0))

interestlabel=t.Label(root,text='Interest Rate: ',bg='#009688', fg='white',font=('Raleway',15, 'bold'))
interestlabel.grid(row=1,column=1,sticky=W,pady='10px')

monthlabel=t.Label(root,text='Months:  ',bg='#009688', fg='white',font=('Raleway',15, 'bold'))
monthlabel.grid(row=1,column=2,sticky=W,pady='10px')

endingcomment=t.Label(root,text="</> WITH ♡ BY UJJWAL ACHARYA",bg='#009688', fg='white',font=('PT Sans',12, 'bold'))
endingcomment.grid(row=7,column=1,pady='100px')

#Inputs

loan=t.Entry(root,width=15, bg='white',fg='#009688', border=0,font=('Open Sans',18, 'bold'))
loan.grid(row=2,column=0,sticky=W,pady='10px',padx='10px')

interest=t.Entry(root,width=15, bg='white',fg='#009688', border=0,font=('Open Sans',18, 'bold'))
interest.grid(row=2,column=1,sticky=W,pady='10px')

months=t.Entry(root,width=15, bg='white',fg='#009688', border=0,font=('Open Sans',18, 'bold'))
months.grid(row=2,column=2,sticky=W,pady='10px')

# Buttons
calculate=t.Button(root,text='Calculate',bg='#00BCD4',fg='white',activeforeground='#00BCD4', font=('Raleway',15, 'bold'),border=0,command=emicalc)
calculate.grid(row=3,column=1,sticky=W,pady='20px',ipadx='45px',ipady='10px')



#Define Window Loop
root.mainloop()

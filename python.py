from Tkinter import *
import Tkinter as tk
import tkMessageBox
import tkSimpleDialog
op='+'
j=0
class _converter: # it takes the string and calculates the length of the string ,stores the variables of the string in a list and we are assigning some values (0,1,2,3,4.....) to the variables in the string.  
        def __init__(self,x):
                self.name=x
                self.base=len(x)
                self.d={}
                self.q={}
                for i in range(len(x)):
                    self.d[i]=x[i]
                    self.q[x[i]]=i
        def _sum(self,n):#we are calculating the sum by the base of system 
                 sumi=0
                 for i in range(len(n)):
                         sumi=sumi+(self.base**(len(n)-1-i))*(self.q[n[i]])
                 return sumi
        def base_converter(self,n):#after the calculation of sum,we are converting into the another system .
            k="" 
            m=int(n)
            if m==0:
               k=str(self.d[0])
               l=k
            while m :
               k=k+self.d[m%self.base]
               m=m/self.base
            l=k[::-1]
            u=n-int(n)
            if(u>0):
                l=l+"."
                for j in range(4):
                     while(u<1 and u>0):
                          u=u*self.base
                          l=l+str(self.d[int(u)])
                     u=u-int(u)   
            return l
class calculator(_converter): # operations performed in calculator  
                    def __init__(self,a,b):
                        self.a=a
                        self.b=b
                    def add(self):
                        add=self.a+self.b
                        return add
                    def sub(self):
                        if self.a>self.b:
                            return self.a-self.b
                        else:
                            return self.b-self.a
                    def mul(self):
                        return self.a*self.b
                    def div(self):
                        return float(self.a)/self.b
def show():                     
        main.deiconify()
def end():
        main.destroy()
main=tk.Tk()
def calu(): # code for calculator
        t=0
        class cal:
                def action(self,argi):# links button to their entry
                        self.c.insert(END,argi)

                def clearall(self):# clear the entry widget
                                self.c.delete(0,END)

                def clear1(self):# clear the last entered value of entry widget
                        self.txt=self.c.get()[:-1]
                        self.c.delete(0,END)
                        self.c.insert(0,self.txt)

                        
                def __init__(self,master,t):# intialises elements in window
                        if t==1:
                                n=e.get()
                        else:
                                n=f.get()
                        self.c=Entry(master,width=23,bd=1,font=("Helvetica", 16), relief=RAISED, justify=RIGHT)
                        self.c.grid(column=0,row=0,columnspan=6)
                        self.c.focus_set()
                        self.fr1 = Frame(master,height=2,width=36)
                        self.fr1.grid(column=0,row=1)
                        
                        for i in range(len(n)):
                                newButton=Button(self.fr1,text=n[i],bg="white",width=6,height=2,command=lambda x=n[i]:self.action(x))
                                if i<5:
                                        newButton.grid(column=i,row=2,sticky=N+W)
                                if i>4 and i<10:
                                        newButton.grid(column=i-5,row=3,sticky=N+W)
                                if i>9 and i<15:
                                        newButton.grid(column=i-10,row=4,sticky=N+W)
                                if i>14 and i<20:
                                        newButton.grid(column=i-15,row=5,sticky=N+W)
                        
                        def operation():
                                        global op,j
                                        N1=_converter(e.get())
                                        N2=_converter(f.get())
                                        u=self.c.get()
                                        s1=u[:j-1]
                                        s2=u[j:]
                                        self.c.delete(0,END)
                                        if t==1:
                                                a=N1._sum(s1)
                                                b=N1._sum(s2)
                                                q=calculator(a,b)
                                                if op=='+':
                                                        self.c.insert(0,N1.base_converter(q.add())) 
                                                if op=='-':
                                                        self.c.insert(0,N1.base_converter(q.sub()))
                                                if op=='*':
                                                        self.c.insert(0,N1.base_converter(q.mul()))
                                                if op=='/':        
                                                        self.c.insert(0,N1.base_converter(q.div()))
                                        else:
                                                a=N2._sum(s1)
                                                b=N2._sum(s2)
                                                q=calculator(a,b)
                                                if op=='+':
                                                        self.c.insert(0,N2.base_converter(q.add()))
                                                if op=='-':
                                                        self.c.insert(0,N2.base_converter(q.sub()))
                                                if op=='*':
                                                        self.c.insert(0,N2.base_converter(q.mul()))
                                                if op=='/':        
                                                        self.c.insert(0,N2.base_converter(q.div()))

                        def add():
                                global op,j
                                self.action('+')
                                op='+'
                                s=self.c.get()
                                j=len(s)
                        def sub():
                                global op,j
                                self.action('-')
                                op='-'
                                s=self.c.get()
                                j=len(s)
                        def mul():
                                global op,j
                                self.action('*')
                                op='*'
                                s=self.c.get()
                                j=len(s)
                        def div():
                                global op,j
                                self.action('/')
                                op='/'
                                s=self.c.get()
                                j=len(s)
                                
                        buttonplus=Button(self.fr1,text='+',bd=2,bg="snow4",width=6,height=2,command=add)
                        buttonmin=Button(self.fr1,text='-',bd=2,bg="snow4",width=6,height=2,command=sub)
                        buttonmul=Button(self.fr1,text='*',bd=2,bg="snow4",width=6,height=2,command=mul)
                        buttondiv=Button(self.fr1,text='/',bd=2,bg="snow4",width=6,height=2,command=div)
                        buttonequ=Button(self.fr1,text='=',bg="orange2",fg="white",bd=2,width=6,height=2,command=operation)
                        buttonAC=Button(self.fr1,text='AC',bd=2,bg="firebrick4",fg="white",width=6,height=2,command=self.clearall)
                        buttonC=Button(self.fr1,text='C',bd=2,bg="firebrick4",width=6,fg="white",height=3,command=self.clear1)
                        buttonAC.grid(column=5,row=1)
                        buttonC.grid(column=5,row=2,rowspan=2,sticky=N)
                        buttonplus.grid(column=0,row=1,sticky=E)
                        buttonmin.grid(column=1,row=1,sticky=E)
                        buttonmul.grid(column=2,row=1,sticky=E)
                        buttondiv.grid(column=3,row=1,sticky=E)
                        buttonequ.grid(column=4,row=1,sticky=E)
                
        def cal1():#Calculator(N1) Window
                t=1
                cal1=Tk()
                cal1.title('Calulator(N1)')
                options=Menu(cal1)
                cal1.config(menu=options)
                subMenu=Menu(options)
                options.add_cascade(label='options',menu=subMenu)
                def calu2():
                        cal1.destroy()
                        cal2()
                subMenu.add_command(label='Calculator(N2)',command=calu2)
                def converter():
                        cal1.destroy()
                        conv()        
                subMenu.add_command(label='Converter',command=converter)
                def main():
                        cal1.destroy()
                        show()
                subMenu.add_command(label='Edit Number System',command=main)
                def end1():
                        cal1.destroy()
                        end()
                subMenu.add_command(label='Quit',command=end1)
                obj=cal(cal1,t)
                cal1.mainloop()
        def cal2():#Calculator(N2) Window
                t=2
                cal2=Tk()
                options=Menu(cal2)
                cal2.config(menu=options)
                subMenu=Menu(options)
                options.add_cascade(label='options',menu=subMenu)
                def calu1():
                        cal2.destroy()
                        cal1()
                subMenu.add_command(label='Calculator(N1)',command=calu1)
                def converter():
                        cal2.destroy()
                        conv()        
                subMenu.add_command(label='Converter',command=converter)
                def main():
                        cal2.destroy()
                        show()
                subMenu.add_command(label='Edit Number System',command=main)
                def end1():
                        cal2.destroy()
                        end()
                subMenu.add_command(label='Quit',command=end1)
                cal2.title('Calulator(N2)')
                obj=cal(cal2,t)
                cal2.mainloop()
        cal1()

def conv():# code for converter
        class con: 
                def action(self,argi): # links button to their entry
                        self.c.insert(END,argi)

                def clearall(self): # clear the entry widget
                                self.c.delete(0,END)
                                self.d.delete(0,END)

                def clear1(self):# clear the last entered value of entry widget
                        self.txt=self.c.get()[:-1]
                        self.c.delete(0,END)
                        self.c.insert(0,self.txt)
                
                def __init__(self,master,t):# intialises elements in window
                        def n_1():
                                root1=Tk()
                                root1.title("N1")
                                l=Label(root1,text="N1="+e.get(),font="18")
                                l.pack()
                                root1.mainloop()
                        def n_2():
                                root2=Tk()
                                root2.title("N2")
                                l=Label(root2,text="N2="+f.get(),font="18")
                                l.pack()
                                root2.mainloop()
                        self.l1=Button(master,text="-N1",bd=2,bg="grey79",width=6,command=n_1)
                        self.l2=Button(master,text="-N2",bd=2,bg="grey79",width=6,command=n_2)
                        if t==1:
                                n=e.get()
                                self.l1.grid(column=5,row=0)
                                self.l2.grid(column=5,row=1)
                        else:
                                n=f.get()
                                self.l2.grid(column=5,row=0)
                                self.l1.grid(column=5,row=1)
                        self.c=Entry(master,width=21,bd=1,font=("Helvetica", 16), relief=RAISED, justify=RIGHT)
                        self.c.grid(column=0,row=0,columnspan=5)
                        self.c.focus_set()
                        self.d=Entry(master,width=21,bd=1,font=("Helvetica", 16), relief=RAISED, justify=RIGHT)
                        self.d.grid(column=0,row=1,columnspan=5)
                        ##self.fr=Frame(master,width=34,height=9)
                        ##self.fr.grid(column=0,row=2)
                        if t==1:
                                def operation():# takes entry from N1 _converter system.Convert and display the entry to N2 _converter sysytem
                                        self.d.delete(0,END)
                                        N1=_converter(e.get())
                                        N2=_converter(f.get())
                                        s1=self.c.get()
                                        s1=N1._sum(s1)
                                        s1=N2.base_converter(s1)
                                        self.d.insert(0,s1)
                        else:
                                def operation():# takes entry from N1 _converter system. Convert and display the entry to N2 _converter sysytem
                                        self.d.delete(0,END)
                                        N1=_converter(e.get())
                                        N2=_converter(f.get())
                                        s1=self.c.get()
                                        s1=N2._sum(s1)
                                        s1=N1.base_converter(s1)
                                        self.d.insert(0,s1)
                        convert=Button(master,text='convert',font="Bold",bg="orange2",fg="white",width=8,height=1,command=operation)
                        convert.grid(row=5,column=1,columnspan=2,rowspan=1)
                        buttonAC=Button(master,text='AC',bg="firebrick4",fg="white",bd=2,width=6,height=2,command=self.clearall)
                        buttonC=Button(master,text='C',bd=2,width=6,bg="firebrick4",fg="white",height=2,command=self.clear1)
                        buttonAC.grid(column=5,row=2,sticky=N+E)
                        buttonC.grid(column=5,row=3,sticky=N+E)
                        for i in range(len(n)):
                                button=Button(master,text=n[i],bd=2,bg="white",width=6,height=2,command=lambda x=n[i]:self.action(x))
                                if i<5:
                                        button.grid(column=i,row=2,sticky=N+W)
                                if i>4 and i<10:
                                        button.grid(column=i-5,row=3,sticky=N+W)
                                if i>9 and i<15:
                                        button.grid(column=i-10,row=4,sticky=N+W)
                                if i>14 and i<20:
                                        button.grid(column=i-15,row=5,sticky=N+W)        

        def con1(): # intialise window of converter( N1-->N2)
                con1=Tk()
                con1.title('Converter(N1-->N2)')
                options=Menu(con1)
                con1.config(menu=options)
                subMenu=Menu(options)
                options.add_cascade(label='options',menu=subMenu)
                def conv2():
                        con1.destroy()
                        con2()
                subMenu.add_command(label='Converter(N2-->N1)',command=conv2)
                def calculator():
                        con1.destroy()
                        calu()        
                subMenu.add_command(label='Calculator',command=calculator)
                def main():
                        con1.destroy()
                        show()
                subMenu.add_command(label='Edit Number System',command=main)
                def end1():
                        con1.destroy()
                        end()
                subMenu.add_command(label='Quit',command=end1)
                t=1
                obj=con(con1,t)
                con1.mainloop()
        def con2(): # intialise window of converter(N2-->N1)
                con2=Tk()
                con2.title('Converter(N2-->N1)')
                options=Menu(con2)
                con2.config(menu=options)
                subMenu=Menu(options)
                options.add_cascade(label='options',menu=subMenu)
                def conv1():
                        con2.destroy()
                        con1()
                subMenu.add_command(label='Converter(N1-->N2)',command=conv1)
                def calculator():
                        con2.destroy()
                        calu()        
                subMenu.add_command(label='Calculator',command=calculator)
                def main():
                        con2.destroy()
                        show()
                subMenu.add_command(label='Edit Number System',command=main)
                def end1():
                        con2.destroy()
                        end()
                subMenu.add_command(label='Quit',command=end1)
                t=2
                obj=con(con2,t)
                con2.mainloop()        
        con1()

def scan():  #check if the entry of _converter system fulfill the conditions and if it does it add two button calculator and converter on pressing ok button
        q=0
        u=0
        r=0        
        n1=e.get()
        n2=f.get()
        p1=n1
        p2=n2
        for i in n1:
                if n1.count(i)>1:
                        q=1
        for i in n2:
                if n2.count(i)>1:
                        q=1
        if q==1:
                tkMessageBox.showinfo('Error!',"_converter systems can't have reapeting character.")

        if not n1 and not n2:
                u=1
                tkMessageBox.showinfo('Error!',"Both _converter systems can't be empty.")
        if len(n1)>20 or len(n2)>20:
                r=1
                tkMessageBox.showinfo('Error!',"Program can't handle _converter system with base more than 20.")
        if q==0 and u==0 and r==0:
                def calcu():
                        z=0
                        n1=e.get()
                        n2=f.get()
                        if p1!=n1 or p2!=n2:
                                z=1
                                tkMessageBox.showinfo('Alert!',"Your new input are not registered in program.Press ok to register")
                        if z==0:        
                                main.withdraw()
                                calu()
                def conve():
                        z=0
                        n1=e.get()
                        n2=f.get()
                        if p1!=n1 or p2!=n2:
                                z=1
                                tkMessageBox.showinfo('Alert!',"Your new inputs are not registered in program.Press ok to register")
                        if z==0:
                                main.withdraw()
                                conv()
                button1=Button(frame,text='Calculator',bd=2,bg="white",fg="black",width=34,height=2,command=calcu)
                button2=Button(frame,text='Convertor',bd=2,bg="white",fg="black",width=34,height=2,command=conve)
                button1.grid(column=0,row=4,columnspan=2,sticky=W,padx=2)
                button2.grid(column=2,row=4,columnspan=2,sticky=W,padx=2)

main.title('Please Enter')
frame=Frame(main)
frame.grid(row=0,column=0)
e=Entry(frame,width=18,bd=1,font=(22), relief=RAISED)
f=Entry(frame,width=18,bd=1,font=(22), relief=RAISED)
label1=Label(frame,text='Number System (N1)',font=(8))
label2=Label(frame,text='Number System (N2)',font=(8))      
button1=Button(frame,text='Ok',bd=2,bg="orange2",fg="white",width=10,command=scan)
pic=PhotoImage(file="sel.gif")
label_photo=Label(frame,image=pic)
label_photo.grid(row=0,column=0,columnspan=4)
label1.grid(column=0,row=1)
label2.grid(column=2,row=1)
e.grid(column=0,row=2)
f.grid(column=2,row=2)
button1.grid(column=3,row=2,sticky=E)
main.mainloop()



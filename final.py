# -*- coding: utf-8 -*-
from Tkinter import *
from tkMessageBox import *
import random
import goslate

wel=Tk()
wel.configure(bg='Blanched Almond')
wel.geometry("1000x350+0+0")
wel.title("Welcome")
Tops = Frame(wel,width=1600,bg='Blanched Almond',relief=SUNKEN)
Tops.pack(side=TOP)

fm1=Frame(wel,width=300,height=500,bd=5,bg='Light Steel Blue',relief=SUNKEN)
fm1.pack()

Label(Tops,font=('Comic Sans MS',30,'bold'),text='WELCOME TO LANGUAGE TRANSLATOR',fg='Royal Blue',relief=SUNKEN,bd=20,anchor='w').grid(row=0,column=0)

def exitmain():
    wel.destroy()

def info():
    showinfo("Welcome","Welcome to Translator user manual")
                
    root=Toplevel()
    root.configure(bg='Blanched Almond')
    
    root.title('Help')

    finfo=Frame(root,bd=5,bg='Light Steel Blue',relief=SUNKEN)
    finfo.pack(side=LEFT)

    Label(finfo,text="The project is an multilingual corpus with multiple languages such as English,Hindi,French and German etc. \n There are three simple steps involved:-- \n 1.Press Enter to start the translation procedure.  \n 2.Now enter the text through keyboard which you want to get translated. \n 3.Choose the desired output language by clicking on the repective buttons.",fg="Black",relief='ridge',font="times 20 bold").grid(row=1,column=0,padx=30)


Button(fm1,text='EXIT  ✘',font='times 20 bold',width=13,height=2,bd=10,bg='Indian Red',command=exitmain).grid(row=2,column=5)
Button(fm1,text='HOW TO USE \n (?)',font='times 20 bold',width=13,height=2,bd=10,bg='plum',command=info).grid(row=4,column=3)


def write():
    if a1.get()=='':
        showerror("Oops!,Say something....\n Empty Entry")
def enter():
    showinfo("Welcome","Make myself useful..")
    def exitroot2():
        
        root2.destroy()
    
    root2=Toplevel()
    root2.configure(bg='Beige')
    root2.geometry("800x800+0+0")
    root2.title('Enter')

    f1=Frame(root2,width=1600,height=800,bd=20,bg='Light Steel Blue',relief=SUNKEN)
    f1.pack(side=LEFT)

    Label(f1,text="Say Something...",font='arial 25',fg='Indian Red',bd=5,relief=SUNKEN).grid(row=0,column=0,columnspan=7)   
    a1=Entry(f1,width=16,bd=5,font='arial 20',bg='Ghost white')
    a1.grid(row=1,column=1,columnspan=10)


    Label(f1,text="Choose the one you want to change ",font='arial 25',fg='Indian Red',bd=5,relief=SUNKEN).grid(row=2,column=1,columnspan=7)
    
    Button(f1,text='Hindi \n हिंदी',font='times 20 bold',width=13,height=2,bd=10,bg='Thistle',command=hindi).grid(row=3,column=1)
    
    Button(f1,text='German \n Deutsche',font='times 20 bold',width=13,height=2,bd=10,bg='Thistle',command=german).grid(row=3,column=3)

    Button(f1,text='French \n français',font='times 20 bold',width=13,height=2,bd=10,bg='Thistle',command=french).grid(row=3,column=5)

    Button(f1,text='Spanish \n Español',font='times 20 bold',width=13,height=2,bd=10,bg='Thistle',command=spanish).grid(row=4,column=1)

    Button(f1,text='Urdu \n اردو',font='times 20 bold',width=13,height=2,bd=10,bg='Thistle',command=urdu).grid(row=4,column=3)

    Button(f1,text='Russian \n русский ',font='times 20 bold',width=13,height=2,bd=10,bg='Thistle',command=russian).grid(row=4,column=5)

    Button(f1,text='Arabic \n عربى ',font='times 20 bold',width=13,height=2,bd=10,bg='Thistle',command=arabic).grid(row=5,column=1)

    Button(f1,text='Japanese \n ジャポニス ',font='times 20 bold',width=13,height=2,bd=10,bg='Thistle',command=japanese).grid(row=5,column=3)

    Button(f1,text='Romanian \n Română ',font='times 20 bold',width=13,height=2,bd=10,bg='Thistle',command=romanian).grid(row=5,column=5)

    Button(f1,text='Dutch \n Nederlands ',font='times 20 bold',width=13,height=2,bd=10,bg='Thistle',command=dutch).grid(row=6,column=1)

    Button(f1,text='Bangla \n বাংলা',font='times 20 bold',width=13,height=2,bd=10,bg='Thistle',command=bangla).grid(row=6,column=3)

    Button(f1,text='Other',font='times 20 bold',width=13,height=2,bd=10,bg='Thistle',command=other).grid(row=6,column=5)

    Button(f1,text='Exit ✘',font='times 20 bold',width=13,height=2,bd=10,bg='Indian Red',command=exitroot2).grid(row=7,column=3)

def hindi():
    r2=Toplevel()
    r2.configure(bg='Beige')
    r2.geometry("400x400+0+0")
    r2.title('Hindi')
    Label(r2,text="Your selection is hindi",font='arial 25',fg='Black',bd=5,relief=SUNKEN).grid(row=0,column=0,columnspan=7)
    Label(r2,text="hello this is utkarsh\n means \n नमस्ते यह utkarsh है",font='arial 20',fg='Blue',bd=5,relief=SUNKEN).grid(row=3,column=2)
    gs = goslate.Goslate()
    
    
def german():
    r3=Toplevel()
    r3.configure(bg='Beige')
    r3.geometry("400x400+0+0")
    r3.title('German')
    Label(r3,text="Your selection is German",font='arial 25',fg='Black',bd=5,relief=SUNKEN).grid(row=0,column=0,columnspan=7)
    gs = goslate.Goslate()
    #display2 = gs.translate(a1,'de')
    #print display2
def french():
    r4=Toplevel()
    r4.configure(bg='Beige')
    r4.geometry("400x400+0+0")
    r4.title('French')
    Label(r4,text="Your selection is French",font='arial 25',fg='Black',bd=5,relief=SUNKEN).grid(row=0,column=0,columnspan=7)
    gs = goslate.Goslate()
    #display3 = gs.translate(a1,'fr')
    #print display3
def spanish():
    
    r5=Toplevel()
    r5.configure(bg='Beige')
    r5.geometry("400x400+0+0")
    r5.title('Spansih')
    Label(r5,text="Your selection is Spanish",font='arial 25',fg='Black',bd=5,relief=SUNKEN).grid(row=0,column=0,columnspan=7)
    gs = goslate.Goslate()
    #display4 = gs.translate(a1,'es')
    #print display4
def urdu():
    r6=Toplevel()
    r6.configure(bg='Beige')
    r6.geometry("400x400+0+0")
    r6.title('Urdu')
    Label(r6,text="Your selection is Urdu",font='arial 25',fg='Black',bd=5,relief=SUNKEN).grid(row=0,column=0,columnspan=7)
    gs = goslate.Goslate()
    #display5 = gs.translate(a1,'ur')
    #print display5
def russian():
    r7=Toplevel()
    r7.configure(bg='Beige')
    r7.geometry("400x400+0+0")
    r7.title('Russian')
    Label(r7,text="Your selection is Russian",font='arial 25',fg='Black',bd=5,relief=SUNKEN).grid(row=0,column=0,columnspan=7)
    gs = goslate.Goslate()
    #display6 = gs.translate(a1,'ru')
    #print display6
def arabic():
    r8=Toplevel()
    r8.configure(bg='Beige')
    r8.geometry("400x400+0+0")
    r8.title('Arabic')
    Label(r8,text="Your selection is Arabic",font='arial 25',fg='Black',bd=5,relief=SUNKEN).grid(row=0,column=0,columnspan=7)
    gs = goslate.Goslate()
    #display7 = gs.translate(a1,'ar')
    #print display7
def japanese():
    r9=Toplevel()
    r9.configure(bg='Beige')
    r9.geometry("400x400+0+0")
    r9.title('Japanese')
    Label(r9,text="Your selection is Japanses",font='arial 25',fg='Black',bd=5,relief=SUNKEN).grid(row=0,column=0,columnspan=7)
    gs = goslate.Goslate()
    #display8 = gs.translate(a1,'ja')
    #print display8
def romanian():
    r10=Toplevel()
    r10.configure(bg='Beige')
    r10.geometry("400x400+0+0")
    r10.title('Romanian')
    Label(r10,text="Your selection is Romanian",font='arial 25',fg='Black',bd=5,relief=SUNKEN).grid(row=0,column=0,columnspan=7)
    gs = goslate.Goslate()
    #display9 = gs.translate(a1,'ro')
    #print display9
def dutch():
    r11=Toplevel()
    r11.configure(bg='Beige')
    r11.geometry("400x400+0+0")
    r11.title('Dutch')
    Label(r11,text="Your selection is Dutch",font='arial 25',fg='Black',bd=5,relief=SUNKEN).grid(row=0,column=0,columnspan=7)
    gs = goslate.Goslate()
    #display10 = gs.translate(a1,'nl')
    #print display10
def bangla():
    r12=Toplevel()
    r12.configure(bg='Beige')
    r12.geometry("400x400+0+0")
    r12.title('Bangla')
    Label(r12,text="Your selection is Bangla",font='arial 25',fg='Black',bd=5,relief=SUNKEN).grid(row=0,column=0,columnspan=7)
    gs = goslate.Goslate()
    #display11 = gs.translate(a1,'bn')
    #print display11
def other():
    r13=Toplevel()
    r13.configure(bg='Beige')
    r13.geometry("800x200+0+0")
    r13.title('Other')
    Label(r13,text="-----------------****Other Languages****-----------------",font='arial 25',fg='Black',bd=5,relief=SUNKEN).grid(row=0,column=0,columnspan=7)
    gs = goslate.Goslate()
    #display12 = gs.translate(a1,'hi')
    #print display12
    
    Options=["Afar","Albanian","Aymara","Afgan" "Bambara","Bulgerian","Basque","Catalan", "Cornish","Cree","Denish","Dzongkha","Ewe","Persian","Irish","Fijian","Georgian","Fulah","Greek","Ido","Persian","Hebrew","Portuguese"]   ##ENter the names of all the cars.....Add names of the cars and adjust the size of the drop down
    var = StringVar()
    var.set("Other International Languages")
    DropDownMenu=apply(OptionMenu, (r13, var) + tuple(Options))
    DropDownMenu.grid(row=1,column=2)
    
    Options1=["Marathi","Sanskrit","Bihari","Gujrati","Sindhi","Tamil","Telugu","Odia" ,"Dongri","Nepali","Tripuri","Gondi","Kannada","Malayalam","Kashmiri","Bundeli"]   ##ENter the names of all the cars.....Add names of the cars and adjust the size of the drop down
    var1 = StringVar()
    var1.set("Indian Languages")
    DropDownMenu=apply(OptionMenu, (r13, var1) + tuple(Options1))
    DropDownMenu.grid(row=2,column=2,padx=10,pady=10)
Button(fm1,text='ENTER ⏎',font='times 20 bold',width=13,height=2,bd=10,bg='Thistle',command=enter).grid(row=2,column=2)

wel.mainloop()

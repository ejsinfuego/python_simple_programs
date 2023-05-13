from tkinter import*

root = Tk()
root.geometry('600x300')
root.resizable(0,0)
root.title('Ultra High RTX 100000 Powered Primordial Supreme Calculater')
root.config(bg='seashell3')

equate = StringVar()
value1 = StringVar()
value2 = StringVar()

def concat():
    number1 = value1.get()
    number2 = value2.get()
    result = number1 + number2
    equate.set(result)
    print(result)


Label(root, text = '+', font = 'arial 10').place(x= 230, y=100)
Label(root, text= 'The Best Calculator', font = 'calibri 15').place(x = 20, y = 50)
Label(root, text= 'Result =', font = 'calibri 13').place(x = 125, y = 167)

  
Label = Label(root, text= 'Im Programming!', font = 'calibri 15 bold').place(x = 20, y = 20)
enter_number = Entry(root, width = 10, textvariable = value1) .place (x = 160, y = 100)
enter_number = Entry(root, width = 10, textvariable = value2) .place (x = 250, y = 100)

Button(root, text = 'Calculate', font = 'arial 12 bold', bg = 'gray', padx = 1, command = concat).place(x = 195, y = 130)
equate = StringVar()

Entry(root, width = 15, text =equate, font = 'arial 10 bold', textvariable = equate).place(x=185, y = 170)    
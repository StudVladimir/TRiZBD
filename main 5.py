from Tkinter import *


def print_text():
    lab_text['text'] = var.get()


root = Tk()
root.title('5')
root.resizable(False, False)
root.columnconfigure(0, minsize=40)
root.columnconfigure(1, minsize=100)

lab_text = Label()

var = StringVar()

batton1 = Radiobutton(text='Vladimir',variable=var, value='+7 9999999999', indicatoron=0, command=print_text)
batton2 = Radiobutton(text='Danya',variable=var, value='+7 8888888888', indicatoron=0, command=print_text)
batton3 = Radiobutton(text='Timoxa',variable=var, value='+6 7777777777', indicatoron=0, command=print_text)

lab_text.grid(column=1, row=0, rowspan=2, sticky='ew')
batton1.grid(column=0, row=0, sticky='ew')
batton2.grid(column=0, row=1, sticky='ew')
batton3.grid(column=0, row=2, sticky='ew')

root.mainloop()
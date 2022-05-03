from Tkinter import *

root = Tk()
b1 = Button(text="red")
b2 = Button(text="orange")
b3 = Button(text="yellow")
b4 = Button(text="green")
b5 = Button(text="blue")
b6 = Button(text='dark blue')
b7 = Button(text="magenta")

def change():
    b1['text'] = 'ff0000'
    b1['bg'] = '#ff0000'
    b1['fg'] = '#ffffff'
    b1['activebackground'] = '#000000'
    b1['activeforeground'] = '#ffffff'
b1['command'] = change
b1.pack(side=BOTTOM)
#-----------------------------

def change():
    b2['text'] = 'ff7d00'
    b2['bg'] = '#ff7d00'
    b2['fg'] = '#ffffff'
    b2['activebackground'] = '#000000'
    b2['activeforeground'] = '#ffffff'
b2['command'] = change
b2.pack(side=BOTTOM)
#-----------------------------

def change():
    b3['text'] = 'ffff00'
    b3['bg'] = '#ffff00'
    b3['fg'] = '#ffffff'
    b3['activebackground'] = '#000000'
    b3['activeforeground'] = '#ffffff'
b3['command'] = change
b3.pack(side=BOTTOM)
#-----------------------------

def change():
    b4['text'] = '00ff00'
    b4['bg'] = '#00ff00'
    b4['fg'] = '#ffffff'
    b4['activebackground'] = '#000000'
    b4['activeforeground'] = '#ffffff'
b4['command'] = change
b4.pack(side=BOTTOM)
#-----------------------------

def change():
    b5['text'] = '007dff'
    b5['bg'] = '#007dff'
    b5['fg'] = '#ffffff'
    b5['activebackground'] = '#000000'
    b5['activeforeground'] = '#ffffff'
b5['command'] = change
b5.pack(side=BOTTOM)
#-----------------------------

def change():
    b6['text'] = '0000ff'
    b6['bg'] = '#0000ff'
    b6['fg'] = '#ffffff'
    b6['activebackground'] = '#000000'
    b6['activeforeground'] = '#ffffff'
b6['command'] = change
b6.pack(side=BOTTOM)
#-----------------------------

def change():
    b7['text'] = '7d00ff'
    b7['bg'] = '#7d00ff'
    b7['fg'] = '#ffffff'
    b7['activebackground'] = '#000000'
    b7['activeforeground'] = '#ffffff'
b7['command'] = change
b7.pack(side=BOTTOM)
root.mainloop()
from tkinter import *

root = Tk()

root['bg'] = '#fafafa'
root.title('Two Note')
root.wm_attributes('-alpha', 0.8)
root.geometry('400x500')

btn_01 = Button(text='btn_01', bg='#fafafa', )
btn_01.pack()

frame_top = Frame(root, bg='#ffb700', bd=5)
# Также указываем его расположение
frame_top.place(relx=0.05, rely=0.05, relwidth=0.8, relheight=0.8)

root.mainloop()
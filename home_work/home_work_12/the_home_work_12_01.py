from tkinter import *
from tkinter.filedialog import *
import json


sett_open = dict()
sett_save = dict()


def open_file():
    file_note = askopenfilename(filetypes=[('TEXT Files', '*.txt')],
                                title='Открой текстовый файл дружочек')
    # text_area.insert(END, file_note)
    if file_note:
        text_area.delete(1.0, END)
        sett_open[file_note.split('/')[-1]] = file_note
        root.title(file_note.split('/')[-1][:-4] + ' - NotePad')

        with open(file_note, 'r', encoding='utf-8') as f:
            text_area.insert(END, f.read())

        with open('settings.json', 'w', encoding='utf-8') as f:
            json.dump(sett_open, f, ensure_ascii=False)


def save_file():
    file_name = asksaveasfilename(initialfile='Untitled.txt',
                                  defaultextension='.txt',
                                  filetypes=[('TEXT Files', '*.txt')])
    if file_name:
        file = open(file_name, 'w')
        file.write(text_area.get(1.0, END))
        file.close()
        root.title(file_name.split('/')[-1][:-4] + ' - NotePad')
        sett_save[file_name.split('/')[-1]] = file_name

        with open('settings.json', 'w', encoding='utf-8') as f:
            json.dump(sett_save, f, ensure_ascii=False)


root = Tk()

# Название программы
root.title('NotePad')

# Задаем размеры и расположение по дефолту
root.geometry('500x600+100+100')

# Прикручиваем иконку
icon = PhotoImage(file='notes.png')
root.iconphoto(False, icon)

# Минимальные и максимальные размеры окна
root.minsize(300, 400)
root.maxsize(700, 800)
root.resizable(True, True)

text_area = Text(root)
text_area.grid(row=0, column=0, columnspan=2, stick='wens')

but_open = Button(text='Открыть', command=open_file)
but_open.grid(row=1, column=0, stick='w')

but_save = Button(text='Сохранить', command=save_file)
but_save.grid(row=1, column=1, stick='e')

root.grid_rowconfigure(0,  weight=1)
root.grid_columnconfigure(0, weight=1)

new_open = open('settings.json', 'r', encoding='utf-8')
last_file = new_open.read().split()[-1].split('}')[0].split('"')[1]

with open(last_file, 'r', encoding='utf-8') as f:
    text_area.insert(END, f.read())
    root.title(last_file.split('/')[-1][:-4] + ' - NotePad')


root.mainloop()
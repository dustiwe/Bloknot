from tkinter import *
from tkinter import filedialog
import time
import threading

window = Tk()
window.title('Блокнот')
window.geometry('660x420+700+200')

themes = {
    'dark':{'text_bg':'#483D8B','text_fg':'#FFFFFF','inesrt':'#8A2BE2','select':'#000000'},
    'light':{'text_bg':'#F4A460','text_fg':'#696969','inesrt':'#00BFFF','select':'#696969'}
}

def change_theme(theme):
    text['bg'] = themes[theme]['text_bg']
    text['fg'] = themes[theme]['text_fg']
    text['insertbackground'] = themes[theme]['inesrt']
    text['selectbackground'] = themes[theme]['select']

frame_text = Frame(window)
frame_text.pack(fill=BOTH,expand=1)

text = Text(frame_text,bg='#F4A460',fg='#696969',padx=10,pady=10,wrap=WORD,insertbackground='#00BFFF',selectbackground='#696969',font=13,width=30)
text.pack(fill=BOTH,expand=1,side=LEFT)

scrollbar = Scrollbar(frame_text,command=text.yview)
scrollbar.pack(fill=Y,side=LEFT)

text.config(yscrollcommand=scrollbar.set)

menushka = Menu(window)
window.config(menu=menushka)

def open_file():
    file_path = filedialog.askopenfilename(title='Выбор файла',filetypes=(('Текстовые документы (*.txt)','*.txt'),('Все файлы','*.*')))
    if file_path:
        file = open(file_path,encoding='utf=8')
        text.delete('1.0',END)
        text.insert('1.0',file.read())
        file.close()

def save_file():
    file_path = filedialog.askopenfilename(filetypes = (("Text File", "*.txt"),))
    file = open(file_path, 'w',encoding='utf-8')
    file_text = text.get('1.0',END)
    file.write(file_text)
    file.close()

def open_dialog():
    window2 = Toplevel(window)
    window2.geometry('260x100+800+300')
    window2.resizable(False, False)

    def search_in():
        vvod = pole.get()
        text.tag_remove('found', '1.0', END)
        idx = '1.0'
        idx = text.search(vvod,idx, nocase=1,stopindex=END)
        lastidx = '%s+%dc' % (idx, len(vvod))
        text.tag_add('found', idx, lastidx)
        idx = lastidx
        text.tag_config('found', background='red')

        def return_default(name):
            time.sleep(4)
            text.tag_config('found', background='#F4A460', selectbackground='#696969')

        x = threading.Thread(target=return_default, args=(1,))
        x.start()

    button_search = Button(window2,text='Найти',command=search_in)
    button_search.pack(side=LEFT)
    pole = Entry(window2,width=25)
    pole.place(x=130,y=50,anchor=CENTER)


    window2.grab_set()
    window2.focus_set()


file_menu = Menu(menushka,tearoff=0)
menushka.add_cascade(label='Файл',menu=file_menu)
file_menu.add_command(label='Поиск',command=open_dialog)
file_menu.add_command(label='Открыть',command=open_file)
file_menu.add_command(label='Сохранить',command=save_file)

theme_menu = Menu(menushka,tearoff=0)
menushka.add_cascade(label='Оформление',menu=theme_menu)
theme_menu.add_command(label='Темная тема',command=lambda:change_theme('dark'))
theme_menu.add_command(label='Светлая тема',command=lambda:change_theme('light'))
theme_menu.add_command(label='Изменить шрифт',command=lambda:change_theme('light'))

window.mainloop()
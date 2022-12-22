import random
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from math import pi


def calculate():
    gradus = int(weight_tf.get())
    faring = gradus * 9 / 5 + 32
    if faring >= 0:
        messagebox.showinfo('c-pythonguides', f'Градусы по Фарингейту = {faring} ')
    else:
        messagebox.showinfo('c-pythonguides', f'Градусы по Фарингейту = {faring} ')


window = Tk()
window.title('Конвертация градусов')
window.geometry('300x100')

frame = Frame(
    window,
    padx=10,
    pady=10,
)
frame.pack(expand=True)

weight_lb = Label(
    frame,
    text="Введите градусы Цельсия : ",
)
weight_lb.grid(row=4, column=1)

weight_tf = Entry(
    frame,
    bg='gray'
)
weight_tf.grid(row=4, column=2, pady=5)

cal_btn = Button(
    frame,
    text='Рассчитать',
    command=calculate,
)
cal_btn.grid(row=5, column=2)
window.mainloop()

window = tkinter.Tk()
window.title('Тест на знание англ. яз.')
window.geometry('300x140')


def click_try():
    global k
    var = Entry_slov.get()
    if label_2.cget("text") != "":
        if var.isalpha():
            if k != 0:
                if var == dictionary[rus]:
                    label_otv.config(text="Верно!")
                    k = 5
                else:
                    label_otv.config(text="Ответ неправильный! Попыток:" + str(k))
                    k -= 1
            else:
                label_otv.config(text="Попыток закончились :( ")
                click_rand()
                k = 3
        else:
            label_otv.config(text="Введите заново!")
    else:
        label_otv.config(text="Нажмите <Новое слово>!")


def click_rand():
    global rus, eng
    rus, eng = random.choice(list(dictionary.items()))
    label_2.config(text=rus)


dictionary = {
    'рука': 'hand',
    'нога': 'leg',
    'хвост': 'tail',
    'питон': 'python',
}

k = 3
rus = ""
eng = ""

label_2 = Label(
    width=20,
    borderwidth=2,
    relief="solid")
label_2.grid(row=1, column=2)

label_slovo = Label(
    text=' Cлово :'
)
label_slovo.grid(row=1, column=1)

label_perevod = Label(
    text=' Ведите перевод :'
)
label_perevod.grid(row=2, column=1)

Entry_slov = Entry(
    bg='gray'
)
Entry_slov.grid(row=2, column=2)

label_otv = Label()
label_otv.grid(row=4, column=2)

button = Button(
    text='Проверка',
    command=click_try,
)
button.grid(row=3, column=2)

button_1 = Button(
    text="Генератор ",
    command=lambda: click_rand())
button_1.grid(row=3, column=1)

ex = Button(
    text='Выход',
    command=window.destroy
)
ex.grid(row=5, column=2)

window.mainloop()

html_template1 = """<html>
<head>
<title>Title</title>
</head>
<body>
<h2>Текст в формате html</h2>
<p>
"""
html_template2 = """.</p>
</body>
</html>
"""


def calculate():
    if entry1.get().isdigit():
        inp = float(entry1.get())
        try:
            res = (4 * pi * inp ** 3) / 3
            label3.config(text=res)
        except:
            label3.config(text="Ошибка, некорректный ввод!")
    else:
        label3.config(text="Повторите ввод!")


def saveastxt():
    try:
        path = filedialog.asksaveasfile(filetypes=(("Text files", "*.txt"), ("All files", "*.*"))).name
        window.title('Калькулятор - ' + path + ".txt")
    except:
        return
    with open(path + ".txt", 'w') as f:
        f.write("Результат вычислений = " + str(label3.cget("text")))
        f.close()


def saveashtml():
    try:
        path = filedialog.asksaveasfile(filetypes=(("Html file", "*.html"), ("All files", "*.*"))).name
        window.title('Калькулятор - ' + path + ".html")
    except:
        return
    with open(path + ".html", 'w') as f:
        f.write(html_template1)
        f.write("Результат вычислений = " + str(label3.cget("text")))
        f.write(html_template2)
        f.close()


window = tkinter.Tk()
window.geometry("325x250")
window.title('')

label0 = tkinter.Label(window, text='Программа для вычисления обьема сферы', font=('Coutier', 10, 'bold'))
label0.place(x=10, y=7)

label1 = tkinter.Label(window, text='Введите радиус:', font=('Coutier', 9))
label1.place(x=10, y=45)

entry1 = tkinter.Entry(window, bg='gray')
entry1.place(x=118, y=45, width=100, height=30)

label2 = tkinter.Label(window, text='Результат вычислений:', font=('Coutier', 9))
label2.place(x=10, y=90)

label3 = tkinter.Label(window, bg='gray')
label3.place(x=150, y=90, width=130, height=30)

button1 = tkinter.Button(window, text='Вычислить', bg='gray', command=calculate)
button1.place(x=100, y=130, width=130, height=30)

button2 = tkinter.Button(window, text='Сохранить в .txt', bg='gray', command=saveastxt)
button2.place(x=25, y=170, width=120, height=30)

button3 = tkinter.Button(window, text='Сохранить в .html', bg='gray', command=saveashtml)
button3.place(x=175, y=170, width=120, height=30)

window.mainloop()

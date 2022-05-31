import tkinter as tk
from tkinter import PhotoImage

class SampleAPP(tk.Tk):
    def __init__(self, *arg, **kwargs):
        tk.Tk.__init__(self, *arg, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MenuPage, StartPage, LoginPage, RePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

            self.show_frame("MenuPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #self.controller = controller
        #self.controller.title("")
        #self.backGroundImage = PhotoImage(file=r"yui.png")
        #self.backGroundImageLabel = Label(self, image=self.backGroundImage)
        #self.backGroundImageLabel.place(x=-50, y=0)

        def show_frame(self, page_name):
            frame = self.frames[page_name]
            frame.tkraise()

        def register_user():
            username_info = username_entry.get()
            password_info = password_entry.get()

            file = open(username_info + ".txt", "w")
            file.write(username_info + "\n")
            file.write(password_info)
            file.close()

            username_entry.delete(0, "end")
            password_entry.delete(0, "end")
            tk.Label(self,
                     text="Вы зарегистрированы",
                     fg="green",
                     font=("Arial", 11)).pack()

        def return_page():
            controller.show_frame('RePage')

        tk.Label(self,
                 text="Введите свои данные",
                 bg="white",
                 height="2",
                 font=("Arial", 20)).pack()

        tk.Label(self, text="Имя (клиента) * ").pack()
        username_entry = tk.Entry(self)
        username_entry.pack()
        tk.Label(self, text="Ваш email * ").pack()
        password_entry = tk.Entry(self)
        password_entry.pack()

        tk.Button(self,
                  text="Зарегистрироваться",
                  width=20,
                  height=1,
                  command=return_page).pack()

        tk.Button(self, text="Выход", width=20, height=1,
                  command=return_page).pack()


class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #self.controller = controller
        #self.backGroundImage = PhotoImage(file=r"cccc.png")
        #self.backGroundImageLabel = Label(self, image=self.backGroundImage)
        #self.backGroundImageLabel.place(x=-50, y=0)

        def return_page():
            controller.show_frame('StartPage')

        tk.Label(self,
                 text="Введите ваш логин",
                 bg="white",
                 height="2",
                 font=("Arial", 20)).pack()
        tk.Label(self, text="").pack()
        tk.Label(self, text="Имя", bg="white").pack()
        username_entry = tk.Entry(self)
        username_entry.pack()
        tk.Button(self, text="Войти", width=20, height=1,
                  command=return_page).pack()
        tk.Button(self, text="Выход", width=20, height=1,
                  command=return_page).pack()


class RePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #self.controller = controller
        #self.backGroundImage = PhotoImage(file=r"ooo.png")
        #self.backGroundImageLabel = Label(self, image=self.backGroundImage)
        #self.backGroundImageLabel.place(x=-50, y=0)

        def return_page():
            controller.show_frame('StartPage')

        tk.Button(self,

                  text="Главная",
                  width=20,
                  height=1,
                  command=return_page).pack()
        tk.Button(self, text="Услуги", width=20, height=1,
                  command=return_page).pack()
        tk.Button(self,
                  text="Техобслужвание",
                  width=20,
                  height=1,
                  command=return_page).pack()
        tk.Button(self,
                  text="Вызвать мастера",
                  width=20,
                  height=1,
                  command=return_page).pack()
        tk.Button(self,
                  text="Доставка",
                  width=20,
                  height=1,
                  command=return_page).pack()
        tk.Button(self,
                  text="Личный кабинет",
                  width=20,
                  height=1,
                  command=return_page).pack()
        tk.Button(self, text="О нас", width=20, height=1,
                  command=return_page).pack()


class MenuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        #self.backGroundImage = PhotoImage(file=r"ttt.png")
        #self.backGroundImageLabel = Label(self, image=self.backGroundImage)
        #self.backGroundImageLabel.place(x=140, y=70)

        def return_page():
            controller.show_frame('StartPage')

        def return_login():
            controller.show_frame('LoginPage')

        label5 = tk.Label(self,
                          text="Добро пожаловать!",
                          width="300",
                          height="2",
                          font=("Arial", 20)).pack(pady=30)

        tk.Button(self,
                  text="Логин",
                  height="2",
                  width="30",
                  command=return_login).pack(pady=30)

        tk.Button(self,
                  text="Регистрация",
                  height="2",
                  width="30",
                  command=return_page).pack(pady=30)

    # функция Регистрацмя


if __name__ == "__main__":
    app = SampleAPP()
    app.geometry('800x600')
    app.mainloop()
from tkinter import *
import pyscreenshot
from tkinter import colorchooser


class Paintk:

    def __init__(self):

        self.window = Tk()
        self.window.title("Paintk")
        self.window.minsize(width=1280, height=720)
        self.window.resizable(0, 0)
        self.window.config(bg="#3b3b3b")

        self.img_line = PhotoImage(file="icons/line.png")
        self.img_oval = PhotoImage(file="icons/oval.png")
        self.img_eraser = PhotoImage(file="icons/eraser.png")
        self.img_save = PhotoImage(file="icons/save.png")
        self.img_clean = PhotoImage(file="icons/new.png")
        self.img_square = PhotoImage(file="icons/square.png")

        self.brush_line = False
        self.select_color = "black"
        self.list_colors = ("white", "gray", "black", "red", "blue", "orange", "green", "purple")

        self.bar_color = Frame(self.window, bg="#3b3b3b", padx=10, pady=10)
        self.bar_color.pack(fill="x")

        self.label_colors = Label(self.bar_color, text=" Colors:  ", fg="white", bg="#3b3b3b")
        self.label_colors.pack(side="left")

        for i in self.list_colors:
            colors = Button(self.bar_color, bg=i, width=2, height=2, bd=0, relief="flat",
                            command=lambda num=i: self.colors(num)).pack(side="left")

        self.label_colors_choose = Label(self.bar_color, text="  Color Choose:  ", fg="white", bg="#3b3b3b")
        self.label_colors_choose.pack(side="left")

        self.color_choose = Button(self.bar_color, image=self.img_square, bd=0,
                                   command=self.selected_color)
        self.color_choose.pack(side="left")

        self.label_size = Label(self.bar_color, text=" Size:  ", fg="white", bg="#3b3b3b")
        self.label_size.pack(side="left")

        self.pen_size = Spinbox(self.bar_color, from_=1, to=50)
        self.pen_size.pack(side="left")

        self.label_brushs = Label(self.bar_color, text=" Brushs:  ", fg="white", bg="#3b3b3b")
        self.label_brushs.pack(side="left")

        self.line = Button(self.bar_color, image=self.img_line, bd=0,
                           command=self.Brush_line).pack(side="left")

        self.elipse = Button(self.bar_color, image=self.img_oval, bd=0,
                             command=self.Brush_oval).pack(side="left")

        self.eraser = Button(self.bar_color, image=self.img_eraser, bd=0,
                             command=self.Erase).pack(side="left")

        self.label_options = Label(self.bar_color, text=" Options:  ", fg="white",
                                   bg="#3b3b3b")
        self.label_options.pack(side="left")

        self.save_button = Button(self.bar_color, image=self.img_save, bd=0,
                                  command=self.save).pack(side="left")

        self.clean_button = Button(self.bar_color, image=self.img_clean, bd=0,
                                   command=self.clean).pack(side="left")

        self.area_draw = Canvas(self.window, height=720)
        self.area_draw.pack(fill="x")
        self.area_draw.bind("<B1-Motion>", self.draw)

        self.window.bind("<F1>", self.clean)
        self.window.bind("<F2>", self.save)

        self.window, mainloop()

    def Brush_line(self):
        self.brush_line = True

    def Brush_oval(self):
        self.brush_line = False

    def colors(self, color):
        self.select_color = color

    def Erase(self):
        self.select_color = "gainsboro"

    def draw(self, event):
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 10), (event.y + 10)

        if self.brush_line:
            self.area_draw.create_line(x1, y1, x2, y2, width=self.pen_size.get(), fill=self.select_color)
        else:
            self.area_draw.create_oval(x1, y1, x2, y2, width=self.pen_size.get(), fill=self.select_color,
                                       outline=self.select_color)

    def save(self, event):
        x = self.window.winfo_rootx() + self.area_draw.winfo_x()
        y = self.window.winfo_rooty() + self.area_draw.winfo_y()
        x1 = self.window.winfo_rootx() + self.area_draw.winfo_width()
        y1 = self.window.winfo_rooty() + self.area_draw.winfo_height()

        img = pyscreenshot.grab(bbox=(x, y, x1, y1))
        img.save("img.png", "png")

    def clean(self, event):
        self.area_draw.delete("all")

    def selected_color(self):
        color = colorchooser.askcolor()
        self.select_color = color[1]


Paintk()

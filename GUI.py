#   https://www.tutorialspoint.com/python/python_gui_programming.htm

#---------------------------------------- GUI Window ----------------------------------------------

# from tkinter import *

# window = Tk()
# window.geometry("500x500")  # Chiều dài x Chiều rộng 
# window.title("FORM APU")    # Sửa tiêu đề

# icon = PhotoImage(file="Emotes-face-laugh-icon.png")    
# window.iconphoto(True,icon)              # Thay doi icon cua Frame
# # window.config(background="black")         # Chinh background  
# window.config(background="#5cfcff")       # Co the dung ma hex
# window.mainloop()           # dùng để hiện Frame lên màn hình và lắng nghe sự kiện 

#--------------------------------------- Các Widget của Tkinter trong Python --------------------------
"""
       1	Button	       Button được sử dụng để thêm nhiều nút khác nhau vào ứng dụng python.
       
       2	Canvas	       Canvas được sử dụng để vẽ các hình trên cửa sổ.
       
       3	Checkbutton	Checkbutton được sử dụng để hiển thị CheckButton trên cửa sổ.
       
       4	Entry	       Entry được sử dụng để hiển thị trường văn bản một dòng cho người dùng. Nó thường được sử dụng để 
                            nhập các giá trị của người dùng.
       
       5	Frame	       Frame có thể được định nghĩa là một vùng chứa mà có thể chứa một hoặc nhiều widget khác.
       
       6	Label	       Label là một văn bản được sử dụng để hiển thị một số thông báo hoặc thông tin cho các widget khác.
       
       7	ListBox	ListBox được sử dụng để hiển thị danh sách các tùy chọn cho người dùng.
       
       8	Menubutton	Menubutton được sử dụng để hiển thị các mục menu cho người dùng.
       
       9	Menu	       Menu được sử dụng để thêm các mục menu cho người dùng.
       
       10	Message	Message được sử dụng để hiển thị hộp tin nhắn cho người dùng.
       
       11	Radiobutton	Người dùng được cung cấp các tùy chọn khác nhau và người dùng chỉ có thể chọn một tùy chọn trong 
                            số đó.
       
       12	Scale	       Nó được sử dụng để cung cấp thanh trượt cho người dùng.
       
       13	Scrollbar	Nó cung cấp thanh cuộn cho người dùng để người dùng có thể cuộn cửa sổ lên và xuống.
       
       14	Text	       Nó khác với Entry vì nó cung cấp một trường văn bản nhiều dòng cho người dùng để người dùng có thể 
                            viết văn bản và chỉnh sửa văn bản bên trong nó.
       
       15	Toplevel	Nó được sử dụng để tạo một vùng chứa cửa sổ riêng biệt.
       
       16	Spinbox	Nó là một widget mục nhập được sử dụng để chọn từ các tùy chọn của các giá trị.
       
       17	PanedWindow	Nó giống như một widget container chứa các ô ngang hoặc dọc.
       
       18	LabelFrame	LabelFrame là một widget vùng chứa hoạt động như một container.
       
       18	MessageBox	Nó được sử dụng để hiển thị hộp thông báo trong các ứng dụng desktop.


"""


#--------------------------------------- Bố cục trong GUI ------------------------------------------

# Phương thức pack() được sử dụng để tổ chức widget theo khối. Vị trí các widget được thêm vào ứng dụng python bằng phương thức pack() có thể được kiểm soát bằng cách sử dụng các tùy chọn khác nhau được chỉ định trong lệnh gọi phương thức.
""" 
       Các tùy chọn (options):
              expand : Nếu expand là true thì tiện ích con sẽ mở rộng để lấp đầy khoảng trống.
              
              Fill : Xác định xem widget con có lấp đầy bất kỳ không gian thừa nào do trình đóng gói phân bổ cho nó hay không hoặc giữ các kích thước tối thiểu của riêng nó: NONE(mặc định), X (chỉ điền theo chiều ngang), Y (chỉ điền theo chiều dọc) hay BOTH (điền theo cả chiều ngang và chiều dọc ).
              
              side : Nó giúp xác định vị trí của widget so với widget cha.

"""
       # from tkinter import *
       # parent = Tk()
       
       # redbutton = Button(parent, text = "Red", fg = "red")
       # redbutton.pack(side = LEFT)
       # greenbutton = Button(parent, text = "Black", fg = "black")
       # greenbutton.pack(side = RIGHT)
       # bluebutton = Button(parent, text = "Blue", fg = "blue")
       # bluebutton.pack(side = TOP)
       # blackbutton = Button(parent, text = "Green", fg = "green")
       # blackbutton.pack(side = BOTTOM)
       # parent.mainloop()


#Trình quản lý layout grid() sắp xếp các widget ở dạng bảng. Chúng ta có thể chỉ định các hàng và cột. Chúng ta cũng có thể chỉ định khoảng cột (chiều rộng) hoặc chiều dài hàng (chiều cao) của widget con.
"""
       Dưới đây là danh sách tùy chọn của phương thức grid():
              Column: Số cột mà widget con sẽ được đặt. Cột ngoài cùng bên trái được biểu thị bằng 0.
              
              Columnspan: Chiều rộng của widget con. Nó đại diện cho số cột mà đến đó, cột được mở rộng.
              
              ipadx, ipady: Nó đại diện cho số lượng pixel cho đường viền của gidget.
              
              padx, pady: Nó đại diện cho số lượng pixel bên ngoài đường viền của gidget.
              
              row: Số hàng mà widget con sẽ được đặt. Hàng trên cùng được biểu thị bằng 0.
              
              rowspan: Chiều cao của widget con, tức là số hàng mà tiện ích con được mở rộng.
              
              Sticky: Nếu ô lớn hơn một widget, thì Sticky được sử dụng để chỉ định vị trí của widget bên trong ô. Nó có thể là sự ghép nối của các chữ cái sticky đại diện cho vị trí của widget. Nó có thể là N, E, W, S, NE, NW, NS, EW, ES.

"""
# from tkinter import *
# parent = Tk()
# name = Label(parent, text = "Name").grid(row = 0, column = 0)
# e1 = Entry(parent).grid(row = 0, column = 1)
# password = Label(parent, text = "Password").grid(row = 1, column = 0)
# e2 = Entry(parent).grid(row = 1, column = 1)
# submit = Button(parent, text = "Submit").grid(row = 4, column = 0)
# parent.mainloop()

# Trình quản lý layout place() sắp xếp các widget theo các tọa độ x và y.
"""
              Dưới đây là danh sách các tùy chọn:

                     Anchor: Nó thể hiện vị trí chính xác của widget con trong container. Giá trị mặc định là NW (góc trên bên trái).
                     
                     bordermode: Giá trị mặc định của kiểu đường viền là INSIDE đề cập đến việc bỏ qua giá trị gốc bên trong đường viền. Tùy chọn còn lại là OUTSIDE.
                     
                     height, width: Nó đề cập đến chiều cao và chiều rộng của widget tính bằng pixel.
                     
                     relheight, relwidth: Chiều cao và chiều rộng có giá trị trong khoảng 0,0 và 1,0.
                     relx, rely: Có giá trị trong khoảng 0,0 và 1,0, là độ lệch theo hướng ngang và dọc.
                     
                     x, y: Nó đề cập đến độ lệch ngang và dọc theo pixel.
"""
# from tkinter import *
 
# top = Tk()
# top.geometry("400x250")
# name = Label(top, text = "Name").place(x = 30, y = 50)
# email = Label(top, text = "Email").place(x = 30, y = 90)
# password = Label(top, text = "Password").place(x = 30, y = 130)
# e1 = Entry(top).place(x = 80, y = 50)
# e2 = Entry(top).place(x = 80, y = 90)
# e3 = Entry(top).place(x = 95, y = 130)
# top.mainloop()

#---------------------------------------- Label -------------------------------------------------

# from tkinter import *

# window = Tk()
# icon = PhotoImage(file="Orc-icon.png")
# label = Label(master=window,
#               text="Hello World",
#               font=("MV Boli",40,"bold"),
#               background="red",
#               foreground="green",
#               relief=RAISED,
#               border=10,
#               padx=20,
#               pady=20,
#               image=icon,
#               compound="left")            # master: Tên component chứa nó, bắt buộc phải có 
#                                           # relief : hiện đường viền xung quanh label 
#                                           # border : độ dày đường viền 
#                                           # padx : khoang cach tu text den khung vien theo chieu ngang
#                                           # pady : khoang cach tu text den khung vien theo chieu doc
#                                           # image : set hinh anh cho label
#                                           # compound: vi tri cua image so voi text, mac dinh image se de len text
                                          

# # label.config(background="red")
# label.pack()

# window.mainloop()

# --------------------------------------- Button ---------------------------------------------
# from tkinter import *

# def click():
#        print("You click button")

# window = Tk()

# image = PhotoImage(file="Emotes-face-smile-big-icon.png")

# button = Button(master=window,
#                 text="click me",
#                 command=click,
#                 font=("MV Boli",30,"bold"),
#                 foreground="green",
#                 background="black",
#                 activebackground="yellow",
#                 activeforeground="blue",
#                 state=ACTIVE,
#                 image=image,
#                 compound="bottom")           # command = gọi tới hàm làm nhiệm vụ nào đó khi ta ấn nút 
#                                           # activebackground = chỉnh màu background khi ta ấn nút
#                                           # activeforeground = chỉnh màu foreground khi ta ấn nút 
#                                           # state = DISABLED (không thể ấn), ACTIVITE ( chế độ mặc định, có thể ấn)
                                          

# button.pack()

# window.mainloop()

#------------------------------------------ Entry --------------------------------------
# là 1 hộp thoại cho phép người dùng nhập text vào ( nhưng chỉ cho phép nhập 1 dòng )

# from tkinter import *
# def getText():
#        name = entry.get()
#        if(name == "Enter your Fucking name"):
#               print("Fucking Ediot")
#        else:
#               print("Hello "+name)
#        entry.config(state=DISABLED)

# def delete():
#        entry.delete(first=0,last=END)
       

# if __name__ == "__main__": 
#        window = Tk()
#        entry  = Entry(master=window,
#                      font=("MV Boli",20,"bold"),
#                      foreground="green",
#                      background="black",
#                      show="*")                   # show : các ký tự sẽ được hiển thị giống theo quy định trong chuỗi 
       
#        entry.insert(0,string="Enter your Fucking name")        # thêm chuỗi vào vị trí index 

#        submit_button = Button(master=window,
#                             text="Submit",
#                             font=("Arial",10),
#                             command=getText)
       
#        delete_button = Button(master=window,
#                             text="Delete",
#                             font=("Arial",10),
#                             command=delete)

#        entry.pack( side=LEFT)
#        submit_button.pack(side=RIGHT)
#        delete_button.pack(side=RIGHT)
#        window.mainloop()

# ------------------------------------------------- Checkbox ----------------------------------------
# from tkinter import *


# def Check():
#        if(x.get() == 1):
#               print("Fuckup !!")
#               check_button.config(image= icon_yes )
#               # check_button_1.config(image=icon_yes)
#        elif(x.get() == 0):
#               print("OKE !!")
#               check_button.config(image=icon_no)
#               # check_button_1.config(image=icon_no)

# if __name__ == "__main__":       
#        window = Tk()
#        x = IntVar()
#        icon_no = PhotoImage(file="no-icon.png")
#        icon_yes = PhotoImage(file="Ok-icon.png")
#        check_button = Checkbutton(master=window,
#                             text="You are GAY",
#                             font=("MV boli",20,"bold"),
#                             variable=x,
#                             onvalue=1,
#                             offvalue=0,
#                             command=Check,
#                             background="black",
#                             foreground="green",
#                             activebackground="yellow",
#                             activeforeground="blue",
#                             padx= 20,
#                             pady= 20,
#                             image=icon_no,
#                             compound="left",
#                             indicatoron=False)          # variable = chỉ định biến sẽ nhận giá trị onvalue hoặc offvalue,     
#                                                                       # ngoài ra còn dùng để nhóm các nút lại nếu chung 1 tên biến 
#                                                         # onvalue = giá trị khi ta click chọn checkbox
#                                                         # offvalue = giá trị khi ta bỏ click checkbox
#                                                         # activebackground = chỉnh màu background khi ta ấn nút
#                                                         # activeforeground = chỉnh màu foreground khi ta ấn nút 
#                                                         # indicatoron = Nhận giá trị True hoặc False, hiện ô checkbox hay không
#                                                         # image = thêm ảnh cho checkbox
       
#        # check_button_1 = Checkbutton(master=window,
#        #                      text="You are GAY",
#        #                      font=("MV boli",20,"bold"),
#        #                      variable=x,
#        #                      onvalue=1,
#        #                      offvalue=0,
#        #                      command=Check,
#        #                      background="black",
#        #                      foreground="green",
#        #                      activebackground="yellow",
#        #                      activeforeground="blue",
#        #                      padx= 20,
#        #                      pady= 20,
#        #                      image=icon_no,
#        #                      compound="left",
#        #                      indicatoron=False)
       
#        check_button.pack(side="top")
#        # check_button_1.pack(side="bottom")

#        window.mainloop()

#----------------------------------------------- Radio Button --------------------------------------
# from tkinter import *

# def order():
#        if(x.get() == 0):
#               print("PIZZA !!")
#        elif(x.get() == 1):
#               print("HAMBURGER !!")
#        else:
#               print("HOTDOG !!")


# if __name__ == "__main__":
#        window = Tk()
#        x = IntVar()
#        food = ["pizza","hamburger","hotdog"]

#        imgae_pizza = PhotoImage(file="pizza.png")
#        image_hamburger = PhotoImage(file="hamburger.png")
#        image_hotdog = PhotoImage(file="hot-dog.png")

#        image_food = [imgae_pizza,image_hamburger,image_hotdog]

#        for index in range(len(food)):
#               check_radio = Radiobutton(master=window,
#                                    text=food[index],
#                                    variable=x,                   # nhóm các radiocheck lại (cùng biến x)
#                                    value=index,                  # đặt giá trị khác nhau cho từng radiocheck 
#                                    padx= 25,
#                                    font=("MV Boli",20,"bold"),
#                                    image=image_food[index],      # set image cho tung radio
#                                    compound="left",
#                                    command=order)
              
#               check_radio.pack(anchor=W)                              # Căng thẳng hàng các nút radio 

#        window.mainloop()

# ----------------------------------------- Scale ----------------------------------------

# from tkinter import *

# def submit():
#        print("Nhiet do la: "+ str(scale.get()))

# if __name__ == "__main__":
#        window = Tk()
#        scale = Scale(master=window,
#                      from_=100,           # Giới hạn trên thanh kéo
#                      to=0,                # Giới hạn dưới thanh kéo
#                      length=500,          # Chiều dài thanh kéo
#                      orient=VERTICAL,     # Quy định thanh kéo nằm ngang (HORIZONTAL) hay nằm dọc (VERTICAL)
#                      tickinterval=10,     # Chia khoảng của thanh Scale ( mỗi khoảng 10 đơn vị )
#                      # showvalue=False,      # Hiên giá trị thay đổi khi kéo thanh 
#                      troughcolor="blue",         # màu thanh kéo 
#                      foreground="red")
#        scale.set((scale["from"] - scale["to"])/2)       # set thanh keo o giua 
            
#        button_submit = Button(master=window,
#                             text="submit",
#                             command=submit)
#        scale.pack()
#        button_submit.pack()



#        window.mainloop()

# ----------------------------------------- ListBox --------------------------------------

# from tkinter import *

# def submit():
#        food = []
       
#        for index in list_box.curselection():                          # curselection : cho ra mảng các phần tử đang được chọn 
#               food.insert(index,list_box.get(index))
#        print(food)

# def add():
#        list_box.insert(list_box.size()+1,entry.get())
       
# def delete():
#        # list_box.delete(list_box.curselection())
#        for index in reversed(list_box.curselection()):         # phải reversed lại vì khi xóa mục trong list thì giá trị các mục còn lại bị thay đổi
#               list_box.delete(index)
# if __name__ == "__main__":
#        window = Tk()
       
#        list_box = Listbox(master=window,
#                           selectmode=MULTIPLE,          # cho phep chon nhiu muc
#                           )
       
#        list_box.insert(1,"pizza")
#        list_box.insert(2,"soda")
#        list_box.insert(3,"hamburger")
       
#        entry = Entry(master=window)
       
#        submit = Button(master=window,
#                        text="submit",
#                        command=submit)
#        add = Button(master=window,
#                        text="add",
#                        command=add)
#        delete = Button(master=window,
#                        text="delete",
#                        command=delete)
#        list_box.pack()
#        entry.pack()
#        submit.pack()
#        add.pack()
#        delete.pack()
#        window.mainloop()

#--------------------------------------------- MessageBox --------------------------------------
# from tkinter import *
# from tkinter import messagebox

# def mes():
#        messagebox.showinfo(title="APU",message="DAY LA THONG BAO")

# def war():
#        messagebox.showwarning(title="APU",message="DAY LA CANH BAO")

# def error():
#        messagebox.showerror(title="APU",message="DAY LA LOI")

# def ask_question():
#        anser = messagebox.askquestion(title="APU",message="TRA LOI CAU HOI")
#        print(anser)
       
# def ask_cancel():
#        answer = messagebox.askokcancel(title="APU",message="TRA LOI CAU HOI")
#        print(answer)
# def ask_yes_no():
#        answer = messagebox.askyesno(title="APU",message="TRA LOI CAU HOI")
#        print(answer)
# def ask_strycancel():
#        answer = messagebox.askretrycancel(title="APU",message="TRA LOI CAU HOI")
#        print(answer)

# if __name__ == "__main__":
#        window = Tk()
       
#        mes_but = Button(master=window,
#                         text="message",
#                         command=mes)
       
#        war_but = Button(master=window,
#                         text="warning",
#                         command=war)
#        error_but = Button(master=window,
#                         text="error",
#                         command=error)
#        ask_question_but = Button(master=window,
#                         text="ask_question",
#                         command=ask_question)
#        ask_cancel_but = Button(master=window,
#                         text="ask_cancel",
#                         command=ask_cancel)
       
#        ask_yes_no_but = Button(master=window,
#                         text="ask_yes_no",
#                         command=ask_yes_no)
#        ask_etrycancel_but = Button(master=window,
#                         text="ask_strycancel",
#                         command=ask_strycancel)
       
#        mes_but.pack()
#        war_but.pack()
#        error_but.pack()
#        ask_question_but.pack()
#        ask_cancel_but.pack()
#        ask_yes_no_but.pack()
#        ask_etrycancel_but.pack()

#        window.mainloop()
       
# -------------------------------------------- Color Chosser ------------------------------
# from tkinter import *
# from tkinter import colorchooser

# def click_background():
#        tuppel =  colorchooser.askcolor()
#        print(tuppel)
#        label.config(background=tuppel[1])

# def click_foreground():
#        tuppel =  colorchooser.askcolor()
#        print(tuppel)
#        label.config(foreground=tuppel[1])

# if __name__ == "__main__":
#        window = Tk()
#        label = Label(master=window,
#                      text="PHUC APU",
#                      font=("MV Boli",30,"bold"))
#        button = Button(master=window,
#                        text="change background color",
#                        command=click_background)
#        button2 = Button(master=window,
#                        text="change foreground color",
#                        command=click_foreground)
#        label.pack()
#        button.pack()
#        button2.pack()
       
#        window.mainloop()

# ------------------------------------------- Text Area ---------------------------------------------
# from tkinter import *

# def click():
#        chuoi = text.get(index1="1.0",index2=END)
#        print(chuoi)

# if __name__ == "__main__":
#        window = Tk()
#        text = Text(master= window,
#                    background="light yellow")
#        click = Button(master=window,
#                       text="click",
#                       command=click)
#        text.pack()
#        click.pack()
       
#        window.mainloop()

# ----------------------------------------- Open Dialog file --------------------------------------

# from tkinter import *
# from tkinter import filedialog
# def click():
#        path = filedialog.askopenfilename(initialdir="D:\\New",                      # thư mục muốn hiện lên khi mở dialog
#                                          title="APU",                               # tiêu đề
#                                          filetypes=(("file text","*.txt"),("all file","*.*"))     # lựa chọn file 
#                                          )
#        file = open(file=path,mode='r',encoding="UTF-8")
#        print(file.read())
#        file.close()

# if __name__ == "__main__":
#        window = Tk()
#        click = Button(master=window,
#                       text="click",
#                       command=click)
#        click.pack()
#        window.mainloop()

#----------------------------------------- Save Dialog File -----------------------------------------
# from tkinter import *
# from tkinter import filedialog

# def click():
#        file = filedialog.asksaveasfile(initialdir="D:\\New",
#                                        filetypes=(("file text","*.txt"),("all file","*.*")),     # lựa chọn file 
#                                           defaultextension=".txt",
#                                           )
#        file_text = text.get(1.0,END)
#        file.write(file_text)
#        file.close()
# if __name__ == "__main__":
#        window = Tk()
       
#        text = Text(master= window,
#                    background="light yellow")
       
#        click = Button(master=window,
#                       text="click",
#                       command=click)
#        text.pack()
#        click.pack()
       
#        window.mainloop()

#------------------------------------- MenuBar --------------------------------------------------
# from tkinter import *

# def openFile():
#        print("File da duoc mo")

# def saveFile():
#        print("FIle da duoc save") 

# if __name__ == "__main__":
       
#        window = Tk()
       
#        image = PhotoImage(file="hamburger.png")
       
#        menubar = Menu(master=window)                           # set up thanh menubar
#        window.config(menu=menubar)
       
#        file_menu = Menu(menubar,tearoff=0)                     # tearoff = bo duong gach ngang
#        menubar.add_cascade(label="File",menu=file_menu)        # Tạo đề mục cho thanh menubar
       
#        # tạo các menu item file 
       
#        file_menu.add_command(label="Open",command=openFile,image=image,compound="left")
#        file_menu.add_command(label="Save",command=saveFile)
#        file_menu.add_separator()                 # đường phân chia 
#        file_menu.add_command(label="Exit",command=quit)
       
#        edit_menu = Menu(menubar,tearoff=0)                     # tearoff = bo duong gach ngang
#        menubar.add_cascade(label="Edit",menu=edit_menu)        # Them đề mục cho thanh menubar
       
#        # tạo các menu item edit
       
#        edit_menu.add_command(label="Fix",command=openFile)
       
#        # mở rộng của menu item more trong edit 
#        More_menu = Menu(edit_menu,tearoff=0)
#        edit_menu.add_cascade(label="More..",menu=More_menu)
       
#        More_menu.add_command(label="hihi")
       
#        window.mainloop()

#---------------------------------------- Frame ------------------------------------------

# from tkinter import *

# if __name__ == "__main__":
#        window = Tk()
       
#        frame = Frame(master=window,
#                      background="pink",
#                      )
#        Button(master=frame,font=("MV Boli",20,"bold"),text="W").pack(side="top")
#        Button(master=frame,font=("MV Boli",20,"bold"),text="A").pack(side="left")
#        Button(master=frame,font=("MV Boli",20,"bold"),text="S").pack(side="left")
#        Button(master=frame,font=("MV Boli",20,"bold"),text="D").pack(side="left")
#        frame.pack()
#        window.mainloop()

# -------------------------------------- new window -----------------------------------

# from tkinter import *
# def new_window():
       
#        window.destroy()
#        new_window = Tk()
       
#        new_window.mainloop()


# if __name__ == "__main__":
#        window = Tk()
       
       
#        Button(master=window,font=("MV Boli",20,"bold"),text="new window",command=new_window).pack(side="top")
       
#        window.mainloop()

#---------------------------------------- tab ------------------------------------------
# from tkinter import *
# from tkinter import ttk

# if __name__ == "__main__":
#        window = Tk()
       
#        note_book = ttk.Notebook(master=window)          # tao node book
       
#        tab1 = Frame(master=note_book)
#        tab2 = Frame(master=note_book)
       
#        note_book.add(tab1,text="Tab 1")
#        note_book.add(tab2,text="Tab 2")
       
#        note_book.pack(side="left")
       
#        # them noi dung
#        Label(master=tab1,text="day la tab 1",font=("MV Boli",20,"bold")).pack()
#        Label(master=tab2,text="day la tab 2",font=("MV Boli",20,"bold")).pack()
       
       
#        window.mainloop()

#---------------------------------- progress bar -----------------------------------------

# from tkinter import *
# from tkinter.ttk import *
# import time
# import threading
# def start():
#        task  = 100
#        x = 0
#        while(x < task):
#               time.sleep(0.05)
#               bar['value'] +=5
#               x += 5 
#               percent.set(str(int((x/task)*100))+"%")

# if __name__ == "__main__":
#        window = Tk()
#        percent = StringVar()
#        bar = Progressbar(master=window, length= 300)
#        bar.pack(pady=10)
       
#        a = threading.Thread(target=start)                      # phải tạo luồn cho nó chạy song song nếu không nso sẽ bị đứng máy 
       
#        percentLabel = Label(master=window,textvariable=percent).pack()
#        Button(master=window,text="download",command=a.start).pack()
       
       
#        window.mainloop()

#--------------------------------------------- Canvas ----------------------------------------------
# vẽ hình 

# from tkinter import *

# if __name__ == "__main__":
#        window = Tk()
       
#        canvas = Canvas(master= window,height=300,width=300)
       
#        canvas.create_line(0,0,300,300,fill="red",width=10)            # duong thang
#        canvas.create_rectangle(30,30,250,250,fill="purple")           # hinh vuong
       
#        canvas.pack()
       
#        window.mainloop()

#------------------------------------- keyboard event ----------------------------------------------

# from tkinter import *

# def doSomething(event):
#       label.config(text=event.keysym)

# if __name__ == "__main__":
       
#        window = Tk()

#        window.bind(sequence="<Key>",func=doSomething)
#        label = Label(master=window,font=("MV Boli",50,"bold"))
#        label.pack()

#        window.mainloop()

#------------------------------------ mouse event -------------------------------------------------
# from tkinter import *

# def doSomething(event):
#       print("Toa do click: "+ str(event.x)+ ","+str(event.y))

# if __name__ == "__main__":
       
#        window = Tk()

#        # window.bind(sequence="<Button-1>",func=doSomething)     # chuot trai
#        # window.bind(sequence="<Button-2>",func=doSomething)     # chuot giua ( lăng chuột )
#        # window.bind(sequence="<Button-3>",func=doSomething)     # chuot phải
#        # window.bind(sequence="<ButtonRelease>",func=doSomething)     # bấm rồi thả chuột mới kích hoạt  
#        window.bind(sequence="<Enter>",func=doSomething)     # Khi chuột vào vùng được chỉ định 
#        window.bind(sequence="<Leave>",func=doSomething)     # Khi chuột ra vùng được chỉ định 
#        window.bind(sequence="<Motion>",func=doSomething)     # Khi chuột di chuyển trong vùng được chỉ định 

#        window.mainloop()

#------------------------------------ Drag and Drop ---------------------------------------------
# from tkinter import *

# def drag_start(event):
#     widget = event.widget                  # event.widget = truyền 1 cái label vào ( xem lại ở đầu trang về các widget)
#     widget.startX = event.x               #  event.x = vị trí x ta click chuột vào 
#     widget.startY = event.y               #  event.x = vị trí y ta click chuột vào 

# def drag_motion(event):
#     widget = event.widget
#     # x= tọa độ ban đầu(mặc định) - tọa độ ta click chuột + tọa độ chuột di chuyển
#     x = widget.winfo_x() - widget.startX + event.x    
    
#     y = widget.winfo_y() - widget.startY + event.y
#     widget.place(x=x,y=y)

# window = Tk()

# label = Label(window,bg="red",width=10,height=5)
# label.place(x=0,y=0)

# label2 = Label(window,bg="blue",width=10,height=5)
# label2.place(x=100,y=100)

# label.bind("<Button-1>",drag_start)
# label.bind("<B1-Motion>",drag_motion)

# label2.bind("<Button-1>",drag_start)
# label2.bind("<B1-Motion>",drag_motion)

# window.mainloop()

#------------------------------------- Move -----------------------------------------------

# from tkinter import *


# def up(event):
#        print(label_rocket.winfo_x())
#        label_rocket.place(x=label_rocket.winfo_x(), y=label_rocket.winfo_y()-10)

# def right(event):
#        label_rocket.place(x=label_rocket.winfo_x()+10, y=label_rocket.winfo_y())

# def left(event):
#        label_rocket.place(x=label_rocket.winfo_x()-10, y=label_rocket.winfo_y())

# def down(event):
#        label_rocket.place(x=label_rocket.winfo_x(), y=label_rocket.winfo_y()+10)

# if __name__ == "__main__":
#        window = Tk()
#        window.geometry("500x500")
       
#        rocket_image = PhotoImage(file="rocket-icon.png")
       
#        label_rocket = Label(master=window,image=rocket_image)
#        window.bind(sequence="<w>",func=up)
#        window.bind(sequence="<d>",func=right)
#        window.bind(sequence="<a>",func=left)
#        window.bind(sequence="<s>",func=down)
#        label_rocket.place(x=0,y=0)
       
#        window.mainloop()



# from tkinter import *
# import time
# import threading
# WIDTH = 500
# HEIGHT = 500
# xVelocity = 1
# yVelocity = 1



# def run(image_width,image_height):
#        global xVelocity
#        global yVelocity
#        while True:
#               coordinates = canvas.coords(my_image)               # trả về cặp tòa độ x y của bức ảnh 
#               print(coordinates)
#               if(coordinates[0]>=(WIDTH-image_width) or coordinates[0]<0):
#                      xVelocity = -xVelocity
#               if(coordinates[1]>=(HEIGHT-image_height) or coordinates[1]<0):
#                      yVelocity = -yVelocity
#               canvas.move(my_image,xVelocity,yVelocity)           # di chuyển bức ảnh 
#               # window.update()                                     # update lai
#               time.sleep(0.01)                             

       

# Tạo 1 canvas
# window = Tk()
# canvas = Canvas(window,width=WIDTH,height=HEIGHT)
# canvas.pack()

# # background_photo = PhotoImage(file='https___www.uschamber.com_assets_images_background_outer-space.png')
# # background = canvas.create_image(0,0,image=background_photo,anchor=NW)

# # tạo image con tàu 
# photo_image = PhotoImage(file='space-ship.png')
# my_image = canvas.create_image(0,0,image=photo_image,anchor=NW)


# image_width = photo_image.width()
# image_height = photo_image.height()

# # run_image = threading.Thread(target=run,args=(image_width,image_height,))

# # run_image.start()


# while True:
#     coordinates = canvas.coords(my_image)               # trả về cặp tòa độ x y của bức ảnh 
#     print(coordinates)
#     if(coordinates[0]>=(WIDTH-image_width) or coordinates[0]<0):
#         xVelocity = -xVelocity
#     if(coordinates[1]>=(HEIGHT-image_height) or coordinates[1]<0):
#         yVelocity = -yVelocity
#     canvas.move(my_image,xVelocity,yVelocity)           # di chuyển bức ảnh 
#     window.update()                                     # update lai
#     time.sleep(0.01)                             

# window.mainloop()



# ******************************************************
# Python Tic Tac Toe game
# ******************************************************

# from tkinter import *
# import random

# def next_turn(row, column):

#     global player

#        # kiểm tra nếu người chơi trước chưa thắng và nước đi tiếp theo rỗng 
#     if buttons[row][column]['text'] == "" and check_winner() is False:
#        # nếu người chơi là o 
#         if player == players[0]:

#             buttons[row][column]['text'] = player            # text trên button đó bằng o 
#                                                         # có thể chỉnh sửa text trên button bằng cách button['text']
#               # nếu kiểm tra chưa thắng thì tới người tiếp theo 
#             if check_winner() is False:
#                 player = players[1]
#                 label.config(text=(players[1]+" turn"))
#               # đúng thì thông báo 
#             elif check_winner() is True:
#                 label.config(text=(players[0]+" wins"))
#               # hòa 
#             elif check_winner() == "Tie":
#                 label.config(text="Tie!")

#         else:

#             buttons[row][column]['text'] = player

#             if check_winner() is False:
#                 player = players[0]
#                 label.config(text=(players[0]+" turn"))

#             elif check_winner() is True:
#                 label.config(text=(players[1]+" wins"))

#             elif check_winner() == "Tie":
#                 label.config(text="Tie!")

# def check_winner():

#        # kiểm tra theo hàng ngang 
#     for row in range(3):
#         if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
#             buttons[row][0].config(bg="green")
#             buttons[row][1].config(bg="green")
#             buttons[row][2].config(bg="green")
#             return True
#        # kiểm tra theo hàng dọc 
#     for column in range(3):
#         if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
#             buttons[0][column].config(bg="green")
#             buttons[1][column].config(bg="green")
#             buttons[2][column].config(bg="green")
#             return True
#        # kiểm tra theo hàng chéo từ [0][0] -> [2][2]
#     if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
#         buttons[0][0].config(bg="green")
#         buttons[1][1].config(bg="green")
#         buttons[2][2].config(bg="green")
#         return True
#        # kiểm tra theo hàng chéo từ [0][2] -> [2][0]
#     elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
#         buttons[0][2].config(bg="green")
#         buttons[1][1].config(bg="green")
#         buttons[2][0].config(bg="green")
#         return True
#        # kiểm tra hòa ( nếu đánh đủ tất cả các ô rồi )
#     elif empty_spaces() is False:

#         for row in range(3):
#             for column in range(3):
#                 buttons[row][column].config(bg="yellow")       # tô mày vàng tất cả các ô 
#         return "Tie"
       
#     else:
#         return False


# def empty_spaces():         # kiểm tra xem đã đánh đủ hết tất cả các ô chưa ( còn ô trống không )

#     spaces = 9

#     for row in range(3):
#         for column in range(3):
#             if buttons[row][column]['text'] != "":
#                 spaces -= 1

#     if spaces == 0:         #  đkhông còn ô trống  
#         return False
#     else:                   # còn ô trống 
#         return True

# def new_game():

#     global player

#     player = random.choice(players)

#     label.config(text=player+" turn")

#     for row in range(3):
#         for column in range(3):
#             buttons[row][column].config(text="",bg="#F0F0F0")   # set lại các nút đều rỗng 


# window = Tk()
# window.title("Tic-Tac-Toe")
# players = ["x","o"]
# player = random.choice(players)
# buttons = [[0,0,0],
#            [0,0,0],
#            [0,0,0]]

# label = Label(text=player + " turn", font=('consolas',40))
# label.pack(side="top")

# reset_button = Button(text="restart", font=('consolas',20), command=new_game)
# reset_button.pack(side="top")

# frame = Frame(window)
# frame.pack()

# for row in range(3):
#     for column in range(3):
#         buttons[row][column] = Button(frame, text="",font=('consolas',40), width=5, height=2,
#                                       command= lambda row=row, column=column: next_turn(row,column))
#         buttons[row][column].grid(row=row,column=column)

# window.mainloop()

# ******************************************************
import random
from tkinter import *
GAME_WIDTH = 600
GAME_HEIGHT = 600
SPEED = 100
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "GREEN"
FOOD_COLOR = "RED"
BACKGROUND_COLOR = "BLACK"
direction = "right"      # huong snake ban dau
score = 0 

class Snake :
    
    body_size = BODY_PARTS
    canvas_background = None
    ToaDo_chieu_dai_snake = []
    squares = []
    def __init__(self,canvas_background : Canvas) -> None:
        
        self.canvas_background = canvas_background
        for i in range(0,BODY_PARTS):
            self.ToaDo_chieu_dai_snake.append([0,0])            # chèn tọa độ thân[x,y] snake vào list ( list 2 chiều ) 
        
        for x,y in self.ToaDo_chieu_dai_snake:
            square = self.canvas_background.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOR,tag = "snake")
            self.squares.append(square)
            
        

class Food:
    
    random_x_y = None
    
    def __init__(self,canvas_background) -> None:
        x = random.randint(0,GAME_WIDTH/SPACE_SIZE - 1) * SPACE_SIZE
        y = random.randint(0,GAME_HEIGHT/SPACE_SIZE - 1) * SPACE_SIZE
        
        self.random_x_y = [x,y] 
        canvas_background.create_oval(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=FOOD_COLOR,tags="food")
        

def next_move(snake : Snake,food : Food, window , canvas_background,label_score ):
    x,y = snake.ToaDo_chieu_dai_snake[0]
    global direction
    if direction == "up":
        y = y - SPACE_SIZE
    elif direction == "down":
        y = y + SPACE_SIZE
    elif direction == "left":
        x = x - SPACE_SIZE
    elif direction == "right":
        x = x + SPACE_SIZE
        
    snake.ToaDo_chieu_dai_snake.insert(0,(x,y))
    
    square = canvas_background.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOR,tag = "snake")
    snake.squares.insert(0,square)
    
    
    
    if x == food.random_x_y[0] and y == food.random_x_y[1]:
        global score
        score += 1
        label_score.config(text = "SCORE {}".format(score))
        canvas_background.delete("food")
        
        food = Food(canvas_background)
        
    else:       # chi xoa khi khong an duoc food 
        snake.ToaDo_chieu_dai_snake.remove(snake.ToaDo_chieu_dai_snake[-1])         # xóa đi tọa độ của ô sau cùng 
   
        snake.canvas_background.delete(snake.squares[-1])               # xóa hình vuông sau cùng 
   
        snake.squares.remove(snake.squares[-1])                         # xoa hình vuông trong list squares
         
    if check_collision(snake) == True:
        game_over(canvas_background=canvas_background)
    else:
        window.after(SPEED,next_move,snake,food,window, canvas_background,label_score)       # cứ sao 50 gọi hàm 1 lần 

def change_move(change_direction):
    global direction
    
    if change_direction == "left":
        if direction != "right":             # khong cho no quay dau tro lai
            direction = change_direction
    
    elif change_direction == "right":
        if direction != "left":             # khong cho no quay dau tro lai
            direction = change_direction
    
    elif change_direction == "up":
        if direction != "down":             # khong cho no quay dau tro lai
            direction = change_direction
            
    elif change_direction == "down":
        if direction != "up":             # khong cho no quay dau tro lai
            direction = change_direction
    
def check_collision(snake : Snake):
    x,y = snake.ToaDo_chieu_dai_snake[0]
    
    # kiem tra snake dung cua so
    if x < 0 or  x >= GAME_WIDTH:
        return True
    if y < 0 or  y >= GAME_WIDTH:
        return True 
    
    # kiem tra snake dung body
    
    for body_part in snake.ToaDo_chieu_dai_snake[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
    return False
def game_over(canvas_background):
    canvas_background.delete(ALL)
    canvas_background.create_text( canvas_background.winfo_width()/2,canvas_background.winfo_height()/2,
                                  font=("MV Boli",40,"bold"),
                                  text = "GAME OVER",
                                  fill = "red",
                                  tag="gameover")

if __name__ == "__main__":
    
    window = Tk()
    
    window.title("APU")
    window.resizable(width=False,height=False)          # khong cho nguoi dung mo rong window
    
    
    
    
    label_score = Label(master=window,
                  text="SCORE {}".format(score),
                  font=("MV Boli",30,"bold"))
    
    label_score.pack()
    
    canvas_background = Canvas(master=window,
                               background=BACKGROUND_COLOR,
                               height=GAME_HEIGHT,
                               width=GAME_WIDTH)
    canvas_background.pack() 
    
    window.update()
    
    window_height = window.winfo_height()
    window_width = window.winfo_width()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    # làm cho window xuất hiện giữa màn hình 
    x = int((screen_width/2)-(window_width/2))
    y = int((screen_height/2)-(window_height/2))
       
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    window.bind(sequence="<Down>",func= lambda event : change_move("down"))
    window.bind(sequence="<Up>", func= lambda event : change_move("up"))
    window.bind(sequence="<Right>", func = lambda event : change_move("right"))
    window.bind(sequence="<Left>", func = lambda event : change_move("left"))
    
    
    food = Food(canvas_background=canvas_background)
    snake = Snake(canvas_background=canvas_background)
    next_move(snake,food,window,canvas_background,label_score)
    window.mainloop()


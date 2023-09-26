# ------------------String and vairibles-------------------
# print("", end = "")       # end la ket thuc chuoi bang ky tu nao, neu khong co tham so end thi no se mac dinh la xuong dong
# name = "phuc" 
# last_name = "Truong"
# print(name + last_name)

# age = 21
# print(type(age))           # in kieu bien
# print("Tuoi cua ban la: " + str(21))             # doi so --> chuoi   

# height = 174.5
# print(type(height))
# print("Chieu cao cua ban la: "+str(height))

# human = True
# print(type(human))
# print("Ban co phai la con nguoi: "+str(human))

#----------------------Khai bao nhieu bien tren 1 dong-----------------------------------
# name = "phuc"
# old = 21
# human = True
# name,old,human = "Phuc",21,True           
# old = somthing = 20
# print(name)
# print(old)
# print(human)
# print(somthing)

#------------------------- Mot so thao tac tren chuoi--------------------------------------
# name = "Truong Cong Phuc"
# print(len(name))            # chieu dai chuoi
# print(name.find("o"))       #tim ky tu trong chuoi
# print(name.upper())         # in hoa
# print(name.lower())         # in thuong
# print(name.isdigit())       # phai la chu so khong
# print(name.isalpha())       # co phai la ky tu khong
# print(name.count("o"))      # dem ky tu chi dinh co trong chuoi
# print(name.replace("Phuc","Apu"))         # thay the chuoi 
# print(name * 3)      # in name ra 3 lan

#-------------------------- Ep kieu bien -------------------------------------------------------
# So_nguyen = 1
# So_thuc = 1.0
# Chuoi = "3"
# print(int(So_thuc))         # ep kiem float --> int
# print(float(Chuoi) * 3)       # ep kieu string --> float 
# print(So_nguyen * So_thuc)       # int * float = float
# print (Chuoi + str(So_nguyen))

#--------------------------- Nhap du lieu ------------------------------------------------------
# name =  input("Nhap ten cua ban: ")   # du lieu nhap vao se duoc tra ve duoi dang chuoi
# Tuoi = int(input("Nhap tuoi cua ban: "))         # ep kieu du lieu tra ve la chuoi --> int
# print("Ten ban la: " +name)                     # loi --> vi du lieu tra ve la dang chuoi nen khong the + int
# print(Tuoi + 1)

#---------------------------- import math ----------------------------------------------------
# import math
# a = 3.14
# print(round(a))      # lam tron so 
# print(math.ceil(a))  # lam tron len
# print(math.floor(a)) # lam tron xuong
# print(abs(a))        # tri tuyet doi
# print(pow(a,2))      # ham mu
# print(math.sqrt(9))  # can bac 2
# print(max(1,2,3))    # tim max
# print(min(1,2,3))    #tim min 

#-------------------------- Cat chuoi --------------------------------------------------------
# chuoi trong py nhu mot mang cac ky tu duoc ghep noi voi nhau va duoc giu boi con tro nao do
# co the cac chuoi thong qua mang index[] or slide()
# [start:end:step]   <-> [bat dau tu start : dieu kien dung lai : buoc nhay ]
# khong nhat thiet phai du 3 dieu kien
# nếu tính từ đầu chuỗi thì sẽ là 0,1,2,...
# nếu tính từ cuối chuỗi lên thì sẽ là 0,-1,-2 
# => name[0:4] = "Truo"
# => name[0:-4] = "Truong Cong"
# name = "Truong Cong Phuc"

# fist_name = name[:6]       # lay ky tu tu 0 -> 5 [start:end]  neu khong dien start thi py se set gia gia mac dinh bat dau = 0
# last_name = name[12:]    # lay ky tu tu 12 ->16 [start:end]  neu khong dien gia tri end thi py se mac dinh la chieu dai cua chuoi
# random_name = name[::3]

# reserved_name = name[::-1]           # dao chuoi


# print(fist_name)
# print(last_name)
# print(random_name)
# print(reserved_name)

# web = "http://google.com"
# slice = slice(0,-4)
# print(web[slice])

#------------------------------- if - else -----------------------------------------------
# old = int(input("Ban bao nhieu tuoi: "))

# if old >18:
#        print("Ban la thanh thieu nien")
#        print("Ban da du tuoi cuoi vo")
# elif old < 18:
#        print("Ban la vi thanh nien")
#        print("Ban chua du tuoi cuoi vo")
# else:
#        print("Ban 18 tuoi")

#------------------------------- Toan tu logic ( ket noi cac dieu kien)-------------------------
# and , or , not
# old = input("Ban bao nhieu tuoi: ")     
# if( not(old.isdigit()) == True):
#        print("sai du lieu")
# elif (old.isdigit()):
#        old = int(old)  
#        if old >18 and old < 100 :
#               print("Ban la thanh thieu nien")
#               print("Ban da du tuoi cuoi vo")
#        elif old < 18 or old >= 0:
#               print("Ban la vi thanh nien")
#               print("Ban chua du tuoi cuoi vo")

#        else:
#               print("Ban 18 tuoi")     

#---------------------------------- Toán tử khai thác, toán tử xác thực --------------------------
# Toán tử khai thác : in , not in
#Toán tử xác thực : is , not is
# a = [1,2,3,4]
# b = 4

# print(b in a)        # true
# print( b not in a)   #false

# c = 3
# d = 4

# print(c is d)        #false
# print(c is not d)    # true

#---------------------------------- while ----------------------------------------------------
# while 1==1:
#        print("vong lap vo han")

# ---------------------------------- for ----------------------------------------------------
# cau truc: for i in range (start,end,step) :

# for i in range(10):         # [0,9]
#        print(i)

# for i in range(5,10):         # [5,9]
#        print(i)

# for i in range(0,10,2):           # [start = 0, end = 10,step = 2]
#        print(i)

# for i in "Truong Cong Phuc":       # in tung ky tu trong chuoi
#        print(i)

# import time
# for i in range (10,0,-1):          # in tu 10 -> 0
#        print(i)
#        time.sleep(1)               # cho luồng ngủ 
# print("Happy New Year")

#--------------------------- vong for lồng nhau - nhập mảng 2 chiều -------------------------
# rows = int(input("Nhap so dong: "))
# colums = int(input("Nhap so cot: "))
# symbol = input("Nhap bieu tuong muon in: ")
# for i in range (rows):
#        for j in range (colums):
#               print(symbol, end="")
#        print()

#----------------------------- break - continue - pass -------------------------------------
# break : phá vòng lặp 
# continue : bỏ qua thao tác nào đó để tiếp tục vòng lặp
# pass : không làm gì       ( chua duoc dung nhieu)

# while True: 
#        name = input("Nhap ten cua ban: ")
#        if(name != ""): break
# print(name)

# for i in range (10):
#        if(i % 2 == 0):
#               continue
#        print(i, end= " ")

# for i in range (10):
#        if(i % 2 == 0):
#               pass
#        else:
#               print(i, end=" ")
               
#------------------------------ Mảng 1 chiều ---------------------------------------------------
# food = ["Banh chung","Tra sua","Banh my"]
# food.append("Banh tet")            # chen vao cuoi
# food.remove("Banh chung")        # xoa obj duoc chi dinh
# food.pop()                       # xoa phan lay phan tu dau va xoa no di
# food.insert(0,"Banh chung")      # chen vao index duoc chi dinh
# food.sort()                      # sao xep
# food.clear()                     # xoa mang
# for i in  food:
#        print(i)

#------------------------------ Mảng 2 chiều ---------------------------------------------------
# food = ["Banh chung","Com","Banh my"]
# drink = ["Nuoc",1]

# menu = [food,drink]
# print(menu[1][1])

#-------------------------------- Tuples -------------------------------------------------------
# Tuples (Bộ) : đưoc dùng để nhóm các dữ liệu liên quan lại với nhau và không thể thay đổi 
# student = ("Phuc",19,"SGU")
# print(student.count("Phuc"))
# print(student.index(19))

# for x in student:
#        print(x)

#---------------------------------- Set ---------------------------------------------------
# Set :  là cấu trúc tập hợp các dữ liệu không có thứ tự và không tồn tại 2 giá trị giống nhau trong cùng 1 set 
# food1 = {"Com","Banh my","Banh my","Banh tet"}          # 1 giá trị bánh mỳ sẽ bị lượt bỏ bớt 
# print(food1)
# drink = {"coca","pepsi"}

# food1.add("Com tam")        # them gia tri
# food1.remove("Banh my")
# food1.clear()
# food1.update(drink)         # them nhứng giá trị từ drink vào food1 nếu những giá trị đó chưa có trong food1 

# temp = food1.union(drink)   # hợp 
# temp1 = food1.difference(drink)    # phép trừ : food1 - drink
# temp2 = food1.intersection(drink)  # Phép giao 

# for i in temp:
#        print(i)

#----------------------------------- Dictionary (giống map) ---------------------------------------------------
# Map : giống set  , những được lưu trữ dưới dạng cặp key và value 
# food = {"USA" : "My" , "VN":"Viet nam" , "JP":"Japan"}
# food.update({"TL":"Thai lan"})     # them 1 key-value moi
# food.update({"USA":"Washinton DC"})       # update đè lên valur cũ
# food.pop("USA")             # xoa dua vao key
# print(food["JP"])           # dùng key để gọi đến giá trị nó nắm giữ (chữ không cần thông qua biến index)
# print(food.get("USA"))      # cách 2 để lấy giá trị của key 
# print(food.keys())          # lấy ra bộ key có trong Map 
# print(food.values())        # lấy ra bộ value có trong Map
# print(food.items())         # lấy ra bộ key-value có trong Map 

# for key,value in food.items():
#        print(key,value)

#------------------------------------- Nhap mang 1,2 chieu ----------------------------------------------
# arr = []

# m = int(input("Nhap so dong: "))
# n = int(input("Nhap so cot: "))
# for i in range (m):
#        brr = []
#        for j in range (n):
#               a = int(input("Nhap pt: "))
#               brr.append(a)
#        arr.insert(i,brr)

# for i in range (m):
#        temp = arr[i]
#        for j in range (n):
#               print(temp[j], end=" ")
#        print()              

#--------------------------------------- Ham con --------------------------------------------------------
# def Xinchao( name ):          
#        print("Xin chao " + name)

# Xinchao(name="Phuc")

# def SNT ( check : int):          # Chúng ta có thể quy định kiểu dữ liệu truyền vào cho người nhập biết 
#        if( check < 2):
#               return False
#        for i in range (2,check):
#               if( check % i == 0):
#                      return False
#        return True


# n = int(input("Nhap n vao tim so nguyen to 1-> n: "))
# for i in range (2,n+1):
#        if( SNT(i) == True):
#               print(i,end=" ")

# ---------------------------------------- Keyword arguments  ------------------------------------
# def Hello(first_name,Last_name,Mid_name):
#        print(first_name +" "+ Mid_name+" "+ Last_name)

# Hello(first_name="Truong",Mid_name="Cong",Last_name="Phuc")    # Là cách chúng ta quy định các giá trị truyền vào sẽ dành cho tham số nào, lúc đó không cần truyền đúng thứ tự tham số mà chỉ cần quy định giá trị nào của tham số nào 

# ---------------------------------------- Nested funtion ---------------------------------------
# Là một hàm được gọi trong 1 hàm khác, hàm lòng hàm 

#VD:
# num = int(input("Nhap so n: "))
# num = float(num)            # đổi sữ liệu sang float
# num = abs(num)              # Tri tuyet doi
# num = round(num)            # lam tron so
# print(num)

# Ta có thể viết ngắn gọn bằng cách sao
# print(round(abs(float(int(input("Nhap so n: "))))))

#----------------------------------------- Biến toàn cục và biến cục bộ ---------------------------
# độ ưu tiên biến: Cục bộ , Gần nhất , Toàn cục, Biến truyền vào lúc biên dịch
# name = "Phuc"        # Biến toàn cục 

# def Hello(name):
#        name = "Tuan"               # Biến cục bộ
#        print("xin chao "+name)     # Chọn biến cục bộ hay vì biến toàn cục theo đọ ưu tiên 

# Hello(name)

# Ta có thể khai báo biến toàn cục trong hàm con bằng cách thêm từ khóa global 
# name = "Phuc"        # Biến toàn cục 

# def Hello():
#        global name                        # thông báo rằng biến name này chính là biến toàn cục được khai báo trước đó 
#        name = "APU"            
#        print("xin chao "+name)      

# Hello(name)


#--------------------------------------- *argv - **kwargv ----------------------------------------
# Để tôi bắt đầu nói tôi yêu thích tên toán tử này - nó rất là … trực quan. * là  ký hiệu phổ biến nhất về phép nhân, nhưng ở Python nó còn có nghĩa toán tử Splat.

# Tôi nghĩa toán tử này như cái hộp piñata - cái hộp nhét bánh kẹo vào trong rồi người ta dùng gậy đập tung nó ra. Tôi đã từng mô tả về toán tử mở rộng - một cái tương đương splat của JavaScript - nó giải nén một chuỗi domino rồi đẩy và một danh sách đơn lớn hơn, nhưng splat bảo đảm tương tự một cái mạnh mẽ hơn.

# a = [1,2,3]
# b = [*a,4,5,6]
# print(b)             # [1,2,3,4,5,6] - Giải nén nó (*) ra 

# Vậy chúng ta đã biết toán tử splat giải nén toàn bộ dữ liệu có kí hiệu *, và có 2 loại tham số function. Vậy, nếu bạn chưa phát hiện ra, *args là viết tắt của (arguments) đối số, **kwargs là viết tắt của (keyword arguments) đối số từ khóa.

# Nó được sử dụng để giải nén ra loại đối số tương ứng, cho phép gọi function có list đối số có số lượng giá trị thay đổi. 

# VD 1:
# def KT_SNT(*argv):
#        argv = list(argv)     # Có thể ép kiểu về list để tiền sửa đổi (thay đổi giá trị)
#                             # Lúc này trong list argv sẽ có một bộ [[a,b,c]] và bộ này nằm ở index thứ 0 
#        arr = argv[0]
#        kq = []
#        for i in arr:             
#               if(i >= 2):
#                      check = -1
#                      for j in range(2,i):
#                             if( i % j == 0):
#                                     check = 1
#                      if(check == -1):
#                             kq.append(i)
#        return kq

# n = int(input("Nhap so pt: "))
# a = []
# for i in range(n):
#        number = int(input("Nhap gia tri "+ str(i)+ " : "))
#        a.append(number)
# a = list(a)
# print("Mang truoc luc KT_SNT: ")
# for i in a:
#        print(i,end=" ")
# print("Mang sau khi kiem tra: ")
# kq = KT_SNT(a)
# print(kq)

# VD 2:
# def sua_mang(*argv):
#        argv = list(argv)           # argv = [ [1,2,3] , 2 , 5]      argv[0] = [1,2,3]      argv[1] = 2          argv[2] = 5
#        check = -1
#        for i in argv[0]:
#               if(i == argv[1]):
#                      argv[0][i] = argv[2]
#                      check = 1
#        if(check == -1):
#               print("Khong co so can sua trong mang")
#        print (argv)


# # main
# n = int(input("Nhap so pt: "))
# arr = []
# for i in range(n):
#        number = int(input("Nhap gia tri "+ str(i)+ " : "))
#        arr.append(number)

# a = int(input("Nhap so can sua trong mang: "))
# b = int(input("Nhap so thay the so can sua do: "))

# print("Mang cua ban la: ")
# print(arr)
# print("So ban muon sua: "+str(a))
# print("So ban muon thay the: "+str(b))
# print("Ket qua:")
# sua_mang(arr,a,b)

# # Nó sẽ là 1 mảng gồm các key-value tương ứng do người dùng truyền vào 
# def Hello (**kwargv):
#        # kwargv = list(kwargv)
#        print(kwargv) # {'name': 'Phuc', 'mid_name': 'Cong', 'first_name': 'Truong'}
#        print(kwargv.keys())
#        print(kwargv.values())

# Hello(name="Phuc",mid_name = "Cong",first_name = "Truong")

#------------------------------------------- String Format ---------------------------------------
# name = "Phuc"
# nick_name = "Apu"

# print("My name is {} and my nick name is {}".format(name,nick_name))
# print("My name is {} and my nick name is {}".format("Phuc","Apu"))
# print("My name is {1} and my nick name is {0}".format(name,nick_name))
# print("My name is {name} and my nick name is {nick_name}".format(name = "Phuc",nick_name = "Apu"))
# print("My name is {:10} and my nick name is {}".format(name,nick_name))
# print("My name is {:>10} and my nick name is {}".format(name,nick_name))
# print("My name is {:<10} and my nick name is {}".format(name,nick_name))

# pi = 3.14159
# print("{:.3f}".format(pi))
# print("{:,}".format(pi))

#------------------------------------------- Random ---------------------------------------------
# import random

# x = random.randint(1,6)     # random 1 số từ 1 -> 6
# y = random.random()         # random 1 số trong [0,1)

# mtList = ["hi","Hello","Xin chao"]
# z = random.choice(mtList)          # random 1 giá trị trong list
# print(z)

# random.shuffle(mtList)             # xóa trộn các giá trị trong 1 list

#------------------------------------- Exception ------------------------------------------------
# try - except - else - finally

# try:
#        a = int(input("Nhap so bi chia: "))
#        b = int(input("Nhap so chia: "))
#        kq = a/b
# except ZeroDivisionError as e:      # Phải khai báo các ngoại lệ con có thể xảy ra trước khi khai báo ngoại lện cha (Exception)
#        print(e)
#        print("Khong the chia 1 so cho 0")
# except ValueError as e:
#        print(e)
#        print("Nhap sai kieu du lieu")
# except Exception:
#        print("CO LOI !!")
# else:                              # Nếu không có ngoại lệ xảy ra thì thực hiện khối lệnh này 
#        print("Ket qua = " + str(kq))
# finally:                           # Dù không có hay có ngoại lệ, khối lệnh này sẽ vẫn đc thực hiện
#        print("Hoan tat chuong trinh")

#------------------------------------ Check a file exist ------------------------------------------
# import os

# path = "C:\\Users\\ACER\\Desktop\\nhap.txt"

# if os.path.exists(path):
#        print("Co ton tai")
#        if(os.path.isfile(path)):
#               print("No la 1 file")
#        elif (os.path.isdir(path)):
#               print("No la 1 thu muc")
# else:
#        print("Khong ton tai")

#------------------------------------ Read a File --------------------------------------------------
# open("Tên file", mode = ' w', encoding = " " )        mode là w (mở để ghi ) , r (mở để đọc),... (giống bên c)
# try :
#        with open("C:\\Users\\ACER\\Desktop\\nhap.txt",mode='w',encoding="utf8") as file:
#               print(file.read())
# except FileNotFoundError as e:
#        print("File khong ton tai!!")

#----------------------------------- Write File --------------------------------------------------

# with open("nhap.txt",mode='w',encoding="utf8") as file:
#        file.write("Hello my friend \nMy name is PhucApu")

#----------------------------------- Copy File ---------------------------------------------------
#copyfile(src, dst)	Copy nội dung một file                    
#copy(src, dst)	Copy nội dung một file kèm quyền truy cập
#copy2(src, dst)	Copy nội dung một file kèm Permission và Metadata
#copytree(src, dst)	Copy toàn bộ file trong một thư mục

# import shutil
# shutil.copyfile(src="nhap.txt",dst="nhap2.txt")

#----------------------------------- Move a File ( or Directory) ----------------------------------------------------
# import os

# src = "nhap.txt"
# destination = "nhap3.txt"

# try:
#        if (os.path.exists(path=destination)):
#               print("Da co file do o day roi!!")
#        else:
#               os.replace(src=src,dst=destination)
#               print("File da duoc di chuyen")
# except FileNotFoundError as e:
#        print("Duong dan khong ton tai")

#----------------------------------- Delete a File -----------------------------------------
# import os
# path = "nhap3.txt"
# try:
#        os.remove(path=path)
# except FileNotFoundError:
#        print("File can xoa khong ton tai!!")
# else:
#        print("Xoa thanh cong")

#----------------------------------- Modules -------------------------------------------------
# Là cách import 1 file py khác vào file đang làm việc
# # giả sử tạo file py Examble_Modules có hàm hello() và import nó vào file chính 

# import Examble_Modules
# Examble_Modules.hello(name="Apu")

# from Examble_Modules import hello
# hello(name="Apu")

# help(request="modules")          # Để xem các file của hệ thống py có thể import 

# ------------------------------------ Game -------------------------------------------------
# import random

# options = ("rock", "paper", "scissors")
# running = True

# while running:

#     player = None
#     computer = random.choice(options)

#     while player not in options:
#         player = input("Enter a choice (rock, paper, scissors): ")

#     print(f"Player: {player}")
#     print(f"Computer: {computer}")

#     if player == computer:
#         print("It's a tie!")
#     elif player == "rock" and computer == "scissors":
#         print("You win!")
#     elif player == "paper" and computer == "rock":
#         print("You win!")
#     elif player == "scissors" and computer == "paper":
#         print("You win!")
#     else:
#         print("You lose!")

#     if not input("Play again? (y/n): ").lower() == "y":
#         running = False

# print("Thanks for playing!")


# ------------------------------------ Game -------------------------------------------------
#● ┌ ─ ┐ │ └ ┘
# import random

# dice_art = {
#     1: ("┌─────────┐",
#         "│         │",
#         "│    ●    │",
#         "│         │",
#         "└─────────┘"),
#     2: ("┌─────────┐",
#         "│  ●      │",
#         "│         │",
#         "│      ●  │",
#         "└─────────┘"),
#     3: ("┌─────────┐",
#         "│  ●      │",
#         "│    ●    │",
#         "│      ●  │",
#         "└─────────┘"),
#     4: ("┌─────────┐",
#         "│  ●   ●  │",
#         "│         │",
#         "│  ●   ●  │",
#         "└─────────┘"),
#     5: ("┌─────────┐",
#         "│  ●   ●  │",
#         "│    ●    │",
#         "│  ●   ●  │",
#         "└─────────┘"),
#     6: ("┌─────────┐",
#         "│  ●   ●  │",
#         "│  ●   ●  │",
#         "│  ●   ●  │",
#         "└─────────┘")
# }

# dice = []
# total = 0
# num_of_dice = int(input("How many dice?: "))

# for die in range(num_of_dice):
#     dice.append(random.randint(1, 6))

# # PRINT VERTICALLY
# # for die in range(num_of_dice):
# #    for line in dice_art.get(dice[die]):
# #        print(line)

# # PRINT HORIZONTALLY
# for line in range(5):
#     for die in dice:
#         print(dice_art.get(die)[line], end="")
#     print()

# for die in dice:
#     total += die
# print(f"total: {total}")

#----------------------------------------- Mã hóa ----------------------------------------

# import random
# import string

# chars = " " + string.punctuation + string.digits + string.ascii_letters
# chars = list(chars)
# key = chars.copy()

# random.shuffle(key)

# #ENCRYPT
# plain_text = input("Enter a message to encrypt: ")
# cipher_text = ""

# for letter in plain_text:
#     index = chars.index(letter)
#     cipher_text += key[index]

# print(f"original message : {plain_text}")
# print(f"encrypted message: {cipher_text}")

# #DECRYPT
# cipher_text = input("Enter a message to encrypt: ")
# plain_text = ""

# for letter in cipher_text:
#     index = key.index(letter)
#     plain_text += chars[index]

# print(f"encrypted message: {cipher_text}")
# print(f"original message : {plain_text}")

# ------------------------------------- Toán tử := --------------------------------------------
# là toán tử giúp chũng ta vừa thao tác vừa gán giá trị trên cùng 1 dòng 
# x= 1
# # print(x = x + 1 )           # Sẽ báo lỗi vì không thể vừa tăng giá trị vừa gán trên cùng 1 dòng 
# print(x := x + 1)             # Không báo lỗi ( vừa tăng x lên vừa gán x bằng giá trị mới )

# foods = []

# while food := input("Nhap mon an ( thoat nhap quit): ").lower() != "quit":
#        foods.append(food) 

# ------------------------------------ Địa chỉ hàm ------------------------------------------

# def Hello():
#        print("Hello")

# print(Hello)                # Nó sẽ in ra địa chỉ dùng để lưu chương trình ngay thời điểm biên dịch 

# Hi = Hello                  # Hi và Hello cùng trỏ tới 1 địa chỉ 
# print(Hi)

# Hi()                     # in ra Hello
# Hello()                  # in ra Hello

# Say = print
# Say("Xin chao ban")

#------------------------------------- Truyền hàm vào hàm ------------------------------------
# Do hàm trong py được xem như là 1 object nên có thể truyền vào được
# def lower(text : str):
#        return text.lower()

# def upper(text):
#        return text.upper()

# def Hello(func):
#        Chuoi = func("Hello")
#        print(Chuoi)

# Hello(upper)                # Truyền tên hàm vào 

# def So_bi_chia(x):
#        def So_chia(y):
#               return y/x
#        return So_chia

# chia = So_bi_chia(2)        #  Hàm So_bi_chia() được gọi với giá trị x = 2 được truyền vào
#                             # Vào bên trong, hàm So_chia() chưa được gọi nên nó bỏ qua và nó trả về địa chỉ của hàm So_chia()
#                             # Nên lúc này chia = So_chia ( xem giải thích ở địa chỉ hàm)
# print(chia(10))             # --> chia(10) = So_chia(10) 

#-------------------------------------- LambDa ---------------------------------------
# Lambda funtion = là 1 hàm được viết rút gọn trên 1 dòng bằng cách dùng từ khóa lamda, nhưng chỉ có thể có 1 thao tác (thường là giá trị trả về)
# Cấu trúc: <tên hàm> = lamda <biến a> , <biến b> , ... : trả về giá trị các biến đó sao khi đã thao tác 

# Hello = lambda x : x + 1           # Nhận giá trị đầu vào là tham số x --> trả về giá trị x + 1   
# print(Hello(3))

# Check_So_Chan = lambda x : True if(x % 2 == 0) else False
# print(Check_So_Chan(2))


# def myfunc(n):
#   return lambda a : a * n

# # mydoubler = myfunc(2)

# print(myfunc(11))           # Trả về địa chỉ hàm 

#----------------------------------- Sort - Sorted --------------------------------------
# Sorted:  Đây là một hàm có sẵn trong Python. Đúng như tên gọi của nó thì hàm này có thể sắp xếp các phần tử ở trong một list, set hay tuple. Kết quả trả về là 1 list, bạn có thể ép kiểu nó sang kiểu dữ liệu khác.
# Hàm sorted được dùng thường xuyên với việc sắp xếp các số.

# List
# number_list = [7, 5, 8, 2, 4, 1, 3]
# Sap_xep_list = sorted(number_list)             # trả về 1 list  
# print(Sap_xep_list)

# Set 
# number_set = {7, 5, 8, 2, 4, 1, 3}
# Sap_xep_set = sorted(number_set)
# print(Sap_xep_set)

# Tuple
# number_tuple = (7, 5, 8, 2, 4, 1, 3)
# Sap_xep_tuple = sorted(number_tuple)
# print(Sap_xep_tuple)

#Hàm sorted() cũng có thể được sử dụng để sắp xếp các chuỗi ký tự. Lưu ý là hàm sorted() là case-sensitive, tức là các ký tự in hoa sẽ có giá trị và thứ tự khác với các ký tự không in hoa.

# char_list = ['I', 'i', 'one', 'two', 'three', 'a', 'b', 'c']
# Sort = sorted(char_list)
# print(Sort)          # ['I', 'a', 'b', 'c', 'i', 'one', 'three', 'two']

# sentence = 'I like abc'
# Sort = sorted(sentence)
# print(Sort)                 # [' ', ' ', 'I', 'a', 'b', 'c', 'e', 'i', 'k', 'l']

# Các tham số :
       # reverse : ( True hoặc False) được dùng để đảo ngược vị trí sắp xếp tăng dần thành giảm dần nếu reverse = True 
       # number_list = [7, 5, 8, 2, 4, 1, 3]
       # Sap_xep_list = sorted(number_list,reverse=True)             # trả về 1 list  
       # print(Sap_xep_list)                       # [8, 7, 5, 4, 3, 2, 1]
       
       # Key: Nếu bạn có một hàm đặc biệt và cần chạy hàm này với mỗi phần tử của đối tượng truyền vào hàm sorted(), bạn có thể truyền vào tham số key, và sorted sẽ sắp xếp các phần tử dựa trên kết quả trả về của hàm đó. Giả dụ, bạn có 1 mảng 2 chiều:
       # multidimensional_array = [[1, 3], [4,0], [2,1], [7,3], [9,9]]
       # Và giờ bạn muốn sắp xếp mảng này dựa trên phần tử tại vị trí thứ 2 (tức index là 1), bạn có thể truyền vào key một hàm lambda, ở đây chúng ta chỉ cần sắp xếp theo phần thử tại index 1, vậy hàm lambda sẽ là:
       # Sort = sorted(multidimensional_array, key=lambda x : x[1])
       # print(Sort)          # [[4, 0], [2, 1], [1, 3], [7, 3], [9, 9]]
       
# Lưu ý:
       # Không thể sắp xếp nếu các giá trị không cùng kiểu dữ liệu. VD : [1,2,3,"Phuc"]
       # Hàm trong tham số key chir nhận 1 giá trị đầu vào và 1 giá trị trả về:

       # def Key( x,y):
       #        return x*y

       # number_list = [7, 5, 8, 2, 4, 1, 3]
       # Sap_xep_list = sorted(number_list,key=Key)             # Key() missing 1 required positional argument: 'y'  
       # print(Sap_xep_list)                       
       
       # Hàm trong key phải giải quuyết được tất cả giá trị có trong mảng
       
# Sort: 
# So với hàm sorted() thì hàm sort() có chức năng gần như tương tự, trừ 1 số điểm khác biệt. Hàm sort() là một method của kiểu dữ liệu list trong python. Có 1 số điểm cần lưu ý

# Hàm sort() vẫn nhận thêm từ khóa key và reverse như hàm sorted
# Hàm sort() không phải là method của tuple và set, nên đối tượng thuộc kiểu này sẽ không gọi được nó
# # Hàm sort() không trả về một list mới được sắp xếp, mà thay đổi ngay tại chỗ đối tượng list đã gọi nó. Vì vậy bạn không nên gán kết quả trả về của list.sort() vào 1 biến vì giá trị của biến đó sẽ là None.

# multidimensional_array = [[1, 3], [4,0], [2,1], [7,3], [9,9]]
# multidimensional_array.sort(reverse=True, key=lambda x:x[1])
# print(multidimensional_array)             # [[9, 9], [1, 3], [7, 3], [2, 1], [4, 0]]

# ----------------------------------- Filter --------------------------------------------
# Là hàm trả về tập hợp các phần tử được lọc theo 1 điều kiện nào đó ( hàm điều kiện )
# filter( <function> , <iterable>)
# friend = [("Phuc",18),("Tuan",20),("Thinh",23)]
# DK_Loc = lambda data : data[1] <= 18

# ds_loc = list(filter(DK_Loc,friend))
# print(ds_loc)

# ----------------------------------- Map -----------------------------------------------
# Là hàm nhận vào các bộ giá trị trong list, set, .... và trả về các bộ giá trị dựa trên giá trị trả về của hàm function
# Cấu trúc: map( function, iterable) 

# friend = [("Phuc",18),("Tuan",20),("Thinh",23)]
# DK_Loc = lambda data : data[0]+" "+str(data[1])

# ds_loc = list(map(DK_Loc,friend))

# print(ds_loc)        # ['Phuc 18', 'Tuan 20', 'Thinh 23']

#----------------------------------- List Comprehension ------------------------------------
# Là cách để tạo 1 list danh hơn bằng việc kết hợp với vòng for và điều kiện với các phần tử bên trong for đó 
# Các cấu trúc hay dùng:
# list = [ i trong vòng lặp for ]
# list = [ i trong vòng lặp for + điều kiện if của i ]
# list = [ điều kiện if của i + điều kiện else của i + i trong vòng lặp for]

# list_so_chan = [i if i % 2 == 0 else "FAILUS"  for i in range(1,10)]  # mảng chứa các số i thuộc từ 1 đến 10. Nếu i chia hết cho 2 thì thêm vào mảng, không thì thêm "FAILUS"
# list_so_le = [i for i in range(1,10) if i % 2 != 0]
# print(list_so_chan)
# print(list_so_le)

# list = [1,2,3,4,5,6,7,8,9,10]

# Loc = [i  for i in list if i > 5]          # Thay thế Filter 
# print(Loc)

# --------------------------------- Distionary Comprehension ------------------------------
# Là cách để tạo ra 1 Distionary ( giống map với cặp key - value ) nhanh hơn bằng việc kết hợp với vòng lặp for và điều kiện với các phần tử bên trong for

# dictionary = { key : expression for (key,value) in iterable }
# dictionary = {"Phuc":18,"Tuan":20,"thinh": 21}
# Loc = { key: (value + 20) for (key,value) in dictionary.items()}
# print(Loc)

# dictionary = { key : expression for (key,value) in iterable if conditional }
# dictionary = {"Phuc":18,"Tuan":20,"thinh": 21}
# Loc = { key: value for (key,value) in dictionary.items() if value >19 }
# print(Loc)

# dictionary = { key : (if/else) for (key,value) in iterabl }
# dictionary = {"Phuc":18,"Tuan":20,"thinh": 21}
# Loc = { key: (value if value > 18 else "Not") for (key,value) in dictionary.items() }
# print(Loc)

# def Check_old(old : int):
#        if old > 18:
#               return old
#        return "Not"
# dictionary = {"Phuc":18,"Tuan":20,"thinh": 21}
# Loc = { key: (Check_old(value)) for (key,value) in dictionary.items() }
# print(Loc)

# ----------------------------------- if __name__ == "__main__" ---------------------------
# Được dùng để phân biệt các file được import vào file chính và file chính (main)

# Do trong pyhon không có hàm main (hàm nhận biết để thực thi chương trình) như các ngôn ngữ lập trình khác nên khi thực hiện các dự án lớn gồm có 1 file chính  và các file nhỏ dùng để bổ xung file chính. Do trong pyhton chỉ cần vào 1 file bấm run thì nó sẽ chạy mà không biết file nào là file chính file nào file con nên dễ dẫn đến lỗi
# VD:
       # file A:
              # def Hi():
                     # print("Day là file A")
              
              # Hi()
       
       # file B:
              # def Hi():
                     # print("Day la file B")
       
              # Hi()
       # file C ( file chính) (gồm 2 file con A và B được import vào):
              # import A
              # import B
              
              # print("Day la file chinh")
              
       
       # Khi ta vào file A biên dịch --> Nó chạy hàm Hi()
       # Khi ta vào file B biên dịch --> Nó chạy hàm Hi()
       # Khi ta vào file C( file chính) biên dịch --> Nó chạy hàm Hi() trong cả hi file con A và B và hàm print của riêng nó
       
       # Vậy khi ta chỉ muốn chạy hàm print("Day là file chinh") mà bỏ qua 2 file A và B thì ta làm các nào :
       
       # file A.py:
              # def Hi():
                     # print("Day là file A")
              
              # Hi()
       
       # file B.py:
              # def Hi():
                     # print("Day la file B")
       
              # Hi()
       # file C.py ( file chính) (gồm 2 file con A và B được import vào):
              # import A
              # import B
              
              # if __name__ == "__main__":
                     # print("Day la file chinh")
       
       # Khi ta chạy file C thì file C được mặc định __name__ = "__main__" 
       # file A thì __name__ = "__A__"
       # file B thì __name__ = "__B__"
       
# Tóm lại: if __name__ == "__main__": xem như là hàm main được ta quy định file đó sẽ chạy những gì 

# --------------------------------------------- Time -------------------------------------------
# xu ly cac tac vu lien quan den thoi gian
# import time                        # modul time       

# Hàm time() trả về số giây tính từ epoch, hay còn gọi là giá trị timestamp. Đối với hệ thống Unix, 00:00:00 ngày 1/1/1970 theo giờ UTC được gọi là epoch (thời điểm bắt đầu thời gian).
# print("So giay tinh tu epoch: "+str(time.time()))

# time.ctime(). Phương thức này chuyển đổi một time được biểu diễn bằng số giây tính từ epoch thành một biểu diễn ở dạng chuỗi.
# second = time.time()
# print("Doi ra ngay thang nam: "+time.ctime(second))            # đổi ra ngày tháng năm dựa vào số giây truyền vào, nếu không truyền vào thì nó sẽ trả về thời gian hệ thống

# time.sleep(). Hàm sleep() dừng thực thi luồng hiện tại trong số giây truyền vào.
# print ("Start :", time.ctime())
# time.sleep(3)
# print ("End :", time.ctime())

# ----------------------------------------- Thread --------------------------------------------
# Tạo ra các luồng chạy song song với luồng chính

# import threading
# import time

# def Day( name : str):
#        time.sleep(3)
#        print(name + " da day")

# def An( name : str):
#        time.sleep(4)
#        print(name+" da an")
       
# def DiHoc(name : str):
#        time.sleep(5)
#        print(name+ " di hoc")

# # Day()
# # An()
# # DiHoc()

# a = threading.Thread(target=Day,args= ("APU", ))        # argv : tham so truyen vao neu co, " Lưu ý phải có dấu phẩy" 
# b = threading.Thread(target=An,args=("APU", ))
# c = threading.Thread(target=DiHoc,args=("APU", ))
# a.start()
# b.start()
# c.start()

# print(threading.active_count())    # dem so luong dang haot dong
# print(threading.enumerate())       # thong tin cac luong 

# Join thread: Do trong quá trình chạy, các thread có thể tranh dành lẫn nhau chạy hoặc thread này kết thúc trước thread kia dẫn đến sai xót. 
# Phương thức join() dùng để thông báo là luồng được chỉ định được chạy từ đầu đến cuối không thread nào có thể ngắn cản và các thread khác phải đợi khi nó kết thúc mới được làm tiếp 
# from threading import Thread
# import time

# def HamA():
       
#        for i in range(0,10):
#               time.sleep(1)
#               print("Dang o ham A")
              
# def HamB():
#        for i in range(0,10):
#               time.sleep(1)
#               print("Dang o ham B")
              
# Luong_1 = Thread(target=HamA)
# Luong_2 = Thread(target=HamB)

# Luong_1.start()
# Luong_1.join()              # các luồng khác phải đợi luồng 1 chạy xong và không được tranh giành với nó trong quá trình chạy 

# Luong_2.start()
# Luong_2.join()

# ------------------------------------------ Deamon Thread --------------------------------------
# Luồng hiểm: là luồng sẽ bị buộc kết thúc ( dù xong hay chưa ) khi các luồng khác hoàn thành xong tác vụ của mình
# VD :
       # Luồng 1: in các số từ 1 đến 5
       # Luồng 2 (Luồng hiểm): in các số từ 1 đến 10 
       # Do luồng 2 là Luồng Hiểm nên dù nó hoàn thành xong hay chưa việc in của nó thì khi luồng 1 in xong 5 số thì luồng 2 sẽ bị bắt buộc kết thúc 
# import threading
# import time

# def Luong1():
#        for i in range(1,6):
#               time.sleep(1)
#               print ("Luong 1: "+str(i))

# def Luong2():
#        for i in range(1,11):
#               time.sleep(1)
#               print ("Luong 2: "+str(i))

# Luong_1 = threading.Thread(target=Luong1)
# Luong_2 = threading.Thread(target=Luong2,daemon=True)          # set up luong hiem 

# Luong_1.start()
# Luong_2.start()
       
# --------------------------------------------- Multi Processing --------------------------------
# Đa tiến trình: nhiều tiến trình cùng thực hiện nhiều công việc khác nhau
# Lưu ý: phần biệt giữa đa tiến trình và đa luồng:
       # Một tiến trình có thể có nhiều luồng thực hiện nhiều công việc của tiến trình đó ( tiến trình chứa các luồng)
       # Mỗi tiến trình được thực hiện trên các vùng nhớ khác nhau nên không thể chia sẻ tài nguyên với nhau, còn các luồng thì thực hiện cùng trên cùng một vùng nhớ nơi tiến trình chứa nó được phân bố. 
# import multiprocessing             # khai bao
# import time

# def square(numbers):
#        time.sleep(10)
#        print("Dang tinh hinh vuong!!")
#        for i in numbers:
#               time.sleep(1)
#               print("square: " ,i*i)

# def cube(numbers):
#        time.sleep(10)
#        print("Dang tinh hinh lap phuong !!")
#        for i in numbers:
#               print("cube: " ,i*i*i)

# if __name__ == "__main__":
#        arr = [1,2,3,4,5]
#        process_1 = multiprocessing.Process(target=square,args = (arr,))
#        process_2 = multiprocessing.Process(target=cube,args = (arr,))
       
#        process_1.start()
#        process_2.start()
       
#        process_1.join()
#        process_2.join()

# ---------------------------------------- Timer ---------------------------------------
# Là luồng sẽ được thực thi sau 1 khoảng thời gian interval nhất định 
# import threading

# def HI():
#        print("Hello")
       
# Timer_1 = threading.Timer(interval=1,function=HI)
# Timer_1.start()

# ------------------------------------- Đồng bộ hóa - Lock -------------------------------
# import threading
# import time


# class TaiKhoan:
#        name = None
#        Money = None
#        def __init__(self,name,Money) -> None:
#               self.name = name
#               self.Money = Money
       
#        def getMoney(self):
#               return self.Money
       
#        def setMoney(self,Money):
#               self.Money = Money


# def RutTien( taikhoan : TaiKhoan, so_lan_rut : int, soTien : int, stt_luong : int):
#        Khoa_luong.acquire()               # khóa khi có luồng vào
       
#        for i in range(0,so_lan_rut):
#               time.sleep(2)
#               if(taikhoan.getMoney() >= soTien):
#                      Money_Con_lai = taikhoan.getMoney() - soTien
#                      taikhoan.setMoney(Money=Money_Con_lai)
#                      print("Luong "+str(stt_luong)+" rut lan " + str(i))
#                      print("Luong "+str(stt_luong)+": So tien con lai: "+ str(taikhoan.getMoney()))
#               else:
#                      print("Tai khoan khong du tien de rut!!")
       
#        Khoa_luong.release()              # mở khóa khi luồng đó đi ra 

# if __name__ == "__main__":
#        Khoa_luong = threading.Lock()             # Tạo một lock để khóa tài nguyên dùng chung khi có 1 luồng đi vào 
       
#        Man_A = TaiKhoan("APU",100)
       
#        Luong_1 = threading.Thread(target=RutTien,args=(Man_A,5,20,1,))
#        Luong_2 = threading.Thread(target=RutTien,args=(Man_A,5,20,2,))
       
#        Luong_1.start()
#        Luong_2.start()
       
#        Luong_1.join()
#        Luong_2.join()
       


       
       
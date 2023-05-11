#-------------------------------- Object Oriented Programing--------------------------------
# Các tính chất trong python giống bên java (4 tính chất): polymorphism, inheritance, abstration, encapsulation

# class hello :
#        name = None
#        nick_name = None
       
#        def __init__(self,name,nickname) :    # self : Giống như con trỏ this trong java, nhưng khác là phải truyền vào để class biết, nó ko cần giá trị truyền vào 
#               self.name = name
#               self.nick_name = nickname
       
#        def xinchao(self):
              
#               print("Hello "+ self.name + self.nick_name)



# a = hello("Phuc","Apu")
# hello(name="Phuc",nickname="Apu").xinchao()
# a.xinchao()

# ---------------------------------- Variables ----------------------------------------------
# Cũng giống như các ngôn ngữ khác, có 3 kiểu biến : Local (biến được tạo ra bên trong các method nằm trong class) , instance và static . Tuy nhiên biến instance và static trong python giống nhau về cách khai báo vì mọi biến được khai báo trong class (ngoài các biến local) thì nó đều là biến thể hiện của class đó, có nghĩa là có thể gọi thông qua tên class chứ không cần tạo đối tượng của class đó mới gọi được 

# Về phạm vi truy cập thì chỉ có public và private, cũng có protected nhưng về ý nghĩa trong python nó giống public 

# class hello:
#        name = None                        # đây là biến instance (static) ở dạng public
#        nick_name = None                   # đây là biến instance (static) ở dạng public
       
#        _Tuoi = 20     # đây là biến instance (static) ở dạng protected (bằng cách thêm dấu _ trước tên biến), tuy là protected nhưng vẫn có thể truy cập được như public 
#        __Lop = 12     # đây là biến instance (static) ở dạng priavte (bằng cách thêm dấu __ trước tên biến), vì là private nên nó không thể bị truy cập từ bên ngoài class vào 
#        def __init__(self,name,nick_name) :
#               self.name = name
#               self.nick_name = nick_name
       
#        def __HamPrivate():                # method private
#               pass
       
#        def XinChao(self):
#               print("Hello "+ self.name + self.nick_name+" "+str(self.__Lop))



# studen1 = hello(name="Phuc",nick_name="Apu")
# # print(studen1.__Lop )            # 'hello' object has no attribute '__Lop'
# # studen1.__HamPrivate()           # hello' object has no attribute '__HamPrivate'
# studen1.__Lop = 2                  # Tuy có thể làm vậy nhưng giá trị bên trong nó sẽ không bị thay đổi  

# studen1.XinChao()

#------------------------------------- Inheritance ---------------------------------------------
# Gồm có 5 loại kế thừa (như bên java): đơn kế thừa, đa kế thừa , kế thừa đa cấp, kế thừa phân cấp và kế thừa lai( gồm các kế thừa trên cộng lại )
# Cấu trúc: class <con> ( <cha1> , <cha2>, .... ):

# Đơn kế thừa (lớp con kế thừa từ 1 lớp cha):
# class Animal:
       
#        def Eat(self):
#               print("Dang an")
#        def Sleep(self):
#               print("Zzzzz")

# class Dog(Animal):
#        def Sound(self):
#               print("Gau Gau")
              
# dog1 = Dog()
# dog1.Eat()                # Thừa hưởng từ Animal
# dog1.Sleep()              # Thừa hưởng từ Animal
# dog1.Sound() 

# Đa kế thừa (Lớp con kế thừa từ nhiều lớp cha):
# class Father:
#        def Football(self):
#               print("Da bong rat hay")
# class Mom:
#        def Golf(self):
#               print("Choi golf rat hay")

# class Son(Father,Mom):
#        def Basketball(self):
#               print("Choi bong ro rat hay")

# Son1 = Son()


# Son1.Basketball()
# Son1.Football()             # Thừa hưởng từ Father
# Son1.Golf()                 # Thừa hưởng từ Mom

# Kế thừa phân cấp ( lớp cha có nhiều lớp con ):
# class Animal:
       
#        def Eat(self):
#               print("Dang an")
#        def Sleep(self):
#               print("Zzzzz")

#  # Có 3 lớp con : Dog, Cat, Mouse 
# class Dog(Animal):
#        def Sound_dog(self):
#               print("Gau Gau")
# class Cat(Animal):
#        def Sound_cat(self):
#               print("Meow Moew")
# class Mouse(Animal):
#        def Sound_mouse(self):
#               print("Chit Chit")

# Kế thừa đa cấp (lớp cha này là con của lớp cha khác):
# class GrandFather:
#        def finger(self):
#               print("Co ngon tay di dang")
# class Father(GrandFather):
#        def Foot(self):
#               print("Co ban chan di dang")
# class Son(Father):
#        def Hello(self):
#               print("Toi la con")
              
# Son1 = Son()
# Father1 = Father()

# Father1.finger()            # Thừa hưởng từ GrandFather
# Father1.Foot()              # Dị dạng riêng của bố

# Son1.Foot()                 # Thừa hưởng từ Father
# Son1.finger()               # Thừa hưởng từ GrandFather
# Son1.Hello()                

#---------------------------------- Self -------------------------------------------------
# Đặt vấn đề :
# class Test:
       
#        def Hello(name):                       # Không truyền biến self
#               print("XIN CHAO "+str(name))

# test1 = Test()
# test2 = Test()
# Test.Hello("Test 0")        # Gọi trực tiếp thông qua tên class 

# test1.Hello("test 1")       # TypeError: Test.Hello() takes 1 positional argument but 2 were given       
# test2.Hello("test 2")       # TypeError: Test.Hello() takes 1 positional argument but 2 were given

# Dịch nôm na là Hàm Hello() chỉ nhận 1 đối số nhưng có tận 2 đối số chuyền vào, nhưng rõ ràng ta chỉ truyền vào giá trị của đối số name thôi, đâu có truyền giá trị nào khác nữa đâu 

# --> tham số còn lại chính là đối tượng thể hiện của lớp đó (tham số self) ( với giá trị là đối tượng test1 ), được truyền tự động một cách ngầm định nhưng lại không được nhận ngầm định bởi các hàm trong class 

# Do các biến được tạo trong class được xem như các biến static của class đó (vì có thể truy cập thông qua tên class ) nên cần phải truyền đối tượng được tạo ra từ lớp đó ( VD : test 1, test 2) để lớp đó biết là đối tượng nào để lấy giá trị tương ứng, việc truyền này sẽ được truyền một cách tự động khi ta tạo đối tượng của class và gọi đến các phương thức trong class đó 

# Còn nếu ta gọi phương thức đó trực tiếp thông qua tên class mà không cần tạo đối tượng --> không có đối tượng truyền vào --> chương trình sẽ không báo lỗi 

# VÌ VẬY KHI TA TẠO 1 METHOD TRONG CLASS CẦN PHẢI THÊM THAM SỐ SELF ĐỂ TRÁNH LỖI KHI ĐỐI TƯỢNG THỂ HIỆN CỦA LỚP ĐÓ TRUY CẬP ĐẾN CÁC METHOD TRONG LỚP ĐÓ 

# Ngoài ra tham số self hoạt động giống như từ khóa this trong java, nó có thể được dùng để gọi các biến instance bên trong class và các method bên trong class 

# class Test:
#        name = None
#        def __init__(self,name) :
#               self.name = name                   # DÙng để gọi biến instance
       
#        def Hello(self):                       
#               print("XIN CHAO "+str(self.name))  
              
#        def Hi(self):
#               self.Hello()                       # DÙng để gọi method 
              

# test = Test("Phuc")
# test.Hello()
# test.Hi()

# Ngoài ra chúng ta có thể gọi liên tục các method trên 1 dòng bằng cách sao:

# class Test:
#        def Hi(self):
#               print("Hi")
#               return self      # như đã nói ở trên, self nhận giá trị là đối tượng thể hiện của lớp đó, trả về self là tra về đối tượng được truyền vào
       
#        def Hello(self):
#               print("Hello")
#               return self
       
#        def XinChao(self):
#               print("Xin chao")
#               return self
       
# test = Test()
# test.Hello().Hi().XinChao()       # Khi gọi method Hello(), đầu tiên chương trình sẽ tự truyền giá trị cho tham số self là đối tượng test vào method Hello(). Trong hàm Hello(), dòng đầu in ra "Hello", dòng 2 trả lại self chính là đối tượng test rồi đối tượng đó lại tiếp tục gọi method Hi() và được truyền vào hàm Hi()

# -------------------------------------------- Overiding -------------------------------------------------
# Giống bên java, khi lớp con muốn định nghĩa lại 1 method đã có ở lớp cha 
# Chú ý ghi đè trong py : phương thức ghi đè phải giống tên,cùng số lượng tham số và cùng liểu dữ liệu tra về. Do không có kiểu dữ liệu xác định nên không cần cùng kiểu dữ liệu truyền vào 
# class Farther:
#        def CongViec(self):
#               print("Dang lam cong nhan")

              
# class Son(Farther):
#        def CongViec1(self):                       # định nghĩa lại method CongViec() ở lớp cha 
#               print("Dang di hoc")
#               return 1                           # có thể khác nhau về kiểu dữ liệu trả về 
              
# son = Son()
# print(son.CongViec())

# --------------------------------------------- OverLoading ----------------------------------------------
# là các phương thức nằm trong cùng 1 class, cùng tên , khác nhau về số lượng tham số, về kiểu dữ liệu tham số truyền vào và dữ liệu tra về 
# class Farther:
#        def CongViec(self):
#               print("Dang lam cong nhan")

#        def CongViec(self,hientrang : bool):
#               if(hientrang == False):
#                      print("That nghiep")
       
# father = Farther()
# father.CongViec(hientrang=False)

# --------------------------------------------- Hàm siêu khởi tạo - super() -----------------------------------------
# Ý nghĩa giống bên java 
# class Animal:
#        name = None
#        old = None
#        def __init__(self,name : str, old : int):
#               self.name = name
#               self.old = int(old)
       
#        def get_name(self):
#               return self.name
       
#        def get_old(self):
#               return self.old

# class Dog(Animal):
#        skin = None
#        # Hàm siêu khởi tạo
#        def __init__(self, name: str, old: int,skin):
#               super().__init__(name, old)
#               self.skin = skin
#        def Hello(self):
#               print("Xin chao tui la cho, tui ten "+super().get_name()+" tui "+str(super().get_old())+" tuoi, tui co bo long mau "+self.skin)
       
# dog  = Dog(name="Apu",old=2,skin="vang")
# dog.Hello()

#-------------------------------------------- Abstraction ------------------------------------------------
# Về ý nghĩa nó giống bên java, là việc tổng quát hóa vấn đề nào đó lên (ở lớp cha). Các lớp con khi kế thừa lại lớp cha thì phải triển khai chi tiết vấn đề trừu tượng đó
# abstract method: là method không có phần thân hàm, việc triển khai sẽ do các lớp con đảm nhận. Trong pyhton có thể triển khai thân hàm của phương thức ảo nhưng dường như việc đó không có ý nghĩa
# abstract class: đươch dùng để chứa nhiều hoặc ít nhất 1 abstract method và không thể khởi tạo đối tượng. Trong py, một abstract class có thể khởi tạo đối tượng khi  abstract class đó không chứa bất kỳ method ảo nào  

#  Cấu trúc khai báo class abstract và method abstract: 
# from abc import ABC,abstractclassmethod          # phải import 

# class Animal(ABC):                               # Khai báo class ảo 
#        @abstractclassmethod                      # Khai báo phương thức ảo 
#        def Eat(self):
#               pass
              
#        def Drink(self):
#               print("Uong nuoc")

# class Dog(Animal):
#        def Eat(self):                            # Phải định nghĩa lại phương thức ảo đó, nếu không sẽ báo lỗi 
#               print("dang uong nuoc")

# dog = Dog()
# dog.Eat()

# Một class abstract có thể tạo đối tượng nếu không chứa bất kỳ method abstract nào bên trong nó:
# from abc import ABC,abstractclassmethod
# class Animal(ABC):
#        def Drink(self):
#               print("Uong nuoc")

# animal = Animal()
# animal.Drink()

# ---------------------------------------- Truyền Object vào hàm -----------------------------------------

# class Animal:
#        name = None
       
# def Hello(Animal : Animal,name):
#        Animal.name = name
       
       
# animal = Animal()
# Hello(Animal=animal,name="phuc") 

# print(animal.name)


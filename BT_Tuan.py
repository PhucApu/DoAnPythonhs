# import thư viện sympy
import sympy as sp

# khai báo biến x là biến ký hiệu
x = sp.Symbol('x')

# nhập vào bậc đa thức
n = int(input("Nhập vào bậc đa thức: "))

# khởi tạo đa thức F(x) bằng 0
F = 0

# lặp từ n đến 0
for i in range(n, -1, -1):
    # nhập vào hệ số An-i
    An_i = float(input(f"Nhập vào hệ số An-{i}: "))# cộng vào đa thức F(x) với An-i*x**i
    F += An_i*x**i

# in ra đa thức F(x)
print("Đa thức F(x) là:", F)

H = sp.integrate(F, x)

# in ra kết quả
print("Nguyên hàm của F(x) là:", H)

# nhập vào giá trị x
x_value = float(input("Nhập vào giá trị x: "))

# tính giá trị F(x) tại x_value
F_value = F.evalf(subs={x: x_value})

# in ra kết quả
print("Giá trị F(x) tại", x_value, "là:", F_value)

# nhập vào đa thức G(x)
G_str = input("Nhập vào đa thức G(x): ")

# chuyển chuỗi thành biểu thức
# G = sp.sympify(G_str)
G=0

for i in range(G_str, -1, -1):
    # nhập vào hệ số An-i
    An_i = float(input(f"Nhập vào hệ số An-{i}: "))# cộng vào đa thức F(x) với An-i*x**i
    G += An_i*x**i

# tìm hiệu hai đa thức F(x) - G(x)
G1 = sp.integrate(G, x)

# in ra kết quả
print("Nguyên hàm của F(x) là:", G1)

T = H - G1


# in ra kết quả
print("Hiệu hai đa thức F(x) - G(x) là:", T)
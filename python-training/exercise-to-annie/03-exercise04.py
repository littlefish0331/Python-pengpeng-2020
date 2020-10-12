# 請示範 A 除以 B = C 餘 D。
print("以下示範除法: A 除以 B = C 餘 D")
A=input("輸入A: ")
B=input("輸入B: ")

C=int(A)//int(B)
D=int(A)%int(B)
print(A," 除以 ", B ," = ", C, " 餘 ", D)

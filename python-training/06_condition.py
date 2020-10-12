# 判斷式
if True:
    print("this is True - 01")

if False:
    print("this is False - 02")

if True:
    print("this is True - 03")
else:
    print("this is else - 04")

if False:
    print("this is False - 05")
else:
    print("this is else - 06")

# 輸入資訊
x=input("請輸入數字: ") # 基本輸入為字串型態。取得字串形式的訊息。
print(x) #可能看不出來有是字串
x=int(x) # 轉換字串為整數型態
print(x)

# 範例01
x=input("請輸入數字: ")
x=int(x)
if x>100:
    print("大於 100")
else:
    print("小於等於 100")

# 範例02
x=input("請輸入數字: ")
x=int(x)
if x>200:
    print("大於 200")
elif x>100:
    print("大於 100，小於200")
else:
    print("小於 100")

# ---
# 四則運算
n1=int(input("請輸入數字一: "))
n2=int(input("請輸入數字二: "))
op=input("請輸入運算(+, -, *, /): ")
if op=="+":
    print(n1+n2)
elif op=="-":
    print(n1-n2)
elif op=="*":
    print(n1*n2)
elif op=="/":
    print(n1/n2)
else:
  print("不支援的運算")

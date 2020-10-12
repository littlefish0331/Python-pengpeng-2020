# 定義函式
# 只是定義，如果沒有被呼叫就不會執行。
# 函式內部的程式碼，或是沒有做函式呼叫，就不會執行。
def multiply():
    print(3*4)

# 呼叫函式
multiply()
multiply()

# ---
def multiply(n1,n2):
    print(n1*n2)

multiply(3,4)
multiply(10,8)

# ---
# 函式跳回來要看回傳值
def multiply(n1,n2):
    print(n1*n2)

value=multiply(3,4)
print(value) # None

# ---
def multiply(n1,n2):
    print(n1*n2)
    return

value=multiply(3,4)
print(value) # None

# ---
def multiply(n1,n2):
    print(n1*n2)
    return 10

value=multiply(3,4)
print(value) # None

# ---
def multiply(n1,n2):
    print(n1*n2)
    return n1*n2

value=multiply(3,4)
print(value) # None

# ---
# 程式有含是外部操作資料的需求，就會用回傳值。
def multiply(n1,n2):
    return n1*n2

value=multiply(3,4)+multiply(5,10) # (3*4)+(5*10)
print(value) # None


# 函式最大的用途: 程式的包裝
# 函式可以用來做程式的包裝，同樣的邏輯可以重複利用!!
sum=0
for n in range(1,11):
    sum=sum+n
print(sum)

def calculate(max):
    sum=0
    for n in range(1,max+1):
        sum=sum+n
    print(sum)

calculate(10)
calculate(20)


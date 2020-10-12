# 數字運算
x=3+6
print(x)

x=3-6
print(x)

x=3*6
print(x)

x=3/6 # 小數除法
print(x)

x=3//6 # 整數除法
print(x)

x=2**3
print(x)

x=2**0.5
print(x)

x=7%3 # 取餘數
print(x)

# ---
x=2+3
print(x)
x+=1 # x=x+1 # 將變數中的數字 + 1
print(x)
x-=3
print(x)
x*=2
print(x)

# ---
# 字串運算
s="Hello"
print(s)

s='Hello'
print(s)

s="Hell\"o" # 這個反斜線叫做跳脫符號。
print(s)

# 字串的串接
# "+"可以做為字串的串接；" "(空白)也可以是字串的串接。
s="Hello"+"World"
print(s)

s="Hello" "World"
print(s)

# 多行文字
# 可用三個雙引號，也可用三個單引號。
s="Hello\nWorld"
print(s)

s="""Hello
這邊也會換行
World"""
print(s)

# 重複字串
s="Hello"*3+"World"
print(s)

# 字串對內部的字元編號(索引)，從 0 開始算起
s="Hello"
print(s)
print(s[0])
print(s[1])
print(s[2])
print(s[1:4]) # 取得子字串。編號包含開頭，不包含結尾。
print(s[1:])
print(s[:3])

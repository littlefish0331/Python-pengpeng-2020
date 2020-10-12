# 輸入英文數字和想要擷取的起點與終點

'''
比如
- 輸入: Beautiful
- start(正整數 or 0): 3
- end(正整數 or 0):8

輸出: utiful
'''

s=input("輸入一個英文字: ")
n1=int(input("start: "))
n2=int(input("end: "))

print(s[n1:n2+1])

# break 的簡易範例
n=0
while n<5:
    if n==3:
        break
    print(n) # 印出迴圈中的 n
    n=n+1
print("最後的 n:", n) # 印出迴圈結束後的 n

# ---
# continue 的簡易範例
n=0
for x in [0,1,2,3]:
    if x%2==0: # x 是偶數
        continue
    print(x)
    n=n+1
print("最後的 x:", x) # 印出迴圈結束後的 n
print("最後的 n:", n) # 印出迴圈結束後的 n


# ---
# else 的簡易範例
sum=0
for n in range(11):
    # sum=sum+x
    sum+=n
else:
    print(sum) # 印出 0+1+2+3+...+10 的結果。


# ---
# 綜合範例: 找出整數平方根
# 輸入9，得到3
# 輸入11，得到[沒有]整數的平方根

op=input("請輸入一個正整數: ")
x=int(op)**0.5
if x%1==0:
    print(x)
else:
    print(op ,"[沒有]整數的平方根")

# ---
# 彭彭的寫法
n=input("請輸入一個正整數: ")
n=int(n)
for i in range(n): # i 從 0 ~ n-1
    if i*i==n:
        print("整數平方根", i)
        break # 用 break 強制結束時，不會執行 else 區塊。
else:
    print("沒有整數平方根")


# while 迴圈

# 無窮迴圈
# n=1
# while True: 
#     print(n)
#     n=n+1

n=1
while n<=3: 
    print(n)
    n=n+1

# 1+2+3+...+10
n=1
sum=0 # 紀錄累加的結果
while n<=10: 
    sum=sum+n
    n=n+1
print(sum)


# ---
# for 迴圈
for x in [3,5,1]:
    print(x)

for x in "Hello":
    print(x)

for x in range(5):
    print(x)

for x in range(5,10):
    print(x)
# 5,6,7,8,9

# 1+2+3+...+10
sum=0
for x in range(1,11):
    sum=sum+x
print(sum)

# 1+2+3+...+10
sum=0
for x in range(11):
    sum=sum+x
print(sum)

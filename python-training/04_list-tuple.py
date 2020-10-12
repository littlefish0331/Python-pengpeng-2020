# 有序可變動列表 List
grades=[12,60,15,70,90]
print(grades) # [12, 60, 15, 70, 90]
print(grades[0]) # 12
grades[0]=55 # 把 55 放到列表中的第一個位置。
print(grades[0]) # 55
print(grades[1:4]) # [60,15,70]

# 刪除列表元素
grades=[12,60,15,70,90]
grades[1:4]=[] # 連續刪除列表中編號 1 到編號 4(不包含)的資料
print(grades) # [12,90]

# 列表串接
grades=grades+[12,33] # 看到等號先看等號的右邊。
print(grades) # [12,90,12,33]

length=len(grades) # 取的列表長度 len(列表資料)
print(length) 

# 巢狀列表
data=[[3,4,5],[6,7,8]]
print(data[0][0])
print(data[0][1])
print(data[0]) # [3, 4, 5]
print(data[0][0:2]) # [3, 4]

print(data)
data[0][0:2]=[5,5,5] # 可以取代比原本數量還多的元素
print(data) # [[5, 5, 5, 5], [6, 7, 8]]



# ---
# 有序不可變動列表 Tuple
data=(3,4,5)
print(data[2])
print(data[0:2])

# data[0]=5 # 錯誤: Tuple 的資料不可變動
# print(data)

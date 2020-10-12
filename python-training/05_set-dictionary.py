# 集合的運算
s1={3,4,5}
print(3 in s1)
print(10 in s1)
print(10 not in s1)

# 集合有無在集合中
print({3,4} not in s1) # True
print({3,5} not in s1) # True
# print([3,4] not in s1) # Error

# 集合 - 交集、聯集、差集、反交集
s1={3,4,5}
s2={4,5,6,7}
s3=s1&s2 # 交集: 取兩個集合中，相同的元素。
print(s3)

s3=s1|s2 # 聯集: 取兩個集合中的所有資料，但不重複取。
print(s3)

s3=s1-s2 # 差集: 從 s1 中，減去和 s2 重疊的部分。
print(s3)

s3=s1^s2 # 反交集: 取兩個集合中，不重疊的部分。
print(s3)

# 從字串建立集合
# - 拆出每個字母且不會顯示重複的
# - 拆出的結果是集合，所以沒有順序性的問題。
s=set("Hello") # 打字串的字母拆解成集合: set(字串)
print(s)
print("H" in s)
print("A" in s)


# ---
# 字典的運算: key-value 配對
dict={"apple":"蘋果", "bug":"蟲蟲"}
print(dict["apple"])
dict["apple"]="小蘋果"
print(dict["apple"])

# 對 dict 用 in 和 not in 是在判斷 key 是否存在。
dict={"apple":"蘋果", "bug":"蟲蟲"}
print("apple" in dict) # 判斷 key 是否存在。
print("test" in dict)
print("test" not in dict)

# 刪除鍵值對
# 以 key 為代表，但是刪除整個鍵值對。
dict={"apple":"蘋果", "bug":"蟲蟲"}
print(dict)
del dict["apple"] # 刪除字典中的鍵值對 (key-value pair)
print(dict)

# 列表的資料當作基礎，當作字典
# dict={x:x*2 for x in 列表}
dict={x:x*2 for x in [3,4,5]}
print(dict)
list=["佑","愛","涵"]
dict={x:x*2 for x in list}
print(dict)

# 測試區
x=["佑","愛","涵"]
print(x)
x=["佑","愛","涵",1]
print(x)


def func(a, b):
    s=100
    if a>b:
        t=a
        a=b
        b=t
    for i in range(0, a):
        for j in range(i, b):
            s=s-j
    return(s)

ans=func(7,4)
print(ans)










# def func(a, b):
#     s=0
#     if a>b:
#         t=a
#         a=b
#         b=t
#         # print("this is a:", a, "this is b:", b)
#     for i in range(0, a):
#         for j in range(i, b):
#             s=s+j
#         # print("this is s now:", s)
#     return(s)

# ans=func(7,4)
# print(ans)

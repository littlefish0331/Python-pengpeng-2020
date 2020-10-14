# def R(x,y,s):
#     t=int((x+y)/2)
#     s=s+t
#     if x<y:
#         if 5 >= t:
#             R(t,y,s)
#         else:
#             R(x,y-5,s)
#     else:
#         print(s) 
           
# ans=R(3,17,0)
# print(ans)





def R(x,y,s):
    print("我進來 R-function 了!!")
    t=int((x+y)/2)
    s=s+t
    if x<y:
        if 5 >= t:
            print("A: (x,y,s,t)", x,y,s,t)
            R(t,y,s)
        else:
            print("B: (x,y,s,t)", x,y,s,t)
            R(x,y-5,s)
    else:
        print(s)    
ans=R(3,17,0)
print(ans)

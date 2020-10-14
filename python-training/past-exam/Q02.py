count = 12

if count > 10:
    count = 11
    print("A")
elif count < 12:
    count = 10
    print("B")
    if count %10 ==0:
        count = 13
    else:
        count = 14


if count == 11:
    count = 10
    print("C")
elif count == 13:
    count = 14
    print("D")


if count %10 ==4:
    count = 13
    print("E")
elif count > 13:
    count = 12
    print("F")

print(count)


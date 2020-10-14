a = 100

def fn():
    global a
    a = 1

print(a)
fn()
print(a)

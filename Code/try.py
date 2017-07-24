#异常处理

try:
    for i in range(0,10):
        print(i)
        if(i==4):
            print(ijk)
    print('hello')
except Exception as err:
    print(err)


for i in range(0,10):
    try:
        print(i)
        if(i==4):
            print(ijk)
    except Exception as err:
        print(err)
print('hello')
    

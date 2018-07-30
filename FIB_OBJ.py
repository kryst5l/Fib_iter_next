#斐波那契数列

def Fib(max):
    n,a,b=0,0,1
    while n < max:
        yield b
        a,b=b,a+b
        n=n+1
    return "没有数据了"



#调用方法，生成10个数来
f=Fib(10)
#使用一个循环捕获最后return返回的值，保存异常stopIteration的value中

while True:
    try:
        x=next(f)
        print("f",x)
    except StopIteration as e:
        print("生成器最后的返回值是：",e.value)
        break

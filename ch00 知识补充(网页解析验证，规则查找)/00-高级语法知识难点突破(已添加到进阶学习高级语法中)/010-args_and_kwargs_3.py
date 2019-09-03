# Python中 *args 和 **kwargs 的区别
# *args 表示任何多个无名参数，它是一个tuple；
# **kwargs 表示关键字参数，它是一个dict。
# 并且同时使用*args和**kwargs时，必须*args参数列要在**kwargs前

# python参数使用总结：
# 位置参数：调用函数时所传参数的位置必须与定义函数时参数的位置相同
# 关键字参数：使用关键字参数会指定参数值赋给哪个形参，调用时所传参数的位置可以任意
# *位置参数：可接受任意数量的位置参数(元组)；只能作为最后一个位置参数出现，其后参数均为关键字参数
# ** 关键字参数：可接受任意数量的关键字参数(字典)；只能作为最后一个参数出现
# 默认参数：默认参数的赋值只会在函数定义的时候绑定一次，默认值不会再被修改

def foo(*args, **kwargs):
    # 先解包出包裹位置参数
    print('args = ', args)
    # 再解包出包裹关键字参数
    print('kwargs = ', kwargs)
    print('---------------------------------------')

if __name__ == '__main__':
    foo(1, 2, 3, 4)
    foo(a=1, b=2, c=3)
    foo(1, 2, 3, 4, a=1, b=2, c=3)
    foo('a', 1, None, a=1, b='2', c=3)



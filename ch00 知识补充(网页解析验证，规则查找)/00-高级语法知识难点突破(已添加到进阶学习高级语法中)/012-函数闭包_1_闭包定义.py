# 闭包的定义

# 定义：闭包是由函数及其相关的引用环境组合而成的实体(即：闭包=函数+引用环境)
# 下面这个就是一个简单的闭包函数
def ExFunc(n):
    sum = n
    def InsFunc():
        return sum + 1
    return InsFunc

myFunc_1 = ExFunc(10)
print(myFunc_1())

myFunc_2 = ExFunc(20)
print(myFunc_2())

# 函数InsFunc是函数ExFunc的内嵌函数，并且是ExFunc函数的返回值。
# 我们注意到一个问题：内嵌函数InsFunc中 引用到外层函数中的局部变量sum，
# Python会这么处理这个问题呢？先让我们来看看这段代码的运行结果。
# 当我们调用分别由不同的参数调用ExFunc函数得到的函数时myFunc_1()，myFunc_2()
# 得到的结果是隔离的，也就是说每次调用ExFunc函数后都将生成并保存一个新的局部变量sum。
# 其实这里ExFunc函数返回的就是闭包。

# ExFunc函数只是返回了内嵌函数InsFunc的地址，在执行InsFunc函数时将会由于在其作用域内找不到sum变量而出错。
# 而在函数式语言中，当内嵌函数体内引用到体外的变量时，将会把定义时涉及到的引用环境和函数体打包成一个整体（闭包）返回。
# 现在给出引用环境的定义就 容易理解了：引用环境是指在程序执行中的某个点所有处于活跃状态的约束
# （一个变量的名字和其所代表的对象之间的联系）所组成的集合。闭包的使用和正常的函数调用没有区别。

# 由于闭包把函数和运行时的引用环境打包成为一个新的整体，所以就解决了函数编程中的嵌套所引发的问题。
# 如上述代码段中,当每次调用ExFunc函数 时都将返回一个新的闭包实例，这些实例之间是隔离的，分别包含调用时不同的引用环境现场。
# 不同于函数，闭包在运行时可以有多个实例，不同的引用环境和相同的函数组合可以产生不同的实例。

# python中的闭包从表现形式上定义（解释）为：
# 如果在一个内部函数里，对在外部作用域（但不是在全局作用域）的变量进行引用，
# 那么内部函数就被认为是闭包(closure).比如上面的函数：sum就外部局部变量，InsFunc就是内部函数

# 再看一个例子：
# (外层函数传入一个参数a, 内层函数依旧传入一个参数b, 内层函数使用a和b, 最后返回内层函数)
def outer(a):
    def inner(b):
        return a + b
    return inner

c = outer(8)
res = c(10)

# c是一个函数，outer(8)运行结果返回值是函数inner,
# c指向的是outer.inner,外部局部变量a就是8
# c(10)就是outer.inner(10)(但是函数运行不能这么写，该处只是比喻)，即b是10
print(type(c))
print(c.__name__) #c函数运行的是inner函数

print(type(res))
print(res)
print(outer(8)(10))


# 结合这段简单的代码和定义来说明闭包：
# 如果在一个内部函数里：inner(y)就是这个内部函数，
# 对在外部作用域（但不是在全局作用域）的变量进行引用：
# a就是被引用的变量，a在外部作用域outer函数里面，但不在全局作用域里，
# 则这个内部函数inner就是一个闭包。

# 再稍微讲究一点的解释是，闭包=函数块+定义函数时的环境，
# 内部函数inner就是函数块，a就是环境，当然这个环境可以有很多，不止一个简单的a。


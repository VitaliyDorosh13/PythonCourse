def func():
    print("Im function func()")

print("cat", func, 42)

object = ['cat', func, 42]
object[1]

object[1]()

d = {"cat": 1, func: 2, 42: 3}
d[func]
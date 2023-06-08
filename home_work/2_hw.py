def task_1()->None:
    a: int = 1
    b: float = 1.5
    c: str = 'строка'
    d: list = [1, 2]
    e: bool = True
    print(type(a), type(b), type(c), type(d), type(e))
task_1()

def task_2()->None:
    a = [1, 2, 3, 5, 8, 13, 21]
    print("a[0:3=] =", a[0:3])
task_2()

def task_3(a)->int:
    return a ** 2
print(task_3(2))

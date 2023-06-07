a: int = 5
b: str = "строка"
c: list = [1, 2]

def indent(s: str, width: int) -> str:
    return " " * (max(0, width - len(s))) + s

print(indent("123", 123))

def indent_1(s: str="") -> int:
    return len(s)


def indent_2(a: list, b: list) -> int:
    return max(len(a), len(b))

def indent_3(list = [1, 2]):
    list.append(3)
    return list

def indent_4(list):
    x = 0
    for i in list
        x = x + i


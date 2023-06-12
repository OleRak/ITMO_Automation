class Rectangle:

    def __init__(self, width, height):  # аргумент
        self.width = width  # атрибут
        self.height = height

    def square(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2

a = int(input("Введите ширину прямоугольника :"))
b = int(input("Введите высоту прямоугольника :"))
obj = Rectangle(a, b)

print ("Площадь треугольника: ", obj.square())
print ("Периметр треугольника: ", obj.perimeter())

class Math:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

    def substruction(self):
        return self.a - self.b

c = int(input("Введите первое число:"))
d = int(input("Введите ввторое число :"))
obj = Math(c, d)

print ("Сложение: ", obj.addition())
print ("Умножение: ", obj.multiplication())
print ("Деление: ", obj.division())
print ("Вычитание: ", obj.substruction())

class Elements:

    def __init__(self, loc):
        self.loc = loc

    def click (self):
        return "Клик по кнопке {}".format(self.loc)

Text = Elements("Text Box")
Check = Elements("Check Box")
Radio = Elements("Radio Button")
Web = Elements("Web Tables")
Buttons = Elements('Buttons')
Links = Elements("Links")
Broken = Elements("Broken Links - Images")
Upload = Elements("Upload and Download")
Dynamic = Elements("Dynamic properties")

print(Text.click())
print(Check.click())
print(Radio.click())
print(Web.click())
print(Buttons.click())
print(Links.click())
print(Broken.click())
print(Upload.click())
print(Dynamic.click())

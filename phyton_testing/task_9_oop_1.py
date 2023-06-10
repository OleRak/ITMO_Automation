class Input:

    def __init__(self, loc, text): #аргумент
        self.loc = loc # атрибут
        self.text = text

search = Input("button_search", "/search") #объект

print(search.loc, search.text) #вывод

class Button:
    def __init__(self, loc, text): # аргумент
        self.loc = loc # атрибут
        self.text = text

push = Button("button_push", "/push")  # объект

print(push.loc, push.text)  # вывод
class Title:
    def __init__(self, loc, text): # аргумент
        self.loc = loc # атрибут
        self.text = text

look = Title("Title_look", "/look") # объект

print(look.loc, look.text) # вывод
class Link:
    def __init__(self, loc, text): # аргумент
        self.loc = loc # атрибут
        self.text = text

merge = Link("Link_merge", "/merge") # объект

print(merge.loc, merge.text) # вывод


class Page:

    def __init__(self, url):
        self.url = url

    def get(self):
        return "URL {}".format(self.url) #print(self.url)


home = Page("Link")

print(home.get()) #home.get()

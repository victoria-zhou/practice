from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author 

class MyBook(Book): # attn: interance happens between parathethese
    def __init__(self, title, author, price): # attn: space between def and __
        super().__init__(title, author)
        self.price=price

    def display(self): # dont forget to supply self
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)

title = 'Book'
author = 'Amy'
price = '15 dollars'
new_novel=MyBook(title,author,price) # dont mix with Java as how to define an instance to use constructor and methods
new_novel.display()
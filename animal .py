from abc import ABC, abstractmethod
class Animal(ABC):
    def move(self):
        pass
class human(Animal):
    def move(self):
        print('I can walk and talk')

class snake(Animal):
        def move(self):
             
            print('I can crawl')
class dog(Animal):
        def move(self):
            print('I can bark')
R=human()

R.move()

t=snake()
t.move()

m=dog()

m.move()



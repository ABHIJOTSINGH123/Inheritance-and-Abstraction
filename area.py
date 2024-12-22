from abc import ABC, abstractmethod
class polygon(ABC):
    def move(self):
        pass
class rectangle(polygon):
    def move(self):
        print('i am a rectangle of {area=2(l+b)},l=length of rect. and b=breath of rectangle')

class square(polygon):
        def move(self):
             
            print('I am a square of {area=s**2},s=side of square.')
class circle(polygon):
        def move(self):
            print('I am a circle of {area=2*22/7*radius}')
R=rectangle()
R.move()

t=circle()
t.move()

m=square()
m.move() 
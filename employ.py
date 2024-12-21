class person(object):
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)
class employ(person):
    def __init__(self, name, idnumber, post, salary):
        self.post = post
        self.salary = salary
        person.__init__(self,name,idnumber)
a=employ('penguin',202134587548478,15000,"intern")
a.display()
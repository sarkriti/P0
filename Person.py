import datetime

class Person:
    def __init__(self,name,username,password,status,session):
        self.name = name
        self.username = username
        self.password = password
        self.status = status
        self.session = session
    
    def printAttributes(self):
        print("Person\n------\nname: "+self.name+"\nusername: "+self.username+"\nstatus: "+self.status)
        print("updated: "+ str(datetime.datetime.now()))

p1 = Person('kriti','sarkriti','lzy6253','working on homework','2398ywfeehoewfh')

p1.printAttributes()
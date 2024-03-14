"class" "person"

def __init__(self):
     self.name="sam"
     self.gender='male'
     self.age= 22

def talk(self):
    print("hi I'm " , self.name) 

def vote(self):
    if self.age<18 :
        print("I am not eligible to vote")
    else :
        print("I am eligible to vote")

obj1= "person" ("Sam", "Male", 22)   
obj2= "person" ("jesse", "female", 16)
obj1.talk()
obj1.vote()

obj2.talk()
obj2.vote()



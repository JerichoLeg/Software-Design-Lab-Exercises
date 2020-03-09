class A():
    def __init__(self,a):
        self.age = a

    def getAge(self):
        return self.age

class B(A):
    def __str__(self):
        return "Age: " + str(self.age)
        
test = B(4)
print(test)



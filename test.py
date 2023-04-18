class Person:
    def __init__(self,name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def __str__(self):
        return f"my name is {self.name} and i am {self.age} years old.
                    my height is {self.height} and i weight {self.weight}"    

def work():
    x = 3 
    y = 4
    if x<y:
        print(t)


    count = 10
    while count > 0:
        print(count,"!")
        count -= 1
    if (count == 0):
        print("BLAST OFF!!!")
        print(t)

    pers = Person()
    pers.name = "John"
    pers.age = "28"
    pers.height = "5'10"
    pers.weight = "180"
    print(pers)

    


    

#initiate class
class employee:
    # special method/magic method/dunder method - constructor

    def __init__(self):
        print("Started executing data/attribute")
        self.id = 123 
        self.salary = 50000
        self.designation = "MLE"
        print("attribute/data have been initiated")

    def travel(self,destination):
        print("travel function was called manually")
        print(f"The employee is traveling to {destination}")


#create and obj/instance of the class 
sam = employee()
#printing attribute 
#print(sam.salary)

#calling a method
#sam.travel('kerela')
print(type(sam))
 
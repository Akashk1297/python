# Parent class
class Cars:
    def __init__(self,name,fuel,type):
        self.name=name
        self.fuel=fuel
        self.type=type

    @staticmethod
    def carDisplay():
        #This is a static method inside the Base class
        print('Displaying properties of Car:')
        
    def carDetails(self):
        print('Name of car:',self.name)
        print('Fuel used:',self.fuel)
        print('Type of car:',self.type)

        

# Child class
class Maruti(Cars):
    def __init__(self,model,country,engine):
        super().__init__('maruti','petrol','hatchback')
        self.model=model
        self.country=country
        self.engine=engine

    def display(self):
        super().carDisplay()
        super().carDetails()
        print('Model of car:',self.model)
        print('Origin country:',self.country)
        print('Type of engine:',self.engine)

    @classmethod
    def clsMethod(cls):
        print('This is a class method')

class Mahindra(Cars):
    def __init__(self,model,country,engine):
        super().__init__('mahindra','diesel','xuv')
        self.model=model
        self.country=country
        self.engine=engine

    def display(self):
        super().carDisplay()
        super().carDetails()
        print('Model of car:',self.model)
        print('Origin country:',self.country)
        print('Type of engine:',self.engine)

# creating instance of child class
m1=Maruti('alto k10','india','4 stroke engine')
# calling child class function
m1.display()
 

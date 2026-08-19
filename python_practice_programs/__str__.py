class car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
    
c=car("Toyota", "fortuner", 2020)        
print(c)  #without __str__ method it will print the address of the object but with __str__ method it will print the value of the object.




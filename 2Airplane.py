import math 

class Airplane:
    
    
    #constructor
    def __init__(self, initX, initY, consumption, initial_fuel_level):
        self.consumption = consumption
        self.position = (initX, initY)
        self.fuel_level = initial_fuel_level
        
        #I would also set the maximum fuel level as a feature
        
    def refuel (self, liters):
        
        #add liters
        self.fuel_level = self.fuel_level + liters
        
        
        
    def goto (self, x, y):    
        
        #calculation of the distance between two points
        distance = math.sqrt((x - self.position[0])**2 + (y - self.position[1])**2)
        
        #total consumption
        total_cons = self.consumption * distance
        
        
        if (self.fuel_level < total_cons):
            #no fuel
            return False;
        else:
            #update position
            self.position = (x,y)
            #update fuel_level
            self.fuel_level = self.fuel_level - total_cons
            return True;

class TestAirplane ():        
        
       
     def test_class_airplane_add_fuel (self):     
           airplane1 = Airplane(2, 1, 20, 2.50) 
           airplane1.refuel(3.22) == 5.72
    
        
     def test_class_airplane_no_fuel (self):
        
           airplane1 = Airplane(2, 1, 20, 2.50) 
           airplane1.refuel(3.22)
           airplane1.refuel(5.33)
           assert airplane1.goto (5,10) == False
        
        
     def test_class_airplane_yes_fuel (self):
        
           airplane1 = Airplane(2, 1, 20, 2.50) 
           airplane1.refuel(500.33)
           assert airplane1.goto (5,10) == True   
           assert airplane1.position == (5,10)
           assert round (airplane1.fuel_level,2) == 313.09  
           
     def test_class_airplane_go_negative (self):
        
           airplane1 = Airplane(2, 1, 20, 300) 
           
           assert airplane1.goto (-6,-3) == True  
           assert airplane1.position == (-6,-3)
        
        

        
        
        



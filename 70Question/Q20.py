class Car():
    def __init__(self,year,model,speed):
        self.year= year
        self.model = model
        self.speed = speed

    def set_year(self, year):
        self.year = year
    
    def set_model(self, model):
        self.model = model
  
    def set_speed(self, speed):
        self.__speed = speed



    def get_year(self):
        return self.year
    
    def get_model(self):
        return self.model
  
    def get_speed(self):
        return self.speed 

    def accelerate(self):
        self.speed +=5





def main():

    year = input('Enter the car year: ')
    model = input('Enter the car model: ')
    speed = int(input("Enter the car's speed:" ))


    mycar = Car(year, model, speed)

    #Accelerate 
    mycar.accelerate()
    print('The current speed is: ', mycar.get_speed())


main()
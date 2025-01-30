class robot:
      
    def __init__(self,name : str,age : float) -> None:   
        self.name = name
        self.age = age  

    def cahrge(self) -> None :  
        print (f"{self.name} is charging")  


class robot_dog (robot):

       
        
        def bark(self) -> None :  
            print (f"{self.name} says wooff and has age ${self.age:,.2f}")    



dog : robot_dog = robot_dog("s",123.3453)
print(f"name {dog.name} breed {dog.age}") 
dog.bark()  
oldstr : str = input("how old?\n")
try : 
    old  : int = int(oldstr)   
except :
    print("Invalid number")
    quit()      
decades: int  =  old//10
years : int = old % 10  
print("you are " + str(decades) + " decades and " + str(years) + " old")  
tempstr : str = input("temperature?\n")  
try :
    temp : float= float(tempstr)
except :
    print("Invalid number")
    quit()      
if temp > 30 or temp  <0 :
    print("stay at home")      
else :
    print("It's warm")   
    print("go for a walk")
amountstr : str = input("amout?\n")
try : 
    amount : float = float(amountstr)   
except :
    print("Invalid number")
    quit()      
tax : float=  0.06  
total : float = amount + amount * tax
print(total)
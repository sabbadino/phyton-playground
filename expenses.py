expenses : list[float] = [1,13.5,6.7] # This is the list of expenses  
for i in  range(3) : # This is the list of expenses
    expenses.append(float(input("enter expense\n"))) # This is the list of expenses 
total : float = 0 # This is the total of the expenses   
for ix in expenses :  
    total = total + ix   
total = sum(expenses) # This is the total of the expenses
print("totale is ", total) # This is the total of the expenses
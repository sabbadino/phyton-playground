dic : dict[str, str] = {
    "rock" : "scissors", 
    "scissors" : "paper", 
    "paper" : "rock"
}
for key1, value1 in dic.items() :
    print(key1,":",value1)

dic["scissors"] =  "rock"
key : str = input ("enter key\n")
value : str|None = dic.get(key)
if value :
    print(key, "is in dic")
else :
    print(key, "is not in dic") 


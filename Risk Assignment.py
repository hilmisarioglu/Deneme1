age = (input("Are you a cigarette addict older than 75 years old? Yes/No")).title().split()
chronic = (input("Do you have a severe chronic disease? Yes/No ")).title().split()
immune = (input("Is your immune system too weak? Yes/No")).title().split()
print(age , chronic, immune)
risk = (age == ["Yes"]) and (chronic == ["Yes"]) and (immune == ["Yes"])

if risk == True:
    print("You are in risky group")
else: 
    print("You are not in risky group")

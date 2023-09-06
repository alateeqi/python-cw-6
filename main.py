# write your code here
person = {
"name":"jana",
'age':17,
"hobbies":["drawnig","swimming","tennis","cookng"] 
}
print(person["name"])
print(person["age"])

person["age"]="200"
person["country"]=" kuwait"
print(person)
print(len(person))

person["hobbies"].append("singing")

def checking_hobbies(person):
    
    if len(person["hobbies"]) >= 3:
        print("wow you are amazing")

checking_hobbies(person)
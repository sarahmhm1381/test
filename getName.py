numberOfUsers =int(input("Please enter number of users: ")) 

personsList = []
number = 1

while number <= numberOfUsers:
    userName = input(f"Enter user {number} name: ")
    userAge = input(f"Enter user {number} age: ")
    personsList.append({"name": f"{userName}" , "age": f"{userAge}"})
    number += 1

print(f"the list is: {personsList}")
name = input("\nEnter name to search: ")

if next((item for item in personsList if item["name"] == f"{name}"),None):
    valueOfAge =  next((sub for sub in personsList if sub['name'] == f"{name}"), None)
    print(valueOfAge)
else:
    print("there is no user with given name")    
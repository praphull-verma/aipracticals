
def vacumCleanerAgent(location, status):

    if status == "Dirty":
        return "Suck"

    elif location == "A":
        return "Right"

    else:
        return "Left"


rooms = {

        "A":"Dirty",
        "B":"Dirty"

        }

location = "A"

print("Initial status: ", rooms);


while "Dirty" in rooms.values():
    status = rooms[location]
    print("\nLocation: ", location)
    print("Status: ", status)
    
    action = vacumCleanerAgent(location,status)
    print("Action: ", action)

    if action == "Suck":
        rooms[location] = "Clean"

    elif action == "Right":
        location = "B"

    elif action == "Left":
        location = "A"

print("\n", rooms)
print("Both rooms are cleaned")
print("Ending the program")





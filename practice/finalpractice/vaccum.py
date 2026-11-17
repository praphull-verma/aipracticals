

def vaccum_agent(location, status):
    
    if status == "Dirty":
        return "Suck"

    elif location == "A":
        return "Right"

    elif location == "B":
        return "Left"

rooms = {

        "A":"Dirty",
        "B":"Dirty"

        }

location = "A"

while "Dirty" in rooms.values():

    status = rooms[location]
    print(status)

    action = vaccum_agent(location,status)
    print(action)

    if action == "Suck":
        print("Cleaning room ", location)
        rooms[location] = "Clean"

    elif action == "Left":
        print("Moving to the left room")
        location = "A"
    elif action == "Right":
        print("Moving to the right room")
        location = "B"

    else:
        break






def vacumm_agent(location, status):

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

    action = vacumm_agent(location, status)

    if action=="Suck":
        print("Cleaning...")
        rooms[location] = "Clean"

    elif action == "Left":
        print("Moving to room A")
        location = "A"

    elif action == "Right":
        print("Moving to room B")
        location = "B"



print("All rooms cleaned")
    


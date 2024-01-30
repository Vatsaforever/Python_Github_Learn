def start_engine():
    print("Starting Engine")
def moving_forward():
    print("Moving Forward")
def Turn_Direction(direction)-> str:
    print(f"Turning {direction}")
def follow_roundabout(exit_number):
    print(f"Taking the exit number {exit_number} from the roundabout")
def Announce_Arrival(Target):
    print(f"You have arrived at {Target}")
def stop_engine():
    print("Stopping Engine")


Direct_Routes = ("Library","Tech Park")
Roundabout_Routes = ("Hospital", "Mall", "Airport", "University", "Stadium")
while True:
    Destination = str(input("Please enter your destination: ")).capitalize()
    if Destination in Direct_Routes + Roundabout_Routes:
        break
    else:
        print("Invalid Destination. Please try again")

start_engine()

if Destination in Direct_Routes:
    if Destination == "Library":
        moving_forward()
        Turn_Direction("left")
        Announce_Arrival(Destination)
    else:
        moving_forward()
        Turn_Direction("Right")
        Announce_Arrival(Destination)
else:
    moving_forward()
    print("Taking the roundabout")
    if Destination == "Hospital":
        follow_roundabout("One")
        Announce_Arrival(Destination)
    elif Destination == "Mall":
        follow_roundabout("Two")
        Turn_Direction("Right")
        Announce_Arrival(Destination)
    elif Destination in ("University", "Stadium"):
        follow_roundabout("Four")
        if Destination == ("University"):
            Turn_Direction("Left")
            Announce_Arrival(Destination)
        else:
            Turn_Direction("Right")
            Announce_Arrival(Destination)
    else:
        follow_roundabout("Three")
        Announce_Arrival(Destination)

stop_engine()




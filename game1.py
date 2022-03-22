from adventurelib import *


space = Room("""
	You are drifting in space. It feels very cold.
	A slate-blue spaceship sits completely silently to your left,
	its airlock open and waiting.
	""")

spacecraft	= Room("""
	The bridge of the spaceship is shiny and white, with thousands 
	of small, red, blinking lights.
	""")

cargo = Room("""
	The place where the ships come in and drop there cargo off
	""")

docking = Room("""
	Where another spaceship is in space
	""")


hallway = Room("""
	A very long hallway in the big Spacecraft
	""")

quarters = Room("""
	4 diffrent rooms in one big room
	""")

mess_hall = Room("""
	Where people gather in a room or building to eat together
	""")

escape_pods = Room("""
	This is needed if your spacecraft is about to blow up or your 
	losing oxygen or something else bad has happened
	""")



@when ("go DIRECTION")
def travel(direction):
	global current_room
	if direction in current_room.exits():
		current_room = current_room.exit(direction)
		print(f"You go {direction}.")
		print(current_room)




current_room = space

@when("enter airlock")
@when("enter spaceship")
@when("enter ship")
def enter_spaceship():
	global current_room
	#check if action can be done
    if current_room is not space:
    	say("There is no airlock here")
        return

	else:
		current_room = spaceship 
		print("""You heave yourself into the spaceship and
		slam your hand on the button to close the door.
		""")
		print(current_room)
	










#Hallway = Room
#Puzzle Room = Room 











@when("brush teeth")
def brush_teeth():
	print("You brush your teeth")
@when("brush teeth")
@when("brush")
@when("clean teeth")
def brush_teeth():
	print("You brush your teeth")

@when("comb hair")
@when("comb")
def comb_hair():
	say("""
		You brush your long flowing locks with the gold hairbrush that you have selected from the red basket
		""")


def main():
	start()

if __name__ == '__main__':
	main()

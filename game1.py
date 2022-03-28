from adventurelib import *


space = Room("""
	You are drifting in space. It feels very cold.
	A slate-blue spaceship sits completely silently to your left,
	its airlock open and waiting.
	""")

airlock	= Room("""
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

bridge = Room("""
	For people to walk on when there is a big river or some big hole
	""")

Item.description = ""

knife = Item("a dirty knife","knife")
knife.descrition = "the knife has a dull sheen to it but it looks rather sharp."

red_keycard = Item("a red keycard","keycard","red card","red card")
red_keycard.descrition = "it's a red keycard. It probably opens a door or locker."


screw_driver = Item("a rusty screw driver","a clean screw driver")
screw_driver.descrition = "it's a screw driver it probably opens a hatch to the engine room"


torch = Item("a wet piece of wood that needs to be dry to light on fire","wood is now dry because you left it in your backpack")
torch.descrition = "it's a peice of wood that you found can now turn into a torch that can be used to light up the room"




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
	


spaceship.east = hallway
spaceship.south = quarters
hallway.east == bridge
hallway.north = cargo
quarters.east = mess_hall
mess_hall.north = hallway
hallway.north = cargo
cargo.east = docking
bridge.south = escape_pods
quarters.south = airlock







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

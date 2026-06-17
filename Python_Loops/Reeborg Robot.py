# So this robot is a great way to practice python
# It was fun for me, right now i kinda solved it but not in a good way
# So i am at the Hurdle4 i did eventually get the robot to the goal but problem is he does not stop
# The main problem is i made too much functions.
# Here check out my code:
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def check_wall():
    while not front_is_clear():
        go_up()
    go_down()

def go_up():
    turn_left()
    move()
    turn_right()
    check_wall()

def go_down():
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    while not at_goal():
        if front_is_clear():
            move()
        else:
            jump()

def jump():
    go_up()
    go_down()

while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()
"""

# Now i am going to delete and retry everything from scratch

# Check this out i got my first infinit loop XD
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    while not front_is_clear():
        move()

while not at_goal():
    if front_is_clear() :
        move()
    else :
        jump()
# Robot will go around itself forever
"""


# Soooooooo eventually i did it myself ( i didn`t know there was a wall_on_right() function)
# so here it is :
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()


while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()
"""
# With this code you can pass the Hurdle4 challenge, i will put down the sites link below:
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json



# Maze challenge:
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
"""
For this challenge you just have to know 1 rule and that`s the right-hand roul:
1. If there is no wall on the right, turn right and move.
2. Otherwise, if there is no wall in front, move forward.
3. Otherwise, turn left (because you're blocked on both the right and the front).
"""

"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def check():
    if not wall_on_right():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
        
while not at_goal():
    check()
"""
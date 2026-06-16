# So this robot is a great way to practice python
# It was fun for me, right now i kinda solved it but not in a good way
# So i am at the Hurdle4 i did eventually get the robot to the goal but problem is he does not stop
# The main problem is i made too much functions.
# Here check out my code:
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


# Now i am going to delete and retry everything from scratch
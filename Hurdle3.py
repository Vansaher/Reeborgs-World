def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_right()
    move()
    turn_right()

while at_goal() != True:
    if front_is_clear():
        move()
    elif wall_in_front():
        turn_left()
    while is_facing_north():
        if wall_on_right():
            move()
        else:
            jump()

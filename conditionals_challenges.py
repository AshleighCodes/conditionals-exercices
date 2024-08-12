def can_climb(has_helmet: bool, has_rope: bool):
    """To go rock climbing, you need a helmet and some rope. This function 
    calculates whether you are able to go rock climbing.

    Arguments:
        - has_helmet: a boolean representing whether or not the climber has their helmet
        - has_rope: a boolean representing whether or not the climber has their rope

    Returns:
        - a boolean that is true when the climber is allowed to climb, and false otherwise.
    """
    if has_helmet and has_rope == True:
        print("You can go climbing")
        return True
    else:
        print("You can't go climbing")
        return False


def red_light_camera(light_colour: str, car_detected: bool):
    """A function to determine whether or not a driver should get a ticket 
    for running a red light.

    Arguments:
        - light_colour: a string representing the colour of the light. 
            Valid colours are "Red", "Amber", or "Green"
        - car_detected: a boolean representing whether or not a car 
            is driving through the intersection.

    Returns: A boolean that is true if a car ran the red light, and false otherwise.
    """

    if light_colour == "Red" and car_detected == True:
        print("Hey! You get a ticket")
        return True
    else:
        print("You don't get a ticket")
        return False
    

def can_ride_rollercoaster(rider_height: float):
    """Only people who are over 120cm in height can ride the rollercoaster.
    
    Arguments:
        - rider_height: a float representing the height of the prospective rider in centimetres
        
    Returns: a boolean representing whether or not the prospective rider is allowed on the rollercoaster.
    """

    if rider_height > 120:
        print("Rollercoaster time!")
        return  True
    else:
        print("No LOL you can't.")
        return False


def login(password: str):
    """Only users who enter the password "quartzgleam?1" can log in successfully.

    Arguments:
        - password: a string representing the user's password input.

    Returns:
        - a boolean representing whether or not the user's password was correct.
    """

    if password == "quartzgleam?1":
        print("Congratulations! You can log in!")
        return True
    else:
        print("Nah-uh-uh! You didn't say the magic word!")
        return False

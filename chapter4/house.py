from gasp import *          # import everything from the gasp library

def draw_house(x,y):
                # open the graphics canvas

    Box((x, y), 100, 100)     # the house
    Box((x+35, y), 30, 50)       # the door
    Box((x+20,y+60), 20, 20)       # the left window
    Box((x+60, y+60), 20, 20)       # the right window
    Line((x, y+100), (x+50, y +140))  # the left roof
    Line((x+50, y+140), (x+100, y+100)) # the right roof

              
                                
                                
begin_graphics()

#first level
draw_house(20,20)
draw_house(275,20)
draw_house(500,20)
#second level
draw_house(150,150)
draw_house(385,150)
#third level
draw_house(275,280)
update_when('key_pressed')  
end_graphics()   
"""
# 2 - we don't see the house because we wrapped the code in a function.
# 3 - now we see the house because the code was called.

"""

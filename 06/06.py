from pico2d import *

import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90
r = 235

angle = 90

move = False

while(True):
    if(move == False):
        move = True
        while(x + 20 < 800):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            x += 2
            delay(0.01)
        
        while(y + 40 < 600):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            y += 2
            delay(0.01)
    
        while(x - 10 > 0):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            x -= 2
            delay(0.01)
    
        while(y > 90):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            y -= 2
            delay(0.01)

        while(x < 400):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            x += 2
            delay(0.01)
            
    elif(move == True):
        move = False
        while(angle < 360 + 90):
            x = 400 - r * math.cos(angle / 360 * 2 * math.pi)
            y = 325 - r * math.sin(angle / 360 * 2 * math.pi)
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            angle += 0.1
            
close_canvas()

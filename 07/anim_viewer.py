from pico2d import *

open_canvas()

character = load_image('sprite.png')

def draw_animation(left, start, bottom, width, height, frame):
    count = 0
    while(count < frame):
        clear_canvas()
        character.clip_draw(left * count + start, bottom, width, height, 400, 300)
        update_canvas()
        count += 1
        delay(0.1)
        get_events()
    
while True:
    draw_animation(128, 20, 1285, 100, 120, 16)   # line 1
    draw_animation(128, 10, 1155, 100, 125, 12)   # line 2
    draw_animation(128, 5, 1025, 115, 135, 12)    # line 3
    draw_animation(128, 20, 900, 100, 125, 12)    # line 4
    draw_animation(128, 20, 775, 110, 120, 11)    # line 5
    draw_animation(128, 20, 645, 100, 120, 12)    # line 6
    draw_animation(128, 20, 520, 100, 120, 12)    # line 7
    draw_animation(128, 20, 390, 110, 120, 15)    # line 8
    draw_animation(128, 20, 260, 100, 120, 15)    # line 9
    draw_animation(128, 20, 135, 100, 120, 12)    # line 10
    draw_animation(128, 20, 0, 100, 130, 16)      # line 11
    break
    
close_canvas()
from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

def handle_events():
    global running
    global dirX
    global dirY
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                dirX = -1
            elif event.key == SDLK_RIGHT:
                dirX = 1
            elif event.key == SDLK_UP:
                dirY += 1
            elif event.key == SDLK_DOWN:
                dirY -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                dirX = -2
            elif event.key == SDLK_RIGHT:
                dirX = 2
            elif event.key == SDLK_UP:
                dirY -= 1
            elif event.key == SDLK_DOWN:
                dirY += 1


open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x = TUK_WIDTH // 2
y = TUK_HEIGHT // 2
frame = 0
dirX = 0
dirY = 0

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if dirX == 1:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    elif dirX == -1:
        character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)
    elif dirX == 2:
        character.clip_draw(frame * 100, 100 * 3, 100, 100, x, y)
    elif dirX == -2:
        character.clip_draw(frame * 100, 100 * 2, 100, 100, x, y)
    else:
        character.clip_draw(frame * 100, 100 * 3, 100, 100, x, y)

    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    
    if x + 10 < TUK_WIDTH and x - 10 > 0:
        if dirX == 1 or dirX == -1:
            x += dirX * 5
    elif x + 15 > TUK_WIDTH:
        x -= 5
    elif x - 15 < 0:
        x += 5
            
    if y + 40 < TUK_HEIGHT and y - 5 > 0:
         y += dirY * 5
    elif y + 40 > TUK_HEIGHT:
        y -= 5
    elif y - 10 < 0:
        y += 5
         
    delay(0.01)

close_canvas()


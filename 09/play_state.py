from pico2d import *
import game_framework
import logo_state
import item_state
import boy_state
import random

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = 0
        self.dir = 1 # ¿À¸¥ÂÊ
        self.image = load_image('animation_sheet.png')
        self.item = None
        self.boy_num = None
        self.ball_image = load_image('ball21x21.png')
        self.big_ball_image = load_image('ball41x41.png')

    def update(self):
        self.frame = random.randint(0, 7)
        self.x += self.dir * 1
        if self.x > 800:
            self.x = 800
            self.dir = -1 # ¿ŞÂÊ
        elif self.x < 0:
            self.x = 0
            self.dir = 1

    def draw(self):
        if self.item == 'Ball':
            self.ball_image.draw(self.x + 10, self.y + 40)
        elif self.item == 'Bigball':
            self.big_ball_image.draw(self.x + 10,self.y + 50)
            
        if self.boy_num == 'Addboy':
            Number_Boy += 1
        elif self.boy_num == 'Deleteboy':
            if Number_Boy - 1 < 1:
                Number_Boy -= 1
            
        if self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)



def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_i:
                game_framework.push_state(item_state)
            elif event.key == SDLK_b:
                game_framework.push_state(boy_state)


Number_Boy = 1
boy = None
grass = None
running = True

# ì´ˆê¸°?™”
def enter():
    global boy, grass, running
    boy = Boy()
    grass = Grass()
    running = True

# finalization code
def exit():
    global boy, grass
    del boy
    del grass

def update():
    boy.update()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def draw_world():
    grass.draw()
    boy.draw()
    
def pause():
    pass

def resume():
    pass






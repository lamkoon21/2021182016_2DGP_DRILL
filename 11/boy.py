from pico2d import *

class IDLE:
    @staticmethod
    def enter(self, event):
        print('EVENT IDLE')
        self.dir = 0
        self.timer = 1000
        
    @staticmethod
    def exit(self):
        print('EXIT IDLE')
        
    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.timer -= 1 # 시간 감소
        if self.timer == 0: # 시간이 다 다되면,
            self.add_event(TIMER) # 타이머 이벤트를 큐에 삽입
        
    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)

class RUN:
    
    # 어떤 이벤트 때문에 Run으로 들어왔는지 파악을 하고, 그 이벤트에 따라서 실제 방향을 결정
    
    def enter(self,event):
        print('ENTER RUN')
        if event == RD:
            self.dir = 1
        elif event == LD:
            self.dir = -1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1
            
    def exit(self):
        self.face_dir = self.dir
        print('EXIT RUN')
        
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        self.x = clamp(0, self.x, 800)
        
    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)

class SLEEP:
    def enter(self, event):
        print('ENTER SLEEP')
        self.dir = 0 # 정지상태

    def exit(self):
        print('EXIT SLEEP')
        
    def do(self):
        self.frame = (self.frame + 1) % 8
        
    def draw(self):
        if self.face_dir == 1:
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100, 
                                           -3.141592 / 2, '', self.x + 25, self.y - 25, 100, 100)
        else:
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100, 
                                           3.141592 / 2, '', self.x - 25, self.y - 25, 100, 100)
            
class AUTO_RUN:
    def enter(self,event):
        print('ENTER AUTO_RUN')
        self.dir = self.face_dir
        
    def exit(self):
        self.face_dir = self.dir
        print('EXIT AUTO_RUN')
        
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        # self.x = clamp(0, self.x, 800)
        
        if self.x <= 0:
            self.dir = 1
            self.face_dir = 1
        elif self.x >= 800:
            self.dir = -1
            self.face_dir = -1
        
    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)

RD, LD, RU, LU, TIMER, AUTO = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYDOWN, SDLK_a): AUTO
}

next_state = {
    SLEEP : {RU: RUN, LU: RUN, RD: RUN, LD: RUN, TIMER: SLEEP, AUTO: AUTO_RUN},
    IDLE : {RU: RUN, LU: RUN, RD: RUN, LD: RUN, TIMER: SLEEP, AUTO: AUTO_RUN},
    RUN : {RU: IDLE, LU: IDLE, LD: RUN, RD: RUN, TIMER: RUN, AUTO: AUTO_RUN},
    AUTO_RUN : {RU: AUTO_RUN, LU: AUTO_RUN, LD: RUN, RD: RUN, TIMER: RUN, AUTO: IDLE}
}

class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')
        
        self.timer = 100
        
        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)
        
        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self)
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        
    def add_event(self, event):
        self.event_que.insert(0, event)
    
    def handle_events(self, event):
        if (event.type, event.key ) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
        
        
        
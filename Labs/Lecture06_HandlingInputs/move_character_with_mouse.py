from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
     global running
     global  x, y
     events = get_events()
     for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def suchan():
    global x, y, hand_arrow_x, hand_arrow_y
    h = 0
    s = 0
    hand_arrow_x - x


open_canvas(KPU_WIDTH, KPU_HEIGHT)


kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

hand_arrow_x = random.randint(0, 1280)
hand_arrow_y = random.randint(0, 1024)


running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    hand_arrow.draw(hand_arrow_x, hand_arrow_y)
    update_canvas()

    frame = (frame + 1) % 8

    handle_events()

close_canvas()





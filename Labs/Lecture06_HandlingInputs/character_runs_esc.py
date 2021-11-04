from pico2d import *

open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')


running = True
x = 0
frame = 0


def handle_events():
    global running

    events = get_events()
    for event in events:  # events 리스트에 담겨 있는 각각에 event를 하나씩 꺼낸다.
      if event.type == SDL_QUIT:  # 윈도우 x버튼을 눌렀을때 종료
          running = False
      elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:  # 어떤 event 하나가 키가 눌렸고 # 그게 ESCAPE면 종료하여라
          running = False





while x < 800 and running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 100, 100, 100, x, 90)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    x += 5
    delay(0.01)

close_canvas()


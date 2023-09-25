from pico2d import *


BackGround_Width,BackGround_Height = 1280, 1024



open_canvas(BackGround_Width,BackGround_Height)

BackGround = load_image("TUK_GROUND.png")




running = True


def HandleEvent():
    global running

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
            return
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
                return


while running:
    clear_canvas()

    BackGround.draw(BackGround_Width // 2, BackGround_Height // 2)
    #Draw between here

    HandleEvent()
    update_canvas()




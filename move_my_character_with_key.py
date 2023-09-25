from pico2d import *


BackGround_Width,BackGround_Height = 1280, 1024



open_canvas(BackGround_Width,BackGround_Height)

BackGround = load_image("TUK_GROUND.png")




running = True



while running:
    clear_canvas()

    BackGround.draw(BackGround_Width // 2, BackGround_Height // 2)
    #Draw between here


    update_canvas()


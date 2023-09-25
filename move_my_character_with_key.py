from typing import List, Any

from pico2d import *
import string
from enum import Enum, auto

BackGround_Width, BackGround_Height = 1280, 1024

open_canvas(BackGround_Width, BackGround_Height)

BackGround = load_image("TUK_GROUND.png")

running = True


class Image:
    def __init__(self, path=string, frame=int, width=int, height=int):
        # 이미지 이름
        self.Path = path
        # 스프라이트의 총 프레임 수
        self.Frame = frame
        # 스프라이트의 단위 가로 길이
        self.Width = width

        # 스프라이트의 단위 세로 길이
        self.Height = height


class Behavior(Enum):
    Idle = auto()
    Run = auto()


class Character:
    def __init__(self, DefaultImg=Image):
        self.IdleImage = DefaultImg
        self.RunImage = None
        self.CurrentImage = DefaultImg
        self.Object = load_image(DefaultImg.Path)
        self.FrameCount = 0
        self.DirectionX = 0
        self.x = 400
        self.y = 400
        self.isComposite = False

    def ChangeBehavior(self, TargetBehavior=Behavior):
        if TargetBehavior == Behavior.Idle.name:
            self.FrameCount = 0
            if self.IdleImage is not None:
                self.CurrentImage = self.IdleImage


        elif TargetBehavior == Behavior.Run.name:
            self.FrameCount = 0
            if self.RunImage is not None:
                self.CurrentImage = self.RunImage
                print("Run")


        self.Object = load_image(self.CurrentImage.Path)

    def EventHandler(self,Events = List[Any]):
        for event in Events:
            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_LEFT:
                    self.ChangeBehavior('Run')
                    self.isComposite = True
                    self.DirectionX -= 1
                elif event.key == SDLK_RIGHT:
                    self.ChangeBehavior('Run')
                    self.DirectionX += 1
                elif event.key == SDLK_DOWN:
                    self.ChangeBehavior('Run')
                    

            elif event.type == SDL_KEYUP:
                if event.key == SDLK_LEFT:
                    self.ChangeBehavior('Idle')
                    self.isComposite = False
                    self.DirectionX += 1
                elif event.key == SDLK_RIGHT:
                    self.ChangeBehavior('Idle')

                    self.DirectionX -= 1


    def ResisterRunImage(self,runImage = Image):
        self.RunImage = runImage



    def Draw(self,Scale=int):

        self.FrameCount = (self.FrameCount + 1) % self.CurrentImage.Frame
        self.x += self.DirectionX * 5

        if not self.isComposite:
            self.Object.clip_draw(
                self.CurrentImage.Width * self.FrameCount,
                0,
                self.CurrentImage.Width,
                self.CurrentImage.Height,
                self.x,
                self.y,
                150 * Scale,
                100 * Scale
            )
        elif self.isComposite:
            self.Object.clip_composite_draw(
                self.CurrentImage.Width * self.FrameCount,
                0,
                self.CurrentImage.Width,
                self.CurrentImage.Height,
                0,
                'h',
                self.x,
                self.y,
                150 * Scale,
                100 * Scale,
            )

def HandleEvent(Events = List[Any]):
    global running


    for event in Events:
        if event.type == SDL_QUIT:
            running = False
            return
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
                return


Character_IdleImage = Image("_Idle.png", 10, 120, 80)
Character_RunImage = Image("_Run.png", 10, 120, 80)



MainCharacter = Character(Character_IdleImage)
MainCharacter.ResisterRunImage(Character_RunImage)


EventList: List[Any] = []
# Main Process
while running:
    clear_canvas()
    EventList = get_events()
    BackGround.draw(BackGround_Width // 2, BackGround_Height // 2)
    # Draw between here

    MainCharacter.EventHandler(EventList)
    MainCharacter.Draw(4)
    # Draw between here
    delay(0.05)
    HandleEvent(EventList)
    update_canvas()

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
        self.Direction = 0
        self.x = 400
        self.y = 400
        self.isComposite = False

    def ChangeBehavior(self, TargetBehavior=Behavior):
        if TargetBehavior == Behavior.Idle:
            self.FrameCount = 0
            if self.IdleImage is not None:
                self.CurrentImage = self.IdleImage

        elif TargetBehavior == Behavior.Run:
            self.FrameCount = 0
            if self.RunImage is not None:
                self.CurrentImage = self.RunImage


    def EventHandler(self):
        events = get_events()
        for event in events:
            if event.type == SDL_KEYDOWN:
                pass







    def Draw(self,Scale=int):

        self.FrameCount = (self.FrameCount + 1) % self.CurrentImage.Frame
        self.x += self.Direction * 5

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


Character_IdleImage = Image("_Idle.png", 10, 120, 80)
Character_RunImage = Image("_Run.png", 10, 120, 80)
MainCharacter = Character(Character_IdleImage)
MainCharacter.isComposite = True
FrameNo = 0

# Main Process
while running:
    clear_canvas()

    BackGround.draw(BackGround_Width // 2, BackGround_Height // 2)
    # Draw between here

    MainCharacter.Draw(4)

    # Draw between here
    delay(0.05)
    HandleEvent()
    update_canvas()

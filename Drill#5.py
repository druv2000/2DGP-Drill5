from pico2d import *
from pygame.display import update

open_canvas()
character = load_image('george.png')
background = load_image('grass_template2.jpg')

def handle_events():
    global isProgramRunning, xPos, yPos, xDir, yDir

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            isProgramRunning = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            isProgramRunning = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_a:
            xDir -= 1
        elif event.type == SDL_KEYUP and event.key == SDLK_a:
            xDir += 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_d:
            xDir += 1
        elif event.type == SDL_KEYUP and event.key == SDLK_d:
            xDir -= 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_w:
            yDir += 1
        elif event.type == SDL_KEYUP and event.key == SDLK_w:
            yDir -= 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_s:
            yDir -= 1
        elif event.type == SDL_KEYUP and event.key == SDLK_s:
            yDir += 1


def drawAnimation():
    global frame, head
    if xDir != 0:
        if xDir == -1:
            head = 1  # 'left'
        elif xDir == 1:
            head = 3 #'right'
    elif yDir != 0:
        if yDir == -1:
            head = 0 #'down'
        elif yDir == 1:
            head = 2 #'up'

    if xDir != 0 or yDir != 0:
        character.clip_draw(head * 48, frame * 48, 48, 48, xPos, yPos, 100, 100)
    else:
        character.clip_draw(head * 48, 48, 48, 48, xPos, yPos + frame, 100, 100)

def clamp(value, minValue, maxValue):
    return min(maxValue, max(value, minValue))

#============== main ===========

isProgramRunning = True
xPos = 400; yPos = 300
xDir = 0; yDir = 0
frame = 0
frameCount = 0
head = 0 #'down'


while(isProgramRunning):
    clear_canvas()
    background.draw(400, 300)
    handle_events()
    drawAnimation()
    update_canvas()

    if frameCount % 10 == 0:
        frame = (frame + 1) % 4
        frameCount = 0;
    frameCount += 1

    if xDir != 0:
        xPos += 5 * xDir
    elif yDir != 0:
        yPos += 5 * yDir

    xPos = clamp(xPos, 0, 800)
    yPos = clamp(yPos, 0, 600)

    delay(0.01)

close_canvas()
#


import pygame
import time
import random

##colours
white = (255, 255, 255)
black = (0, 0, 0)
blue = (19, 100, 60)
lblue = (50, 100, 0)
red = (255, 0, 0)
green = (0, 255, 0)  # RGB

x = pygame.init()
# size of display width,height and block(that builds up snake)
display_w = 300
display_h = 300
block_s = 10

gameD = pygame.display.set_mode((display_w, display_h))  #'gameD' is main game screen
pygame.display.set_caption("new game snake")
gameD.fill(white)  # background
pygame.display.update()

clock = pygame.time.Clock()
# Fonts
smallfont = pygame.font.SysFont(None, 20)
mediumfont = pygame.font.SysFont(None, 33)
largefont = pygame.font.SysFont(None, 38)


def randgen():  # random coordinates generator function for apple
    randap_x = round(random.randrange(0, display_w - block_s) / block_s) * block_s
    randap_y = round(random.randrange(0, display_h - block_s) / block_s) * block_s
    return randap_x, randap_y


def text_obj(text, color):
    textsurf = mediumfont.render(text, True, color)  # text surface
    return textsurf, textsurf.get_rect()


def message_screen(msg, color, y_disp=0):
    textsurf, textrect = text_obj(msg, color)
    textrect.center = (display_w / 2), (
        display_h / 2
    ) + y_disp  # text surface center at middle of page
    gameD.blit(textsurf, textrect)


def snakefn(snakelist):  # making of FULL SNAKE in particular frame
    for xny in snakelist[:-1]:
        pygame.draw.rect(gameD, blue, [xny[0], xny[1], block_s, block_s])
    pygame.draw.rect(
        gameD, black, [snakelist[-1][0], snakelist[-1][1], block_s, block_s]
    )  # the head block(separately for different color)


def pause():
    message_screen("Paused", black, -20)
    message_screen("Press q to quit OR c to continue", lblue, 50)
    paused = True
    pygame.display.update()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()


def gamel():

    randapx, randapy = randgen()
    snakelength = 1
    snakehead = []
    snakelist = []
    gameexit = False
    leadx = display_w / 2
    leady = display_h / 2
    leadx_c = block_s
    leady_c = 0
    gameover = False
    direction = "right"
    FPS = 18

    while not gameexit:

        while gameover == True:
            message_screen("GAME OVER", black, -30)
            message_screen("Score: " + str(snakelength - 1), black, -10)
            message_screen("Press c to continue OR q to quit ", red, 50)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameexit = True
                    gameover = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameexit = True
                        gameover = False
                    elif event.key == pygame.K_c:
                        gamel()
        count = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameexit = True
            if event.type == pygame.KEYDOWN:
                count += 1
                if count > 1:
                    break
                if event.key == pygame.K_LEFT and direction != "right":
                    leadx_c = -block_s
                    leady_c = 0
                    direction = "left"
                elif event.key == pygame.K_RIGHT and direction != "left":
                    leadx_c = block_s
                    leady_c = 0
                    direction = "right"
                elif event.key == pygame.K_UP and direction != "down":
                    leady_c = -block_s
                    leadx_c = 0
                    direction = "up"
                elif event.key == pygame.K_DOWN and direction != "up":
                    leady_c = block_s
                    leadx_c = 0
                    direction = "down"
                elif event.key == pygame.K_p:
                    pause()

        gameD.fill(white)
        snakehead = []
        leadx += leadx_c
        leady += leady_c

        if (
            leadx >= randapx
            and leadx < randapx + 2 * block_s
            and leady >= randapy
            and leady < randapy + 2 * block_s
        ):  # meeting apple
            randapx, randapy = randgen()
            snakelength += 1
            if FPS < 50:
                FPS += 1.3  # increasing FPS after every increase of length

        pygame.draw.rect(gameD, green, [randapx, randapy, 2 * block_s, 2 * block_s])
        pygame.display.update()

        if (
            leadx >= display_w
        ):  # if statements to pass through walls and enter from the other end
            leadx = 0
        elif leadx < 0:
            leadx = display_w

        elif leady >= display_h:
            leady = 0
        elif leady < 0:
            leady = display_h

        snakehead.append(leadx)
        snakehead.append(leady)
        snakelist.append(snakehead)

        if (
            len(snakelist) > snakelength
        ):  # maintaining length of snake (as list is appended each time)
            del snakelist[0]

        for eachseg in snakelist[0:-1]:
            if eachseg == snakehead:
                gameover = True
                break

        snakefn(snakelist)
        txtt = smallfont.render("Score: " + str(snakelength - 1), True, red)
        gameD.blit(txtt, [0, 0])
        pygame.display.update()

        clock.tick(FPS)
    pygame.quit()
    quit()


gamel()

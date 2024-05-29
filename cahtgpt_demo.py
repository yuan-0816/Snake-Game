import pygame
import random
from config import *



pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
font_title = pygame.font.SysFont("Rockwell Condensed", 45)
font_story = pygame.font.SysFont("Rockwell Condensed", 30)





text_renderer = TextRenderer(50, 150, SCREEN_WIDTH-75, SCREEN_HEIGHT-50+200, font_story)



def message(msg, color, position):
    mesg = font_title.render(msg, True, color)
    screen.blit(mesg, position)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, BLACK, [x[0], x[1], snake_block, snake_block])

def game_intro(level):
    intro = True
    while intro:
        # draw_story(level)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                intro = False

def gameLoop():
    game_over = False
    game_close = False
    level = 0

    x1 = SCREEN_WIDTH / 2
    y1 = SCREEN_HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / float(BLOCK_SIZE)) * float(BLOCK_SIZE)
    foody = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / float(BLOCK_SIZE)) * float(BLOCK_SIZE )
    bombx = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / float(BLOCK_SIZE)) * float(BLOCK_SIZE )
    bomby = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / float(BLOCK_SIZE)) * float(BLOCK_SIZE )

    score = 0

    game_intro(level)

    while not game_over:

        while game_close:
            screen.fill(LIGHT_GRAY)
            message("你輸了! 按 Q 退出或 C 繼續遊戲", DARK_GRAY, [SCREEN_WIDTH / 6, SCREEN_HEIGHT / 3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -BLOCK_SIZE
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = BLOCK_SIZE
                    x1_change = 0

        if x1 >= SCREEN_WIDTH or x1 < 0 or y1 >= SCREEN_HEIGHT or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(LIGHT_GRAY)
        pygame.draw.rect(screen, GAINSBORO, [foodx, foody, BLOCK_SIZE, BLOCK_SIZE])
        pygame.draw.rect(screen, DARK_GRAY, [bombx, bomby, BLOCK_SIZE, BLOCK_SIZE])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(BLOCK_SIZE, snake_List)
        message(f"Score: {score}", BLACK, [0, 0])

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / float(BLOCK_SIZE)) * float(BLOCK_SIZE )
            foody = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / float(BLOCK_SIZE)) * float(BLOCK_SIZE )
            Length_of_snake += 1
            score += 1

        if x1 == bombx and y1 == bomby:
            bombx = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / float(BLOCK_SIZE)) * float(BLOCK_SIZE )
            bomby = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / float(BLOCK_SIZE)) * float(BLOCK_SIZE )
            score -= 2

        if score >= 5:
            level += 1
            if level > 5:
                game_intro(6)
                pygame.time.delay(3000)
                game_over = True
            else:
                game_intro(level)
                x1 = SCREEN_WIDTH / 2
                y1 = SCREEN_HEIGHT / 2
                x1_change = 0
                y1_change = 0
                snake_List = []
                Length_of_snake = 1
                foodx = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / float(BLOCK_SIZE)) * float(BLOCK_SIZE )
                foody = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / float(BLOCK_SIZE)) * float(BLOCK_SIZE )
                bombx = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / float(BLOCK_SIZE)) * float(BLOCK_SIZE )
                bomby = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / float(BLOCK_SIZE)) * float(BLOCK_SIZE )
                score = 0

        if score <= -5:
            game_close = True

        clock.tick(FPS)

    pygame.quit()
    quit()

gameLoop()

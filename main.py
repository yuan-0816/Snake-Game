import pygame
import random
import sys
from config import *

level_list = [Recap, Level1, Level2, Level3, Level4, Level5, Conclusion]

pygame.init()

# 設置螢幕和時鐘
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# 字體設置
font_title = pygame.font.Font("./material/YatraOne_Regular.ttf", 45)
font_story = pygame.font.Font("./material/YatraOne_Regular.ttf", 30)
font_infor = pygame.font.Font("./material/YatraOne_Regular.ttf", 23)

# 文本渲染器
title_render = TextRenderer(INTRO_GAP, INTRO_GAP*2, TITLE_WIDTH, TITLE_HEIGHT, font_title)
story_render = TextRenderer(INTRO_GAP, INTRO_GAP*2+TITLE_HEIGHT, STORY_WIDTH, STORY_HEIGHT, font_story)
next_level_render = TextRenderer(SCREEN_WIDTH - NEXT_LEVEL_WIDTH, SCREEN_HEIGHT - NEXT_LEVEL_HEIGHT, NEXT_LEVEL_WIDTH, NEXT_LEVEL_HEIGHT, font_infor, text_color=SILVER)
score_render = TextRenderer(0, 0, 100, 50, font_story, text_color=BLACK)

start_button = Button(
    int(SCREEN_WIDTH / 2 - COMPONENT_GAP - BUTTON_WIDTH),
    int(SCREEN_HEIGHT / 2 + COMPONENT_GAP),
    BUTTON_WIDTH,
    BUTTON_HEIGHT,
    "EMPEZAR",
    GRAY,
    font_story,
)

exit_button = Button(
    int(SCREEN_WIDTH / 2 + COMPONENT_GAP),
    int(SCREEN_HEIGHT / 2 + COMPONENT_GAP),
    BUTTON_WIDTH,
    BUTTON_HEIGHT,
    "SALIR",
    GRAY,
    font_story,
)

text_input = TextInputBox(
    int(SCREEN_WIDTH / 2 - TEXT_INPUTBOX_WIDTH / 2),
    int(SCREEN_HEIGHT / 2 - TEXT_INPUTBOX_HEIGHT),
    TEXT_INPUTBOX_WIDTH,
    TEXT_INPUTBOX_HEIGHT,
    "Your name",
    font_story,
)

# 蛇類別
class Snake:
    def __init__(self):
        self.size = SNAKE_SIZE
        self.body = [[SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 'RIGHT']]
        self.x_change = 0
        self.y_change = 0
        self.direction = 'RIGHT'

    def move(self):
        new_head = [self.body[0][0] + self.x_change, self.body[0][1] + self.y_change, self.direction]
        self.body = [new_head] + self.body[:-1]

    def grow(self):
        tail = self.body[-1]
        self.body.append(tail)

    def draw(self):
        for i, segment in enumerate(self.body):
            if i == 0:
                rotated_img = self.get_rotated_image(snake_head_img, segment[2])
            elif i == len(self.body) - 1:
                rotated_img = self.get_rotated_image(snake_tail_img, segment[2])
            else:
                rotated_img = self.get_rotated_image(snake_body_img, segment[2])
            screen.blit(rotated_img, (segment[0], segment[1]))

    def get_rotated_image(self, img, direction):
        if direction == 'LEFT':
            return pygame.transform.rotate(img, 90)
        elif direction == 'RIGHT':
            return pygame.transform.rotate(img, -90)
        elif direction == 'UP':
            return pygame.transform.rotate(img, 0)
        elif direction == 'DOWN':
            return pygame.transform.rotate(img, 180)

    def get_rect(self):
        return pygame.Rect(self.body[0][0], self.body[0][1], self.size, self.size)

    def check_collision(self):
        head = self.body[0]
        for segment in self.body[1:]:
            if head[0] == segment[0] and head[1] == segment[1]:
                return True
        return False

    def update_direction(self, x_change, y_change, direction):
        self.x_change = x_change
        self.y_change = y_change
        self.direction = direction
        self.body[0][2] = direction

# 食物類別
class Food:
    def __init__(self, snake_body):
        self.size = SNAKE_SIZE
        self.x, self.y = self.random_position(snake_body)

    def random_position(self, snake_body):
        while True:
            x = random.randint(0, (SCREEN_WIDTH - self.size) // SNAKE_SIZE) * SNAKE_SIZE
            y = random.randint(0, (SCREEN_HEIGHT - self.size) // SNAKE_SIZE) * SNAKE_SIZE
            if [x, y, ''] not in snake_body:
                return x, y

    def draw(self):
        screen.blit(food_img, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)

def message(msg, color, position):
    mesg = font_title.render(msg, True, color)
    screen.blit(mesg, position)

def draw_snake(snake_block, snake_list):
    for segment in snake_list:
        pygame.draw.rect(screen, BLACK, [segment[0], segment[1], snake_block, snake_block])

def game_intro(level, player_name="Player"):
    print(level_list[level])
    intro = True
    while intro:
        screen.fill(GRAY)
        title_render.draw_text(screen, level_list[level].title)
        story_render.draw_text(screen, level_list[level].story.format(PLAYER_NAME=player_name))
        next_level_render.draw_text(screen, "presione cualquier botón") # press any key to continue
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                intro = False
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

def login():
    login = True
    player_name = ""
    while login:
        screen.fill(DARK_GRAY)
        for event in pygame.event.get():
            player_name = text_input.handle_event(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.is_clicked(event.pos):
                    pygame.quit()
                    sys.exit()
                if start_button.is_clicked(event.pos):
                    login = False
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        start_button.draw(screen)
        exit_button.draw(screen)
        text_input.draw(screen)
        pygame.display.update()
    return player_name

def generate_position(snake_body):
    while True:
        x = random.randint(0, (SCREEN_WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
        y = random.randint(0, (SCREEN_HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
        if [x, y, ''] not in snake_body:
            return x, y

def game_loop():
    game_over = False
    game_close = False
    level = 0

    snake = Snake()
    food = Food(snake.body)
    bomb = Food(snake.body)

    score = 0
    player_name = login()
    game_intro(level, player_name)
    level += 1
    game_intro(level, player_name)

    while not game_over:
        while game_close:
            screen.fill(LIGHT_GRAY)
            story_render.draw_text(screen, "Desafortunadamente, x prueba fracasada.:( ¿Te gustaría retomar tu aventura con Don Quijote?")
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        game_loop()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.update_direction(-SNAKE_SIZE, 0, 'LEFT')
                elif event.key == pygame.K_RIGHT:
                    snake.update_direction(SNAKE_SIZE, 0, 'RIGHT')
                elif event.key == pygame.K_UP:
                    snake.update_direction(0, -SNAKE_SIZE, 'UP')
                elif event.key == pygame.K_DOWN:
                    snake.update_direction(0, SNAKE_SIZE, 'DOWN')

        if snake.body[0][0] >= SCREEN_WIDTH or snake.body[0][0] < 0 or snake.body[0][1] >= SCREEN_HEIGHT or snake.body[0][1] < 0:
            game_close = True

        snake.move()
        screen.fill(LIGHT_GRAY)
        food.draw()
        bomb.draw()

        if snake.check_collision():
            game_close = True

        for segment in snake.body:
            if segment[0] == bomb.x and segment[1] == bomb.y:
                bomb = Food(snake.body)
                score -= 2

        if snake.body[0][0] == food.x and snake.body[0][1] == food.y:
            food = Food(snake.body)
            snake.grow()
            score += 1

        snake.draw()
        score_render.draw_text(screen, "Score:" + str(score))
        pygame.display.update()

        if score >= 5:
            level += 1
            if level > 5:
                game_intro(6)
                pygame.time.delay(3000)
                game_over = True
            else:
                game_intro(level)
                snake = Snake()
                food = Food(snake.body)
                bomb = Food(snake.body)
                score = 0

        if score <= -5:
            game_close = True

        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    game_loop()

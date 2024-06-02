# pyinstaller --noconsole --onefile  --icon="E:/code training/python/Snake-Game/material/icon.ico" .\main.py -p .\config.py

import pygame
import random
import sys
from config import *

level_list = [Recap, Level1, Level2, Level3, Level4, Level5, Conclusion]


pygame.init()


# 設置螢幕和時鐘
pygame.display.set_caption('Alonso Quijano')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame_icon = pygame.image.load('./material/food/1_1_alonso_quijano.png')
pygame.display.set_icon(pygame_icon)


# 字體設置

font_title = pygame.font.Font("./material/YatraOne_Regular.ttf", 45)
font_story = pygame.font.Font("./material/YatraOne_Regular.ttf", 30)
font_infor = pygame.font.Font("./material/YatraOne_Regular.ttf", 23)

# 文本渲染器
title_render = TextRenderer(
    INTRO_GAP, INTRO_GAP * 2, TITLE_WIDTH, TITLE_HEIGHT, font_title
)
story_render = TextRenderer(
    INTRO_GAP, INTRO_GAP * 2 + TITLE_HEIGHT, STORY_WIDTH, STORY_HEIGHT, font_story
)
next_level_render = TextRenderer(
    SCREEN_WIDTH - NEXT_LEVEL_WIDTH,
    SCREEN_HEIGHT - NEXT_LEVEL_HEIGHT,
    NEXT_LEVEL_WIDTH,
    NEXT_LEVEL_HEIGHT,
    font_infor,
    text_color=SILVER,
)
score_render = TextRenderer(10, 10, 500, 50, font_story, text_color=DARK_GRAY)
target_food_render = TextRenderer(
    SCREEN_WIDTH // 2 - INTRO_GAP + INTRO_GAP*2, 10, 800, 50, font_story, text_color=DARK_GRAY
)

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
    "Nombre:",
    font_story,
)


class Snake:
    def __init__(self, speed=7000):
        self.size = BLOCK_SIZE
        self.body = [[SCREEN_WIDTH // 2, (SCREEN_HEIGHT + INFO_HEIGHT) // 2, None]]
        self.x_change = 0
        self.y_change = 0
        self.direction = None
        self.head_color = DARK_GRAY  # 蛇頭顏色
        self.body_color = DIM_GRAY  # 蛇身顏色
        self.speed = speed
        self.move_counter = 0


    def move(self, delta_t):
        self.move_counter += delta_t
        if self.move_counter >= 1000 / self.speed:
            if self.direction:
                new_head = [
                    self.body[0][0] + self.x_change,
                    self.body[0][1] + self.y_change,
                    self.direction,
                ]
                self.body = [new_head] + self.body[:-1]
            self.move_counter = 0
            return self.check_collision()

        
    def grow(self):
        tail = self.body[-1]
        self.body.append(tail)

    def shrink(self):
        if len(self.body) > 1:
            self.body.pop()
        if len(self.body) > 1:  # 再次檢查
            self.body.pop()

    def draw(self):
        for i, segment in enumerate(self.body):
            if i == 0:  # 如果是蛇頭，使用不同的顏色
                pygame.draw.rect(
                    screen, self.head_color, [segment[0], segment[1], self.size, self.size], border_radius=15
                )
            else:  # 如果是蛇身，使用不同的顏色
                pygame.draw.rect(
                    screen, self.body_color, [segment[0], segment[1], self.size, self.size], border_radius=15
                )
    def get_rotated_image(self, img, direction):
        if direction == "LEFT":
            return pygame.transform.rotate(img, 90)
        elif direction == "RIGHT":
            return pygame.transform.rotate(img, -90)
        elif direction == "UP":
            return pygame.transform.rotate(img, 0)
        elif direction == "DOWN":
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

    def can_change_direction(self, new_direction):
        if self.direction is None:
            return True
        if new_direction == "LEFT" and self.direction != "RIGHT":
            return True
        if new_direction == "RIGHT" and self.direction != "LEFT":
            return True
        if new_direction == "UP" and self.direction != "DOWN":
            return True
        if new_direction == "DOWN" and self.direction != "UP":
            return True
        return False
    
    def init(self, speed=8000):
        self.size = BLOCK_SIZE
        self.body = [[SCREEN_WIDTH // 2, (SCREEN_HEIGHT + INFO_HEIGHT) // 2, None]]
        self.x_change = 0
        self.y_change = 0
        self.direction = None
        self.head_color = DARK_GRAY  # 蛇頭顏色
        self.body_color = DIM_GRAY  # 蛇身顏色
        self.speed = speed
        self.move_counter = 0


# 食物類別
class Food:
    def __init__(self, snake_body, level):
        self.size = BLOCK_SIZE
        self.level = level
        self.target_food = self.random_food()  # 生成目標食物
        self.foods = self.generate_foods(snake_body)

    def generate_foods(self, snake_body):
        foods = [self.target_food]  # 包含目標食物
        while len(foods) < 5:
            food = self.random_food()
            if food[0] not in [food_item[0] for food_item in foods]:  # 確保不重複
                foods.append(food)

        food_positions = []
        for food in foods:
            x, y = self.random_position(snake_body, food_positions)
            food_positions.append({"name": food[0], "image": food[1], "x": x, "y": y})
        return food_positions

    def random_position(self, snake_body, foods):
        while True:
            x = random.randint(0, (SCREEN_WIDTH - self.size) // BLOCK_SIZE) * BLOCK_SIZE
            y = (
                random.randint(
                    INFO_HEIGHT // BLOCK_SIZE, (SCREEN_HEIGHT - self.size) // BLOCK_SIZE
                )
                * BLOCK_SIZE + 10
            )
            if all(
                [x != segment[0] or y != segment[1] for segment in snake_body]
            ) and all([x != food["x"] or y != food["y"] for food in foods]):
                head_x, head_y, direction = snake_body[0]
                if direction == "LEFT" and (head_x - 3 * BLOCK_SIZE <= x < head_x) and head_y == y:
                    continue
                if direction == "RIGHT" and (head_x < x <= head_x + 3 * BLOCK_SIZE) and head_y == y:
                    continue
                if direction == "UP" and head_x == x and (head_y - 3 * BLOCK_SIZE <= y < head_y):
                    continue
                if direction == "DOWN" and head_x == x and (head_y < y <= head_y + 3 * BLOCK_SIZE):
                    continue
                return x, y

    def random_food(self):
        food_name = random.choice(self.level.food)
        food_image = self.level.food_img[food_name].convert_alpha()
        return food_name, food_image

    def draw(self):
        for food in self.foods:
            screen.blit(food["image"], (food["x"], food["y"]))

    def get_food_rects(self):
        return [
            pygame.Rect(food["x"], food["y"], self.size, self.size)
            for food in self.foods
        ]


def game_intro(level, player_name="Player"):
    # print(level_list[level])
    intro = True
    while intro:
        screen.fill(GRAY)
        title_render.draw_text(screen, level_list[level].title)
        story_render.draw_text(
            screen, level_list[level].story.format(PLAYER_NAME=player_name)
        )
        next_level_render.draw_text(
            screen, "presione la tecla espacio para continuar"
        )  # press any key to continue
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    button_sound.play()
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
                    button_sound.play()
                    pygame.quit()
                    sys.exit()
                if start_button.is_clicked(event.pos):
                    button_sound.play()
                    login = False
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        start_button.draw(screen)
        exit_button.draw(screen)
        text_input.draw(screen)
        pygame.display.update()
    return player_name


def generate_position() -> tuple:
    x = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    y = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    return (x, y)



def game_over_screen(current_level):
    while True:
        screen.fill(LIGHT_GRAY)
        story_render.draw_text(
            screen,
            f"Desafortunadamente, {LEVEL_NAMES[current_level-1]} prueba fracasada. :(\n¿Te gustaría retomar tu aventura con Don Quijote?",
        )
        TextRenderer(
            SCREEN_WIDTH - NEXT_LEVEL_WIDTH * 2,
            SCREEN_HEIGHT - NEXT_LEVEL_HEIGHT,
            NEXT_LEVEL_WIDTH * 2,
            NEXT_LEVEL_HEIGHT,
            font_infor,
            text_color=DIM_GRAY,
        ).draw_text(
            screen, "Presione Q para salir Presione C para continuar"
        ) 
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

                elif event.key == pygame.K_c:
                    game_loop()
                    break
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


def game_win_screen():
    while True:
        screen.fill(GRAY)
        title_render.draw_text(screen, level_list[6].title)
        story_render.draw_text(screen, level_list[6].story)
        TextRenderer(
            SCREEN_WIDTH - NEXT_LEVEL_WIDTH * 2,
            SCREEN_HEIGHT - NEXT_LEVEL_HEIGHT,
            NEXT_LEVEL_WIDTH * 2,
            NEXT_LEVEL_HEIGHT,
            font_infor,
            text_color=SILVER,
        ).draw_text(
            screen, "Presione Q para salir Presione C para continuar"
        )  # press "c" to continue, "q" to quit
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

                elif event.key == pygame.K_c:
                    game_loop()
                    break
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


def game_loop():

    game_over = False
    level = 0
    score = 0

    player_name = login()
    game_intro(level, player_name)
    level += 1
    game_intro(level, player_name)
    snake = Snake()
    food = Food(snake.body, level_list[level])

    while not game_over:

        delta_t = clock.tick(FPS) / 1000
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake.can_change_direction("LEFT"):
                    snake.update_direction(-snake.size, 0, "LEFT")
                elif event.key == pygame.K_RIGHT and snake.can_change_direction(
                    "RIGHT"
                ):
                    snake.update_direction(snake.size, 0, "RIGHT")
                elif event.key == pygame.K_UP and snake.can_change_direction("UP"):
                    snake.update_direction(0, -snake.size, "UP")
                elif event.key == pygame.K_DOWN and snake.can_change_direction("DOWN"):
                    snake.update_direction(0, snake.size, "DOWN")

        if snake.move(delta_t):
            game_over_screen(level)

        if (
            snake.body[0][0] < 0
            or snake.body[0][0] >= SCREEN_WIDTH
            or snake.body[0][1] < INFO_HEIGHT
            or snake.body[0][1] >= SCREEN_HEIGHT
        ):
            game_over_screen(level)

        for food_item in food.foods:
            if snake.get_rect().colliderect(
                pygame.Rect(food_item["x"], food_item["y"], food.size, food.size)
            ):
                if food_item["name"] == food.target_food[0]:  # 如果吃到了目標食物
                    level_list[level].food_sound[food.target_food[0]].play()
                    snake.grow()
                    score += 1
                else:  # 如果吃到了錯誤的食物
                    error_sound.play()
                    snake.shrink()
                    score -= 2
                if score >= 15:
                    score = 0
                    level += 1
                    snake.init()
                    if level > 5:
                        game_win_screen()
                    else:
                        game_intro(level)
                food = Food(snake.body, level_list[level])

        screen.fill(LIGHT_SLATE_GRAY)
        pygame.draw.rect(screen, SLATE_GRAY, (0, 0, SCREEN_WIDTH, INFO_HEIGHT))
        snake.draw()
        food.draw()

        score_render.draw_text(screen, " Prueba:" + str(level) + " Puntos:" + str(score))
        target_food_render.draw_text(screen, "Instrucción: " + food.target_food[0])

        pygame.display.update()

        if score <= -1:
            game_over_screen(level)

        

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    game_loop()
    # game_win_screen()

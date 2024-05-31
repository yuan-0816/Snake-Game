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
score_render = TextRenderer(10, 5, 200, 50, font_story, text_color=DARK_GRAY)
target_food_render = TextRenderer(
    SCREEN_WIDTH // 2 - INTRO_GAP, 5, 800, 50, font_story, text_color=DARK_GRAY
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
    "Your name",
    font_story,
)


class Snake:
    def __init__(self):
        self.size = BLOCK_SIZE
        self.body = [[SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, None]]
        self.x_change = 0
        self.y_change = 0
        self.direction = None
        self.head_color = DARK_GRAY  # 蛇頭顏色
        self.body_color = DIM_GRAY  # 蛇身顏色
        self.speed = 0.1

    def move(self):
        if self.direction:
            new_head = [
                round(self.body[0][0] + self.x_change * self.speed),
                round(self.body[0][1] + self.y_change * self.speed),
                self.direction,
            ]
            print(new_head)
            self.body = [new_head] + self.body[:-1]

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
                    screen, self.head_color, [segment[0], segment[1], self.size, self.size]
                )
            else:  # 如果是蛇身，使用不同的顏色
                pygame.draw.rect(
                    screen, self.body_color, [segment[0], segment[1], self.size, self.size]
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
                * BLOCK_SIZE
            )
            if all(
                [x != segment[0] or y != segment[1] for segment in snake_body]
            ) and all([x != food["x"] or y != food["y"] for food in foods]):
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


def generate_position() -> tuple:
    x = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    y = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    return (x, y)


def game_over_screen():
    while True:
        screen.fill(LIGHT_GRAY)
        story_render.draw_text(
            screen,
            "Desafortunadamente, x prueba fracasada.:( ¿Te gustaría retomar tu aventura con Don Quijote?",
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

        # events = pygame.event.get()
        # # key_list = pygame.key.get_pressed()

        # # if key_list[pygame.K_RIGHT]:
        # #     print("right")

        # for event in events:
        #     if event.type == pygame.KEYDOWN:
        #         if (
        #             (event.key == pygame.K_LEFT and snake.direction == "LEFT")
        #             or (event.key == pygame.K_RIGHT and snake.direction == "RIGHT")
        #             or (event.key == pygame.K_UP and snake.direction == "UP")
        #             or (event.key == pygame.K_DOWN and snake.direction == "DOWN")
        #         ):
        #             pygame.event.clear(event.type)

        
        # for event in events:
        #     if event.type == pygame.QUIT:
        #         pygame.quit()
        #         sys.exit()
        #     elif event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_LEFT and snake.can_change_direction("LEFT"):
        #             snake.update_direction(-snake.size, 0, "LEFT")
        #         elif event.key == pygame.K_RIGHT and snake.can_change_direction(
        #             "RIGHT"
        #         ):
        #             snake.update_direction(snake.size, 0, "RIGHT")
        #         elif event.key == pygame.K_UP and snake.can_change_direction("UP"):
        #             snake.update_direction(0, -snake.size, "UP")
        #         elif event.key == pygame.K_DOWN and snake.can_change_direction("DOWN"):
        #             snake.update_direction(0, snake.size, "DOWN")

        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # 檢查按鍵狀態，並更新蛇的移動方向
        if keys[pygame.K_LEFT] and snake.can_change_direction("LEFT"):
            snake.update_direction(-snake.size, 0, "LEFT")
        elif keys[pygame.K_RIGHT] and snake.can_change_direction("RIGHT"):
            snake.update_direction(snake.size, 0, "RIGHT")
        elif keys[pygame.K_UP] and snake.can_change_direction("UP"):
            snake.update_direction(0, -snake.size, "UP")
        elif keys[pygame.K_DOWN] and snake.can_change_direction("DOWN"):
            snake.update_direction(0, snake.size, "DOWN")
        
        snake.move()

        if (
            snake.body[0][0] < 0
            or snake.body[0][0] >= SCREEN_WIDTH
            or snake.body[0][1] < INFO_HEIGHT
            or snake.body[0][1] >= SCREEN_HEIGHT
            or snake.check_collision()
        ):
            game_over_screen()

        # print([food_item['name'] for food_item in food.foods])

        for food_item in food.foods:
            if snake.get_rect().colliderect(
                pygame.Rect(food_item["x"], food_item["y"], food.size, food.size)
            ):
                if food_item["name"] == food.target_food[0]:  # 如果吃到了目標食物
                    snake.grow()
                    score += 1
                else:  # 如果吃到了錯誤的食物
                    snake.shrink()
                    score -= 2
                food = Food(snake.body, level_list[level])

        screen.fill(LIGHT_SLATE_GRAY)
        pygame.draw.rect(screen, DIM_GRAY, (0, 0, SCREEN_WIDTH, INFO_HEIGHT))
        snake.draw()
        food.draw()

        score_render.draw_text(screen, "Score:" + str(score))
        target_food_render.draw_text(screen, "Target Food: " + food.target_food[0])

        pygame.display.update()

        if score >= 15:
            level += 1
            if level > 5:
                game_win_screen()
            else:
                game_intro(level)
                score = 0

        if score <= -20:
            game_over_screen()

        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    game_loop()
    # game_win_screen()

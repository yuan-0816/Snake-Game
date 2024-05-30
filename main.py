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
target_food_render = TextRenderer(SCREEN_WIDTH // 2, 0, 200, 50, font_story, text_color=BLACK)

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
        self.body = [[SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 'RIGHT']]
        self.x_change = 0
        self.y_change = 0
        self.direction = 'RIGHT'
        # self.grow()

    def move(self):
        new_head = [self.body[0][0] + self.x_change, self.body[0][1] + self.y_change, self.direction]
        self.body = [new_head] + self.body[:-1]

    def grow(self):
        tail = self.body[-1]
        self.body.append(tail)

    def shrink(self):
        if len(self.body) > 1:
            self.body.pop()
            self.body.pop()

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, BLACK, [segment[0], segment[1], self.size, self.size])

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
    def __init__(self, snake_body, level):
        self.size = BLOCK_SIZE
        self.level = level
        self.foods = self.generate_foods(snake_body)

    def generate_foods(self, snake_body):
        foods = []
        while len(foods) < 10:
            x, y = self.random_position(snake_body, foods)
            name, image = self.random_food()
            foods.append({'name': name, 'image': image, 'x': x, 'y': y})
        return foods


    def random_position(self, snake_body, foods):
        while True:
            x = random.randint(0, (SCREEN_WIDTH - self.size) // BLOCK_SIZE) * BLOCK_SIZE
            y = random.randint(0, (SCREEN_HEIGHT - self.size) // BLOCK_SIZE) * BLOCK_SIZE
            if all([x != segment[0] or y != segment[1] for segment in snake_body]) and all([x != food['x'] or y != food['y'] for food in foods]):
                return x, y


    def random_food(self):
        if self.level.food is not None:
            food_name = random.choice(self.level.food)
            food_image = self.level.food_img[food_name].convert_alpha()
            return food_name, food_image
        else:
            return None, None

    def draw(self):
        for food in self.foods:
            screen.blit(food['image'], (food['x'], food['y']))

    def get_food_rects(self):
        return [pygame.Rect(food['x'], food['y'], self.size, self.size) for food in self.foods]




def game_intro(level, player_name="Player"):
    # print(level_list[level])
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



def generate_position() -> tuple:
    x = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    y = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    return (x, y)



def game_loop():
    game_over = False
    game_close = False
    level = 0


    score = 0

    player_name = login()
    game_intro(level, player_name)
    level += 1
    game_intro(level, player_name)
    snake = Snake()
    food = Food(snake.body, level_list[level])

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
                if event.key == pygame.K_LEFT and snake.x_change == 0:
                    snake.update_direction(-snake.size, 0, 'LEFT')
                elif event.key == pygame.K_RIGHT and snake.x_change == 0:
                    snake.update_direction(snake.size, 0, 'RIGHT')
                elif event.key == pygame.K_UP and snake.y_change == 0:
                    snake.update_direction(0, -snake.size, 'UP')
                elif event.key == pygame.K_DOWN and snake.y_change == 0:
                    snake.update_direction(0, snake.size, 'DOWN')

        snake.move()

        if (snake.body[0][0] < 0 or snake.body[0][0] >= SCREEN_WIDTH or
                snake.body[0][1] < 0 or snake.body[0][1] >= SCREEN_HEIGHT or
                snake.check_collision()):
            game_close = True

        for food_item in food.foods:
            if snake.get_rect().colliderect(pygame.Rect(food_item['x'], food_item['y'], food.size, food.size)):
                if food_item['name'] == level_list[level].food[0]:  # 如果吃到了正確的食物
                    snake.grow()
                    score += 1
                else:  # 如果吃到了錯誤的食物
                    snake.shrink()
                    score -= 2
                food = Food(snake.body, level_list[level])

        screen.fill(WHITE)
        snake.draw()
        food.draw()



        score_render.draw_text(screen, "Score:" + str(score))
        # target_food_render.draw_text(screen, "Target Food:" + food.name)
        pygame.display.update()

        if score >= 2:
            level += 1
            if level > 5:
                game_intro(6)
                pygame.time.delay(3000)
                game_over = True
            else:
                game_intro(level)
                score = 0

        if score <= -10:
            game_close = True

        clock.tick(FPS)

    pygame.quit()
    sys.exit()



if __name__ == '__main__':
    game_loop()


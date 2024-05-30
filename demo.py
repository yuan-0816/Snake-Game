import pygame
import random

# 初始化 Pygame
pygame.init()

# 設置視窗大小
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 800
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake")

# 定義顏色
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 蛇的大小
SNAKE_SIZE = 50

# 載入圖片並縮放
snake_head_img = pygame.transform.scale(pygame.image.load('material/snake.png'), (SNAKE_SIZE, SNAKE_SIZE))
snake_body_img = pygame.transform.scale(pygame.image.load('material/snake_body.png'), (SNAKE_SIZE, SNAKE_SIZE))
snake_tail_img = pygame.transform.scale(pygame.image.load('material/snake_tail.png'), (SNAKE_SIZE, SNAKE_SIZE))
food_img = pygame.transform.scale(pygame.image.load('material/food.png'), (SNAKE_SIZE, SNAKE_SIZE))

# 蛇類別
class Snake:
    def __init__(self):
        self.size = SNAKE_SIZE
        self.body = [[WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, 'RIGHT']]
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
            WINDOW.blit(rotated_img, (segment[0], segment[1]))

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
            x = random.randint(0, (WINDOW_WIDTH - self.size) // SNAKE_SIZE) * SNAKE_SIZE
            y = random.randint(0, (WINDOW_HEIGHT - self.size) // SNAKE_SIZE) * SNAKE_SIZE
            if [x, y, ''] not in snake_body:
                return x, y

    def draw(self):
        WINDOW.blit(food_img, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)

# 主遊戲函數
def game():
    snake = Snake()
    food = Food(snake.body)
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
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

        if (snake.body[0][0] < 0 or snake.body[0][0] >= WINDOW_WIDTH or
                snake.body[0][1] < 0 or snake.body[0][1] >= WINDOW_HEIGHT or
                snake.check_collision()):
            running = False

        if snake.get_rect().colliderect(food.get_rect()):
            snake.grow()
            food = Food(snake.body)

        WINDOW.fill(WHITE)
        snake.draw()
        food.draw()

        pygame.display.update()
        clock.tick(10)

# 執行遊戲
game()

# 關閉 Pygame
pygame.quit()

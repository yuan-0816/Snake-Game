import pygame
import random

# 初始化 Pygame
pygame.init()

# 設置視窗大小
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 600
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('貪食蛇')

# 定義顏色
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 載入圖片
snake_img = pygame.image.load('material/snake.png')
food_img = pygame.image.load('material/food.png')

# 蛇的大小
SNAKE_SIZE = 50

# 蛇類別
class Snake:
    def __init__(self):
        self.size = SNAKE_SIZE
        self.x = WINDOW_WIDTH // 2
        self.y = WINDOW_HEIGHT // 2
        self.x_change = 0
        self.y_change = 0

    def move(self):
        self.x += self.x_change
        self.y += self.y_change

    def draw(self):
        WINDOW.blit(snake_img, (self.x, self.y))

# 食物類別
class Food:
    def __init__(self):
        self.size = SNAKE_SIZE
        self.x = random.randint(0, WINDOW_WIDTH - self.size)
        self.y = random.randint(0, WINDOW_HEIGHT - self.size)

    def draw(self):
        WINDOW.blit(food_img, (self.x, self.y))

# 主遊戲函數
def game():
    snake = Snake()
    food = Food()
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.x_change = -snake.size
                    snake.y_change = 0
                elif event.key == pygame.K_RIGHT:
                    snake.x_change = snake.size
                    snake.y_change = 0
                elif event.key == pygame.K_UP:
                    snake.y_change = -snake.size
                    snake.x_change = 0
                elif event.key == pygame.K_DOWN:
                    snake.y_change = snake.size
                    snake.x_change = 0

        snake.move()

        if snake.x < 0 or snake.x >= WINDOW_WIDTH or snake.y < 0 or snake.y >= WINDOW_HEIGHT:
            running = False

        WINDOW.fill(WHITE)
        snake.draw()
        food.draw()

        pygame.display.update()
        clock.tick(10)

# 執行遊戲
game()

# 關閉 Pygame
pygame.quit()

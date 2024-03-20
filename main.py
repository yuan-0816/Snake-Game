import pygame
import sys

pygame.init()

# 定義顏色
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)
DARK_GRAY = (30, 30, 30)


# 设置屏幕大小
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600

BUTTON_WIDTH = 100
BUTTON_HEIGHT = 50

TEXT_INPUTBOX_WIDTH = 220
TEXT_INPUTBOX_HEIGHT = 50

COMPONENT_GAP = 10



screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake")


font = pygame.font.SysFont('Bauhaus 93', 30)


class Button:
    def __init__(self, x, y, width, height, text, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)


class TextInputBox:
    def __init__(self, x, y, width, height, text=''):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
                if self.text=="Your name":
                    self.text = ""
            else:
                self.active = False
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.active = False
                elif event.key == pygame.K_BACKSPACE:
                    print(self.text)
                    self.text = self.text[:-1]
                else:
                    print(self.text)
                    self.text += event.unicode
                     

    def update(self):
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, GRAY if self.active else DARK_GRAY, self.rect)
        text_surface = font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

# 创建按钮和输入框对象
start_button = Button(int(SCREEN_WIDTH/2 - COMPONENT_GAP - BUTTON_WIDTH), int(SCREEN_HEIGHT/2 + COMPONENT_GAP), 
                      BUTTON_WIDTH, BUTTON_HEIGHT, "START", GRAY)

exit_button = Button(int(SCREEN_WIDTH/2 + COMPONENT_GAP), int(SCREEN_HEIGHT/2 + COMPONENT_GAP), 
                     BUTTON_WIDTH, BUTTON_HEIGHT, "EXIT", GRAY)


text_input = TextInputBox(int(SCREEN_WIDTH/2 - TEXT_INPUTBOX_WIDTH/2), int(SCREEN_HEIGHT/2 - TEXT_INPUTBOX_HEIGHT), TEXT_INPUTBOX_WIDTH, TEXT_INPUTBOX_HEIGHT, 
                          "Your name")

running = True
while running:
    screen.fill(DARK_GRAY)  # 清空畫面並設定背景色

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        text_input.handle_event(event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if exit_button.is_clicked(event.pos):
                running = False
            if start_button.is_clicked(event.pos):
                print("开始游戏")
                print("玩家名称:", text_input.text)

    start_button.draw(screen)
    exit_button.draw(screen)
    text_input.draw(screen)

    pygame.display.flip()  # 更新畫面

pygame.quit()
sys.exit()




if __name__ == '__main__':
    pass
import pygame
import sys
import random
from config import *


def Genrate_Food(food_dict: dict) -> str:

    food_list = list(food_dict.keys())
    random_food = random.choice(food_list)
    food_image_path = food_dict[random_food]
    return food_image_path


class Button:
    def __init__(self, x, y, width, height, text, color, font):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.font = font

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = self.font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)


class TextInputBox:
    def __init__(self, x, y, width, height, text="", font=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.active = False
        self.font = font

    def handle_event(self, event) -> str:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
                if self.text == "Your name":
                    self.text = ""
            else:
                self.active = False
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.active = False
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if len(self.text) < 10:  # 增加這一行來限制字數
                        self.text += event.unicode
        return self.text

    def update(self):
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, GRAY if self.active else DARK_GRAY, self.rect)
        text_surface = self.font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)


class TextRenderer:
    def __init__(self, x, y, width, height, font, text_color=(0, 0, 0), bg_color=None):
        pygame.font.init()
        self.font = font
        self.text_color = text_color
        self.bg_color = bg_color
        self.rect = pygame.Rect(x, y, width, height)


    def draw_text(self, screen, text, aa=False):
        """
        Draw text on the screen with word wrapping.
        """
        y = self.rect.top
        line_spacing = -2

        # Get the height of the font
        font_height = self.font.size("Tg")[1]

        while text:
            i = 1

            # Determine if the row of text will be outside our area
            if y + font_height > self.rect.bottom:
                break

            # Determine maximum width of line
            while self.font.size(text[:i])[0] < self.rect.width and i < len(text):
                i += 1

            # If we've wrapped the text, then adjust the wrap to the last word
            if i < len(text):
                i = text.rfind(" ", 0, i) + 1

            # Render the line and blit it to the screen
            if self.bg_color:
                image = self.font.render(text[:i], 1, self.text_color, self.bg_color)
                image.set_colorkey(self.bg_color)
            else:
                image = self.font.render(text[:i], aa, self.text_color)

            screen.blit(image, (self.rect.left, y))
            y += font_height + line_spacing

            # Remove the text we just blitted
            text = text[i:]




pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake")

font_title = pygame.font.SysFont("Rockwell Condensed", 45)
font_story = pygame.font.SysFont("Rockwell Condensed", 30)
# font_story = pygame.font.SysFont("Viner Hand ITC", 26)




game_state = STATE_LOGIN
start_button = Button(
    int(SCREEN_WIDTH / 2 - COMPONENT_GAP - BUTTON_WIDTH),
    int(SCREEN_HEIGHT / 2 + COMPONENT_GAP),
    BUTTON_WIDTH,
    BUTTON_HEIGHT,
    "START",
    GRAY,
    font_title,
)

exit_button = Button(
    int(SCREEN_WIDTH / 2 + COMPONENT_GAP),
    int(SCREEN_HEIGHT / 2 + COMPONENT_GAP),
    BUTTON_WIDTH,
    BUTTON_HEIGHT,
    "EXIT",
    GRAY,
    font_title,
)

text_input = TextInputBox(
    int(SCREEN_WIDTH / 2 - TEXT_INPUTBOX_WIDTH / 2),
    int(SCREEN_HEIGHT / 2 - TEXT_INPUTBOX_HEIGHT),
    TEXT_INPUTBOX_WIDTH,
    TEXT_INPUTBOX_HEIGHT,
    "Your name",
    font_title,
)



text_renderer = TextRenderer(50, 150, SCREEN_WIDTH-75, SCREEN_HEIGHT-50+200, font_story)

PLAYER_NAME = None



def Login(event):

    global game_state
    global PLAYER_NAME
    screen.fill(DARK_GRAY)

    PLAYER_NAME = text_input.handle_event(event)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if exit_button.is_clicked(event.pos):
            game_state = STATE_QUIT
        if start_button.is_clicked(event.pos):
            game_state = STATE_STORY

    start_button.draw(screen)
    exit_button.draw(screen)
    text_input.draw(screen)


def Story(event, Level_class):
    global game_state
    screen.fill(GRAY)

    TextInputBox(
        COMPONENT_GAP,
        COMPONENT_GAP,
        SCREEN_WIDTH - 2 * COMPONENT_GAP,
        100,
        Level_class.title,
        font_title,
    ).draw(screen)

    text_renderer.draw_text(screen, Recap.story.format(PLAYER_NAME=PLAYER_NAME))

    next_button = Button(
        int(SCREEN_WIDTH - BUTTON_WIDTH - COMPONENT_GAP),
        int(SCREEN_HEIGHT - BUTTON_HEIGHT - COMPONENT_GAP),
        BUTTON_WIDTH - COMPONENT_GAP,
        BUTTON_HEIGHT - COMPONENT_GAP,
        "NEXT",
        LIGHT_GRAY,
        font_title,
    )

    if event.type == pygame.MOUSEBUTTONDOWN:
        if next_button.is_clicked(event.pos):
            game_state = STATE_RUNNING

    next_button.draw(screen)

def main():
    global game_state
    while game_state != STATE_QUIT:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif game_state == STATE_LOGIN:
                Login(event)
            elif game_state == STATE_STORY:
                Story(event, Level2)
            elif game_state == STATE_RUNNING:
                screen.fill(GRAY)

        pygame.display.flip()  # 更新畫面

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()

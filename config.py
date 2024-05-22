

# ------------------------------------ 顏色 ------------------------------------ #
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)
DARK_GRAY = (30, 30, 30)


# ----------------------------------- 物件大小 ----------------------------------- #
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600

BUTTON_WIDTH = 100
BUTTON_HEIGHT = 50

TEXT_INPUTBOX_WIDTH = 220
TEXT_INPUTBOX_HEIGHT = 50

COMPONENT_GAP = 10

# ----------------------------------- 遊戲狀態 ----------------------------------- #
STATE_PLOT = 0
STATE_START = 1
STATE_RUNNING = 2
STATE_GAME_OVER = 3


# ----------------------------------- 玩家名稱 ----------------------------------- #
PLAYER_NAME = "YUAN"


# ------------------------------------ 故事 ------------------------------------ #
class Recap:
    story = '''
            Érase una vez, Alonso Quijano, un hidalgo a quien le encantaba leer novelas de caballerías, 
            se nombró don Quijote de la Mancha. Durante su aventura en solitario pidió a un ventero que 
            dirigiera la ceremonia de nombramiento de caballero y se convirtió oficialmente en el caballero 
            andante Don Quijote. Cuando todo estaba listo, nuestro protagonista, a lomos de su corcel 
            Rocinante junto con su escudero, Sancho Panza, y con la fe en su dama imaginaria, Dulcinea, 
            se marcharon en busca de aventuras. ¿{PLAYER_NAME}, estás listo/a para realizar viajes más insólito con él? ¡Vámonos!
            '''

class Level1:
    title = "Primera prueba: Preparación"
    story = '''
            Don Quijote se prepara para emprender sus aventuras 
            ¡Conozcamos a algunos de los personajes principales de la historia 
            y los objetos que deben preparar antes de la partida!
            '''
    object = [
                "Alonso Quijano",         # 唐吉軻德
                "armadura",               # 盔甲
                "caballo Rocinante",      # 馬
                "lanza",                  # 長矛
                "escudero",               # 隨從
                "novela de caballerías",  # 騎士小說
                "Dulcinea del Toboso",    # 一個女的
                "Asno Rucio",             # 驢子
                "alforjas",               # 馬鞍掛袋
                "ventero"                 # 客棧主人
              ]

    
    
              

    




if __name__ == '__main__':
    print(Level1.story.format(PLAYER_NAME=PLAYER_NAME))


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

BLOCK_SIZE = 20

# ----------------------------------- 遊戲狀態 ----------------------------------- #
STATE_LOGIN = 0
STATE_RUNNING = 1
STATE_GAME_OVER = 2


# ----------------------------------- 玩家名稱 ------------------------------------ #
PLAYER_NAME = "Juan"



# ----------------------------------- 關卡和食物 ---------------------------------- #
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
    
    food = {
                "Alonso Quijano": "./material/food.png",           # 唐吉軻德
                "armadura": "./material/food.png",                 # 盔甲
                "caballo Rocinante": "./material/food.png",        # 馬
                "lanza": "./material/food.png",                    # 長矛
                "escudero": "./material/food.png",                 # 隨從
                "novela de caballerías": "./material/food.png",    # 騎士小說
                "Dulcinea del Toboso": "./material/food.png",      # 一個女的
                "Asno Rucio": "./material/food.png",               # 驢子
                "alforjas": "./material/food.png",                 # 馬鞍掛袋
            }
    

class Level2:
    title = "Segunda prueba: La aventura de los molinos de viento"
    story = '''
            Don Quijote se prepara para emprender sus aventuras 
            ¡Conozcamos a algunos de los personajes principales de la historia 
            y los objetos que deben preparar antes de la partida!
            '''
    
    food = {
                "Alonso Quijano": "./material/food.png",           # 唐吉軻德
                "armadura": "./material/food.png",                 # 盔甲
                "caballo Rocinante": "./material/food.png",        # 馬
                "lanza": "./material/food.png",                    # 長矛
                "escudero": "./material/food.png",                 # 隨從
                "novela de caballerías": "./material/food.png",    # 騎士小說
                "Dulcinea del Toboso": "./material/food.png",      # 一個女的
                "Asno Rucio": "./material/food.png",               # 驢子
                "alforjas": "./material/food.png",                 # 馬鞍掛袋
            }
    


# ---------------------------------- Method ---------------------------------- #
    
              

    




if __name__ == '__main__':
    print(Level1.story.format(PLAYER_NAME=PLAYER_NAME))
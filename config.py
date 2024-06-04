import pygame

pygame.init()


# ------------------------------------ 顏色 ------------------------------------ #
WHITE = (255, 255, 255)
LIGHT_GRAY = (211, 211, 211)
SILVER = (192, 192, 192)
GRAY = (128, 128, 128)
DIM_GRAY = (105, 105, 105)
DARK_GRAY = (30, 30, 30)
BLACK = (0, 0, 0)
GAINSBORO = (220, 220, 220)
SMOKE = (245, 245, 245)
SLATE_GRAY = (112, 128, 144)
LIGHT_SLATE_GRAY = (119, 136, 153)
DARK_SLATE_GRAY = (47, 79, 79)

HEART_RED = (219, 99, 99)

# ----------------------------------- 物件大小 ----------------------------------- #

INFO_HEIGHT = 60

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 800 + INFO_HEIGHT
SCREEN_CENTER = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


COMPONENT_GAP = 10

BUTTON_WIDTH = 200
BUTTON_HEIGHT = 60

TEXT_INPUTBOX_WIDTH = BUTTON_WIDTH * 2 + COMPONENT_GAP * 2
TEXT_INPUTBOX_HEIGHT = 60



INTRO_GAP = 50

TITLE_WIDTH = SCREEN_WIDTH - 2 * INTRO_GAP
TITLE_HEIGHT = 100
STORY_WIDTH = SCREEN_WIDTH - 2 * INTRO_GAP
STORY_HEIGHT = 600

NEXT_LEVEL_WIDTH = 300
NEXT_LEVEL_HEIGHT = 50


BLOCK_SIZE = 50
FPS = 60

# ----------------------------------- 關卡和食物 ---------------------------------- #
# 第一關：primera
# 第二關：segunda
# 第三關：tercera
# 第四關：cuarta
# 第五關：quinta

error_sound = pygame.mixer.Sound("./material/sound/error.wav")
type_sound = pygame.mixer.Sound("./material/sound/type.wav")
button_sound = pygame.mixer.Sound("./material/sound/button.mp3")


LEVEL_NAMES = ["primera", "segunda", "tercera", "cuarta", "quinta"]

class Recap:
    title = 'Introducción'
    story = '   Érase una vez, Alonso Quijano, un hidalgo a quien le encantaba leer novelas de caballerías, se nombró don Quijote de la Mancha. Durante su aventura en solitario pidió a un ventero que dirigiera la ceremonia de nombramiento de caballero y se convirtió oficialmente en el caballero andante Don Quijote.\n   Cuando todo estaba listo, nuestro protagonista, a lomos de su corcel Rocinante junto con su escudero, Sancho Panza, y con la fe en su dama imaginaria, Dulcinea, se marcharon en busca de aventuras. ¿{PLAYER_NAME}, estás listo/a para realizar viajes más insólito con él? ¡Vámonos!'
    food = None


class Level1:
    title = "Primera prueba: Preparación"
    story = "    Don Quijote se prepara para emprender sus aventuras ¡Conozcamos a algunos de los personajes principales de la historia y los objetos que deben preparar antes de la partida!"

    food_img = {
        "Alonso Quijano": pygame.image.load("./material/food/1_1_alonso_quijano.png"),                  # 唐吉軻德
        "armadura": pygame.image.load("./material/food/1_2_armadura.png"),                              # 盔甲
        "caballo Rocinante": pygame.image.load("./material/food/1_3_caballo_Rociante.png"),             # 馬
        "lanza": pygame.image.load("./material/food/1_4_lanza.png"),                                    # 長矛
        "escudero": pygame.image.load("./material/food/1_5_escudero_Sancho_Panza.png"),                 # 隨從
        "novela de caballerías": pygame.image.load("./material/food/1_6_novela_de_cabalerias.png"),     # 騎士小說
        "Dulcinea del Toboso": pygame.image.load("./material/food/1_7_Dulcinea_de_Toboso.png"),         # 一個女的
        "Asno Rucio": pygame.image.load("./material/food/1_8_asno_Rucio.png"),                          # 驢子
        "alforjas": pygame.image.load("./material/food/1_9_alforjas.png"),                              # 馬鞍掛袋
        "ventero": pygame.image.load("./material/food/1_10_ventero.png"),                               # 客棧主人
    }

    food_sound = {
        "Alonso Quijano": pygame.mixer.Sound("./material/sound/1_1_alonso_quijano.wav"),                  # 唐吉軻德
        "armadura": pygame.mixer.Sound("./material/sound/1_2_armadura.wav"),                              # 盔甲
        "caballo Rocinante": pygame.mixer.Sound("./material/sound/1_3_caballo_rocinante.wav"),             # 馬
        "lanza": pygame.mixer.Sound("./material/sound/1_4_lanza.wav"),                                    # 長矛
        "escudero": pygame.mixer.Sound("./material/sound/1_5_escudero.wav"),                 # 隨從
        "novela de caballerías": pygame.mixer.Sound("./material/sound/1_6_novela_de_caballerias.wav"),     # 騎士小說
        "Dulcinea del Toboso": pygame.mixer.Sound("./material/sound/1_7_dulcinea_del_toboso.wav"),         # 一個女的
        "Asno Rucio": pygame.mixer.Sound("./material/sound/1_8_asno_rucio.wav"),                          # 驢子
        "alforjas": pygame.mixer.Sound("./material/sound/1_9_alforjas.wav"),                              # 馬鞍掛袋
        "ventero": pygame.mixer.Sound("./material/sound/1_10_ventero.wav"),                               # 客棧主人
    }

    

    food = [
        "Alonso Quijano",
        "armadura",
        "caballo Rocinante",
        "lanza",
        "escudero",
        "novela de caballerías",
        "Dulcinea del Toboso",
        "Asno Rucio",
        "alforjas",
        "ventero",
    ]


class Level2:
    title = "Segunda prueba: La aventura de los molinos de viento"
    story = "    Por el campo de Montiel, Don Quijote y su escudero encontraron decenas de molinos de viento con aspas enormes. Don Quijote pensó que el Mago Frestón convirtió los molinos de viento en unos gigantes malignos que no paraban de mover sus brazos, por eso quiso entrar en batalla contra ellos. ¡Ayudemos a Don Quijote a derrotar a los enemigos que viven en su imaginación!"

    food_img = {
        "molinos de viento": pygame.image.load("./material/food/2_1_molinos_de_viento.png"),  # 風車
        "imaginación": pygame.image.load("./material/food/2_2_imaginacion.png"),  # 想像
        "batalla": pygame.image.load("./material/food/2_3_batalla.png"),  # 戰爭
        "gigante": pygame.image.load("./material/food/2_4_gigante.png"),  # 巨人
        "brazo": pygame.image.load("./material/food/2_5_brazo.png"),  # 手臂
        "aspa": pygame.image.load("./material/food/2_6_aspa.png"),  # 風車架
        "espuela": pygame.image.load("./material/food/2_7_espuela.png"),  # 馬刺
        "golpe": pygame.image.load("./material/food/2_8_golpe.png"),  # 撞擊
        "caída": pygame.image.load("./material/food/2_9_caida.png"),  # 跌倒
        "Mago Frestón": pygame.image.load("./material/food/2_10_mago_freston.png"),  # 魔法師
    }

    food_sound = {
        "molinos de viento": pygame.mixer.Sound("./material/sound/2_1_molinos_de_viento.wav"),  # 風車
        "imaginación": pygame.mixer.Sound("./material/sound/2_2_imaginacion.wav"),  # 想像
        "batalla": pygame.mixer.Sound("./material/sound/2_3_batalla.wav"),  # 戰爭
        "gigante": pygame.mixer.Sound("./material/sound/2_4_gigante.wav"),  # 巨人
        "brazo": pygame.mixer.Sound("./material/sound/2_5_brazo.wav"),  # 手臂
        "aspa": pygame.mixer.Sound("./material/sound/2_6_aspa.wav"),  # 風車架
        "espuela": pygame.mixer.Sound("./material/sound/2_7_espuela.wav"),  # 馬刺
        "golpe": pygame.mixer.Sound("./material/sound/2_8_golpe.wav"),  # 撞擊
        "caída": pygame.mixer.Sound("./material/sound/2_9_caida.wav"),  # 跌倒
        "Mago Frestón": pygame.mixer.Sound("./material/sound/2_10_mago_freston.wav"),  # 魔法師
    }

    food = [
        "molinos de viento",
        "imaginación",
        "batalla",
        "gigante",
        "brazo",
        "aspa",
        "espuela",
        "golpe",
        "caída",
        "Mago Frestón"
    ]

class Level3:
    title = "Tercera prueba: La batalla de los rebaños de ovejas"
    story = "    Una mañana, cuando Don Quijote estaba caminando, vio desde una loma gran polvareda y en seguida escuchaba el tocar de clarín y tambor, y pensó que fue el pagano Alifanfarón y su ejército que venían a combatir contra Pentapolín del Arremangado Brazo, porque el primero se enamoró de la hija del segundo y quería secuestrar a la bella joven. Don Quijote estaba del lado de Pentapolín, pero en realidad el ejército era un rebaño de ovejas inocentes. ¿Estás listo/a para afrontar este desafío?"

    food_img = {
        "loma": pygame.image.load("./material/food/3_1_loma.png"),  # 山丘
        "polvareda": pygame.image.load("./material/food/3_2_polvareda.jpg"),  # 大灰霧
        "ejército": pygame.image.load("./material/food/3_3_ejercito.png"),  # 軍隊
        "tambor y trompeta": pygame.image.load("./material/food/3_4_tambor_y_trompeta.png"),  # 鼓、小號
        "pastor": pygame.image.load("./material/food/3_5_pastor.png"),  # 牧羊人
        "rebaño de ovejas": pygame.image.load("./material/food/3_6_rebano_de_ovejas.png"),  # 羊群
        "honda y piedra": pygame.image.load("./material/food/3_7_honda_y_piedra.png"),  # 彈弓、石頭
        "bálsamo de Fierabrás": pygame.image.load("./material/food/3_8_balsamo_de_fierabras.png"),  # 療傷藥油
        "celada": pygame.image.load("./material/food/3_9_celada.png"),  # 頭盔
        "dientes": pygame.image.load("./material/food/3_10_dientes.png"),  # 牙齒
    }

    food_sound = {
        "loma": pygame.mixer.Sound("./material/sound/3_1_loma.wav"),  # 山丘
        "polvareda": pygame.mixer.Sound("./material/sound/3_2_polvareda.wav"),  # 大灰霧
        "ejército": pygame.mixer.Sound("./material/sound/3_3_ejercito.wav"),  # 軍隊
        "tambor y trompeta": pygame.mixer.Sound("./material/sound/3_4_tambor_y_trompeta.wav"),  # 鼓、小號
        "pastor": pygame.mixer.Sound("./material/sound/3_5_pastor.wav"),  # 牧羊人
        "rebaño de ovejas": pygame.mixer.Sound("./material/sound/3_6_rebano_de_ovejas.wav"),  # 羊群
        "honda y piedra": pygame.mixer.Sound("./material/sound/3_7_honda_y_piedra.wav"),  # 彈弓、石頭
        "bálsamo de Fierabrás": pygame.mixer.Sound("./material/sound/3_8_balsamo_de_fierabras.wav"),  # 療傷藥油
        "celada": pygame.mixer.Sound("./material/sound/3_9_celada.wav"),  # 頭盔
        "dientes": pygame.mixer.Sound("./material/sound/3_10_dientes.wav"),  # 牙齒
    }   

    food = [
        "loma",
        "polvareda",
        "ejército",
        "tambor y trompeta",
        "pastor",
        "rebaño de ovejas",
        "honda y piedra",
        "bálsamo de Fierabrás",
        "celada",
        "dientes"
    ] 


class Level4:
    title = "Cuarta prueba: La batalla contra los cueros de vino"
    story = "    Acompañado por el cura, el barbero, la princesa Micomicona y Sancho, Don Quijote finalizó su penitencia en Sierra Morena, y todos fueron a la venta de Juan Palomeque para pasar la noche. Mientras los huéspedes escuchaban al cura leyendo un libro de caballería sacado del baúl del ventero, de repente oyeron a Sancho pidiendo ayuda, porque don Quijote empezó otra guerra.\n    Esta vez se trató de una batalla contra los cueros de vino del ventero en pleno sueño de nuestro caballero. Pensó que los cueros de vino eran las cabezas de los gigantes. Para eliminar a los diablos que le perseguían, metió cuchilladas a los cueros y provocó ríos de sangre por el desván. ¡Vayamos a detener esta farsa!"

    food_img = {
        "cura y barbero": pygame.image.load("./material/food/4_1_cura_y_barbero.png"),  # 牧師和理髮師
        "venta de Juan Palomeque": pygame.image.load("./material/food/4_2_venta_de_Juan_Palomeque.png"),  # 旅店
        "baúl de libros de caballería": pygame.image.load("./material/food/4_3_baul_de_libros_de_caballeria.png"),  # 寶藏箱
        "desván": pygame.image.load("./material/food/4_4_desvan.png"),  # 閣樓
        "espada": pygame.image.load("./material/food/4_5_cuchillada_de_espada.png"),  # 劍
        "cabeza de gigante": pygame.image.load("./material/food/4_6_cabeza_de_gigante.png"),  # 巨人的頭
        "cuero de vino": pygame.image.load("./material/food/4_7_cuero_de_vino.png"),  # 酒囊
        "río de sangre": pygame.image.load("./material/food/4_8_rio_de_sangre.jpg"),  # 血河
        "sonámbulo": pygame.image.load("./material/food/4_9_sonambulo.png"),  # 夢遊
        "caldero de agua fría": pygame.image.load("./material/food/4_10_caldero_de_agua_fria.png"),  # 冷水鍋
    }

    food_sound = {
        "cura y barbero": pygame.mixer.Sound("./material/sound/4_1_cura_y_barbero.wav"),  # 牧師和理髮師
        "venta de Juan Palomeque": pygame.mixer.Sound("./material/sound/4_2_venta_de_Juan_Palomeque.wav"),  # 旅店
        "baúl de libros de caballería": pygame.mixer.Sound("./material/sound/4_3_baul_de_libros_de_caballeria.wav"),  # 寶藏箱
        "desván": pygame.mixer.Sound("./material/sound/4_4_desvan.wav"),  # 閣樓
        "espada": pygame.mixer.Sound("./material/sound/4_5_espada.wav"),  # 劍
        "cabeza de gigante": pygame.mixer.Sound("./material/sound/4_6_cabeza_de_gigante.wav"),  # 巨人的頭
        "cuero de vino": pygame.mixer.Sound("./material/sound/4_7_cuero_de_vino.wav"),  # 酒囊
        "río de sangre": pygame.mixer.Sound("./material/sound/4_8_rio_de_sangre.wav"),  # 血河
        "sonámbulo": pygame.mixer.Sound("./material/sound/4_9_sonambulo.wav"),  # 夢遊
        "caldero de agua fría": pygame.mixer.Sound("./material/sound/4_10_caldero_de_agua_fria.wav"),  # 冷水鍋
    }

    food = [
        "cura y barbero",
        "venta de Juan Palomeque",
        "baúl de libros de caballería",
        "desván",
        "espada",
        "cabeza de gigante",
        "cuero de vino",
        "río de sangre",
        "sonámbulo",
        "caldero de agua fría"
    ]


class Level5:
    title = "Quinta prueba: La última batalla con el Caballero de la Blanca Luna"
    story = "    Bajo la cuidadosa planificación de su amigo aldeano, Sansón Carrasco, Don Quijote encontró al Caballero de la Blanca Luna que sostenía un escudo con dibujo de luna en la playa de Barcelona. Vino a competir porque se enteró de las hazañas heroicas de Don Quijote y pidió que el vencido tuviera que regresar a su pueblo natal y que no pudiera volver a la aventura del caballero durante un año. Además, tenía que aceptar que había mujeres más bellas que Dulcinea en el mundo. Don Quijote aceptó el reto de mala gana."

    food_img = {
        "playa de Barcelona": pygame.image.load("./material/food/5_1_playa_de_Barcelona.png"),  # 巴塞隆納海邊
        "bachiller Sansón Carrasco": pygame.image.load("./material/food/5_2_bachiller_Sanson_Carrasco.png"),  # 學士
        "caballero de la Blanca Luna": pygame.image.load("./material/food/5_3_caballero_de_la_Blanca_Luna.png"),  # 白月騎士
        "duelo": pygame.image.load("./material/food/5_4_duelo.png"),  # 決鬥
        "escudo": pygame.image.load("./material/food/5_5_escudo.png"),  # 盾牌
        "herencia": pygame.image.load("./material/food/5_6_herencia.png"),  # 遺產
        "derrota": pygame.image.load("./material/food/5_7_derrota.png"),  # 失敗
        "tristeza": pygame.image.load("./material/food/5_8_tristeza.png"),  # 難過
        "testamento": pygame.image.load("./material/food/5_9_testamento.png"),  # 遺書
        "muerte": pygame.image.load("./material/food/5_10_muerte.png"),  # 死亡
    }

    food_sound = {
        "playa de Barcelona": pygame.mixer.Sound("./material/sound/5_1_playa_de_Barcelona.wav"),  # 巴塞隆納海邊
        "bachiller Sansón Carrasco": pygame.mixer.Sound("./material/sound/5_2_bachiller_Sanson_Carrasco.wav"),  # 學士
        "caballero de la Blanca Luna": pygame.mixer.Sound("./material/sound/5_3_caballero_de_la_Blanca_Luna.wav"),  # 白月騎士
        "duelo": pygame.mixer.Sound("./material/sound/5_4_duelo.wav"),  # 決鬥
        "escudo": pygame.mixer.Sound("./material/sound/5_5_escudo.wav"),  # 盾牌
        "herencia": pygame.mixer.Sound("./material/sound/5_6_herencia.wav"),  # 遺產
        "derrota": pygame.mixer.Sound("./material/sound/5_7_derrota.wav"),  # 失敗
        "tristeza": pygame.mixer.Sound("./material/sound/5_8_tristeza.wav"),  # 難過
        "testamento": pygame.mixer.Sound("./material/sound/5_9_testamento.wav"),  # 遺書
        "muerte": pygame.mixer.Sound("./material/sound/5_10_muerte.wav"),  # 死亡
    }

    food = [
        "playa de Barcelona",
        "bachiller Sansón Carrasco",
        "caballero de la Blanca Luna",
        "duelo",
        "escudo",
        "herencia",
        "derrota",
        "tristeza",
        "testamento",
        "muerte"
    ]


class Conclusion:
    title = None
    story = "    Don Quijote perdió este duelo decisivo y regresó a su pueblo natal como había prometido. Después de regresar, sufrió fiebre alta y estuvo reposando en cama durante varios días. Un día despertó repentinamente y dijo a todos que él ya no era Don Quijote, sino Alonso Quijano. Sintió que se estaba muriendo, por lo que comenzó a hacer testamento, dejando su herencia a su sobrina y a Sancho. Tres días después, Alonso Quijano puso fin a su legendaria vida."
    food = None





# ---------------------------------- Object ---------------------------------- #
class Button:
    def __init__(self, x, y, width, height, text, color, font):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.font = font

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=15)
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
                button_sound.play()
                self.active = not self.active
                if self.text == "Nombre:":
                    self.text = ""
            else:
                self.active = False
        if event.type == pygame.KEYDOWN:
            if self.active:
                type_sound.play()
                if event.key == pygame.K_RETURN:
                    self.active = False
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if len(self.text) < 15:  # 增加這一行來限制字數
                        self.text += event.unicode
        return self.text

    def update(self):
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, GRAY if self.active else DARK_GRAY, self.rect, border_radius=15)
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
        Draw text on the screen with word wrapping and handling newlines.
        """
        if text is None:
            return  # If text is None, do nothing

        y = self.rect.top
        line_spacing = -2

        # Get the height of the font
        font_height = self.font.size("Tg")[1]

        # Split the text into lines based on newline characters
        lines = text.split('\n')

        for line in lines:
            while line:
                i = 1

                # Determine if the row of text will be outside our area
                if y + font_height > self.rect.bottom:
                    break

                # Determine maximum width of line
                while self.font.size(line[:i])[0] < self.rect.width and i < len(line):
                    i += 1

                # If we've wrapped the text, then adjust the wrap to the last word
                if i < len(line):
                    i = line.rfind(" ", 0, i) + 1

                # Render the line and blit it to the screen
                if self.bg_color:
                    image = self.font.render(line[:i], 1, self.text_color, self.bg_color)
                    image.set_colorkey(self.bg_color)
                else:
                    image = self.font.render(line[:i], aa, self.text_color)

                screen.blit(image, (self.rect.left, y))
                y += font_height + line_spacing

                # Remove the text we just blitted
                line = line[i:]

            # After each line (split by \n), move to the next line
            y += font_height + line_spacing






if __name__ == "__main__":
    # print(Level1.story.format(PLAYER_NAME="Yuan"))
    # y = random.randint(int(INFO_HEIGHT//BLOCK_SIZE), (SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
    # print(int(INFO_HEIGHT//BLOCK_SIZE))
    # print((SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE)

    pass

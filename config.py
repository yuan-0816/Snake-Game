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

# ----------------------------------- 物件大小 ----------------------------------- #
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

BUTTON_WIDTH = 110
BUTTON_HEIGHT = 60

TEXT_INPUTBOX_WIDTH = 240
TEXT_INPUTBOX_HEIGHT = 60

COMPONENT_GAP = 10

BLOCK_SIZE = 20

# ----------------------------------- 遊戲狀態 ----------------------------------- #
STATE_LOGIN = 0
STATE_STORY = 1
STATE_RUNNING = 2
STATE_GAME_OVER = 3
STATE_QUIT = 4



# ----------------------------------- 關卡和食物 ---------------------------------- #
class Recap:
    title = None
    story = """
            Érase una vez, Alonso Quijano, un hidalgo a quien le encantaba leer novelas de caballerías, se nombró don Quijote de la Mancha. Durante su aventura en solitario pidió a un ventero que dirigiera la ceremonia de nombramiento de caballero y se convirtió oficialmente en el caballero andante Don Quijote. 
            Cuando todo estaba listo, nuestro protagonista, a lomos de su corcel Rocinante junto con su escudero, Sancho Panza, y con la fe en su dama imaginaria, Dulcinea, se marcharon en busca de aventuras. ¿{PLAYER_NAME}, estás listo/a para realizar viajes más insólito con él? ¡Vámonos!

            """
    food = None


class Level1:
    title = "Primera prueba: Preparación"
    story = """
            Don Quijote se prepara para emprender sus aventuras 
            ¡Conozcamos a algunos de los personajes principales de la historia 
            y los objetos que deben preparar antes de la partida!
            """

    food = {
        "Alonso Quijano": "./material/food/1_1_alonso_quijano.png",                 # 唐吉軻德
        "armadura": "./material/food/1_2_armadura.png",                             # 盔甲
        "caballo Rocinante": "./material/food/1_3_caballo_Rociante.png",            # 馬
        "lanza": "./material/food/1-4_lanza.png",                                   # 長矛
        "escudero": "./material/food/1_5_escudero_Sancho_Panza.png",                # 隨從
        "novela de caballerías": "./material/food/1_6_novela_de_cabalerias.png",    # 騎士小說
        "Dulcinea del Toboso": "./material/food/1_7_Dulcinea_de_Toboso.png",        # 一個女的
        "Asno Rucio": "./material/food/1_8_asno_Rucio.png",                         # 驢子
        "alforjas": "./material/food/1_9_alforjas.png",                             # 馬鞍掛袋
        "ventero": "./material/food/1_10_ventero.png"                               # 客棧主人
    }


class Level2:
    title = "Segunda prueba: La aventura de los molinos de viento"
    story = """
            Por el campo de Montiel, Don Quijote y su escudero encontraron decenas de molinos de viento con aspas enormes. Don Quijote pensó que el Mago Frestón convirtió los molinos de viento en unos gigantes malignos que no paraban de mover sus brazos, por eso quiso entrar en batalla contra ellos. ¡Ayudemos a Don Quijote a derrotar a los enemigos que viven en su imaginación!
            """

    food = {
        "molinos de viento": "./material/food/2_1_molinos_de_viento.png",   # 風車
        "imaginación": "./material/food/2_2_imaginacion.png",               # 想像
        "batalla": "./material/food/2_3_batalla.png",                       # 戰爭
        "gigante": "./material/food/2_4_gigante.png",                       # 巨人
        "brazo": "./material/food/2_5_brazo.png",                           # 手臂
        "aspa": "./material/food/2_6_aspa.png",                             # 風車架
        "espuela": "./material/food/2_7_espuela.png",                       # 馬刺
        "golpe": "./material/food/2_8_golpe.png",                           # 撞擊
        "caída": "./material/food/2_9_caida.png",                           # 跌倒
        "Mago Frestón": "./material/food/2_10_mago_freston.png"             # 魔法師
    }


class Level3:
    title = "Tercera prueba: La batalla de los rebaños de ovejas"
    story = """
            Una mañana, cuando Don Quijote estaba caminando, vio desde una loma gran polvareda y en seguida escuchaba el tocar de clarín y tambor, y pensó que fue el pagano Alifanfarón y su ejército que venían a combatir contra Pentapolín del Arremangado Brazo, porque el primero se enamoró de la hija del segundo y quería secuestrar a la bella joven.
            Don Quijote estaba del lado de Pentapolín, pero en realidad el "ejército" era un rebaño de ovejas inocentes. ¿Estás listo/a para afrontar este desafío?

            """
    
    food = {
        "loma": "./material/food/3_1_loma.png",                                 # 山丘
        "polvareda": "./material/food/3_2_polvareda.jpg",                       # 大灰霧
        "ejército": "./material/food/3_3_ejercito.png",                         # 軍隊
        "tambor y trompeta": "./material/food/3_4_tambor_y_trompeta.png",       # 鼓、小號
        "pastor": "./material/food/3_5_pastor.png",                             # 牧羊人
        "rebaño de ovejas": "./material/food/3_6_rebano_de_ovejas.png",         # 羊群
        "honda y piedra": "./material/food/3_7_honda_y_piedra.png",             # 彈弓、石頭
        "bálsamo de Fierabrás": "./material/food/3_8_balsamo_de_fierabras.png", # 療傷藥油
        "celada": "./material/food/3_9_celada.png",                             # 頭盔
        "dientes": "./material/food/3_10_dientes.png"                           # 牙齒
    }


class Level4:
    title = "Cuarta prueba: La batalla contra los cueros de vino"
    story = """
            Acompañado por el cura, el barbero, la princesa Micomicona y Sancho, Don Quijote finalizó su penitencia en Sierra Morena, y todos fueron a la venta de Juan Palomeque para pasar la noche. Mientras los huéspedes escuchaban al cura leyendo un libro de caballería sacado del baúl del ventero, de repente oyeron a Sancho pidiendo ayuda, porque don Quijote empezó otra guerra.
            Esta vez se trató de una batalla contra los cueros de vino del ventero en pleno sueño de nuestro caballero. Pensó que los cueros de vino eran las cabezas de los gigantes. Para eliminar a los diablos que le perseguían, metió cuchilladas a los cueros y provocó ríos de sangre por el desván. ¡Ven a detener esta farsa!

            """
   
    food = {
        "cura y barbero": "./material/food/4_1_cura_y_barbero.png",             # 牧師和理髮師
        "venta de Juan Palomeque": "./material/food/4_2_venta_de_Juan_Palomeque.png",   # 旅店
        "baúl de libros de caballería": "./material/food/4_3_baul_de_libros_de_caballeria.png",   # 寶藏相
        "desván": "./material/food/4_4_desvan.png",                             # 閣樓
        "cuchillada de espada": "./material/food/4_5_cuchillada_de_espada.png",   # 劍
        "cabeza de gigante": "./material/food/4_6_cabeza_de_gigante.png",       # 巨人的頭
        "cuero de vino": "./material/food/4_7_cuero_de_vino.png",               # 酒囊
        "río de sangre": "./material/food/4_8_rio_de_sangre.jpg",               # 血河
        "sonámbulo": "./material/food/4_9_sonambulo.png",                       # 夢遊
        "caldero de agua fría": "./material/food/4_10_caldero_de_agua_fria.png"   # 冷水鍋
    }


class Level5:
    title = "Quinta prueba: La última batalla con el Caballero de la Blanca Luna"
    story = """
            Bajo la cuidadosa planificación de su amigo aldeano, Sansón Carrasco, Don Quijote encontró al Caballero de la Blanca Luna que sostenía un escudo con dibujo de luna en la playa de Barcelona. Vino a competir porque se enteró de las hazañas heroicas de Don Quijote y pidió que el vencido tuviera que regresar a su pueblo natal y que no pudiera volver a la aventura del caballero durante un año. Además, tenía que aceptar que había mujeres más bellas que Dulcinea en el mundo. Don Quijote aceptó el reto de mala gana.
            """

    food = {
         
    }


class Conclusion:
    title = None
    story = """
            Don Quijote perdió este duelo decisivo y regresó a su pueblo natal como había prometido. Después de regresar, sufrió fiebre alta y estuvo reposando en cama durante varios días. Un día despertó repentinamente y dijo a todos que él ya no era Don Quijote, sino Alonso Quĳano. Sintió que se estaba muriendo, por lo que comenzó a hacer testamento, dejando su herencia a su sobrina y a Sancho. Tres días después, Alonso Quijano puso fin a su legendaria vida.
            """
    food = None
# ---------------------------------- Method ---------------------------------- #


if __name__ == "__main__":
    print(Level1.story.format(PLAYER_NAME="Yuan"))

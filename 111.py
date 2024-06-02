import pygame
import sys
import ctypes
import time
import os
import re



def color_show():
	# 初始化 Pygame
	pygame.init()

	# 定義顏色
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

	# 顏色列表
	colors = [
		("WHITE", WHITE),
		("LIGHT_GRAY", LIGHT_GRAY),
		("SILVER", SILVER),
		("GRAY", GRAY),
		("DIM_GRAY", DIM_GRAY),
		("DARK_GRAY", DARK_GRAY),
		("BLACK", BLACK),
		("GAINSBORO", GAINSBORO),
		("SMOKE", SMOKE),
		("SLATE_GRAY", SLATE_GRAY),
		("LIGHT_SLATE_GRAY", LIGHT_SLATE_GRAY),
		("DARK_SLATE_GRAY", DARK_SLATE_GRAY)
	]

	# 設置窗口大小
	screen_width = 800
	screen_height = len(colors) * 50

	# 創建窗口
	screen = pygame.display.set_mode((screen_width, screen_height))
	pygame.display.set_caption('顏色展示')

	# 主循環
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		# 填充背景
		screen.fill(BLACK)

		# 繪製顏色塊
		for index, (color_name, color_value) in enumerate(colors):
			pygame.draw.rect(screen, color_value, (50, index * 50, screen_width - 100, 50))
			font = pygame.font.Font(None, 36)
			text = font.render(color_name, True, BLACK if color_value == WHITE else WHITE)
			screen.blit(text, (60, index * 50 + 10))

		# 更新顯示
		pygame.display.flip()

	# 退出 Pygame
	pygame.quit()
	sys.exit()



def gamel():
	import pygame
	import time
	import random
	##colours
	white=(255,255,255)
	black=(0,0,0)
	blue=(19,100,60)
	lblue=(50,100,0)
	red=(255,0,0)
	green=(0,255,0) #RGB

	x=pygame.init()
	#size of display width,height and block(that builds up snake)
	display_w=1000
	display_h=900
	block_s=50

	gameD=pygame.display.set_mode((display_w,display_h))	#'gameD' is main game screen
	pygame.display.set_caption("new game snake")
	gameD.fill(white)	#background
	pygame.display.update()

	clock=pygame.time.Clock()
	#Fonts
	smallfont=pygame.font.SysFont(None,20)
	mediumfont=pygame.font.SysFont(None,33)
	largefont=pygame.font.SysFont(None,38)

	def randgen():	#random coordinates generator function for apple
		randap_x=round(random.randrange(0,display_w - block_s)/block_s)*block_s
		randap_y=round(random.randrange(0,display_h - block_s)/block_s)*block_s
		return randap_x,randap_y

	def text_obj(text,color):
		textsurf=mediumfont.render(text,True,color)	#text surface
		return textsurf,textsurf.get_rect()

	def message_screen(msg,color,y_disp=0):
		textsurf,textrect=text_obj(msg,color)
		textrect.center=(display_w/2),(display_h/2)+y_disp	#text surface center at middle of page
		gameD.blit(textsurf,textrect) 

	def snakefn(snakelist):		#making of FULL SNAKE in particular frame
		for xny in snakelist[:-1]:
			pygame.draw.rect(gameD,blue,[xny[0],xny[1],block_s,block_s])
		pygame.draw.rect(gameD,black,[snakelist[-1][0],snakelist[-1][1],block_s,block_s])    #the head block(separately for different color)

	def pause():
		message_screen("Paused",black,-20)
		message_screen("Press q to quit OR c to continue",lblue,50)
		paused=True
		pygame.display.update()
		while paused:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_c:
						paused=False
					if event.key == pygame.K_q:
						pygame.quit()
						quit()

	def gamel():

		randapx,randapy=randgen()
		snakelength=1
		snakehead=[]
		snakelist=[]
		gameexit=False
		leadx=display_w/2
		leady=display_h/2
		leadx_c=block_s
		leady_c=0
		gameover=False
		direction="right"
		FPS=18

		while not gameexit:

			while gameover==True:
				message_screen("GAME OVER",black,-30)
				message_screen("Score: "+ str(snakelength-1),black,-10)
				message_screen("Press c to continue OR q to quit ",red,50)
				pygame.display.update()
				
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						gameexit=True
						gameover=False
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_q:
							gameexit=True
							gameover=False
						elif event.key == pygame.K_c:
							gamel()
			count=0
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gameexit=True
				if event.type == pygame.KEYDOWN:
					count+=1
					if count > 1:
						break
					if event.key == pygame.K_LEFT and direction !="right":
						leadx_c=-block_s
						leady_c=0
						direction="left"
					elif event.key == pygame.K_RIGHT and direction !="left":
						leadx_c=block_s
						leady_c=0
						direction="right"
					elif event.key == pygame.K_UP and direction !="down":
						leady_c=-block_s
						leadx_c=0
						direction="up"
					elif event.key == pygame.K_DOWN and direction !="up" :
						leady_c=block_s
						leadx_c=0
						direction="down"
					elif event.key == pygame.K_p:
						pause()
			
			gameD.fill(white)
			snakehead=[]
			leadx+=leadx_c
			leady+=leady_c
			
			if leadx >= randapx and leadx < randapx + 2*block_s  and leady >= randapy and leady < randapy + 2*block_s:#meeting apple	
				randapx,randapy=randgen()
				snakelength+=1
				if FPS < 50:	
					FPS+=1.3	#increasing FPS after every increase of length
					
			pygame.draw.rect(gameD,green,[randapx,randapy,2*block_s,2*block_s])
			pygame.display.update()
						
			if leadx >=display_w:		 #if statements to pass through walls and enter from the other end
				leadx=0
			elif leadx < 0:
				leadx=display_w
			
			elif leady >=display_h:
				leady=0
			elif leady < 0:
				leady=display_h

			snakehead.append(leadx)
			snakehead.append(leady)
			snakelist.append(snakehead)
			
			if len(snakelist) > snakelength:	#maintaining length of snake (as list is appended each time)
				del snakelist[0]

			for eachseg in snakelist[0:-1] :
				if eachseg == snakehead:
					gameover = True
					break
		
			snakefn(snakelist)
			txtt=smallfont.render("Score: "+ str(snakelength-1),True,red)
			gameD.blit(txtt,[0,0])
			pygame.display.update()
		
			clock.tick(FPS)
		pygame.quit()
		quit()

	gamel()




def get_keyboard_layout():
    # Get the handle of the foreground window
    hwnd = ctypes.windll.user32.GetForegroundWindow()
    
    # Get the thread ID of the foreground window
    thread_id = ctypes.windll.user32.GetWindowThreadProcessId(hwnd, None)
    
    # Get the keyboard layout for that thread
    layout_id = ctypes.windll.user32.GetKeyboardLayout(thread_id)
    
    # Extract the language ID from the layout ID
    language_id = layout_id & (2**16 - 1)
    
    # Convert the language ID to a hexadecimal string
    return hex(language_id)

def switch_to_english():
    # 0x0409 is the hexadecimal identifier for English (United States)
    english_layout = 0x0409
    hwnd = ctypes.windll.user32.GetForegroundWindow()
    thread_id = ctypes.windll.user32.GetWindowThreadProcessId(hwnd, None)
    ctypes.windll.user32.PostThreadMessageW(thread_id, 0x50, 0, english_layout)

def main_loop():
    last_status = None
    while True:
        current_status = get_keyboard_layout()
        if current_status != last_status:
            if current_status != '0x409':  # If not English (United States)
                print("Switching to English (United States) input method.")
                switch_to_english()
            else:
                print("Current input method is English (United States).")
            last_status = current_status
        time.sleep(0.5)  # Check every 0.5 seconds




def change_file_name(folder_path):
	

	for file_name in os.listdir(folder_path):
		new_file_name = re.sub(r'(?<!^)(?=[A-Z])', '', file_name).lower()
		if file_name!= new_file_name:
			os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_file_name))
			print(f"Renamed {file_name} to {new_file_name}.")

		else:
			print(f"{file_name} is already in lowercase.")



if __name__ == '__main__':
	# gamel()
	# color_show()
	# main_loop()
	change_file_name("material/sound")
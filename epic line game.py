########### KEYBINDS ###########
# R = Red Color
# G = Green Color
# B = Blue Color
# ESC = Quit 
# Page Up = Increase Framerate By 1 
# Page Down = Decrease Framerate By 1 
# F = Fullscreen (BUGGY!)
# D = Debug Mode (Hold it!!)

########## HOW TO PLAY ##########
# Make cool lines and see how many you can make, the higher the score the better! Or just make interesting shapes. I guess. 
# I spent a while making this!! Its a bit overcomplicated

############# BUGS ##############
# Blank spots
# Score bugs out when drawing lines

######### START OF CODE #########
import pyautogui
import pygame
#Set the games stuff
squaresizex, squaresizey = 25,25
color = (255,255,255)
framerate = 14400000000000000000000000000000000000 # its high for a reason..
width = 800
height = 800
screen_color = 255,0,0
# Drawing Code
square_color = (0,0,255)
def player(self):
    player.counter += 1
    pygame.draw.rect(surface, square_color, pygame.Rect(x, y, squaresizex*1.2, squaresizey*1.2))
    pygame.draw.rect(surface, color, pygame.Rect(x, y, squaresizex, squaresizey))
player.counter = 0
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
fswidth = pyautogui.size()[1]
fsheight = pyautogui.size()[0]
from win32api import GetSystemMetrics
pygame.display.set_caption("cool line thing")
isPressed = False
erasecolor = screen_color
clock = pygame.time.Clock()
running = True
surface = pygame.display.set_mode((width,height),pygame.RESIZABLE)
while running:
    screenfill = True

    text_surface = my_font.render('Score : ' + str(player.counter), True, (255, 0, 0))
    mouseX, mouseY = pygame.mouse.get_pos()
    
    clock.tick(framerate)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if pygame.key.get_pressed()[pygame.K_r]:
            square_color = (255,0,0)
        if pygame.key.get_pressed()[pygame.K_g]:
            square_color = (0,255,0)
        if pygame.key.get_pressed()[pygame.K_b]:
            square_color = (0,0,255)
        if pygame.key.get_pressed()[pygame.K_f]:
             surface = pygame.display.set_mode((fsheight,fswidth),pygame.FULLSCREEN)
        if pygame.key.get_pressed()[pygame.K_d]:
           print("Mouse is at the coordinates:", "(",mouseX,",",mouseY,")")
        if pygame.key.get_pressed()[pygame.K_INSERT]:
            screenfill = True
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            running = False
        if pygame.key.get_pressed()[pygame.K_PAGEUP]:
                framerate += 1
                print("Changed Framerate to: ",framerate,"!")
        elif pygame.key.get_pressed()[pygame.K_PAGEDOWN]:
                framerate -= 1
                print("Changed Framerate to: ",framerate)
        if event.type == pygame.MOUSEBUTTONDOWN:
            isPressed = True

        elif event.type == pygame.MOUSEBUTTONUP:
            isPressed = False
            surface.fill((0,0,0))     
        if event.type == pygame.MOUSEMOTION and isPressed == True:
            (x,y) = pygame.mouse.get_pos()
            player('self')
        surface.blit(text_surface, (0,0))
    pygame.display.flip()         
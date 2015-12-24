import pygame, sys
pygame.init()

size = width, height = 500, 450
speed = [2, 2]
white = pygame.Color("White")

frame = pygame.display.set_mode(size)

icon = pygame.image.load("nano.PNG")
iconrect = icon.get_rect()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    iconrect = iconrect.move(speed)
    if iconrect.left < 0 or iconrect.right > width:
        speed[0] = -speed[0]
    if iconrect.top < 0 or iconrect.bottom > height:
        speed[1] = -speed[1]
        
    frame.fill(white)
    frame.blit(icon, iconrect)
    pygame.display.update()
    pygame.time.wait(30)

import pygame


pygame.init()

#Create a displace surface object
DISPLAYSURF = pygame.display.set_mode((1920, 1080))

# title and icon change
pygame.display.set_caption("WheatleyOS")
soundObj = pygame.mixer.Sound('grunt.wav')
soundObj.play()
icon = pygame.image.load('weaticon.png')
pygame.display.set_icon(icon)

#eye img
eyeimg = pygame.image.load('neweye.png')

def Update():
    events = pygame.event.get()
    for event in events:
     if pygame.event.get():
         print("TEST")



def eye():
    DISPLAYSURF.blit(eyeimg, (0, 0))

# Game Loop
run = True
while run:
    Update()
    eyeimg.set_alpha(1000)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #RED GREEN BLUE
    DISPLAYSURF.fill((0, 0, 0))
    eye()
    pygame.display.update()

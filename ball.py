import os, sys, pygame
os.environ["SDL_FBDEV"] = "/dev/fb1"

if len(sys.argv) > 0:

    pygame.init()
    pygame.font.init()
    font = pygame.font.SysFont('Comic Sans MS', 18)
    pygame.mouse.set_visible(0)

    size = width, height = 320, 240
    speed = [2, 2]
    black = 0, 0, 0
    img = sys.argv[1]
    
    if os.path.exists(img):

        screen = pygame.display.set_mode(size)
        text = font.render(os.path.abspath(img),False,(255,255,255))
        ball = pygame.image.load(os.path.abspath(img))
        ball = pygame.transform.scale(ball,size)
        screen.fill(black)
        screen.blit(ball,(0,0))
        screen.blit(text,(0,0))
        pygame.display.flip()

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    sys.exit()

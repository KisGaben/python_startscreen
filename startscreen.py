import os, sys, pygame
from uuid import getnode as get_mac
from time import sleep
from subprocess import check_output
os.environ["SDL_FBDEV"] = "/dev/fb1"

pygame.init()
pygame.font.init()
 
pygame.mouse.set_visible(0)

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0
white = 255, 255, 255;
fontsize = 16
font = pygame.font.SysFont('Fixed', fontsize)

screen = pygame.display.set_mode(size)

mac = get_mac()
mac = ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))
      
bg = pygame.image.load('/home/kisgaben/startscreen/img3.png')
bg = pygame.transform.scale(bg,size)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()

    ip = check_output(['hostname', '-I']).split(' ')[0]
    up = check_output("uptime").decode('utf-8').split(',')
    users = check_output("who").decode('utf-8')

    text_line_1 = font.render('IP: '+ ip,False,white)
    text_line_2 = font.render('MAC: '+ mac,False,white)
    text_line_3 = font.render(up[0].strip() + ', ' + up[1].strip(),False,white)
    text_line_4 = font.render(up[2].strip() + ', ' + up[3].strip() + ', ' + up[4].strip(),False,white)
    text_line_6 = font.render('Users:',False,white)
    
    screen.fill(black)
    screen.blit(bg,(0,0))

    screen.blit(text_line_1,(0,0))
    screen.blit(text_line_2,(0,fontsize+2))
    screen.blit(text_line_3,(0,height-2*(fontsize+2)))
    screen.blit(text_line_4,(0,height-fontsize-2))
    screen.blit(text_line_6,(0,2*(fontsize+2)))

    i = 3
    for user in users.split('\n'):
        text_line= font.render(user.split(' ')[0],False,white)
        screen.blit(text_line,(10,i*(fontsize+2)))
        i = i+1

    pygame.display.flip()
    sleep(60)


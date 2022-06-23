import pygame, sys,random,math,time
from pygame.locals import *
from pygame.math import Vector2
pygame.init()

WHITE = (255, 255, 255)
font = pygame.font.SysFont("Verdana", 60)
font1 = pygame.font.Font(None, 64)
game_over = font.render("Game Over", True, WHITE)
screen = pygame.display.set_mode((1000,800))
background=pygame.image.load('forest_edge.png')
clock = pygame.time.Clock()
eagles=[0]
img=['eagle1.gif']*22
img1=['eagle1.gif']*22
ref_image=pygame.image.load('ref1.png')
ref_image=pygame.transform.scale(ref_image,(15,15))

for i in range(1,22):
    i1=str(i)
    eagles.append('eagle'+i1+'.gif')
    img[i]=pygame.image.load(eagles[i])
    img1[i]=pygame.transform.flip(img[i],True,False)

img2=pygame.transform.rotate(img1[3],-90)
X,Y=50,100
refX,refY=50,100
q1,q2=1,0
N=5
scale1,scale2=28,35
rabbit_img=[0]*N
rabbit_Xpos=[0]*N
rabbit_Ypos=[0]*N

for i in range(N):
    rabbit_img[i]=pygame.image.load('rabbit.png')
    rabbit_img[i]=pygame.transform.scale(rabbit_img[i],(scale1,scale2))
    rabbit_Xpos[i]=(random.randint(0,700))
    rabbit_Ypos[i]=(random.randint(500,750))

def rabbits_motion():
    global N
    for s in range(N):
        rabbit_Xpos[s]=rabbit_Xpos[s]+1.5*(s+1)#8
        rabbit_Ypos[s]=rabbit_Ypos[s]+5*math.sin(r*3.14/4)
        screen.blit(rabbit_img[s],(rabbit_Xpos[s],rabbit_Ypos[s]))
        if rabbit_Xpos[s]>1200:
            rabbit_Xpos[s]=50
            rabbit_Ypos[s]=random.randint(500,750)

i,k,r=0,0,-1
times=0

def count_time():
    global counter
    global N
    counter += 1
    counter1=round(counter/10)
    text1 = font.render(str(counter1), True, (0, 128, 0))
    text2=font.render('Time in sec:',True,(0,128,0))
    screen.blit(text2,(400,48))
    screen.blit(text1, (775, 48))
    if N==0:
        counter-=1

counter=0
while True:
    r=r+1
    if k==0:
        screen.blit(background,(0,0))
        rabbits_motion()
        i=i+1
        i1=i%21
        if i1==0: i1=1
        X=X+5
        X1,Y1=X+90,Y+100
        screen.blit(img1[i1],(X,Y))
        screen.blit(ref_image,(X1,Y1))
        if X>1000: X=50
       
    button=pygame.key.get_pressed()
    if button[pygame.K_DOWN]:
        k=1
    if k==1:
        screen.blit(background,(0,0))
        X,Y=X+15,Y+40
        X1,Y1=X+90,Y+100
        eagle_pos=Vector2(X,Y)
        ref_pos=Vector2(X1,Y1)
        print('N=',N)
        for s in range(N):
            rabbit_Xpos[s]=rabbit_Xpos[s]+4*(s+1)
            rabbit_Ypos[s]=rabbit_Ypos[s]+10*math.sin(r*3.14/4)
            screen.blit(rabbit_img[s],(rabbit_Xpos[s],rabbit_Ypos[s]))
            rabbit_pos=Vector2(rabbit_Xpos[s],rabbit_Ypos[s])
            delta=pygame.math.Vector2.length(ref_pos-rabbit_pos)
            if delta<50:
                rabbit_Xpos[s]=2000
                N=N-1
        screen.blit(img2,(X,Y))
        screen.blit(ref_image,(X1,Y1))
        
        if Y>800:
            X,Y=50,100
            k=0
    if N==0:
        times=times+1
        screen.blit(game_over, (30,250))
        if times==100:
            pygame.quit()
    count_time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(10)
    pygame.display.update()

            
    
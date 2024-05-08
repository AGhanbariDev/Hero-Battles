#Importing library
import pygame
import os
os.chdir("C:\\Users\\aydip\\Player movement")

win = pygame.display.set_mode((1920,1020))
pygame.display.set_caption("Hero's Battles")

screen_width = 1020
   
runRight = [pygame.image.load("run(r)1.png"),pygame.image.load("run(r)2.png"),pygame.image.load("run(r)3.png"),pygame.image.load("run(r)4.png"),pygame.image.load("run(r)5.png"),pygame.image.load("run(r)6.png"),pygame.image.load("run(r)7.png"),pygame.image.load("run(r)8.png")]
runLeft = [pygame.image.load("run(L)1.png"),pygame.image.load("run(L)2.png"),pygame.image.load("run(L)3.png"),pygame.image.load("run(L)4.png"),pygame.image.load("run(L)5.png"),pygame.image.load("run(L)6.png"),pygame.image.load("run(L)7.png"),pygame.image.load("run(L)8.png")]
jumping = [pygame.image.load("jumping1.png"),pygame.image.load("jumping2.png"),pygame.image.load("jumping3.png"),pygame.image.load("jumping4.png"),pygame.image.load("jumping5.png"),pygame.image.load("jumping6.png"),pygame.image.load("jumping7.png"),pygame.image.load("jumping8.png"),pygame.image.load("jumping9.png"),pygame.image.load("jumping10.png")]
idling = [pygame.image.load("idle1.png"), pygame.image.load("idle2.png"), pygame.image.load("idle3.png"), pygame.image.load("idle4.png")]
background = pygame.image.load("background.jpg")
floor = pygame.image.load("floor1.png")
# ball = pygame.image.load("ball.png")
sliding_r = [pygame.image.load("sliding1(r).png"),pygame.image.load("sliding2(r).png"),pygame.image.load("sliding3(r).png"),pygame.image.load("sliding4(r).png"),pygame.image.load("sliding5(r).png"),pygame.image.load("sliding6(r).png")]
sliding_l = [pygame.image.load("sliding1(l).png"),pygame.image.load("sliding2(l).png"),pygame.image.load("sliding3(l).png"),pygame.image.load("sliding4(l).png"),pygame.image.load("sliding5(l).png"),pygame.image.load("sliding6(l).png")]
attacking = pygame.image.load("attack.png")

clock = pygame.time.Clock()

x = screen_width / 2
y = screen_width - 90 - 250
width = 64
height = 200
vel = 5
isJump = False
JumpCount = 10
left = False
right = False
sliding_right = False
walkCount = 0
player_size = width
player_pos = [x,y]
ball_height = 100
ball_width = 100
ball_pos = [screen_width - 100, 250]
ball_size = 100
enemy_list =[ball_pos]
attack = False
sliding_left = False

def redrawGameWindow():
    global walkCount
    win.blit(background, (0,0))
    # win.blit(ball, (ball_pos[0],ball_pos[1]))

    # if ball_pos[1] < 1020 - 228:
    #     ball_pos[1] += 17

    if walkCount + 1 >= 25:
        walkCount = 0
    
    if left:
        win.blit(runLeft[walkCount//5], (x, y))
        walkCount += 1
    
    elif right:
        win.blit(runRight[walkCount//5], (x, y))
        walkCount += 1
    
    elif sliding_right:
            win.blit(sliding_r[walkCount//5], (x,y + 50))
            walkCount += 1
    
    elif sliding_left:
        win.blit(sliding_l[walkCount//5], (x,y + 50))

    elif attack:
        win.blit(attacking, (x,y))
    
    elif isJump:
        win.blit(jumping[walkCount//3], (x,y))
        walkCount += 1

    else:
        win.blit(idling[walkCount//6], (x, y))
        walkCount += 1
    
    if True:
        win.blit(floor, (0,1020 - 140))
        walkCount += 1    
    
    pygame.display.update()

run = True
# Main loop
while run:
    clock.tick(40)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    mouse_pos = pygame.mouse.get_pos()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and x > vel:
        x -= vel + 15
        left = True
        right = False
        sliding_right = False
        sliding_left = False

    elif keys[pygame.K_d] and x < 1920 - width - vel - 30:
        x += vel + 15
        left = False
        right = True
        sliding_right = False
        sliding_left = False
    
    elif keys[pygame.K_p]:
        attack = True

    elif not isJump and keys[pygame.K_s] and x < 1920 - width - vel - 30 and mouse_pos[0] > x + 50:
        if mouse_pos != x:
            width = 200
            height = 150
            x += vel + 15
            walkCount += 1
            sliding_right = True
            sliding_left = False
            right = False
            left = False
            isJump = False

    elif not isJump and keys[pygame.K_s] and x < 1920 - width - vel - 30 and mouse_pos[0] < x - 50:
        if mouse_pos != x:
            width = 200
            height = 150
            x -= vel + 15
            walkCount += 1
            sliding_right = False
            sliding_left = True
            right = False
            left = False
            isJump = False
        
    else:
        right = False
        left = False
        sliding_right = False
        sliding_left = False
        attack = False

    if not (isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            sliding_right = False
            sliding_left = False
    else:
        if JumpCount >= -10: 
            neg = 1
            if JumpCount < 0:
                neg = -1
            y -= (JumpCount ** 2) * 1 * neg
            JumpCount -= 1
        else:
            isJump = False
            JumpCount = 10
    
    redrawGameWindow()

pygame.quit()
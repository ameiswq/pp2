import pygame 
import random
from pygame.locals import *
pygame.init()

W, H = 1200, 800
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
pygame.display.set_caption("Arckanoid")
pygame.display.set_icon(pygame.image.load("images/icon2.png"))
clock = pygame.time.Clock()
done = False
bg = (0, 0, 0)


#paddle
paddleW = 150
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)


#Ball
ballRadius = 25
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

#Game score
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

#Catching sound
collision_sound = pygame.mixer.Sound('sound/catch.mp3')

def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy


#block settings
block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j,
        100, 50) for i in range(10) for j in range (4)]
color_list = [(random.randrange(1, 254), 
    random.randrange(1, 254),  random.randrange(1, 254))
              for i in range(10) for j in range(4)] 

unbreakable_block_index = [30, 23, 16, 15, 4]
bonus_bricks_index = [33, 24, 17, 9, 2]
delete_list = unbreakable_block_index + bonus_bricks_index
delete_list.sort(reverse=True)
bonus_bricks = [block_list[bonus_bricks_index[i]] for i in range(len(bonus_bricks_index))]
unbreakable_block = [block_list[unbreakable_block_index[i]] for i in range(len(unbreakable_block_index))]
for i in range(len(delete_list)):
    block_list.pop(delete_list[i])
    color_list.pop(delete_list[i])



#Game over Screen
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

#Win Screen
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = losefont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(SPEED, 5000)

BRICK = pygame.USEREVENT + 2
pygame.time.set_timer(SPEED, 5000)

k = True
c = 0
p = 0
d = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                done = True
                pygame.quit()
            if event.key == pygame.K_SPACE:
                d = 0
                c += 1
                k = not k
            if event.key == pygame.K_ESCAPE:
                d = 7
            if event.key == pygame.K_1:
                bg = (0, 0, 0)
            if event.key == pygame.K_2:
                bg = (255,192,203)
            if event.key == pygame.K_3:
                bg = (230, 230, 250)
        if event.type == SPEED:
            ballSpeed += 0.5
            paddleSpeed += 0.5
        if event.type == BRICK:
            paddleW -= 10

    
    menu_font = pygame.font.SysFont('comicsansms', 60)
    menu_text = menu_font.render('Press SPACE to continue', True, (255, 255, 255))
    menu_rect = menu_text.get_rect(center=(W // 2, H // 2))

    if not k:
        screen.fill(bg)
        [pygame.draw.rect(screen, color_list[color], block)
        for color, block in enumerate (block_list)] #drawing blocks
        [pygame.draw.rect(screen, (255, 255, 255), block)
        for block in unbreakable_block]
        [pygame.draw.rect(screen, (255, 0, 0), block)
        for block in bonus_bricks]
        pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
        pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)
        # print(next(enumerate (block_list)))

        #Ball movement
        ball.x += ballSpeed * dx
        ball.y += ballSpeed * dy

        #Collision left 
        if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
            dx = -dx
        #Collision top
        if ball.centery < ballRadius + 50: 
            dy = -dy
        #Collision with paddle
        if ball.colliderect(paddle) and dy > 0:
            dx, dy = detect_collision(dx, dy, ball, paddle)

        #Collision blocks
        hitIndex1 = ball.collidelist(block_list)
        hitIndex2 = ball.collidelist(unbreakable_block)
        hitIndex3 = ball.collidelist(bonus_bricks)
        if hitIndex1 != -1:
            hitRect = block_list.pop(hitIndex1)
            hitColor = color_list.pop(hitIndex1)
            dx, dy = detect_collision(dx, dy, ball, hitRect)
            game_score += 1
            collision_sound.play()
        if hitIndex2 != -1:
            dx, dy = detect_collision(dx, dy, ball, unbreakable_block[hitIndex2])
        if hitIndex3 != -1:
            hitRect3 = bonus_bricks.pop(hitIndex3)
            dx, dy = detect_collision(dx, dy, ball, hitRect3)
            paddleW += 30
            collision_sound.play()
            
        #Game score
        game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
        screen.blit(game_score_text, game_score_rect)
        
        #Win/lose screens
        if ball.bottom > H:
            screen.fill((0, 0, 0))
            screen.blit(losetext, losetextRect)
        elif not len(block_list):
            screen.fill((255,255, 255))
            screen.blit(wintext, wintextRect)
            
        #Paddle Control
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and paddle.left > 0:
            paddle.left -= paddleSpeed
        if key[pygame.K_RIGHT] and paddle.right < W:
            paddle.right += paddleSpeed

        pygame.display.flip()
        clock.tick(70)
    elif k and c >= 1:
        p = 0
        screen.fill("black")
        screen.blit(menu_text, menu_rect)
        settings_font = pygame.font.SysFont('comicsansms', 15)
        settings_text = settings_font.render('Press ESCAPE to go to settings', True, (255, 255, 255))
        settings_rect = settings_text.get_rect(center=(W // 2, H // 2 + 60))
        screen.blit(settings_text, settings_rect) 
        pressed_keys = pygame.key.get_pressed()
        if d == 7:
            screen.fill("black")
            pressed_keys2 = pygame.key.get_pressed()
            font = pygame.font.SysFont('comicsansms', 80)
            text = font.render("Сhoose background color:", True, (255, 255, 255))
            text_rect = text.get_rect(center = (W // 2, H // 2 - 200))
            screen.blit(text, text_rect)
            text1 = font.render("1.   BLACK ", True, (255, 255, 255))
            text2 = font.render("2.   PINK  ", True, (255, 255, 255)) # (255,192,203)
            text3 = font.render("3.   PURPLE", True, (255, 255, 255)) # (230,230,250)
            text4 = settings_font.render("Press SPACE to continue the game", True, (255, 255, 255))
            text1_rect = text1.get_rect(center = (W // 2, text_rect.bottom + 60))
            text2_rect = text2.get_rect(center = (W // 2, text1_rect.bottom + 60))
            text3_rect = text3.get_rect(center = (W // 2, text2_rect.bottom + 60))
            text4_rect = text4.get_rect(center = (W // 2, text3_rect.bottom + 100))
            screen.blit(text1, text1_rect)
            screen.blit(text2, text2_rect)
            screen.blit(text3, text3_rect)
            screen.blit(text4, text4_rect)



    elif k and c == 0:
        menu_text = menu_font.render('Press SPACE to start', True, (255, 255, 255))
        screen.fill("black")
        screen.blit(menu_text, menu_rect)  
        
                
    pygame.display.flip()
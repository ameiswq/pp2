import pygame

pygame.init()

width, height = 600, 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ball")
pygame.display.set_icon(pygame.image.load("images/icon3.png"))
screen.fill('white')

x, y = 300, 300
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and x < 570:
                x += 20
            if event.key == pygame.K_LEFT and x > 30:
                x -= 20
            if event.key == pygame.K_UP and y > 30:
                y -= 20
            if event.key == pygame.K_DOWN and y < 570:
                y += 20
        """
    key = pygame.key.get_pressed()

    if key[pygame.K_RIGHT] and x < 570:
        x += 20
    if key[pygame.K_LEFT] and x > 30:
        x -= 20
    if key[pygame.K_UP] and y > 30:
        y -= 20
    if key[pygame.K_DOWN] and y < 570:
        y += 20
        
    screen.fill('white')
    pygame.draw.circle(screen, "red", (x, y), 25)
    pygame.display.update()
    clock.tick(20)
import pygame 
import datetime

pygame.init()

w, h = 829, 836

font = pygame.font.SysFont('Verdana', 30)

screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Mickey Mouse Clock")
pygame.display.set_icon(pygame.image.load("images/icon.webp"))

clock = pygame.image.load("images/main-clock.png")
min = pygame.image.load("images/right-hand.png")
sec = pygame.image.load("images/left-hand.png")
rect = clock.get_rect(center = (w//2, h//2))

Clock = pygame.time.Clock() 

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    screen.fill((255, 255, 255))
    t = datetime.datetime.now().time()
    time_render = font.render(f'{t:%H:%M:%S}', True, pygame.Color('black'), pygame.Color('white'))
    screen.blit(clock, (0, 0))
    clock.blit(time_render, (0, 0))

    a1 = pygame.transform.rotate(min, t.minute * -6)
    a2 = pygame.transform.rotate(sec, t.second * -6)
    screen.blit(a1, a1.get_rect(center = rect.center).topleft)
    screen.blit(a2, a2.get_rect(center = rect.center).topleft)

    pygame.display.flip() 
  
    
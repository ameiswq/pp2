import pygame

pygame.init()

width, height = 550, 650
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Music Player")
pygame.display.set_icon(pygame.image.load("images/icon2.png"))

img1 = pygame.transform.scale(pygame.image.load('images/img1.jpg'), (350, 350))
img2 = pygame.transform.scale(pygame.image.load('images/img2.jpg'), (350, 350))
img3 = pygame.transform.scale(pygame.image.load('images/img3.jpg'), (350, 350))
pause = pygame.image.load('images/pause.jpg')
player = pygame.image.load('images/player.jpg')

songs = ['songs/song1.mp3', 'songs/song2.mp3', 'songs/song3.mp3']
images = [img1, img2, img3]

screen.fill('black')
screen.blit(img2, (100, 100))
screen.blit(pause, (206, 490))
pygame.draw.line(screen, (255, 255, 255), (206, 542), (344, 542), 2)

i = 1
pygame.mixer.music.load(songs[i])
pygame.mixer.music.play()
pygame.mixer.music.pause()
running = True
playing = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if playing:
                    screen.blit(pause, (206, 490))
                    pygame.mixer.music.pause()
                    playing = False
                else:
                    pygame.mixer.music.unpause()
                    playing = True
                    screen.blit(player, (206, 490))
            if event.key == pygame.K_RIGHT:
                i += 1
                if i == 3:
                    i = 0
                screen.blit(images[i], (100, 100))
                pygame.mixer.music.load(songs[i])
                pygame.mixer.music.play()
            if event.key == pygame.K_LEFT:
                i -= 1
                if i == -1:
                    i = 2
                screen.blit(images[i], (100, 100))
                pygame.mixer.music.load(songs[i])
                pygame.mixer.music.play()

    pygame.display.update() 
    
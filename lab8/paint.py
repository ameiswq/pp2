import pygame

#draw rectangles, circles, choose the color and uxe eraser

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Paint")
    pygame.display.set_icon(pygame.image.load("images/paint.png"))
    clock = pygame.time.Clock()
    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []
    eraser = []
    drawing = True
    global rect_x, rect_y
    global mouse_x, mouse_y
    rect_x, rect_y = 0, 0
    mouse_x, mouse_y = 0, 0
    rectangles = []
    rect_colors = []
    circle_colors = []
    circles_center = []
    circles_radius = []
    lines = []
    erase_lines = []
    lines_colors = []
    global x1, y1, w, h
    x1, y1, w, h = 0, 0, 0, 0
    flag_held1 = False
    flag_held2 = False
    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        held1 = pressed[pygame.K_1]
        held2 = pressed[pygame.K_2]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_a:
                    rect_x, rect_y = pygame.mouse.get_pos()
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_y:
                    mode = 'yellow'

            if event.type == pygame.MOUSEMOTION and (held1 or held2):
                mouse_x, mouse_y = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click grows radius
                    radius = min(200, radius + 1)
                elif event.button == 3: # right click shrinks radius
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION and pressed[pygame.K_SPACE]:
                position = pygame.mouse.get_pos()
                points.append(position)

                
            if event.type == pygame.MOUSEMOTION and pressed[pygame.K_e]:
                position = pygame.mouse.get_pos()
                eraser.append(position)

            if not pressed[pygame.K_SPACE]:
                if len(points) != 0:
                    lines.append(points[:])
                    lines_colors.append(mode)
                    points.clear()
            if not pressed[pygame.K_e]:
                if len(eraser) != 0:
                    erase_lines.append(eraser[:])
                    eraser.clear()

            if held1 or held2:
                drawing = True
            elif not held1 and not held2:
                drawing = False


        screen.fill((0, 0, 0))


        if drawing:
            if held1:
                flag_held1 = True
                if mouse_x > rect_x and mouse_y > rect_y:
                    x1, y1, w, h = rect_x, rect_y, mouse_x - rect_x, mouse_y - rect_y
                elif mouse_y < rect_y and mouse_x > rect_x:
                    x1, y1, w, h = rect_x, mouse_y, mouse_x - rect_y, rect_y - mouse_y
                elif mouse_x < rect_x and mouse_y < rect_y:
                    x1, y1, w, h = mouse_x, mouse_y, rect_x - mouse_x, rect_y - mouse_y
                elif mouse_y > rect_y and mouse_x < rect_x:
                    x1, y1, w, h = mouse_x, rect_y, rect_x - mouse_x, mouse_y - rect_y
                pygame.draw.rect(screen, mode, (x1, y1, w, h))
            if held2:
                flag_held2 = True
                pygame.draw.circle(screen, mode, (rect_x, rect_y), abs(mouse_x - rect_x))
        else:
            if flag_held1 == True:
                rectangles.append((x1, y1, w, h))
                rect_colors.append(mode)
                flag_held1 = False
            if flag_held2 == True:
                circles_radius.append(mouse_x - rect_x)
                circle_colors.append(mode)
                circles_center.append((rect_x, rect_y))
                flag_held2 = False

        for i in range(len(rectangles)):
            pygame.draw.rect(screen, rect_colors[i], rectangles[i])
            
        for i in range(len(circles_radius)):
            pygame.draw.circle(screen, circle_colors[i], circles_center[i], circles_radius[i])

        j = 0
        for line in lines:
            i = 0
            while i < len(line) - 1:
                drawLineBetween(screen, i, line[i], line[i + 1], radius, lines_colors[j])
                i += 1
            j += 1

        for line in erase_lines:
            i = 0
            while i < len(line) - 1:
                drawLineBetween(screen, i, line[i], line[i + 1], radius, (0, 0, 0))
                i += 1
        pygame.display.flip()
        
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color_mode, (x, y), width)

main()
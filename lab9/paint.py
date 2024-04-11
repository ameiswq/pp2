import pygame
import math
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
    squares = []
    squares_colors = []
    triangle = []
    triangle_colors = []
    right_triangle = []
    right_triangle_color = []
    rhombus = []
    rhombus_color = []
    lines = []
    erase_lines = []
    lines_colors = []
    global x1, y1, w, h
    x1, y1, w, h = 0, 0, 0, 0
    global z, third_x, third_y
    z, third_x, third_y = 0, 0, 0
    flag_held1 = False
    flag_held2 = False
    flag_held3 = False
    flag_held4 = False
    flag_held5 = False
    flag_held6 = False
    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        held1 = pressed[pygame.K_1]
        held2 = pressed[pygame.K_2]
        held3 = pressed[pygame.K_3]
        held4 = pressed[pygame.K_4]
        held5 = pressed[pygame.K_5]
        held6 = pressed[pygame.K_6]

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

            if event.type == pygame.MOUSEMOTION and (held1 or held2 or held3 or held4 or held5 or held6):
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

            if held1 or held2 or held3 or held4 or held5 or held6:
                drawing = True
            elif not held1 and not held2 and not held3 and not held4 and not held5 and not held6:
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
            if held3:
                flag_held3 = True
                if mouse_x > rect_x and mouse_y > rect_y:
                    x1, y1, w, h = rect_x, rect_y, mouse_y - rect_y, mouse_y - rect_y
                elif mouse_y < rect_y and mouse_x > rect_x:
                    x1, y1, w, h = rect_x, mouse_y, rect_y - mouse_y, rect_y - mouse_y
                elif mouse_x < rect_x and mouse_y < rect_y:
                    x1, y1, w, h = mouse_x, mouse_y, rect_y - mouse_y, rect_y - mouse_y
                elif mouse_y > rect_y and mouse_x < rect_x:
                    x1, y1, w, h = mouse_x, rect_y, mouse_y - rect_y, mouse_y - rect_y
                pygame.draw.rect(screen, mode, (x1, y1, w, h))
            if held4:
                flag_held4 = True
                pygame.draw.polygon(screen, mode, [(rect_x, rect_y), (mouse_x, mouse_y), (2*rect_x - mouse_x, mouse_y)])
            if held5:
                flag_held5 = True
                z = ((mouse_x - rect_x)**2 + (mouse_y - rect_y)**2)**0.5
                third_x = rect_x + z/2
                third_y = rect_y + (z*(3**0.5)) / 2
                pygame.draw.polygon(screen, mode, [(rect_x, rect_y), (mouse_x, mouse_y), (third_x, third_y)])
            if held6:
                flag_held6 = True
                pygame.draw.polygon(screen, mode, [(rect_x, rect_y), (mouse_x, (rect_y + mouse_y)/2), (rect_x, mouse_y), (2*rect_x - mouse_x, (rect_y + mouse_y)/2)])



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
            if flag_held3 == True:
                squares.append((x1, y1, w, h))
                squares_colors.append(mode)
                flag_held3 = False
            if flag_held4:
                triangle.append([(rect_x, rect_y), (mouse_x, mouse_y), (2*rect_x - mouse_x, mouse_y)])
                triangle_colors.append(mode)
                flag_held4 = False
            if flag_held5:
                right_triangle.append([(rect_x, rect_y), (mouse_x, mouse_y), (third_x, third_y)])
                right_triangle_color.append(mode)
                flag_held5 = False
            if flag_held6:
                rhombus.append([(rect_x, rect_y), (mouse_x, (rect_y + mouse_y)/2), (rect_x, mouse_y), (2*rect_x - mouse_x, (rect_y + mouse_y)/2)])
                rhombus_color.append(mode)
                flag_held6 = False

        for i in range(len(rectangles)):
            pygame.draw.rect(screen, rect_colors[i], rectangles[i])
            
        for i in range(len(circles_radius)):
            pygame.draw.circle(screen, circle_colors[i], circles_center[i], circles_radius[i])

        for i in range(len(squares)):
            pygame.draw.rect(screen, squares_colors[i], squares[i])

        for i in range(len(triangle)):
            pygame.draw.polygon(screen, triangle_colors[i], triangle[i])
        
        for i in range(len(rhombus)):
            pygame.draw.polygon(screen, rhombus_color[i], rhombus[i])

        for i in range(len(right_triangle)):
            pygame.draw.polygon(screen, right_triangle_color[i], right_triangle[i])

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
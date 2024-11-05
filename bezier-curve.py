# 베지에 곡선

import pygame

pygame.init()

screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption("Bezier Curve")


X = 300
frame = 30


clock = pygame.time.Clock()

points = []

run = True
depict = False


colors = [
    (0, 0, 0),
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (0, 255, 255),
    (255, 0, 255)
]


def draw(ps: list, t: float):
    new_ps = []
    if len(ps) > 1:
        for i in range(len(ps) - 1):
            # ps[i]와 ps[i+1] 사이 t:(1-t) 내분점

            in_branch = (ps[i][0] * (1-t) + ps[i+1][0] * t, ps[i][1] * (1-t) + ps[i+1][1] * t)
            pygame.draw.circle(screen, colors[len(ps) - 2], in_branch, 5)

            new_ps.append(in_branch)
    
        draw(new_ps, t)

while run:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                points.append(pygame.mouse.get_pos())
                print(1)
        elif event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
                depict = True
        

    screen.fill((255, 255, 255))

    # 그림은 이 아래에서

    for p in points:
        pygame.draw.circle(screen, (0, 0, 0), p, 5)

    pygame.display.update()
else:
    if depict:
        for time in range(X):
            clock.tick(frame)

            for p in points:
                pygame.draw.circle(screen, (0, 0, 0), p, 5)

            draw(points, time / X)
            
            pygame.display.update()
import pygame
pygame.init()

screen = pygame.display.set_mode((1080, 800))
pygame.display.set_caption("HAPPY")
nblue =(0, 0, 128)
dpink = (255, 20, 147)
exit = False
while not exit:
    pygame.draw.line(screen, (0, 0, 0), [0, 10], [1080, 10], 100)
    pygame.draw.line(screen, (148, 0, 211), [0, 710], [1080, 710], 100)#V
    pygame.draw.line(screen, (75, 0, 130), [0, 610], [1080, 610], 100)#I
    pygame.draw.line(screen, (0, 0, 255), [0, 510], [1080, 510], 100)#B
    pygame.draw.line(screen, (0, 255, 0), [0, 410], [1080, 410], 100)#G
    pygame.draw.line(screen, (255, 255, 0), [0, 310], [1080, 310], 100)#Y
    pygame.draw.line(screen, (255, 127,0), [0, 210], [1080, 210], 100)#O
    pygame.draw.line(screen, (255, 0, 0), [0, 110], [1080, 110], 100)#R
    #(surface, colour, start_position[x, y_from_top], end_position[x, y_from_top], width)


    #H
    pygame.draw.line(screen, nblue, [50, 50], [50, 250], 25)
    pygame.draw.line(screen, nblue, [50, 150], [200, 150], 25)
    pygame.draw.line(screen, nblue, [200, 50], [200, 250], 25)
    #A
    pygame.draw.line(screen, nblue, [250, 250], [350, 50], 25)
    pygame.draw.line(screen, nblue, [450, 250], [350, 50], 25)
    pygame.draw.line(screen, nblue, [285, 175], [415, 175], 25)
    #p
    pygame.draw.line(screen, nblue, [500, 50], [500, 250], 25)
    pygame.draw.line(screen, nblue, [500, 62], [640, 62], 25)
    pygame.draw.line(screen, nblue, [628, 62], [628, 162], 25)
    pygame.draw.line(screen, nblue, [500, 162], [640, 162], 25)
    #P
    pygame.draw.line(screen, nblue, [690, 50], [690, 250], 25)
    pygame.draw.line(screen, nblue, [690, 62], [830, 62], 25)
    pygame.draw.line(screen, nblue, [818, 62], [818, 162], 25)
    pygame.draw.line(screen, nblue, [690, 162], [830, 162], 25)
    #Y
    pygame.draw.line(screen, nblue, [880, 50], [967, 175], 25)
    pygame.draw.line(screen, nblue, [1030, 50], [930, 250], 25)

    #+
    pygame.draw.line(screen, (0, 0, 0), [540, 300], [540, 500], 25)
    pygame.draw.line(screen, (0, 0, 0), [440, 400], [640, 400], 25)

    #L
    pygame.draw.line(screen, dpink, [150, 550], [150, 750], 25)
    pygame.draw.line(screen, dpink, [150, 738], [300, 738], 25)
    #I
    pygame.draw.line(screen, dpink, [350, 550], [500, 550], 25)
    pygame.draw.line(screen, dpink, [425, 540], [425, 750], 25)
    pygame.draw.line(screen, dpink, [350, 740], [500, 740], 25)
    #P
    pygame.draw.line(screen, dpink, [580, 550], [580, 750], 25)
    pygame.draw.line(screen, dpink, [580, 562], [700, 562], 25)
    pygame.draw.line(screen, dpink, [688, 562], [688, 662], 25)
    pygame.draw.line(screen, dpink, [580, 662], [700, 662], 25)
    #I
    pygame.draw.line(screen, dpink, [780, 550], [930, 550], 25)
    pygame.draw.line(screen, dpink, [855, 540], [855, 750], 25)
    pygame.draw.line(screen, dpink, [780, 740], [930, 740], 25)

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
pygame.quit()
quit()
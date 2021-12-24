import pygame
import random
from tkinter import *

screen_width = 480
screen_height = 640


background_image = "C:/Users/aa/Desktop/PythonWorkspace/project1/back_ground.png"
solo_cat_image = "C:/Users/aa/Desktop/PythonWorkspace/project1/solo_cat.png"
couple_cat_image = "C:/Users/aa/Desktop/PythonWorkspace/project1/couple_cat.png"

def main():
    pygame.init()

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("avoid couple")

    background = pygame.image.load(background_image)
    solo_cat = pygame.image.load(solo_cat_image)
    couple_cat = pygame.image.load(couple_cat_image)

    solo_cat_size = solo_cat.get_rect().size 
    solo_cat_width = solo_cat_size[0]
    solo_cat_height = solo_cat_size[1]

    couple_cat_size = couple_cat.get_rect().size
    couple_cat_width = couple_cat_size[0]
    couple_cat_height = couple_cat_size[1]

    solo_x_pos = screen_width / 2 - solo_cat_width / 2
    solo_y_pos = screen_height - solo_cat_height 

    solo_to_x = 0

    couple_x_pos = screen_width / 2
    couple_y_pos = 0
    couple_to_y = 0.2

    score = 0
    clock = pygame.time.Clock()
    game_font = pygame.font.Font(None, 40)
    start_ticks = pygame.time.get_ticks()

    running = True
    while running:

        screen.blit(background, (0, 0))
        dt = clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    solo_to_x -= 1
                elif event.key == pygame.K_RIGHT:
                    solo_to_x += 1
                    

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    solo_to_x = 0

        solo_x_pos += solo_to_x * dt
        if solo_x_pos > screen_width - solo_cat_width:
            solo_x_pos = screen_width - solo_cat_width
        elif solo_x_pos < 0:
            solo_x_pos = 0
        
        couple_y_pos += couple_to_y * dt

        if couple_y_pos > screen_height:
            couple_y_pos = 0
            couple_x_pos = random.randrange(0, screen_width - couple_cat_width)

        solo_rect = solo_cat.get_rect()
        solo_rect.left = solo_x_pos
        solo_rect.top = solo_y_pos

        couple_rect = couple_cat.get_rect()
        couple_rect.left = couple_x_pos
        couple_rect.top = couple_y_pos


        if solo_rect.colliderect(couple_rect):
            game_over(score)
            score = 0

        score += (pygame.time.get_ticks() - start_ticks) / 10000    
        score_board = game_font.render(str(int(score)), True, (0, 0, 0))

        screen.blit(score_board, (0, 0))
        screen.blit(solo_cat, (solo_x_pos, solo_y_pos))
        screen.blit(couple_cat, (couple_x_pos, couple_y_pos))


        pygame.display.update()


def game_over(score):
    global root
    root = Tk()
    label = Label(root, text = f"your score is : {int(score)}")
    label.pack()
    restart_button = Button(root, text = "restart", command = push_restart)
    quit_button = Button(root, text = "quit", command = push_quit)
    
    restart_button.pack()
    quit_button.pack()
    root.mainloop()

def push_restart():
    global running
    running = False
    running = True
    root.destroy()

def push_quit():
    pygame.quit()
    root.destroy()

if __name__ == "__main__":
    main()
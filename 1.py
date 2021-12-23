import pygame

screen_width = 480
screen_height = 640


background_image = "back_ground.png"
cat_image = "cat.png"

def main():
    global screen
    pygame.init()

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("avoid cat")

    background = pygame.image.load(background_image)
    cat = pygame.image.load(cat_image)
    cat_size = cat.get_rect().size 
    cat_width = cat_size[0]
    cat_height = cat_size[1]
    
    game_font = pygame.font.Font(None, 40)

    start_ticks = pygame.time.get_ticks()

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        screen.blit(background, (0, 0))
        pygame.display.update()
        

if __name__ == "__main__":
    main()
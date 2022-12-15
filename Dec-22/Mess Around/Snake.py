import pygame 


# VARIABLES 
running = True
WIDTH, HEIGHT = 800, 600
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
player = pygame.Rect(WIDTH/2+15, HEIGHT/2+15, 15, 15)
clock = pygame.time.Clock


def main(): 
    while running:

        # Quit Check 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            player.y += 7
        screen.fill(color=(255, 255, 255))
        pygame.draw.rect(screen, pygame.Color("Black"), player)
        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()

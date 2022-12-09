import pygame, sys



clock = pygame.time.Clock()
running = True

# Screen
HEIGHT, WIDTH = 500,1000
BALL_SPEED_Y, BALL_SPEED_X = 7,7
PLAYER_SPEED = 0
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # only one can exist
pygame.display.set_caption('Game')


ball = pygame.Rect(WIDTH/2-15, HEIGHT/2-15, 30, 30)
player = pygame.Rect(WIDTH-20, HEIGHT/2-70, 10, 140)
opponent = pygame.Rect(10, HEIGHT/2-70, 10, 140)

def collisions():
    global BALL_SPEED_X, BALL_SPEED_Y
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        BALL_SPEED_Y *= -1
    if ball.left <= 0 or ball.right >= WIDTH:
        BALL_SPEED_X *= -1

    #if ball.colliderect(player) or ball.collidedict(opponent):
        #BALL_SPEED_X *= -1

# Quit
while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Check the keys being pressed
        if keys[pygame.K_UP]:
            if not PLAYER_SPEED == 7:
                PLAYER_SPEED +=7
        if keys[pygame.K_DOWN]:
            PLAYER_SPEED -=7



    player.y += PLAYER_SPEED

    ball.x += BALL_SPEED_X
    ball.y += BALL_SPEED_Y

    collisions()

    screen.fill(pygame.Color("White"))
    pygame.draw.rect(screen, (pygame.Color("Black")), player)
    pygame.draw.rect(screen, (pygame.Color("Black")), opponent)
    pygame.draw.ellipse(screen, (pygame.Color("Black")), ball)
    pygame.display.update()
    clock.tick(FPS)
   

pygame.quit()






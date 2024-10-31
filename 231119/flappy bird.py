import pygame
import random
import time

pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Flappy lỏ")
running = True
move = "down"
x = 200
y = 200
clock = pygame.time.Clock()
clock.tick(60)
is_end = False
pipe_spawn_time = 0
pipes = []
score = 0


def check_position():
    global y, move
    if y >= 450 and move == "down":
        move = "up"
    elif y <= 50 and move == "up":
        move = "down"
    if move == "up":
        y -= 1
    else:
        y += 1

class Bird:
    def __init__(self):
        self.x = 200
        self.y = 100
        #pygame.draw.circle(screen,"yellow", (self.x,self.y), 10)
        flappy_bird = pygame.image.load("flappy.png")
        scale_bird = pygame.transform.scale(flappy_bird, (10, 10))
    def update(self):
        global is_end
        if self.y >= 490:
            is_end = True
        elif self.y <= 10:
            self.y += 1
        else:
            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_SPACE]:
                self.y -= 3.5
            else:
                self.y += 2
        flappy_bird = pygame.image.load("flappy.png")
        scale_bird = pygame.transform.scale(flappy_bird, (10,10))
        screen.blit(scale_bird, (self.x, self.y))

class Pipe:
    def __init__(self):
        self.x = 500
        self.y = 0
        self.height = random.randint(50,250)
        self.space = random.randint(60,200)
    def update(self):
        self.x -= 2
        pygame.draw.rect(screen, "green", (self.x,self.y, 40, self.height))
        pygame.draw.rect(screen, "green", (self.x,self.height + self.space, 40, 500 - self.height - self.space))

bird = Bird()
bird.update()
print("")

font = pygame.font.SysFont("chalkduster", 20, bold = True)
score_text = font.render("Score: "+str(score), True, "red", "white")
font_end = pygame.font.SysFont("chalkduster", 47, bold = True)
end_text = font_end.render("GAME OVER", True, "red", "white")
back = pygame.image.load("city.jpeg")
scale_back = pygame.transform.scale(back, (500,500))



while running:
    clock.tick(60)
    screen.fill((0,0,0))
    screen.blit(scale_back, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if is_end:
        print("")
        print("GET A LIFE LOSER!")
        print("")
        screen.blit(score_text, (0,0))
        screen.blit(end_text, (80,200))
    else:
        current_time = pygame.time.get_ticks()
        bird.update()
        if current_time > (pipe_spawn_time + random.randint(1000, 8000)):
            pipes.append(Pipe())
            pipe_spawn_time = current_time
        for pipe in pipes:
            pipe.update()
            screen.blit(score_text, (0,0))
            if pipe.x < -30:
                pipes.remove(pipe)
            if (bird.y+ 20 >= pipe.height + pipe.space or bird.y - 20 <= pipe.height) and (bird.x + 20 >= pipe.x and bird.x - 20 <= pipe.x + 30):
                is_end = True
                break
            if bird.x - 10 >= pipe.x and bird.x + 10 <= pipe.x + 20:
                score += 1
                score_text = font.render("Score: "+str(score), True, "red", "white")
    check_position()
    pygame.display.flip()

pygame.quit()

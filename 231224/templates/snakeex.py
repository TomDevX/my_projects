import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snake with Pygame")
food_color = ['red', 'purple', 'yellow', 'cyan', 'orange', 'pink']

class Snake():
    def __init__(self):
        self.x = 400
        self.y = 300
        self.x_move = 0
        self.y_move = 0
        self.body = []
        self.speed = 3
        pygame.draw.circle(screen, 'blue', (self.x, self.y), 10)

    def get_direction(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_UP] == True:
            self.x_move = 0
            self.y_move = -self.speed
        if key_pressed[pygame.K_DOWN] == True:
            self.x_move = 0
            self.y_move = self.speed
        if key_pressed[pygame.K_LEFT] == True:
            self.x_move = -self.speed
            self.y_move = 0
        if key_pressed[pygame.K_RIGHT] == True:
            self.x_move = self.speed
            self.y_move = 0

    def update(self):
        # Set first element of body to be head position
        if len(self.body) >= 1:
            # Move body of snake
            for i in range(len(self.body)-1, 0, -1):
                self.body[i] = self.body[i-1]
            self.body[0] = {"x": self.x, "y": self.y}

        if self.x_move != 0:
            self.x += self.x_move
        if self.y_move != 0:
            self.y += self.y_move

    def drawSnake(self):
        pygame.draw.circle(screen, 'blue', (self.x, self.y), 10)
        for body in self.body:
            pygame.draw.circle(screen, 'red', (body['x'], body['y']), 10)


    def level_up(self):
        self.speed += 2

    def check_end_game(self):
        if (self.x <= 10 or self.x >= 790) or (self.y <= 10 or self.y >= 590):
            return True

class Food():
    def __init__(self):
        self.x = random.randint(10, 790)
        self.y = random.randint(10, 590)
        self.color = random.choice(food_color)

    def update(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), 10)

def create_food():
    global food_list
    numFood = random.randint(1, 10)
    food_list = []
    for i in range(numFood):
        food_list.append(Food())



running = True
FPS = 60
clock = pygame.time.Clock()
snake = Snake()
create_food()
is_end = False

level_score = [0, 5, 10, 15]
font = pygame.font.SysFont("couriernew", 28, bold=True)
score = 0
level = 1

pause = False

while running:
    clock.tick(FPS)
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    is_end = snake.check_end_game()
    if is_end:
        game_over_text = font.render("GAME OVER!", True, 'black')
        replay_text = font.render("(Press Space to play again)", True, 'black')
        screen.blit(game_over_text, (320, 230))
        screen.blit(replay_text, (180, 280))
        #reset
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_SPACE] == True:
        score = 0
        level = 1
        is_end = False
        snake.__init__()
        create_food()
        for food in food_list:
            food.update()
    elif pause:
        screen.blit(freeze_text, (350, 300))
        snake.drawSnake()
        for food in food_list:
            food.update()
        if pygame.time.get_ticks() > (freeze_time + 3000):
            pause = False
    else:
        snake.get_direction()
        snake.update()
        snake.drawSnake()
        for food in food_list:
            food.update()
            distance = math.sqrt((snake.x - food.x)**2 + (snake.y - food.y)**2)
            if distance <= 20:
                if food.color == 'red':
                    score += 1
                elif food.color == 'pink':
                    score += 2
                elif food.color == 'purple':
                    score -= 2
                elif food.color == 'yellow':
                    if snake.speed > 2:
                        snake.speed -= 2
                    else:
                        snake.speed = 1
                elif food.color == 'orange':
                    snake.speed += 2
                elif food.color == 'cyan':
                    freeze_text = font.render("Freezing...", True, 'black')
                    freeze_time = pygame.time.get_ticks()
                    pause = True

                for mark in level_score:
                    if score == mark:
                        level = level_score.index(mark)
                        #snake.level_up()
                        break
                if len(snake.body) == 0:
                    snake.body.append({'x': snake.x, 'y': snake.y})
                else:
                    snake.body.append(snake.body[-1])
                food_list.remove(food)
                break
        if len(food_list) == 0:
            create_food()

    score_text = font.render("Score: " + str(score) + ' - Level: ' + str(level), True, 'black')
    screen.blit(score_text, (0, 0))

    print(snake.body)
    pygame.display.flip()

pygame.quit()

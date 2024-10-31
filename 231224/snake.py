import pygame
from pygame.locals import *
import random
import math
import time

pygame.init()
running = True
score = 0
level_score = [0,5,10,15, 20, 25, 30, 35, 40]
level = 1
font = pygame.font.SysFont("couriernew", 20, bold = True)
font2 = pygame.font.SysFont("couriernew", 60, bold = True)
surface = pygame.display.set_mode((500, 500))
surface.fill((110, 110, 5))
clock = pygame.time.Clock()
clock.tick(60)
back = pygame.image.load("background.jpg")
scale_back = pygame.transform.scale(back, (500,500))
food_color = ("black", "red", "yellow", "blue", "brown", "purple", "cyan", "ghostwhite", "royalblue", "deepskyblue", "lightskyblue", "orange")
color = random.choice(food_color)
head_color = color
pause = False
food = []
for i in range(10):
    color = random.choice(food_color)
    food.append(color)


class Snake:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.x_move = 0
        self.y_move = 0
        self.snake = pygame.draw.circle(surface, "red", (self.x, self.y), 10)
        self.body = []
        self.speed = 2
        self.head_rect = pygame.draw.circle(surface, head_color, (self.x, self.y), 10)
    def get_direction(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_LEFT]:
            self.x_move = -self.speed
            self.y_move = 0
        if key_pressed[pygame.K_RIGHT]:
            self.x_move = self.speed
            self.y_move = 0
        if key_pressed[pygame.K_UP]:
            self.x_move = 0
            self.y_move = -self.speed
        if key_pressed[pygame.K_DOWN]:
            self.x_move = 0
            self.y_move = self.speed
    def update(self):
        if len(self.body) >= 1:
            for i in range(len(self.body)-1, 0, -1):
                self.body[i] = self.body[i-1]
            # self.body[0] = self.snakei
            self.body[0] = {"x": self.x, "y": self.y}
        if (self.x_move == -self.speed and  self.x > 20) or (self.x_move == self.speed and self.x < 490):
            self.x += self.x_move
        if (self.y_move == -self.speed and self.y > 20) or (self.y_move == self.speed and self.y < 490):
            self.y += self.y_move
        pygame.draw.circle(surface, head_color, (self.x, self.y), 10)
        for body in self.body:
            pygame.draw.circle(surface, "lightgreen", (body["x"], body["y"]), 10)
        if self.x_move != 0:
            self.x += self.x_move
        if self.y_move != 0:
            self.y += self.y_move
    def level_up(self):
        for i in range(1,len(level_score)):
            if level == level_score[i]:
                self.speed += 1
    def check_end_game(self):
        if (self.x <= 10 or self.x >= 490) or (self.y <= 10 or self.y >= 490):
            return True
    def draw_snake():
        pygame.draw.circle(surface, head_color, (self.x, self.y), 10)
        for body in self.body:
            pygame.draw.circle(surface, "lightgreen", (body["x"], body["y"]), 10)

class Fruit:
    def __init__(self):
        self.x = random.randint(10,480)
        self.y = random.randint(10,480)
        self.color = random.choice(food_color)
        self.rect = pygame.draw.circle(surface, self.color, (self.x,self.y), 10)
    def update(self):
        pygame.draw.circle(surface, self.color, (self.x, self.y),7)
        pygame.draw.circle(surface, self.color, (self.x,self.y), 10)

def create_food():
        global food_list
        numFood = random.randint(1,10)
        food_list = []
        for i in range(numFood):
            food_list.append(Fruit())

class Wall():
    def __init__(self):
        self.x = random.randint(10,480)
        self.y = random.randint(10,480)
        self.height = random.randint(50,200)
        self.direction = random.randint(0,1)
        if self.direction == 0:
            self.rect = pygame.draw.rect(surface, "#0e7819", (self.x, self.y, 20, self.height))
        else:
            self.rect = pygame.draw.rect(surface, "#0e7819", (self.x, self.y, self.height, 20))
    def update(self):
        if self.direction == 0:
            self.rect = pygame.draw.rect(surface, "#0e7819", (self.x, self.y, 20, self.height))
        else:
            self.rect = pygame.draw.rect(surface, "#0e7819", (self.x, self.y, self.height, 20))
    def create_wall():
        global wall_list
        numWall = random.randint(5,15)
        wall_list = []
        for i in range(numWall):
            wall_temp = Wall()
            while wall_temp.rect.colliderect(snake.head_rect):
                wall_temp = Wall()
            for food in food_list:
                while wall_temp.rect.colliderect(food.rect):
                    wall_temp = Wall()
            wall_list.append(wall_temp)

food = Fruit()
snake = Snake()
wall = Wall()
create_food()

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    if snake.check_end_game() == True:
        game_over_text = font2.render("GAME OVER!", True, "black")
        surface.blit(game_over_text, (80, 200))
    elif pause:
        #snake.draw_snake()
        for food in food_list:
            food.update()
        if pygame.time.get_ticks() > (freeze_time + 3000):
            pause = False
    else:
        surface.blit(scale_back, (0,0))
        snake.get_direction()
        snake.update()
        for food in food_list:
            food.update()
            distance = math.sqrt((snake.x - food.x)**2 + (snake.y - food.y)**2)
            if distance <= 17:
                food.update()
                if food.color == "red":
                    snake.y_move = -snake.speed
                elif food.color == "blue":
                    snake.y_move = snake.speed
                elif food.color == "orange":
                    score += 1
                    level += 2
                elif food.color == "black":
                    level += 2
                elif food.color == "yellow":
                    score += 2
                elif food.color == "brown":
                    snake.speed -= 1
                elif food.color == "purple":
                    score += 1
                    snake.speed += 1
                elif food.color == "cyan":
                    score += 2
                    snake.speed -= 1
                elif color == "ghostwhite":
                    score -= 1
                elif food.color == "royalblue":
                    freeze_time = pygame.time.get_ticks()
                    pause = True
                else:
                    score += 1
                    level += 1
                snake.level_up()
                if len(snake.body) == 0:
                    snake.body.append({"x": snake.x, "y": snake.y})
                else:
                    snake.body.append(snake.body[-1])
                food_list.remove(food)
        if len(food_list) == 0:
            create_food()
    clock.tick(60)
    score_text = font.render("Score: "+str(score), True, "white", "red")
    surface.blit(score_text, (0,0))
    pygame.display.flip()

pygame.quit()

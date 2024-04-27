import pygame
import random

pygame.init()


win_width = 500
win_height = 500
background = pygame.transform.scale(pygame.image.load('background.png'), (win_width, win_height))
FPS = 5

win = pygame.display.set_mode((win_width, win_height))
win.blit(background, (0, 0))
clock = pygame.time.Clock()


class Apple(pygame.sprite.Sprite):
    def __init__(self, image, x, y, wadth, height):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(image), (width, height))


        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def teleport(self):
        self.rect.x = random.randint(0, (win_width - self,rect.width) // self.rect.width) * self.rect.width
        self.rect.y = random.randint(0, (win_height - self,rect.height) // self.rect.height) * self.rect.height


    def draw(self):
        win.blit(self,image, (self.rect.x, self.rect.y))



class Snake:
    def __init__(self, x, y, size, color=(100,100,255)):
        self.rect = pygame.Rect(x, y, size, size)
        self.color = color
        self.last_pos = [x, y]
        self.direction = 'right'
        self.step = size


    def draw(self):
        pygame.draw.rect(win, self.color, self.rect)


SIZE = 30

snakes = []

Apple = Apple('apple_png', 0, 0, SIZE, SIZE)
apple = teleport()
head = Snake(100, 100, SIZE)
snakes.append(head)

scores = 0

def move(x, y):
    lx, ly = x, y
    for s in snakes:
        s.goto(lx, ly)
        lx, ly = s.last_pos[0], s.last_pos[1]


while True:

    if apple.rect.colliderect(head.rect):
        scores += 1
        apple.teleport()
        last_pos = snakes[-1].last_pos
        snakes.append(Snake(last_pos[0], SIZE))


    win.blit(background, (0, 0))

    apple. draw()

    for snake in snake:
        snake.draw()

    pygame.display.update()
    clock.tick(FPS)
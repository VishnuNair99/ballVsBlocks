import pygame, sys, random
from pygame.locals import *
pygame.init()

height = 800
width = 600
resolution = (width, height)

white = (255,255,255)
black = (0,0,0)

FPS = 24

fpsClock = pygame.time.Clock()

ball = pygame.image.load("ball.png")
block = pygame.image.load("block.png")

ball = pygame.transform.scale(ball,(int(width/10),int(width/10)))
block = pygame.transform.scale(block, (int(width/10),int(width/10)))

ball.set_colorkey(ball.get_at((0,0)), RLEACCEL)
block.set_colorkey(block.get_at((0,0)), RLEACCEL)

screen = pygame.display.set_mode(resolution)
pygame.display.set_caption('Ball Vs Block')

blockPos = [int(var*(width/10)) for var in range(10)]

pygame.mouse.set_visible(False)

class Ball:
    head_pos = 3
    length = 10
    list = [i for i in range(length)]
    ball_size = 25

    def update(self):
        self.head_pos = pygame.mouse.get_pos()[0]
        self.list.append(pygame.mouse.get_pos()[0])



    def draw(self):
        temp = int(height/2+self.ball_size)
        screen.blit(ball, (self.head_pos, int(height/2)))
        for var in range(2, self.length+1):
            screen.blit(ball, (self.list[int(-1*var)], temp))
            temp += self.ball_size




class Block:
    Pos = []
    numBlocks = 0
    Y = 0
    def initialize(self, y_coord):
        self.Pos = []
        self.Y = y_coord
        self.numBlocks = random.randint(5, 8)
        while len(self.Pos) < self.numBlocks:
            temp = random.choice(blockPos)
            if temp not in self.Pos:
                self.Pos.append(temp)
    def draw(self):
        for var in self.Pos:
            screen.blit(block, (var, self.Y))
    def scroll(self):
        if self.Y >= (height-width/10):
            self.initialize(0)
        else:
            self.Y += 5

b1 = Ball()
w1 = Block()
w2 = Block()
w3 = Block()
w1.initialize(0)
w2.initialize(300)
w3.initialize(600)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(white)
    b1.update()
    b1.draw()
    w1.scroll()
    w1.draw()
    w2.scroll()
    w2.draw()
    w3.scroll()
    w3.draw()
    fpsClock.tick(FPS)
    pygame.display.flip()

import pygame, sys, random
from pygame.locals import *
pygame.init()

height = 800
width = 600
resolution = (height, width)

white = (255,255,255)
black = (0,0,0)

FPS = 160

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


class Ball:
    pos = (0,0)

    def update(self):
        self.pos = pygame.mouse.get_pos()

    def draw(self):
        screen.blit(ball, self.pos)


class Block:
    Pos = []
    numBlocks = 0
    Y = 0
    def initialize(self):
        self.Pos = []
        self.Y = 0
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
            self.initialize()
        else:
            self.Y += 5

b1 = Ball()
w1 = Block()
w1.initialize()
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
    fpsClock.tick(FPS)
    pygame.display.flip()
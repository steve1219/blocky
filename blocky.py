# simple game class in python

import pygame, sys, time, random

from pygame.locals import *

# Set up basic variables
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)
WIDTH = 800 # Width of 7" display in pixels
HEIGHT = 480 # Height of 7" display in pixels
NAME = 'Blocky'
FPS = 60
XPOS = 16
YPOS = 0

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('ballGrey.png').convert()
        self.rect = self.image.get_rect()
        #self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.dx = -5
        self.dy = -10
        self.moving = False

    def reset(self):
        self.moving = False
        self.rect.midbottom = p.rect.midtop

    def update(self):
        if self.moving:
            if self.rect.x <= 0 or (self.rect.x + self.rect.width) >= WIDTH:
                self.dx = -self.dx
            if self.rect.y <= 0:
                self.dy = -self.dy
            if (self.rect.y + self.rect.height) > HEIGHT:
                self.reset()
                p.lives -= 1
            if pygame.sprite.collide_rect(p, self):
                self.dy = -self.dy
            self.rect.x += self.dx
            self.rect.y += self.dy
        else:
            self.rect.midbottom = p.rect.midtop
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_UP]:
                self.moving = True

class Block(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos):
        pygame.sprite.Sprite.__init__(self)
        self.blocks = ['element_blue_rectangle.png', 'element_red_rectangle.png', 'element_green_rectangle.png', 'element_yellow_rectangle.png']
        self.xpos = xpos
        self.ypos = ypos
        self.image = pygame.image.load(random.choice(self.blocks)).convert()
        self.rect = self.image.get_rect()
        self.rect.x = self.xpos
        self.rect.y = self.ypos

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("paddleBlu.png").convert()
        #self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT - 30)
        self.lives = 3
        self.score = 0
        self.speedx = 0

    def update(self):
        if self.lives > 0:
            self.speedx = 0
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_LEFT]:
                self.speedx = -15
            if keystate[pygame.K_RIGHT]:
                self.speedx = 15
            if keystate[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit
            self.rect.x += self.speedx
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
            if self.rect.left < 0:
                self.rect.left = 0
        else:
            g.game_over()

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.mouse.set_visible(False)
        self.running = False
        self.clock = pygame.time.Clock()

    def draw_text(self, string, fontsize, x, y, colour):
        text_obj = pygame.font.Font('freesansbold.ttf', fontsize)
        text_surf = text_obj.render(string, True, colour)
        text_rect = text_surf.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surf, text_rect)
    
    def new_game(self):
        blocks.empty()
        blockx = 16
        blocky = 0
        for i in range(3):
            for i in range(12):
                b = Block(blockx, blocky)
                blockx += 64
                blocks.add(b)
            blocky += 32
            blockx = 16
        p.lives = 3


    def game_over(self):
        self.screen.fill(WHITE)
        self.draw_text('Game Over', 50, (WIDTH/2), (HEIGHT/2), RED)
        pygame.display.update()
        time.sleep(5)
        self.running = False

    def start_screen(self):
        self.screen.fill(GREEN)
        self.draw_text(NAME, 50, (WIDTH/2), (HEIGHT/2), RED)
        self.draw_text('Press space to play', 20, (WIDTH/2), 300, RED)
        self.new_game()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    self.running = True
                elif event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        
    def main(self):
        # main loop
        self.clock.tick(FPS)
        # Check events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        # Update sprites
        self.screen.fill(BLACK)
        all_sprites.update()
        #blocks.update()
        pygame.sprite.spritecollide(ball, blocks, True)

        # Draw to the screen
        all_sprites.draw(self.screen)
        blocks.draw(self.screen)
        pygame.display.flip()
        #self.clock.tick(FPS)

g = Game()
p = Player()
ball = Ball()
blocks = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(p, ball)
#g.start_screen()
while True:
    if g.running:
        g.main()
    else:
        g.start_screen()


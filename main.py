import pygame as py
import sys
import os




py.display.set_caption("Flappy Bird")

vec = py.math.Vector2 
FPS = 60
FramePerSec = py.time.Clock()


class Player(py.sprite.Sprite):
    """
    Spawn a player
    """
    def __init__(self):
        py.sprite.Sprite.__init__(self)
        
        self.image = py.image.load('FlappyBird.png')
        self.image = py.transform.scale(self.image, (70,70))
        self.rect = self.image.get_rect()
        area = py.display.get_surface().get_rect()
        self.width, self.height = area.width, area.height

        self.pos = vec((50, 20))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
    
    def move(self):
        self.acc = vec(0,.3)
        pressedKeys = py.key.get_pressed()

        self.vel += self.acc
        self.pos += self.vel + .5 * self.acc

        if self.pos.x > Main().width:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = Main().width
        
        self.rect.midbottom = self.pos
    
    def update(self):
        hits = py.sprite.spritecollide(Main().platform , Main().platforms, False)
        #if hits:
            #self.pos.y = hits[0].rect.top + 1
            #self.vel.y = 0
        
    def jump(self):
        self.vel.y = -5
        print("jump")


class Platform(py.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = py.image.load('ground.png')
        #self.image = py.transform.scale(self.image, (700,300))
        self.rect = self.image.get_rect()
        #self.hitbox =  self.rect.inflate(-40,20)
        area = py.display.get_surface().get_rect()
        self.width, self.height = area.width, area.height
        self.rect.midbottom = (area.width/2,area.height)
        
        # self.surf = py.Surface((Main().width, 20))
        # self.surf.fill((255,0,0))
        # print(Main().width)
        # self.rect = self.surf.get_rect(center = (Main().width/2, Main().height - 10))



        
        

 
        


class Main():
    def __init__(self):
        self.Setup()


    def Setup(self):
        py.init()
        size = (self.width, self.height) = (640,360)
        self.screen = py.display.set_mode(size, 0, 32)
        
        self.player = Player()
        self.platform = Platform()
 
        self.all_sprites = py.sprite.Group()
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.platform)

        self.platforms = py.sprite.Group()
        self.platforms.add(self.platform)
 
        self.SetUpBackground()

    def SetUpBackground(self):
        self.background = py.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0,0,0))
        self.screen.blit(self.background, (0,0))
        py.display.flip
    
    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.player.image, self.player.rect)
        py.display.flip()


    def EventLoop(self):
        player = self.player
        while True: 
            for event in py.event.get():
                if ((event.type == py.QUIT) or 
                    (event.type == py.KEYDOWN and 
                     event.key == py.K_ESCAPE)):
                    sys.exit()
                if event.type == py.KEYDOWN:
                    if event.key == py.K_SPACE:
                        player.jump()
            player.update()
            player.move()

            for entity in self.all_sprites:
                self.screen.blit(entity.image, entity.rect)
            py.display.update()
            FramePerSec.tick(FPS)     
            




        

if __name__ == '__main__':
    app = Main()
    app.EventLoop()







""" player = Player()
ground = Platform()

platforms = py.sprite.Group()
platforms.add(ground)

all_sprites = py.sprite.Group()
all_sprites.add(player)
all_sprites.add(ground)


while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
    
    
    
    keys = py.key.get_pressed()
    if keys[py.K_SPACE] and not spaceDown:
       player.jump()
        spaceDown = True
    elif not keys[py.K_SPACE]: spaceDown = False
    



    window.fill((0, 0, 0))  #Fills background black

    
    player.move()
    for entity in all_sprites:
        window.blit(entity.image, entity.rect)

 
        
    window.blit(flappyBirdImg, (100,100))
    py.display.update()
    py.time.Clock().tick(FPS) """

import pygame
import sys

pygame.init()

window = pygame.display.set_mode((500, 500))
windowX, windowY = window.get_size()

pygame.display.set_caption("Flappy Bird")

vec = pygame.math.Vector2 
x = windowX/2
y = windowY/2
radius = 40
FPS = 60

class Player(pygame.sprite.Sprite):
    """
    Spawn a player
    """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128,255,40))
        self.rect = self.surf.get_rect()

        self.pos = vec((100, 385))
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    def move(self):
        self.acc = vec(0 , .5)

        self.vel += self.acc
        self.pos += self.vel + .5 * self.acc


        #re-position the sprite based on the coalucations
        self.rect.midbottom = self.pos
    
    def update(self):
        hits = pygame.sprite.spritecollide(player, platforms, False)
        if hits:
            self.pos.y = hits[0].rect.top + 1
            self.vel.y = 0

    def jump(self):
        self.vel.y = -7



class Platform(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.Surface((windowX, 20))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect(center = (windowX/2, windowY - 10))


        







player = Player()
ground = Platform()

platforms = pygame.sprite.Group()
platforms.add(ground)

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(ground)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not spaceDown:
        player.jump()
        spaceDown = True
    elif not keys[pygame.K_SPACE]: spaceDown = False
    
    print(spaceDown)



    window.fill((0, 0, 0))  #Fills background black

    
    player.move()
    player.update()
    for entity in all_sprites:
        window.blit(entity.surf, entity.rect)
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

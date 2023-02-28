import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.current_health = 100
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.Surface((25, 25))
        self.surf.fill(("green"))
        self.pos_x = 0
        self.pos_y = 0


    def get_current_health(self) -> int:
        return self.current_health


    def set_current_health(self, incoming_health):
        if incoming_health:
            self.current_health += incoming_health
            if self.current_health < 0:
                self.current_health = 0

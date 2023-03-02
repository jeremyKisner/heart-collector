import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.current_health = 10
        self.max_health = 100
        self.health_bar = 400
        pygame.sprite.Sprite.__init__(self)
        self.main_image = self.__load_main_image()
        self.pos_x = 0
        self.pos_y = 200
        self.speed = 2


    def __load_main_image(self):
        return pygame.image.load("./src/main/assets/HeroMain.png").convert_alpha()


    def get_current_health(self) -> int:
        return self.current_health


    def set_current_health(self, incoming_health):
        if incoming_health:
            self.current_health += incoming_health
            if self.current_health < 0:
                self.current_health = 0


    def get_health_ratio(self):
        return self.max_health / self.health_bar

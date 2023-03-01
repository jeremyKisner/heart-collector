import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.current_health = 100
        pygame.sprite.Sprite.__init__(self)
        self.sprite_sheet_image = self.__load_sprite_sheet()
        self.get_image(0, 60, 70, 1)
        self.pos_x = 0
        self.pos_y = 0


    def __load_sprite_sheet(self):
        return pygame.image.load("./src/main/assets/Hero.png").convert_alpha()


    def get_image(self, frame, width, height, scale):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sprite_sheet_image, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey((0,0,0))
        self.surf = image
        return image


    def get_current_health(self) -> int:
        return self.current_health


    def set_current_health(self, incoming_health):
        if incoming_health:
            self.current_health += incoming_health
            if self.current_health < 0:
                self.current_health = 0

import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.type = "player"
        self.current_health = 10
        self.max_health = 100
        self.health_bar = 400
        self.pos_x = 0
        self.pos_y = 200
        self.speed = 2
        self.image = self.__load_main_image()
        self.__get_image_dimensions()
        self.rect = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)


    def __load_main_image(self):
        return pygame.image.load("./src/main/assets/HeroMain.png").convert_alpha()


    def __get_image_dimensions(self):
        self.width = self.image.get_width()
        self.height = self.image.get_height()


    def handle_keys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            self.pos_y -= self.speed
        if key[pygame.K_s]:
            self.pos_y += self.speed
        if key[pygame.K_a]:
            self.pos_x -= self.speed
        if key[pygame.K_d]:
            self.pos_x += self.speed


    def draw(self, screen):
        screen.blit(self.image, (self.pos_x, self.pos_y))
        self.rect = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)


    def get_current_health(self) -> int:
        return self.current_health


    def set_current_health(self, incoming_health):
        if incoming_health:
            self.current_health += incoming_health
            if self.current_health <= 0:
                self.current_health = 0
            elif self.current_health >= self.max_health:
                self.current_health = self.max_health


    def get_health_ratio(self):
        return self.max_health / self.health_bar


    def is_health_full(self):
        self.full_health = False
        if self.current_health == self.max_health:
            self.full_health = True
        return self.full_health

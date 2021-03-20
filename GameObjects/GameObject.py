class Soldier(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('')
        self.health = 100

    def update(self):
        pass

    def move_to(self, target):
        pass        

class Republican(Soldier):
    def __init__(self):
        super().__init__()
        self.counting = False

class Democrat(Soldier):
    def __init__(self):
        super().__init__()
        

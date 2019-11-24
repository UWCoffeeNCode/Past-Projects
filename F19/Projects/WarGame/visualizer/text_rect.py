class TextRect:
    def __init__(self, font, text: str, foreColour):
        self.font = font

        self.last_text = None
        self.text = text

        self.foreColour = foreColour

        self.rect = None
        self.check_update()

    def check_update(self):
        if self.text != self.last_text:
            # Antialias is True
            self.surface = self.font.render(self.text, True, self.foreColour)
            self.last_text = self.text
            self.realignRect()

    def draw(self, window):
        self.check_update()
        window.blit(self.surface, self.rect)

    def realignRect(self):
        if not self.rect:
            self.rect = self.surface.get_rect()

        old_center = self.rect.center

        self.rect.size = self.surface.get_size()
        self.rect.center = old_center

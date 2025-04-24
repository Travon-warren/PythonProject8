import pygame


class RubyMaker(pygame.sprite.Sprite):
    """A tile that is animated. A ruby will be generated here."""

    def __init__(self, x, y, main_group):
        """Initialize the ruby maker."""
        super().__init__()

        # Animation frames
        self.ruby_sprites = []  # Create an empty list for ruby sprites.

        # Rotating
        for i in range(7):  # Iterate from tile000 to tile006.
            self.ruby_sprites.append(
                pygame.transform.scale(
                    pygame.image.load(f"./assets/images/ruby/tile00{i}.png"),
                    (64, 64),
                )
            )

        # Load image and get rect
        self.current_sprite = 0  # Initialize the current sprite index to 0.
        self.image = self.ruby_sprites[self.current_sprite]  # Set the initial image.
        self.rect = self.image.get_rect()  # Get the rectangle of the image.
        self.rect.bottomleft = (x, y)  # Position the sprite.

        # Add to the main group for drawing purposes
        main_group.add(self)

    def update(self):
        """Update the ruby maker."""
        self.animate(self.ruby_sprites, 0.25)  # Call animate method with speed 0.25.

    def animate(self, sprite_list, speed):
        """Animate the ruby maker."""
        if self.current_sprite < len(sprite_list) - 1:
            self.current_sprite += speed  # Increment the current sprite index.
        else:
            self.current_sprite = 0  # Reset to the first frame.


import random
import pygame

class Portal(pygame.sprite.Sprite):
    """A class that if collided with will transport you"""

    def __init__(self, x, y, color, portal_group):
        """Initialize the portal"""
        super().__init__()

        # Animation frames
        self.portal_sprites = []  # Create an empty list for portal sprites

        # Portal animation
        if color == "green":
            # Green portal
            for i in range(22):  # Add images from tile000.png to tile021.png
                if i < 10:
                    self.portal_sprites.append(pygame.transform.scale(
                        pygame.image.load(f"assets/images/portals/green/tile00{i}.png"), (72, 72)))
                else:
                    self.portal_sprites.append(pygame.transform.scale(
                        pygame.image.load(f"assets/images/portals/green/tile0{i}.png"), (72, 72)))

        else:
            # Purple portal
            for i in range(22):  # Add images from tile000.png to tile021.png
                if i < 10:
                    self.portal_sprites.append(pygame.transform.scale(
                        pygame.image.load(f"assets/images/portals/purple/tile00{i}.png"), (72, 72)))
                else:
                    self.portal_sprites.append(pygame.transform.scale(
                        pygame.image.load(f"assets/images/portals/purple/tile0{i}.png"), (72, 72)))


        # Load an image and get a rect
        self.current_sprite = random.randint(0, len(self.portal_sprites) - 1)  # Set a random sprite as the starting frame
        self.image = self.portal_sprites[self.current_sprite]  # Set the current image
        self.rect = self.image.get_rect()  # Get the rect of the image
        self.rect.bottomleft = (x, y)  # Position the sprite

        # Add to the portal group
        portal_group.add(self)

    def update(self):
        """Update the portal"""
        self.animate(self.portal_sprites, 0.2)  # Animate the portal with speed 0.2

    def animate(self, sprite_list, speed):
        """Animate the portal"""
        if self.current_sprite < len(sprite_list) - 1:
            self.current_sprite += speed  # Increment the sprite index
        else:
            self.current_sprite = 0  # Reset to the first frame

        self.image = sprite_list[int(self.current_sprite)]  # Update the current image

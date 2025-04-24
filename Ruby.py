import pygame
import random

class Ruby(pygame.sprite.Sprite):
    """A class the player must collect to earn points and health"""

    def __init__(self, platform_group, portal_group, window_width, window_height):
        """Initialize the ruby"""
        super().__init__()

        # Set constant variables
        self.VERTICAL_ACCELERATION = 3  # Assign 3 to vertical acceleration
        self.HORIZONTAL_VELOCITY = 5  # Assign 5 to horizontal velocity
        self.WINDOW_WIDTH = window_width  # Assign window_width
        self.WINDOW_HEIGHT = window_height  # Assign window_height

        # Animation frames
        self.ruby_sprites = []  # Create an empty list for ruby sprites

        # Rotating
        for i in range(7):  # Add images from tile000.png to tile006.png
            self.ruby_sprites.append(
                pygame.transform.scale(
                    pygame.image.load(f"./assets/images/ruby/tile00{i}.png"),
                    (64, 64),
                )
            )

        # Load image and get rect
        self.current_sprite = 0  # Initialize current sprite index to 0
        self.image = self.ruby_sprites[self.current_sprite]  # Set initial image
        self.rect = self.image.get_rect()  # Get rectangle of image
        self.rect.bottomleft = (window_width // 2, 100)  # Position the sprite

        # Attach sprite groups
        self.platform_group = platform_group
        self.portal_group = portal_group

        # Load sounds
        self.portal_sound = pygame.mixer.Sound("assets/sounds/portal_sound.wav")  # Load portal sound

        # Kinematic vectors
        self.position = pygame.math.Vector2(self.rect.x, self.rect.y)
        self.velocity = pygame.math.Vector2(
            random.choice([-1 * self.HORIZONTAL_VELOCITY, self.HORIZONTAL_VELOCITY]), 0
        )
        self.acceleration = pygame.math.Vector2(0, self.VERTICAL_ACCELERATION)

    def update(self):
        """Update the ruby"""
        self.animate(self.ruby_sprites, 0.25)  # Call animate method
        self.move()  # Call move method
        self.check_collisions()  # Call check collisions method

    def move(self):
        """Move the ruby"""
        # Update kinematics
        self.velocity += self.acceleration  # Add acceleration to velocity
        self.position += self.velocity + 0.5 * self.acceleration  # Update position

        # Wrap-around movement
        if self.position.x < 0:
            self.position.x = self.WINDOW_WIDTH
        elif self.position.x > self.WINDOW_WIDTH:
            self.position.x = 0

        self.rect.bottomleft = self.position  # Update rect position

    def check_collisions(self):
        """Check for collisions with platforms and portals"""
        # Collision with platforms
        collided_platforms = pygame.sprite.spritecollide(self, self.platform_group, False)
        if collided_platforms:
            self.position.y = collided_platforms[0].rect.top + 1
            self.velocity.y = 0

        # Collision with portals
        if pygame.sprite.spritecollide(self, self.portal_group, False):
            self.portal_sound.play()
            # Portal movement
            self.position.x = 86 if self.position.x > self.WINDOW_WIDTH // 2 else self.WINDOW_WIDTH - 150
            self.position.y = 64 if self.position.y > self.WINDOW_HEIGHT // 2 else self.WINDOW_HEIGHT - 132
            self.rect.bottomleft = self.position

    def animate(self, sprite_list, speed):
        """Animate the ruby"""
        if self.current_sprite < len(sprite_list) - 1:
            self.current_sprite += speed  # Increment sprite index
        else:
            self.current_sprite = 0  # Reset to first sprite

        self.image = sprite_list[int(self.current_sprite)]  # Update image

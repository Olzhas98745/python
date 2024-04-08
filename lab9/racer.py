import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
WIDTH, HEIGHT = 400, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
LOSS_SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# Define color constants
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Initialize score and clock
SCORE = 0
clock = pygame.time.Clock()

# Load background image and fonts
background = pygame.image.load('AnimatedStreet.png')
score_font = pygame.font.SysFont("Verdana", 30)
life_font = pygame.font.SysFont("Verdana", 30)

# Load sounds
background_sound = pygame.mixer.Sound("background.wav")
crush_sound = pygame.mixer.Sound("crash.wav")

# Define the Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Set initial speed and load enemy image
        self.speed = 5
        self.image = pygame.image.load('Enemy.png')
        self.rect = self.image.get_rect()
        # Set initial position randomly at the top of the screen
        self.rect.center = (
            random.randint(self.rect.width, WIDTH - self.rect.width),
            0,
        )

    def draw(self, surface):
        # Draw enemy sprite on the surface
        surface.blit(self.image, self.rect)

    def update(self):
        # Move the enemy down the screen
        self.rect.move_ip(0, self.speed)
        # If enemy goes off the screen, reset its position at the top randomly
        if self.rect.y > HEIGHT:
            self.rect.center = (
                random.randint(self.rect.width, WIDTH - self.rect.width),
                0,
            )
            # Increase speed slightly to increase difficulty
            self.speed += 0.3

# Define the Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Set initial speed and load player image
        self.speed = 7
        self.image = pygame.image.load('Player.png')
        self.rect = self.image.get_rect()
        # Set initial position at the bottom center of the screen
        self.rect.center = (WIDTH // 2, HEIGHT - self.rect.height // 2 - 20)

    def draw(self, surface):
        # Draw player sprite on the surface
        surface.blit(self.image, self.rect)

    def update(self):
        # Move the player left or right based on key presses
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] and self.rect.x - self.speed >= 0:
            self.rect.move_ip(-self.speed, 0)
        elif pressed[pygame.K_RIGHT] and self.rect.x + self.speed + self.rect.width <= WIDTH:
            self.rect.move_ip(self.speed, 0)

# Define the Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Load coin image and set initial speed
        self.image = pygame.image.load("small_heart.png")
        self.speed = 7
        # Resize the coin image
        self.resized_image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.resized_image.get_rect()
        # Set initial position randomly at the top of the screen
        if WIDTH - self.rect.width > self.rect.width:
            x = random.randint(self.rect.width, WIDTH - self.rect.width)
        else:
            x = random.randint(WIDTH - self.rect.width, self.rect.width)
        self.rect.center = (x, 0)

    def draw(self, surface):
        # Draw coin sprite on the surface
        surface.blit(self.resized_image, self.rect)

    def update(self):
        # Move the coin down the screen
        self.rect.move_ip(0, self.speed)
        # If coin goes off the screen, reset its position at the top randomly
        if self.rect.y > HEIGHT:
            self.rect.center = (
                random.randint(self.rect.width, WIDTH - self.rect.width),
                0,
            )

    def collide(self, player):
        # Check collision with the player
        if pygame.sprite.collide_rect(self, player):
            # Remove the coin from the group if collided with the player
            self.kill()
            return True
        return False

# Define the main game function
def main():
    global coins
    running = True
    # Create player, enemy, and coin instances
    player = Player()
    enemy = Enemy()
    coin = Coin()
    # Create sprite groups for enemies and coins
    enemies = pygame.sprite.Group()
    enemies.add(enemy)
    coins.add(coin)
    # Start playing the background music
    background_sound.play(-1)

    while running:
        global SCORE
        # Draw the background image on the screen
        SCREEN.blit(background, (0, 0))
        # Render and display the current score
        score = score_font.render(f"Your score: {SCORE}", True, BLACK)
        SCREEN.blit(score, (0, 0))

        # Event handling loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update player and enemy positions
        player.update()
        enemy.update()

        # Handle collisions between player and coins
        for coin in coins:
            if coin.collide(player):
                # Remove collided coin and add a new one
                coins.remove(coin)
                SCORE += 1
                coins.add(Coin())

        # Draw and update coins, player, and enemy
        coin.draw(SCREEN)
        coin.update()
        player.draw(SCREEN)
        enemy.draw(SCREEN)

        # Check collision between player and enemies
        if pygame.sprite.spritecollide(player, enemies, False):
            # Stop background music, play crash sound, wait, then end the game
            background_sound.stop()
            crush_sound.play()
            pygame.time.wait(2000)
            running = False

        # Update display and control frame rate
        pygame.display.flip()
        clock.tick(60)

# Run the main game function
main()
  

# Name: Connor Elzinga
# Date: 05/18/2026
# Pygame Dodge Game

"""
Pygame Dodge Game

"""

import pygame
import random
import sys

pygame.init()

# The Window
WIDTH = 600
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge Game")

# Clock
clock = pygame.time.Clock()
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 120, 255)
RED = (255, 60, 60)
GREEN = (0, 255, 0)
PURPLE = (255, 0, 255)

# ===== Player =====
class Player(object):
    def __init__(self):
        width = 60
        height = 60

        x = WIDTH // 2 - width // 2
        y = HEIGHT - 90

        self.rect = pygame.Rect(x, y, width, height)
        self.speed = 7

    def handle_input(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        # Keep player on the screen
        if self.rect.x < 0:
            self.rect.x = 0

        if self.rect.x > WIDTH - self.rect.width:
            self.rect.x = WIDTH - self.rect.width

    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, self.rect)


# ===== Falling Object =====
class FallingObject(object):
    def __init__(self, speed, color):
        width = 50
        height = 50
        x = random.randint(0, WIDTH - width)
        y = -height
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed
        self.color = color

    def update(self):
        self.rect.y += self.speed

        # Reset at top of the screen at a new position and score
        score = 0
        if self.rect.y > HEIGHT:
            self.reset()
            score = 1
        return score
    
    def reset(self):
        y = -self.rect.height
        x = random.randint(0, WIDTH - self.rect.width)
        self.rect.x = x
        self.rect.y = y
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


# ===== GAME =====
class Game:
    def __init__(self):
        # Player
        self.player = Player()
        
        # Objects
        self.falling_objects = [
            FallingObject(5, RED),
            FallingObject(10, BLUE),
            FallingObject(15, PURPLE),
        ]
        
        self.score = 0
        self.lives = 3
        self.game_over = False

        self.font = pygame.font.SysFont(None, 36)
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True
    
    def update(self):
        keys = pygame.key.get_pressed()

        # Update player with input
        self.player.handle_input(keys)
  
        # Update falling object positions and score
        # Also check for collisions
        for falling_object in self.falling_objects:
            self.score += falling_object.update()

            # On collision with a falling object, reset it and lose a life
            if self.player.rect.colliderect(falling_object.rect):
                self.lives -= 1
                falling_object.reset()

                if self.lives <= 0:
                    self.game_over = True

    def draw(self):
        screen.fill(WHITE)

        self.player.draw(screen)
        
        for falling_object in self.falling_objects:
            falling_object.draw(screen)
        
        # Draw score
        score_text = self.font.render(f"Score: {self.score}", True, BLACK)
        screen.blit(score_text, (20, 20))

        lives_text = self.font.render(f"Lives: {self.lives}", True, BLACK)
        screen.blit(lives_text, (20, 60))
        
        # Draw game state
        if self.game_over:
            game_over_text = self.font.render("GAME OVER", True, BLACK)
            restart_text = self.font.render("Close the window to quit.", True, BLACK)

            screen.blit(game_over_text, (WIDTH // 2 - 90, HEIGHT // 2 - 30))
            screen.blit(restart_text, (WIDTH // 2 - 140, HEIGHT // 2 + 10))
        
        pygame.display.update()
    
    def run(self):
        running = True
        while running:
            running = self.handle_events()
            
            if not self.game_over:
                self.update()
            
            self.draw()
            clock.tick(60)
        
        pygame.quit()
        sys.exit()


# Run the game
if __name__ == "__main__":
    game = Game()
    game.run()
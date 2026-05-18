# Pygame Dodge Game Assignment

## Overview and Goal

Today you are going to build a new Pygame arcade game called **Dodge Game**.

In this game, the player moves left and right at the bottom of the screen while objects fall from the top. The goal is to survive as long as possible without getting hit.

This game is different from a platformer because there is no jumping or gravity for the player. Instead, this game focuses on:

- Keyboard movement
- Falling objects
- Collision detection
- Score
- Game over screen
- Customizing your own game theme

---

## Game Idea

The basic version of the game works like this:

1. A player appears near the bottom of the screen.
2. The player moves left and right using the arrow keys.
3. Objects fall from the top of the screen.
4. If the player touches a falling object, the game ends.
5. The score increases when the player successfully dodges an object.

---

## Theme Ideas

You can customize your game with almost any school-appropriate theme.

Here are some ideas:

- Dodge falling asteroids
- Dodge basketballs
- Dodge fireballs
- Dodge homework
- Dodge tacos
- Dodge football defenders
- Dodge raindrops
- Dodge monsters
- Dodge falling books
- Dodge lava rocks

---

# Step 1: Create a New Python File

Create a new Python file called:

```python
dodge_game.py
```

At the top of your file, add this comment:

```python
# Name:
# Date:
# Pygame Dodge Game
```

---

# Step 2: Import Pygame and Random

Start your code with these imports:

```python
import pygame
import random
```

`pygame` lets us create the game window, draw objects, and check for keyboard input.

`random` lets us make falling objects appear in random places.

---

# Step 3: Initialize Pygame

Add this below your imports:

```python
pygame.init()
```

This starts Pygame and gets it ready to use.

---

# Step 4: Create the Game Window

Add this code:

```python
WIDTH = 600
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge Game")
```

This creates a game window that is 600 pixels wide and 700 pixels tall.

---

# Step 5: Create the Clock

Add this code:

```python
clock = pygame.time.Clock()
FPS = 60
```

The clock controls how fast the game runs.

`FPS = 60` means the game tries to update 60 times per second.

---

# Step 6: Create Colors

Add this code:

```python
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 120, 255)
RED = (255, 60, 60)
```

Colors in Pygame use RGB values.

RGB means:

- Red
- Green
- Blue

Each number can be from 0 to 255.

---

# Step 7: Create the Player

Add this code:

```python
player_width = 60
player_height = 60

player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 90

player_speed = 7
```

This creates the player’s size, starting position, and speed.

The player will start near the bottom center of the screen.

---

# Step 8: Create the First Falling Object

Add this code:

```python
object_width = 50
object_height = 50

object_x = random.randint(0, WIDTH - object_width)
object_y = -object_height

object_speed = 5
```

This creates one falling object.

The object starts above the screen and falls downward.

---

# Step 9: Create the Score and Font

Add this code:

```python
score = 0
font = pygame.font.SysFont(None, 36)
```

The score starts at 0.

The font will be used to display text on the screen.

---

# Step 10: Create Game State Variables

Add this code:

```python
running = True
game_over = False
```

`running` controls whether the game window stays open.

`game_over` controls whether the player has lost.

---

# Step 11: Add the Main Game Loop

Add this code:

```python
while running:
    clock.tick(FPS)
```

Everything inside this `while` loop happens over and over while the game is running.

---

# Step 12: Check for Quit Events

Inside the game loop, add this code:

```python
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
```

This lets the player close the game window.

Your code should now look like this section:

```python
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
```

---

# Step 13: Add Player Movement

Still inside the game loop, add this code:

```python
    if not game_over:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            player_x -= player_speed

        if keys[pygame.K_RIGHT]:
            player_x += player_speed
```

This checks if the left or right arrow key is pressed.

If the player presses left, the player moves left.

If the player presses right, the player moves right.

---

# Step 14: Keep the Player on the Screen

Below the movement code, add this:

```python
        if player_x < 0:
            player_x = 0

        if player_x > WIDTH - player_width:
            player_x = WIDTH - player_width
```

This stops the player from moving off the left or right side of the screen.

---

# Step 15: Move the Falling Object

Below the player boundary code, add this:

```python
        object_y += object_speed
```

This makes the object fall down the screen.

---

# Step 16: Reset the Falling Object

Add this code below the object movement:

```python
        if object_y > HEIGHT:
            object_y = -object_height
            object_x = random.randint(0, WIDTH - object_width)
            score += 1
```

When the object falls past the bottom of the screen, it resets to the top.

The player earns 1 point each time they successfully dodge the object.

---

# Step 17: Create Rectangles for Collision

Add this code below the object reset code:

```python
        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
        object_rect = pygame.Rect(object_x, object_y, object_width, object_height)
```

Pygame uses rectangles to check if two objects are touching.

---

# Step 18: Check for Collision

Add this code below the rectangle code:

```python
        if player_rect.colliderect(object_rect):
            game_over = True
```

If the player touches the falling object, the game is over.

---

# Step 19: Draw the Background

Outside of the `if not game_over:` section, but still inside the game loop, add this:

```python
    screen.fill(WHITE)
```

This clears the screen and fills it with a white background every frame.

---

# Step 20: Draw the Player and Falling Object

Add this below the background:

```python
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))
    pygame.draw.rect(screen, RED, (object_x, object_y, object_width, object_height))
```

This draws the player and the falling object as rectangles.

---

# Step 21: Draw the Score

Add this below the drawing code:

```python
    score_text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, (20, 20))
```

This displays the score in the top-left corner.

---

# Step 22: Draw the Game Over Message

Add this below the score code:

```python
    if game_over:
        game_over_text = font.render("GAME OVER", True, BLACK)
        restart_text = font.render("Close the window to quit.", True, BLACK)

        screen.blit(game_over_text, (WIDTH // 2 - 90, HEIGHT // 2 - 30))
        screen.blit(restart_text, (WIDTH // 2 - 140, HEIGHT // 2 + 10))
```

This shows a game over message when the player gets hit.

---

# Step 23: Update the Display

Add this near the bottom of the game loop:

```python
    pygame.display.update()
```

This updates the screen so the player can see the changes.

---

# Step 24: Quit Pygame

At the very bottom of your file, outside the game loop, add:

```python
pygame.quit()
```

This closes Pygame properly when the game ends.

---

# Checkpoint 1

Before moving on, your game should:

- Open a Pygame window
- Show a blue player rectangle
- Show a red falling object
- Let the player move left and right
- Show a score
- End the game when the player gets hit

If your game does not do these things, fix it before moving on.

---

# Step 25: Add Two More Falling Objects

Now add two more falling objects.

Near your first falling object variables, add this:

```python
object2_x = random.randint(0, WIDTH - object_width)
object2_y = -200
object2_speed = 6

object3_x = random.randint(0, WIDTH - object_width)
object3_y = -400
object3_speed = 7
```

---

# Step 26: Move the New Objects

Inside the `if not game_over:` section, below this line:

```python
object_y += object_speed
```

Add:

```python
object2_y += object2_speed
object3_y += object3_speed
```

---

# Step 27: Reset the New Objects

Below the reset code for the first object, add:

```python
if object2_y > HEIGHT:
    object2_y = -object_height
    object2_x = random.randint(0, WIDTH - object_width)
    score += 1

if object3_y > HEIGHT:
    object3_y = -object_height
    object3_x = random.randint(0, WIDTH - object_width)
    score += 1
```

Make sure this code is indented inside `if not game_over:`.

---

# Step 28: Create Rectangles for the New Objects

Below the first object rectangle, add:

```python
object2_rect = pygame.Rect(object2_x, object2_y, object_width, object_height)
object3_rect = pygame.Rect(object3_x, object3_y, object_width, object_height)
```

---

# Step 29: Check Collision for the New Objects

Change your collision code from this:

```python
if player_rect.colliderect(object_rect):
    game_over = True
```

To this:

```python
if player_rect.colliderect(object_rect) or player_rect.colliderect(object2_rect) or player_rect.colliderect(object3_rect):
    game_over = True
```

---

# Step 30: Draw the New Objects

Below the draw code for the first falling object, add:

```python
pygame.draw.rect(screen, RED, (object2_x, object2_y, object_width, object_height))
pygame.draw.rect(screen, RED, (object3_x, object3_y, object_width, object_height))
```

---

# Checkpoint 2

Before customizing, your game should now have:

- 1 player
- 3 falling objects
- Score that increases
- Game over when the player touches any falling object

---

# Step 31: Customize Your Game

Now make the game your own.

You must add at least **5 customizations**.

Choose from this list:

- Change the title of the game
- Change the colors
- Change the player size
- Change the falling object size
- Add more falling objects
- Make objects fall faster as the score increases
- Add a background color
- Add a theme
- Add images instead of rectangles
- Add a restart option
- Add lives instead of instant game over
- Add a high score variable
- Add text instructions
- Add a “You Win” message after a certain score
- Add a second type of falling object that gives bonus points
- Add sound effects
- Add a start screen

---

# Challenge 1: Make the Game Get Harder

Add this inside the `if not game_over:` section after the object reset code:

```python
object_speed = 5 + score // 5
object2_speed = 6 + score // 5
object3_speed = 7 + score // 5
```

This makes the objects fall faster as the score gets higher.

---

# Challenge 2: Add a Restart Key

Inside your event loop, add this code:

```python
if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_r and game_over:
        game_over = False
        score = 0
        player_x = WIDTH // 2 - player_width // 2

        object_y = -object_height
        object_x = random.randint(0, WIDTH - object_width)

        object2_y = -200
        object2_x = random.randint(0, WIDTH - object_width)

        object3_y = -400
        object3_x = random.randint(0, WIDTH - object_width)
```

Then change your restart message to:

```python
restart_text = font.render("Press R to restart.", True, BLACK)
```

---

# Challenge 3: Add Lives

Instead of ending the game immediately, create a `lives` variable near the score:

```python
lives = 3
```

Display lives on the screen:

```python
lives_text = font.render("Lives: " + str(lives), True, BLACK)
screen.blit(lives_text, (20, 60))
```

When the player gets hit, subtract a life:

```python
lives -= 1
```

Then only end the game when lives are gone:

```python
if lives <= 0:
    game_over = True
```

This is harder because you also need to reset the falling object after a hit so the player does not instantly lose all lives.

---

# Requirements Checklist

Your finished game must include:

- A Pygame window
- A player controlled by the keyboard
- At least 3 falling objects
- Collision detection
- A score
- A game over screen
- At least 5 customizations
- Code that runs without errors
- No inappropriate content

---

# Submission

Submit your `.py` file or paste your code into Google Classroom.

Also answer these questions:

1. What is the theme of your dodge game?
2. What are the player and falling objects supposed to represent?
3. What are 3 customizations you added?
4. What was the hardest bug or problem you had to fix?
5. What would you add if you had more time?

---

# If You Finish Early

Add one or more of these features:

- More falling objects
- A restart button
- Lives
- A timer
- A high score
- Images
- Sound effects
- A win screen
- A start screen
- A second bonus object
- Increasing difficulty
- A custom background
- Different object speeds
- A larger or smaller player

A strong finished project should look like your own game, not just the copied starter version.

---

# Common Errors

## Error: `ModuleNotFoundError: No module named pygame`

This means Pygame is not installed or you are using the wrong coding environment.

Use the same environment you used for your platformer project.

---

## Error: Window Opens and Immediately Closes

Check that you have the main game loop:

```python
while running:
```

Also check that `pygame.quit()` is at the very bottom of your file, outside the loop.

---

## Error: Player Moves Off the Screen

Make sure you included this code:

```python
if player_x < 0:
    player_x = 0

if player_x > WIDTH - player_width:
    player_x = WIDTH - player_width
```

---

## Error: Collision Does Not Work

Make sure you created rectangles:

```python
player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
object_rect = pygame.Rect(object_x, object_y, object_width, object_height)
```

Then make sure you checked collision:

```python
if player_rect.colliderect(object_rect):
    game_over = True
```

---

## Error: IndentationError

Python cares about spacing.

Code inside a `while`, `for`, or `if` section must be indented.

Correct:

```python
if player_x < 0:
    player_x = 0
```

Incorrect:

```python
if player_x < 0:
player_x = 0
```

---

## Error: Score Does Not Show

Make sure you have this code inside the game loop:

```python
score_text = font.render("Score: " + str(score), True, BLACK)
screen.blit(score_text, (20, 20))
```

---

# Final Reminder

Your goal today is to build a working Pygame arcade game.

Start by getting the basic game working first.

Then customize it and make it your own.

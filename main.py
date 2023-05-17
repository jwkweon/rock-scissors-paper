import pygame
import sys
import numpy as np
import numpy.random as rand
from math import sqrt
# Initialize Pygame
pygame.init()

# Set up the display
width = 450
height = 600
numOfDots = 40
sizeOfIcon = 25

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rock Scissors Paper")

# Load images
dot1_img = pygame.image.load("./assets/rock.png")
dot2_img = pygame.image.load("./assets/scissors.png")
dot3_img = pygame.image.load("./assets/paper.png")

# Scale images to desired size
dot1_img = pygame.transform.scale(dot1_img, (sizeOfIcon, sizeOfIcon))
dot2_img = pygame.transform.scale(dot2_img, (sizeOfIcon, sizeOfIcon))
dot3_img = pygame.transform.scale(dot3_img, (sizeOfIcon, sizeOfIcon))

# Init dot coordinates for each status
rocks_poses = [(rand.randint(0, width), rand.randint(0, height)) for _ in range(numOfDots)]
sciss_poses = [(rand.randint(0, width), rand.randint(0, height)) for _ in range(numOfDots)]
paper_poses = [(rand.randint(0, width), rand.randint(0, height)) for _ in range(numOfDots)]


def check_collision(dot_pos, other_dot_pos):
    d_pos = dot_pos
    o_d_pos = other_dot_pos
    for i, pos in enumerate(dot_pos):
        for j, other_pos in enumerate(other_dot_pos):
            # Calculate Euclidean distance between two dots
            distance = sqrt((pos[0] - other_pos[0]) ** 2 + (pos[1] - other_pos[1]) ** 2)
            if distance < sizeOfIcon*0.9:
                d_pos.append((other_pos[0],other_pos[1]))
                o_d_pos.remove((other_pos[0],other_pos[1]))
    return d_pos, o_d_pos


def move_dots(dot_pos):
    for i in range(len(dot_pos)):
        dot_pos[i] = (dot_pos[i][0] + rand.normal()*1.7, dot_pos[i][1] + rand.normal()*1.7)

        # Wrap around screen edges
        if dot_pos[i][0] >= width-sizeOfIcon//2:
            dot_pos[i] = (width-sizeOfIcon//2, dot_pos[i][1])
        if dot_pos[i][1] >= height-sizeOfIcon//2:
            dot_pos[i] = (dot_pos[i][0], height-sizeOfIcon//2)

    return dot_pos

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move dots
    rocks_poses = move_dots(rocks_poses)
    sciss_poses = move_dots(sciss_poses)
    paper_poses = move_dots(paper_poses)

    # Check collisions
    rocks_poses, sciss_poses = check_collision(rocks_poses, sciss_poses)
    sciss_poses, paper_poses = check_collision(sciss_poses, paper_poses)
    paper_poses, rocks_poses = check_collision(paper_poses, rocks_poses)

    # Draw to the screen
    screen.fill((0, 0, 0))  # Fill the screen with black
    for pos in rocks_poses:
        screen.blit(dot1_img, pos)
    for pos in sciss_poses:
        screen.blit(dot2_img, pos)
    for pos in paper_poses:
        screen.blit(dot3_img, pos)

    # Display count of dots
    font = pygame.font.Font(None, 36)
    rock_count_text = font.render(f"Rock: {len(rocks_poses)}", True, (0, 255, 255))
    scissor_count_text = font.render(f"Scissor: {len(sciss_poses)}", True, (0, 255, 255))
    paper_count_text = font.render(f"Paper: {len(paper_poses)}", True, (0, 255, 255))
    screen.blit(rock_count_text, (10, 10))
    screen.blit(scissor_count_text, (10, 50))
    screen.blit(paper_count_text, (10, 90))

    if len(rocks_poses) == numOfDots*3 or len(sciss_poses) == numOfDots*3 or len(paper_poses) == numOfDots*3:
        time.sleep(5)
        quit()

    # Update the display
    pygame.display.flip()
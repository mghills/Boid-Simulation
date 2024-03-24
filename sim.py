from bird_class import Bird
from sim_class import Sim
import pygame
import random

margin = 100

screen_width= 1920
screen_height = 1080

max_speed = 4
min_speed = 2

bird_size = 3

# boid setup
sim = Sim(right_margin=screen_width, bottom_margin=screen_height, margin=margin, max_speed=max_speed, min_speed=min_speed)

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True

for i in range(100):
    temp_bird = Bird(sim, x=random.randrange(margin, screen_width-margin), y=random.randrange(margin, screen_height-margin), vx=random.randrange(min_speed, max_speed), vy=random.randrange(min_speed,max_speed))
    sim.add_bird(temp_bird)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    sim.simulate_instance()

    for bird in sim.bird_list:
        pos = pygame.Vector2(bird.x, bird.y)
        pygame.draw.circle(screen, "red", pos, 3)

    pygame.display.flip()

    clock.tick(60)

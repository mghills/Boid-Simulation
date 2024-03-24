import math
from numba import jit, cuda

class Bird:
    def __init__(self, sim, x=0, y=0, vx=0, vy=0):
        self.sim = sim

        self.x = x
        self.y = y
        
        self.vx = vx
        self.vy = vy

    def distance_from(self, other_bird):
        return math.sqrt(math.pow((self.x-other_bird.x), 2) + math.pow((self.y-other_bird.y), 2))

    def simulate_separation(self):
        close_dx = 0
        close_dy = 0

        for bird in self.sim.bird_list:
            if bird != self:
                if self.distance_from(bird) <= self.sim.protected_range:
                    close_dx += self.x - bird.x
                    close_dy += self.y - bird.y

        return close_dx, close_dy
    
    def simulate_alignment(self):
        xvel_avg = 0
        yvel_avg = 0
        neighboring_boids = 0

        for bird in self.sim.bird_list:
            if bird != self:
                if self.distance_from(bird) <= self.sim.visual_range:
                    xvel_avg += bird.vx
                    yvel_avg += bird.vy
                    neighboring_boids += 1

        if(neighboring_boids > 0):
            xvel_avg = xvel_avg/neighboring_boids
            yvel_avg = yvel_avg/neighboring_boids

        return xvel_avg, yvel_avg
    
    def simulate_cohesion(self):
        xpos_avg = 0
        ypos_avg = 0
        neighboring_boids = 0

        for bird in self.sim.bird_list:
            if bird != self:
                if self.distance_from(bird) <= self.sim.visual_range:
                    xpos_avg += bird.x
                    ypos_avg += bird.y
                    neighboring_boids += 1

        if(neighboring_boids > 0):
            xpos_avg = xpos_avg/neighboring_boids
            ypos_avg = ypos_avg/neighboring_boids

        return xpos_avg, ypos_avg

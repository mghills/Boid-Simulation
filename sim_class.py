import math

class Sim:
    def __init__(self, visual_range=40, protected_range=8, avoid_factor=0.05, matching_factor=0.05, centering_factor=0.0005, turn_factor=0.2, 
                 right_margin=1280, bottom_margin=720, margin=100, max_speed=6, min_speed=3):
        self.visual_range = visual_range
        self.protected_range = protected_range

        self.avoid_factor = avoid_factor
        self.matching_factor = matching_factor
        self.centering_factor = centering_factor
        self.turn_factor = turn_factor

        self.left_margin = margin
        self.right_margin = right_margin - margin
        self.bottom_margin = bottom_margin - margin
        self.top_margin = margin

        self.max_speed = max_speed
        self.min_speed = min_speed

        self.bird_list = list()

    def add_bird(self, bird):
        self.bird_list.append(bird)

    def simulate_instance(self):
        seperations_x = list()
        seperations_y = list()

        alignments_x = list()
        alignments_y = list()

        cohesions_x = list()
        cohesions_y = list()

        for bird in self.bird_list:
            seperation_x, seperation_y = bird.simulate_separation()
            alignment_x, alignment_y = bird.simulate_alignment()
            cohesion_x, cohesion_y = bird.simulate_cohesion()

            seperations_x.append(seperation_x)
            seperations_y.append(seperation_y)

            alignments_x.append(alignment_x)
            alignments_y.append(alignment_y)

            cohesions_x.append(cohesion_x)
            cohesions_y.append(cohesion_y)

        for bird in range(len(self.bird_list)):
            self.bird_list[bird].vx += seperations_x[bird]*self.avoid_factor
            self.bird_list[bird].vy += seperations_y[bird]*self.avoid_factor

            self.bird_list[bird].vx += (alignments_x[bird] - self.bird_list[bird].vx)*self.matching_factor
            self.bird_list[bird].vy += (alignments_y[bird] - self.bird_list[bird].vy)*self.matching_factor

            self.bird_list[bird].vx += (cohesions_x[bird] - self.bird_list[bird].x)*self.centering_factor
            self.bird_list[bird].vy += (cohesions_y[bird] - self.bird_list[bird].y)*self.centering_factor

            speed = math.sqrt(self.bird_list[bird].vx*self.bird_list[bird].vx + self.bird_list[bird].vy*self.bird_list[bird].vy)

            if speed > self.max_speed:
               self.bird_list[bird].vx = (self.bird_list[bird].vx/speed)*self.max_speed
               self.bird_list[bird].vy = (self.bird_list[bird].vy/speed)*self.min_speed
            if speed < self.min_speed:
                self.bird_list[bird].vx = (self.bird_list[bird].vx/speed)*self.min_speed
                self.bird_list[bird].vy = (self.bird_list[bird].vy/speed)*self.min_speed


        for bird in self.bird_list:
            if bird.x < self.left_margin:
                bird.vx = bird.vx + self.turn_factor
            if bird.x > self.right_margin:
                bird.vx = bird.vx - self.turn_factor
            if bird.y > self.bottom_margin:
                bird.vy = bird.vy - self.turn_factor
            if bird.y < self.top_margin:
                bird.vy = bird.vy + self.turn_factor
        
        for bird in self.bird_list:
            bird.x += bird.vx
            bird.y += bird.vy
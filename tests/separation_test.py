import sys
sys.path.append('../')

from bird_class import Bird
from sim_class import Sim

# test setup stuff
sim = Sim()

# print(sim.protected_range)
# print(sim.visual_range)

bird1 = Bird(sim, 5, 5)
sim.add_bird(bird1)
bird2 = Bird(sim, 10, 10)
sim.add_bird(bird2)
# bird3 = Bird(sim, 100, 100)

sim.simulate_instance()

print(bird1.x)
print(bird2.x)


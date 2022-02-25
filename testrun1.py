from trafficSimulator import *

# Create simulation
sim = Simulation()

# Add one road
sim.create_road((300, 98), (0, 98))
sim.create_road((0, 102), (300, 102))
sim.create_road((150, 0), (150, 200))
sim.create_road((154, 200), (154, 00))

# Start simulation
win = Window(sim)
win.loop()
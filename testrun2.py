from trafficSimulator import *

# Create simulation
sim = Simulation()

# Add one road
sim.create_road((300, 98), (0, 98))
sim.create_road((0, 102), (300, 102))
sim.create_road((200, 0), (200, 200))
sim.create_road((204, 200), (204, 00))
sim.create_road((100, 0), (100, 200))
sim.create_road((104, 200), (104, 00))


# Start simulation
win = Window(sim)
win.loop()
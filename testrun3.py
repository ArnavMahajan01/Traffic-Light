from trafficSimulator import *

# Create simulation
sim = Simulation()

# Add multiple roads
sim.create_roads([
    ((0, 100), (140, 100)),
    ((150, 110), (150, 200)),

    *curve_road((140, 100), (150, 110), (150, 100))
])

# Start simulation
win = Window(sim)
win.loop()
#win.offset = (-150, -110)
#win.run(steps_per_update=5)
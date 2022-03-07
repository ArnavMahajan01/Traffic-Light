from trafficSimulator import *

# Create simulation
sim = Simulation()

# Curve resolution
n = 15

# Add multiple roads
sim.create_roads([
    ((-10, 106), (290, 106)),
    ((-10, 102), (290, 102)),

    ((290, 98), (-10, 98)),
    ((290, 94), (80, 94)),
    ((80, 94), (-10, 94)),

    ((101, 90), (80, 94)),
    ((160, 90), (100, 90)),

    *curve_road((250, 10), (160, 90), (210, 90), resolution=n)
])


# Start simulation
win = Window(sim)
win.loop()
#win.offset = (-145, -95)
#win.zoom = 8
#win.run(steps_per_update=5)
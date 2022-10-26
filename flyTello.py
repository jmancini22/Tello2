from easytello import tello

my_drone = tello.Tello()

my_drone.takeoff()

for i in range(4):
    my_drone.forward(10)
    my_drone.cw(45)

my_drone.land()
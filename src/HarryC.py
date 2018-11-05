"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time
import rosebotics_new as rbn
from ev3dev import ev3



def main():
    """ Runs YOUR specific part of the project """
    #test_go_straight_inches(30,-100)
    #test_spin(360,-100)
    #test_turn(180,-100)
    test_camera_beep()

def test_go_straight_inches(inch,speed):
    robot = rb.Snatch3rRobot()
    robot.drive_system.go_straight_inches(inch,duty_cycle_percent=speed)

def test_spin(degree,dutypercent):
    robot = rb.Snatch3rRobot()
    robot.drive_system.spin_in_place_degrees(degree,dutypercent)

def test_turn(degree,dutypercent):
    robot = rb.Snatch3rRobot()
    robot.drive_system.turn_degrees(degree,dutypercent)

def test_camera_beep():
    robot = rbn.Snatch3rRobot()
    while True:
        if robot.camera.get_biggest_blob().get_area()<=300:
            ev3.Sound.beep()
            print(robot.camera.get_biggest_blob().get_area())
            time.sleep(0.001)
        else:
            time.sleep(0.001)



main()

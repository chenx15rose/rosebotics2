"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    #test_go_straight_inches(30,-100)
    test_spin(360,-100)
    #test_turn(180,-100)
    test_polygon_run(5,8)

def test_go_straight_inches(inch,speed):
    robot = rb.Snatch3rRobot()
    robot.drive_system.go_straight_inches(inch,duty_cycle_percent=speed)

def test_spin(degree,dutypercent):
    robot = rb.Snatch3rRobot()
    robot.drive_system.spin_in_place_degrees(degree,dutypercent)

def test_turn(degree,dutypercent):
    robot = rb.Snatch3rRobot()
    robot.drive_system.turn_degrees(degree,dutypercent)
def test_polygon_run(number_of_sides,length_of_sides):
    robot = rb.Snatch3rRobot()
    for k in range(number_of_sides):
        robot.drive_system.go_straight_inches(length_of_sides)
        time.sleep(0.01)
        robot.drive_system.spin_in_place_degrees(180 - (number_of_sides - 2) / number_of_sides * 160)
        time.sleep(0.2)
    robot.drive_system.stop_moving()

main()

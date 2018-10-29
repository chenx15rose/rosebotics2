"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    test_go_straight_inches(30,100)

def test_go_straight_inches(inch,speed):
    robot = rb.Snatch3rRobot()
    robot.drive_system.go_straight_inches(inch,duty_cycle_percent=speed)
    robot.drive_system.stop_moving(rb.StopAction.BRAKE)


main()

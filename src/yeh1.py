"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    test_wait_until_pressed()
    test_wait_until_released()



def test_wait_until_pressed():
    robot = rb.Snatch3rRobot()
    robot.drive_system.start_moving(50, 50)
    robot.touch_sensor.wait_until_released()
    robot.drive_system.stop_moving()

def test_wait_until_released():
    robot = rb.Snatch3rRobot()









main()

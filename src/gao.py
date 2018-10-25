"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    robot = rb.Snatch3rRobot
    robot.drive_system.start_moving(30,30)
    robot.color_sensor.wait_until_diversity_is_less_than(20)
    robot.drive_system.stop_moving

main()

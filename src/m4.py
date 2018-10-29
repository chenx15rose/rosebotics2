"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    robot = rb.Snatch3rRobot()
    # 1
    n = 5
    m = 5
    for k in range(n):
        robot.drive_system.go_straight_inches(m)
        robot.drive_system.spin_in_place_degrees((n - 2) / n * 180)
    robot.drive_system.stop_moving()

main()

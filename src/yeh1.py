"""
  Capstone Project.  Code written by Hengqi Ye(Luis).
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    #test_wait_until_pressed()
    test_wait_until_released()
    #test_color_stop_by(5)


def test_wait_until_pressed():
    robot = rb.Snatch3rRobot()
    while True:
        robot.drive_system.start_moving(50, 50)
        robot.touch_sensor.wait_until_pressed()
        robot.drive_system.stop_moving()
        robot.touch_sensor.wait_until_released()

def test_wait_until_released():
    robot = rb.Snatch3rRobot()
    robot.touch_sensor.wait_until_pressed()
    robot.touch_sensor.wait_until_released()
    robot.drive_system.start_moving(50, 50)
def test_color_stop_by(color_number):
    robot = rb.Snatch3rRobot()
    robot.drive_system.start_moving(50, 50)
    robot.color_sensor.wait_until_color_is(color_number)
    robot.drive_system.stop_moving()
    print(robot.color_sensor.get_color())








main()

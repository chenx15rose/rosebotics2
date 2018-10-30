"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    robot = rb.Snatch3rRobot()
    middle_value = 50
    t = 0.005
    intergral = 0
    delta = 0
    while True:
        p_delta = delta
        delta = robot.color_sensor.get_reflected_intensity() - middle_value
        if robot.color_sensor.get_reflected_intensity() <= middle_value + 5 and \
                robot.color_sensor.get_reflected_intensity() >= middle_value - 5:
            intergral = 0
            robot.drive_system.start_moving(80, 80)
        else:
            intergral += delta
            speedleft = 50 + delta * 0.8 + 0.0125 * intergral + (delta-p_delta)*0.6
            speedright = 50 - delta * 0.8 + 0.0125 * intergral + (delta-p_delta)*0.6
            robot.drive_system.start_moving(speedleft, speedright)

main()

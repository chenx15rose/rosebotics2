"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    robot = rb.Snatch3rRobot


while True:
    self.motor.stop_spinning()
    self.touch_sensor.wait_until_pressed()
    self.motor.start_spinning(100)
    self.touch_sensor.wait_until_released()
main()

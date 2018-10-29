"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    robot = rb.Snatch3rRobot()
    count = 1
    while True:
        print("{:4}.".format(count),
            "Touch sensor value is: ", robot.touch_sensor.get_value())
        if robot.touch_sensor.get_value() == 0:
            rb.DriveSystem.start_moving(100,100)
            time.sleep(1)

        count = count + 1
        time.sleep(0.5)




main()

"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics_even_newer as rb
import time
from ev3dev import ev3

def test_color_go_line():
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
            speedleft = 50 + delta * 0.8 + 0.0125 * intergral + (delta - p_delta) * 0.6
            speedright = 50 - delta * 0.8 + 0.0125 * intergral + (delta - p_delta) * 0.6
            robot.drive_system.start_moving(speedleft, speedright)
def test_color_wait_until_intensity():
    robot = rb.Snatch3rRobot()
    robot.drive_system.start_moving(50,50)
    robot.color_sensor.wait_until_intensity_is_greater_than(50)
    robot.drive_system.stop_moving()
def test_color_wait_until_is():
    robot = rb.Snatch3rRobot()
    robot.drive_system.start_moving(50,50)
    robot.color_sensor.wait_until_color_is(3)
    robot.drive_system.stop_moving()
def beep_when_near():
    robot = rb.Snatch3rRobot()
    while True :
        if robot.proximity_sensor.get_distance_to_nearest_object_in_inches()>9 \
            and robot.proximity_sensor.get_distance_to_nearest_object_in_inches()<15:
            print(robot.proximity_sensor.get_distance_to_nearest_object_in_inches())
            ev3.Sound.beep(0.5)
            # ev3.Sound.play("/home/robot/csse120/assets/sounds/awesome_pcm.wav")




def main():

    """ Runs YOUR specific part of the project """
    beep_when_near()

main()

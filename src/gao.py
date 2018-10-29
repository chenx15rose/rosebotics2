"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():

    """ Runs YOUR specific part of the project """
    robot = rb.Snatch3rRobot()
    #1
    n=5
    for k in range(n):
        robot.drive_system.go_straight_inches(m)
        robot.drive_system.spin_in_place_degrees((n-2)/n*180)
    robot.drive_system.stop_moving()
    #2
    middle_value = 50
    t = 0.005
    intergral = 0
    delta = 0
    while True:
        p_delta = delta
        delta = robot.color_sensor.get_reflected_intensity() - middle_value
        if robot.color_sensor.get_reflected_intensity() <= middle_value+5 and robot.color_sensor.get_reflected_intensity()>=middle_value-5:
            intergral = 0
            robot.drive_system.start_moving(60,60)
            time.sleep(t)
        else:
            intergral += delta
            speedleft = 50 - delta*0.6 + 0.03*intergral #+(delta-p_delta)*0.01
            speedright = 50 + delta*0.6 + 0.03*intergral #+py(delta-p_delta)*0.01
            robot.drive_system.start_moving(speedleft,speedright)
            time.sleep(t)
    #3
    color = 5
    robot = rb.Snatch3rRobot()
    robot.drive_system.start_moving(50,50)
    robot.color_sensor.wait_until_color_is(color)
    robot.drive_system.stop_moving()
    print(robot.color_sensor.get_color())
main()

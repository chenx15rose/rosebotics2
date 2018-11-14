"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

Also: responds to Beacon button-presses by beeping, speaking.

This module runs on the ROBOT.
It uses MQTT to RECEIVE information from a program running on the LAPTOP.

Authors:  David Mutchler, his colleagues, and BERT.
"""
# ------------------------------------------------------------------------------
# DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.  Then delete this TODO.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# TODO: 2. With your instructor, review the "big picture" of laptop-robot
# TODO:    communication, per the comment in mqtt_sender.py.
# TODO:    Once you understand the "big picture", delete this TODO.
# ------------------------------------------------------------------------------

import rosebotics_even_newer as rb
import time
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3


def main():
    # --------------------------------------------------------------------------
    # TODO: 3. Construct a Snatch3rRobot.  Test.  When OK, delete this TODO.
    # --------------------------------------------------------------------------
    robot = rb.Snatch3rRobot()

    rc = RemoteControlEtc(robot)
    mqtt_client = com.MqttClient(rc)
    mqtt_client.connect_to_pc()

    # --------------------------------------------------------------------------
    # TODO: 4. Add code that constructs a   com.MqttClient   that will
    # TODO:    be used to receive commands sent by the laptop.
    # TODO:    Connect it to this robot.  Test.  When OK, delete this TODO.
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # TODO: 5. Add a class for your "delegate" object that will handle messages
    # TODO:    sent from the laptop.  Construct an instance of the class and
    # TODO:    pass it to the MqttClient constructor above.  Augment the class
    # TODO:    as needed for that, and also to handle the go_forward message.
    # TODO:    Test by PRINTING, then with robot.  When OK, delete this TODO.
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # TODO: 6. With your instructor, discuss why the following WHILE loop,
    # TODO:    that appears to do nothing, is necessary.
    # TODO:    When you understand this, delete this TODO.
    # --------------------------------------------------------------------------

        # ----------------------------------------------------------------------
        # TODO: 7. Add code that makes the robot beep if the top-red button
        # TODO:    on the Beacon is pressed.  Add code that makes the robot
        # TODO:    speak "Hello. How are you?" if the top-blue button on the
        # TODO:    Beacon is pressed.  Test.  When done, delete this TODO.
        # ----------------------------------------------------------------------

    while True:
        time.sleep(0.01)  # For the delegate to do its work
class RemoteControlEtc(object):
    def __init__(self, robot):
        """
        Stores a robot.
            :type robot: rb.Snatch3rRobot
        """

        self.robot = robot
        self.mqtt_client = None
    def beep_and_talk(self,speak_string,volume):
            while True:
                if self.robot.beacon_button_sensor.is_bottom_blue_button_pressed() is True:
                    break
                if self.robot.beacon_button_sensor.is_top_red_button_pressed() is True:
                    ev3.Sound.beep(0.5)
                if self.robot.beacon_button_sensor.is_top_blue_button_pressed() is True:
                    ev3.Sound.set_volume(volume)
                    ev3.Sound.speak(speak_string)

    def go_forward(self,speed_string):
        speed = int(speed_string)
        print('Robot should start moving',speed)
        self.robot.drive_system.start_moving(speed,speed)
    def Infrared_beacon(self):
        while True:
            if self.robot.beacon_button_sensor.is_top_blue_button_pressed() is True:
                self.robot.drive_system.go_straight_inches(5,-30)
            if self.robot.beacon_button_sensor.is_top_red_button_pressed() is True:
                self.robot.drive_system.go_straight_inches(5,30)
    def test_beacon(self, distance):
        print('hello')
        while self.robot.beacon_sensor.get_heading_to_beacon() < 0:
            self.robot.drive_system.start_moving(-50,50)
        while self.robot.beacon_sensor.get_heading_to_beacon() > 0:
            self.robot.drive_system.start_moving(50,-50)
        self.robot.drive_system.go_straight_inches(distance)
        self.robot.drive_system.stop_moving()
    def run_as_canvas(self,distance_list,n):
        for k in range(n):
            self.robot.drive_system.go_straight_inches(distance_list[k])
            ev3.Sound.beep(0.1)
        self.robot.drive_system.stop_moving()




main()
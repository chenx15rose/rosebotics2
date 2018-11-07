import ev3dev
import ev3dev.ev3 as ev3
import rosebotics_even_newer as rb
import low_level_rosebotics_new
import mqtt_remote_method_calls as com
import time


class MyDelegate(object):
    def __init__(self):
        self.robot = rb.Snatch3rRobot()
        self.mqtt_client = None  # To be set later.

    def go_straight_inches(self,inch,speed):
        self.robot.drive_system.go_straight_inches(inch, duty_cycle_percent=speed)

    def Brick_Button_method(self):
        self.robot = rb.Snatch3rRobot()
        while True:
            if self.robot.brick_button_sensor.is_top_button_pressed() is True:
                ev3.Sound.beep().wait(0.5)
            elif self.robot.brick_button_sensor.is_bottom_button_pressed() is True:
                ev3.Sound.beep().wait(0.5)
                ev3.Sound.beep()
    def Infraid_beacon(self):
        while True:
            if self.robot.beacon_button_sensor.is_top_blue_button_pressed() is True:
                self.robot.drive_system.go_straight_inches(11,-50)
            if self.robot.beacon_button_sensor.is_top_red_button_pressed() is True:
                self.robot.drive_system.go_straight_inches(11,50)
    def test_beacon(self, distance):
        while self.robot.beacon_sensor.get_heading_to_beacon() < 0:
            self.robot.drive_system.start_moving(-50,50)
        while self.robot.beacon_sensor.get_heading_to_beacon() > 0:
            self.robot.drive_system.start_moving(50,-50)
        self.robot.drive_system.go_straight_inches(distance)
        self.robot.drive_system.stop_moving()


def main():
    my_delegate = MyDelegate()
    mqtt_client = com.MqttClient(my_delegate)
    mqtt_client.connect_to_pc()
    while True:
        time.sleep(1)



main()
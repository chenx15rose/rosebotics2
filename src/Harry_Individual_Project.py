import rosebotics_even_newer as rb
import time
from ev3dev import ev3
import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com

def main():
    receiver = Receiver()
    receiver_client = com.MqttClient(receiver)
    receiver.mqtt_client = receiver_client
    receiver_client.connect_to_ev3()

    window= tkinter.Tk()
    window.title("A robot with multiple personalities")
    frame=ttk.Frame(window,padding=20)
    frame.grid()
    label1 = ttk.Label(frame,text="Welcome!")
    label1.grid(row=0,column=1)
    label2 = ttk.Label(frame,text="Choose A Personality To Interact With")
    label2.grid(row=1,column=1)
    label3 = ttk.Label(frame, text=" ")
    label3.grid(row=3, column=1)
    Arrogant_button = ttk.Button(frame,text='arrogant')
    Arrogant_button.grid(row=2,column=0)
    Arrogant_button['command']= lambda: receiver.If_Arrogant_clicked()
    Cold_button = ttk.Button(frame, text='cold')
    Cold_button.grid(row=2,column=2)
    Cold_button['command'] = lambda: receiver.If_Cold_clicked()
    Kind_button = ttk.Button(frame,text='kind')
    Kind_button.grid(row=2,column=1)
    Kind_button['command'] = lambda: receiver.If_Kind_clicked()
    Exit = ttk.Button(frame, text='Exit')
    Exit['command'] = lambda: exit()
    Exit.grid(row=5,column=2)


    window.mainloop()



class Receiver(object):

    def __init__(self):
        self.mqtt_client = None

    def arrogant_talk_popup(self):
        window4 = tkinter.Toplevel(width=500,height=500)
        window4.title("What do you want to talk")
        frame = ttk.Frame(window4, padding=20)
        frame.grid()
        Talk = ttk.Button(frame, text='You are such a bad tempered robot')
        Talk.grid()
        Talk['command']=lambda: self.mqtt_client.send_message("Bad_Tempered")
        color = ttk.Button(frame, text='What is your favorite color?')
        color.grid()
        color['command']=lambda: self.mqtt_client.send_message("Arrogant_Color")



    def If_Arrogant_clicked(self):
        window2 = tkinter.Toplevel()
        window2.title("I'm ARROGANT!!!")
        frame = ttk.Frame(window2, padding=20)
        frame.grid()
        Talk = ttk.Button(frame, text='You want to talk to me?')
        Talk.grid()
        Talk['command'] = lambda: self.mqtt_client.send_message("Arrogant_Talk")
        Exit = ttk.Button(frame, text='Exit')
        Exit['command'] = lambda: window2.destroy()
        Exit.grid()
        window2.mainloop()

    def If_Cold_clicked(self):
        window3 = tkinter.Toplevel()
        window3.title("......")
        frame = ttk.Frame(window3, padding=20)
        frame.grid()
        Talk = ttk.Button(frame, text='......talk?')
        Talk.grid()
        Talk['command'] = lambda: self.mqtt_client.send_message("Cold_Talk")
        Exit = ttk.Button(frame,text='Exit')
        Exit['command']= lambda: window3.destroy()
        window3.mainloop()

    def cold_talk_popup(self):
        window5 = tkinter.Toplevel(width=500,height=500)
        window5.title("What do you want to talk")
        frame = ttk.Frame(window5, padding=20)
        frame.grid()
        Talk = ttk.Button(frame, text='You are such a cold robot')
        Talk.grid()
        Talk['command']=lambda: self.mqtt_client.send_message("Cold")
        color = ttk.Button(frame, text='What is your favorite color?')
        color.grid()
        color['command']=lambda: self.mqtt_client.send_message("Cold_Color")

    def If_Kind_clicked(self):
        window3 = tkinter.Toplevel()
        window3.title("I'm Kind")
        frame = ttk.Frame(window3, padding=20)
        frame.grid()
        Kind = ttk.Button(frame, text='Greeting')
        Kind.grid(row=0,column=0)
        Kind['command'] = lambda: self.mqtt_client.send_message("Check_Greeting")

        Goodbye = ttk.Button(frame, text='Goodbye')
        Goodbye.grid(row=0, column=1)
        Goodbye['command'] = lambda: self.mqtt_client.send_message("Goodbye")

        Exit = ttk.Button(frame, text='Exit')
        Exit['command'] = lambda: window3.destroy()

        window3.mainloop()






main()
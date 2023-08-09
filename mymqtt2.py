import paho.mqtt.client as mqtt
import time
from random import uniform
import tkinter as tk

mqttBroker = "mqtt.eclipseprojects.io"
mqttPort = 1883

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print_to_output("Connected to MQTT broker")
        client.subscribe("home/bedroom/temperature")
    else:
        print_to_output("Connection failed")

def on_message(client, userdata, msg):
    print_to_output("Received message: " + msg.payload.decode("utf-8"))

def print_to_output(text):
    output_text.insert(tk.END, text + "\n")
    output_text.see(tk.END)  # Scroll to the end

def publisher():
    client = mqtt.Client("Temperature_Publisher")
    client.connect(mqttBroker, mqttPort)

    while True:
        try:
            randNumber = uniform(20.0, 21.0)
            client.publish("home/bedroom/temperature", randNumber)
            print_to_output("Just published " + str(randNumber) + " to topic home/bedroom/temperature")
            window.update()
            time.sleep(1)
        except Exception as e:
            print_to_output("An error occurred: " + str(e))
            break

def subscriber():
    client = mqtt.Client("Temperature_Subscriber")
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(mqttBroker, mqttPort)
    client.loop_start()

def publish_button_click():
    publish_button.config(state=tk.DISABLED)
    subscriber_button.config(state=tk.DISABLED)
    publisher()

def subscribe_button_click():
    publish_button.config(state=tk.DISABLED)
    subscriber_button.config(state=tk.DISABLED)
    subscriber()

# Create the tkinter window
window = tk.Tk()
window.title("MQTT Publisher-Subscriber")
window.geometry("300x300")

# Create buttons
publish_button = tk.Button(window, text="Start Publisher", command=publish_button_click)
publish_button.pack(pady=10)

subscriber_button = tk.Button(window, text="Start Subscriber", command=subscribe_button_click)
subscriber_button.pack(pady=10)

# Create output text area
output_text = tk.Text(window)
output_text.pack(fill=tk.BOTH, expand=True)

# Run the tkinter event loop
window.mainloop()


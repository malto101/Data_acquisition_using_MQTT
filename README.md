MQTT Publisher-Subscriber Example using Python and Tkinter
This is a simple example of an MQTT (Message Queuing Telemetry Transport) publisher-subscriber application implemented in Python using the Paho MQTT client library and the Tkinter GUI framework. MQTT is a lightweight messaging protocol often used in IoT (Internet of Things) applications for efficient communication between devices.

Prerequisites
Python 3.x installed on your system

Paho MQTT client library (paho-mqtt) installed. You can install it using the following command:

bash
Copy code
pip install paho-mqtt
How to Use
Clone or download this repository to your local machine.

Open a terminal and navigate to the directory containing the downloaded files.

Run the Python script using the following command:

bash
Copy code
python mqtt_gui_example.py
The graphical user interface (GUI) window will appear with two buttons: "Start Publisher" and "Start Subscriber".

Publisher: Click the "Start Publisher" button to initiate the MQTT publisher. This will generate random temperature values and publish them to the MQTT broker on the topic home/bedroom/temperature at regular intervals.

Subscriber: Click the "Start Subscriber" button to initiate the MQTT subscriber. The subscriber will connect to the MQTT broker and listen for messages on the home/bedroom/temperature topic. When a message is received, it will be displayed in the output text area.

To stop the publisher or subscriber, you can close the application window.

Important Notes
Make sure you have a working MQTT broker available. The code uses the mqtt.eclipseprojects.io broker by default, but you can replace it with your own broker's address and port in the mqttBroker and mqttPort variables.

The MQTT publisher generates random temperature values between 20.0 and 21.0 degrees Celsius. You can modify the randNumber assignment in the publisher() function to generate different values.

The on_connect() and on_message() functions handle the connection to the MQTT broker and the processing of received messages, respectively.

The GUI is built using the Tkinter framework, providing buttons for starting the publisher and subscriber, as well as a text area to display output messages.

Exception handling is implemented in case any errors occur during the MQTT operations.


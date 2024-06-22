import paho.mqtt.client as mqtt
import time
import Adafruit_DHT
import json
import time

# MQTT broker credentials
broker_url = "broker.hivemq.com"
broker_port =1883
username = "iot_18"
password = "12345_Iot_18"
topic = "IOTBDA"

# Create MQTT client instance
client = mqtt.Client()
#client.username_pw_set(username=username, password=password)

def read_sensor_data():
    sensor = Adafruit_DHT.DHT22
    pin = 4 # GPIO 4
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    return (humidity, temperature)

client.subscribe(topic)

try:
	client.connect(broker_url, broker_port)
except Exception as e:
	print(f"Error connecting to MQTT broker: {e}")
	exit(1)

# Sensor data collection and publishing
while True:
    humidity, temperature =  read_sensor_data()
    T = temperature * 9/5 + 32  # Convert temperature to Fahrenheit
    RH = humidity
    HI = -42.379 + 2.04901523*T + 10.14333127*RH - .22475541*T*RH - .00683783*T*T - .05481717*RH*RH+ .00122874*T*T*RH + .00085282*T*RH*RH - .00000199*T*T*RH*RH
    try:
        payload = {
            "humidity": round(humidity, 1),
            "heat": round(HI, 1),
	    "temperature" : round(temperature, 1)
        }
        client.publish(topic, json.dumps(payload))
        print("published - Humidity:", humidity, ", Temperature:", round(temperature, 1), ", Heat Index:", round(HI, 1))

        # Publish sensor data to MQTT broker

    except Exception as e:
        print(f"Error publishing to MQTT broker: {e}")
        continue

    time.sleep(2) # delay between sensor readings



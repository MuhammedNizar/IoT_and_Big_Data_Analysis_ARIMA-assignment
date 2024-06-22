import Adafruit_DHT
import time

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
LOG_FILE = "sensor_data.log"

def log_sensor_data(temperature, humidity, heat_index):
    """Log temperature, humidity, and heat index data to a file."""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as file:
        file.write(f"{timestamp}, Temperature: {temperature:.1f}°C, Humidity: {humidity:.1f}%, Heat Index: {heat_index:.1f}°C\n")

def calculate_heat_index(temperature, humidity):
    """Calculate the heat index given the temperature and humidity."""
    T_fahrenheit = temperature * 9/5 + 32
    RH = humidity

    # Heat index formula
    HI_fahrenheit = (-42.379 + 2.04901523 * T_fahrenheit + 10.14333127 * RH -
                     0.22475541 * T_fahrenheit * RH - 0.00683783 * T_fahrenheit**2 -
                     0.05481717 * RH**2 + 0.00122874 * T_fahrenheit**2 * RH +
                     0.00085282 * T_fahrenheit * RH**2 - 0.00000199 * T_fahrenheit**2 * RH**2)
    
    # Convert heat index back to Celsius
    HI_celsius = (HI_fahrenheit - 32) * 5/9
    return HI_celsius

def main():
    """Main function to read sensor data and log it."""
    while True:
        try:
            humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)

            if humidity is not None and temperature is not None:
                heat_index = calculate_heat_index(temperature, humidity)
                print("Temperature: {0:.1f}°C, Humidity: {1:.1f}%, Heat Index: {2:.1f}°C".format(temperature, humidity, heat_index))
                log_sensor_data(temperature, humidity, heat_index)
            else:
                print("Failed to retrieve data from sensor. Check wiring.")

        except Exception as e:
            print("An error occurred:", str(e))

        time.sleep(2)

if __name__ == "__main__":
    main()

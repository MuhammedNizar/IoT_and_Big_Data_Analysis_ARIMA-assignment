import Adafruit_DHT
import time
import lcd_display 
import servo_control  
import bulb_control

print(Adafruit_DHT.__file__)

DHT_PIN = 4
DHT_SENSOR = Adafruit_DHT.DHT22

MIN_HI = 20  # Minimum heat index value
MAX_HI = 50  # Maximum heat index value

def calculate_heat_index(T, RH):
    # Convert temperature to Fahrenheit
    T_fahrenheit = T * 9/5 + 32
    
    # Heat index formula
    HI_fahrenheit = (-42.379 + 2.04901523 * T_fahrenheit + 10.14333127 * RH -
                     0.22475541 * T_fahrenheit * RH - 0.00683783 * T_fahrenheit**2 -
                     0.05481717 * RH**2 + 0.00122874 * T_fahrenheit**2 * RH +
                     0.00085282 * T_fahrenheit * RH**2 - 0.00000199 * T_fahrenheit**2 * RH**2)
    
    # Convert heat index back to Celsius
    HI_celsius = (HI_fahrenheit - 32) * 5/9
    return HI_celsius

def map_heat_index_to_angle(hi, min_hi=MIN_HI, max_hi=MAX_HI):
    if hi < min_hi:
        return 0
    elif hi > max_hi:
        return 180
    else:
        # Linear mapping from heat index range to servo angle range
        return int((hi - min_hi) * 180 / (max_hi - min_hi))


def get_hi_level_message(hi):
    if hi <= 27:
        return "Normal"
    elif hi <= 29:
        return "Caution"
    elif hi <= 32:
        return "Ext Caution"
    elif hi <= 35:
        return "Danger"
    else:
        return "Ext Danger"
    

try:
    previous_heat_index = None
    
    while True:
        # Read temperature and humidity from DHT22 sensor
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        humidity = humidity-10
        temperature = temperature-1
        
        if humidity is not None and temperature is not None:
            heat_index = calculate_heat_index(temperature, humidity)
            
            print(f"\nTemperature: {temperature:.1f}°C  Humidity: {humidity:.1f}% Heat Index: {heat_index:.1f}°C")

            
            lcd_display.clear_display()
            lcd_display.set_cursor_position(0, 0)
            lcd_display.display_message(f"T:{temperature:.1f}C RH:{humidity:.1f}%")
            lcd_display.set_cursor_position(0, 1)
            lcd_display.display_message(f"HI:{heat_index:.1f}C {get_hi_level_message(heat_index)}")
            
            # Only update the servo angle if the heat index has changed
            if heat_index != previous_heat_index:
                angle = map_heat_index_to_angle(heat_index)
                servo_control.set_angle(angle)
                previous_heat_index = heat_index
            else:
                print("Heat index unchanged, no servo movement.")
            bulb_control.set_bulbs(heat_index)
        else:
            print("Failed to retrieve data from the sensor")
        
        time.sleep(2) 

except KeyboardInterrupt:
    print("Exiting program.")

finally:
    servo_control.cleanup()
    GPIO.cleanup()



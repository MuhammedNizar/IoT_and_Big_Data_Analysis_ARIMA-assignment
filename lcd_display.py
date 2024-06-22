import time
import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO

lcd_rs = 26  # RS pin
lcd_en = 19  # E pin
lcd_d4 = 13  # D4 pin
lcd_d5 = 6   # D5 pin
lcd_d6 = 5   # D6 pin
lcd_d7 = 11  # D7 pin
lcd_backlight = 4

lcd_columns = 16
lcd_rows = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows, lcd_backlight)

def display_message(message):
    lcd.message(message)


def clear_display():
    lcd.clear()

def set_cursor_position(col, row):
    lcd.set_cursor(col, row)





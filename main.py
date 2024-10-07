import time
import board
import adafruit_ahtx0

# Initialize I2C and the AHT10 sensor
i2c = board.I2C()
sensor = adafruit_ahtx0.AHTx0(i2c)

# Function to read temperature and humidity
def read_sensor_data():
    temperature = sensor.temperature
    humidity = sensor.relative_humidity

    print(f"Temperature: {temperature:.2f} °C")
    print(f"Humidity: {humidity:.2f} %")

if __name__ == "__main__":
    try:
        while True:
            read_sensor_data()
            time.sleep(2)  # Delay between readings
    except KeyboardInterrupt:
        print("Sensor reading stopped.")

import time
from mpu6050 import mpu6050

# Initialize the MPU6050 sensor
sensor = mpu6050(0x68)
sensor.set_accel_range(mpu6050.ACCEL_RANGE_2G)
sensor.set_gyro_range(mpu6050.GYRO_RANGE_250DEG)
sensor.set_filter_range(mpu6050.FILTER_BW_5)

# Function to capture sensor data with high sensitivity
def capture_vibrations():
    print("Capturing minute vibrations with filter bandwidth set to 5Hz...")

    while True:
        accel_data = sensor.get_accel_data()
        gyro_data = sensor.get_gyro_data() 

        # Print out the data for vibration analysis
        print(f"Accelerometer - X: {accel_data['x']:.6f}, Y: {accel_data['y']:.6f}, Z: {accel_data['z']:.6f}")
        print(f"Gyroscope - X: {gyro_data['x']:.6f}, Y: {gyro_data['y']:.6f}, Z: {gyro_data['z']:.6f}")
        print()

        time.sleep(0.05)  

if __name__ == "__main__":
    try:
        capture_vibrations()
    except KeyboardInterrupt:
        print("Stopped capturing data.")
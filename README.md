# Raspberry Pi Setup

### Step 1: Create and activate Python virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 2: Install required libraries
```bash
sudo apt install python3-smbus
pip install smbus
pip install mpu6050-raspberrypi
```

### Step 3: Update system and install I2C tools
```bash
sudo apt-get update
sudo apt-get install -y i2c-tools
sudo i2cdetect -y 1
```

### Step 4: Install AHT10 sensor library
```bash
pip install adafruit-circuitpython-ahtx0
```

### Step 5: Configure I2C for high-speed communication
Follow this [guide to change the Raspberry Pi I2C bus speed](https://www.raspberrypi-spy.co.uk/2018/02/change-raspberry-pi-i2c-bus-speed/).

### Step 6: Locate the `config.txt` file and modify it
```bash
find /boot -name "config.txt" | grep config.txt
sudo nano /boot/firmware/config.txt
```

Add the following line to enable I2C and set the baud rate to 400,000:
```bash
dtparam=i2c_arm=on,i2c_arm_baudrate=400000
```

### Step 7: Reboot the Raspberry Pi
```bash
sudo reboot
```


python3 -m venv venv
source venv/bin/activate
sudo apt install python3-smbus
pip install smbuspip install smbus
pip install mpu6050-raspberrypi
sudo apt-get update
sudo apt-get install -y i2c-tools
sudo i2cdetect -y 1
pip install adafruit-circuitpython-ahtx0
[Link I2C highspeed](https://www.raspberrypi-spy.co.uk/2018/02/change-raspberry-pi-i2c-bus-speed/)
find /boot -name "config.txt" | grep config.txt
sudo nano /boot/firmware/config.txt
dtparam=i2c_arm=on,i2c_arm_baudrate=400000
sudo reboot

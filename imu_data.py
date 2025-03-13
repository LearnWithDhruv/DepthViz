import serial

def get_imu_data(port="/dev/ttyUSB0", baudrate=115200):
    """Reads IMU sensor data."""
    ser = serial.Serial(port, baudrate)
    while True:
        line = ser.readline().decode().strip()
        print("IMU Data:", line)
        return line

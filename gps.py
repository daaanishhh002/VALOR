import serial
import pynmea2

def get_gps_coordinates(port='/dev/ttyTHS1', baudrate=9600, timeout=1):
    """
    Reads from the specified serial port and returns the first valid
    GPS coordinates (latitude, longitude) as a tuple.
    
    Returns:
        (latitude, longitude) if valid data is found.
        None if no valid data is found.
    """
    try:
        ser = serial.Serial(port, baudrate=baudrate, timeout=timeout)
        while True:
            line = ser.readline().decode('ascii', errors='replace')
            if line.startswith('$GPGGA') or line.startswith('$GPRMC'):
                try:
                    msg = pynmea2.parse(line)
                    if msg.latitude != 0.0 and msg.longitude != 0.0:
                        return (msg.latitude, msg.longitude)
                except pynmea2.ParseError:
                    continue
    except serial.SerialException as e:
        print(f"Serial connection error: {e}")
        return None

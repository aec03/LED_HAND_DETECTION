import serial

PORT = "/dev/cu.usbmodem141101"

ser = serial.Serial(PORT, 115200)

while True:
    number = input("Number: ")
    ser.write(number.encode())
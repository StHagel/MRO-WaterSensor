import serial
import time

arduino_path = '/dev/ttyACM0'
dat_path = "flow.dat"
# arduino_path specifies which port the Arduino is using.
# It might need to be adjusted depending on your setup.
# dat_path specifies where the data is going to be stored.

s = serial.Serial(arduino_path, 9600)
s.isOpen()
time.sleep(5)
# This part initialises the Arduino to work properly.
# The waiting is to make sure the Arduino is ready to go
# when starting the program. 

try:
	while True:
		for i in range(3600):
			# We are taking data over one hour (3600 s) each before storing it.
			# Alternatively it is possible to store the values only daily or weekly.
			lasthour_value = 0.0
			response = s.readline()
			l_per_h_value = float(response[0])
			
			print(l_per_h_value) 
			# Optional, prints the output of the arduino driver.
			
			l_per_s_value = l_per_h_value / 3600.0
			lasthour_value += l_per_s_value
		with open(dat_path, "a") as file1:
			file1.write('{0}\r\n'.format(lasthour_value))
			# After one hour the summed up flow, stored in lasthour_value, gets
			# stored in the file specified by dat_path.

except KeyboardInterrupt:
	s.close()


from enum import Enum
import string
import time 
from serial import SerialException, Serial

from utils.data_protocol import EZODataProtocol, Protocol

class UART(EZODataProtocol):
	def __init__(self, port):
		self._port = str(port)
		try:
			self._ser = Serial(self._port, 9600, timeout=0)
		except SerialException as e:
			print( "Error, ", e)

	def read_line(self):
		"""
		taken from the ftdi library and modified to 
		use the ezo line separator "\r"
		"""
		lsl = len(b'\r')
		line_buffer = []
		while True:
			next_char = self._ser.read(1)
			if next_char == b'':
				break
			line_buffer.append(next_char)
			if (len(line_buffer) >= lsl and
					line_buffer[-lsl:] == [b'\r']):
				break
		return b''.join(line_buffer)
		
	def read_lines(self):
		"""
		also taken from ftdi lib to work with modified readline function
		"""
		lines = []
		try:
			while True:
				line = self.read_line()
				if not line:
					break
					self._ser.flush_input()
				lines.append(line)
			return lines
		
		except SerialException as e:
			print( "Error, ", e)
			return None	

	def send_cmd(self, cmd: str):
		"""
		Send command to the Atlas Sensor.
		Before sending, add Carriage Return at the end of the command.
		:param cmd:
		:return:
		"""
		buf = cmd + "\r"     	# add carriage return
		try:
			self._ser.write(buf.encode('utf-8'))
			return True
		except SerialException as e:
			print ("Error, ", e)
			return None
	
	def flush(self):
		self._ser.flush()
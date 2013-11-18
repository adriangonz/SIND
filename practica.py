#!/usr/bin/python

from datetime import datetime
from pymodbus.client.sync import ModbusSerialClient
import sched, time, csv, os

# Helper functions
def to_hex(integer):
        return "0x%0.4X" % integer

def split_hex(hex_string):
        return str(int(hex_string[2:4], 16)), str(int(hex_string[4:], 16))

def get_hex(integer):
	return "0x%0.2X" % integer

def get_string_datetime(_datetime):
	return _datetime.strftime('%H:%M:%S %d/%m/%Y')

def get_datetime_string(_string):
	return datetime.strptime(_string, '%H:%M:%S %d/%m/%Y')

def get_datetime_hex(_datetime):
	# Sacamos los valores
	sec = get_hex(_datetime.second)
	min = get_hex(_datetime.minute)
	hour = get_hex(_datetime.hour)
	day = get_hex(_datetime.day)
	month = get_hex(_datetime.month)
	year = get_hex(_datetime.year % 2000)
	# Los concatenamos en hex
	secmin = sec + min[2:]
	hourday = hour + day[2:]
	monthyear = month + year[2:]
	# Devolvemos lista
	return [int(secmin, 16), int(hourday, 16), int(monthyear, 16)]

def get_device_datetime(client):
	req = client.read_holding_registers(253, 3, unit=25)
	secmin = to_hex(req.getRegister(0))
	hourday = to_hex(req.getRegister(1))
	monthyear = to_hex(req.getRegister(2))
	month, year = split_hex(monthyear)
	hour, day = split_hex(hourday)
	sec, min = split_hex(secmin)
	return datetime(int(year) + 2000, int(month), int(day), int(hour), int(min), int(sec))

def get_row(client):
	# Get V
	req = client.read_holding_registers(2, 1, unit=25)
	V = req.getRegister(0) / 100.0
	# Get I
	req = client.read_holding_registers(7, 2, unit=25)
	I = int(to_hex(req.getRegister(0)) + (to_hex(req.getRegister(1))[2:]), 16) / 1000.0
	# Get PAct
	req = client.read_holding_registers(21, 2, unit=25)
	PAct = int(to_hex(req.getRegister(1)) + (to_hex(req.getRegister(0))[2:]), 16) / 100.0
	# Get PReact
	req = client.read_holding_registers(29, 2, unit=25)
	PReact = int(to_hex(req.getRegister(1)) + (to_hex(req.getRegister(0))[2:]), 16) / 100.0
	# Get FactorPotencia
	req = client.read_holding_registers(10, 1, unit=25)
	FactorPotencia = req.getRegister(0) / 1000.0
	# Get Frec
	req = client.read_holding_registers(9, 1, unit=25)
	Frec = req.getRegister(0) / 100.0
	# Get PAparente
	req = client.read_holding_registers(11, 2, unit=25)
	PAparente = int(to_hex(req.getRegister(1)) + (to_hex(req.getRegister(0))[2:]), 16) / 100.0
	# Return row
	return [
		get_device_datetime(client).isoformat(),
		V,
		I,
		PAct,
		PReact,
		FactorPotencia,
		Frec,
		PAparente
	]

def cycle_csv(client, s):
	filename = 'practica_' + datetime.now().strftime('%Y%m%d_%H:00') + '.csv'
	if os.path.exists(filename):
		header_exists = True
	else:
		header_exists = False
	with open(filename, 'a+') as csvfile:
		writer = csv.writer(csvfile)
		if not header_exists:
			writer.writerow([
					'fecha',
					'V',
					'I',
					'PAct',
					'PReact',
					'FactorPotencia',
					'Frec',
					'PAparente'
			])
		row = get_row(client)
		writer.writerow(row)
		print row
	s.enter(1, 1, cycle_csv, (client,s,))
		

def get_client():
	# Creamos el cliente y lo devolvemos
	client = ModbusSerialClient(method='rtu', port='/dev/ttyUSB0', 
					baudrate=9600, bytesize=8, parity='N', 
					stopbits=2, timeout=0.05, writeTimeout=1.5)
	return client

def print_menu(menu, cliente):
	print '-----------------------------------'
	print 'Hora actual del sistema: ' + get_string_datetime(datetime.now())
	print 'Hora actual del dispositivo: ' + get_string_datetime(get_device_datetime(cliente))
	for num, option in enumerate(menu):
		print str(num + 1) + ') ' + option['text']
	return input('Elige una opcion: ')

# Menu functions
def set_fecha(client):
	string_fecha = raw_input('Introduzca la fecha. El formato debe ser "HH:MM:SS DD/MM/YYYY":\n')
	_datetime = get_datetime_string(string_fecha)
	client.write_registers(253, get_datetime_hex(_datetime), unit=25)
	print 'La fecha actual del dispositivo es ' + get_string_datetime(get_device_datetime(client))

def set_fecha_auto(client):
	client.write_registers(253, get_datetime_hex(datetime.now()), unit=25) 
	print 'La fecha actual del dispositivo es ' + get_string_datetime(get_device_datetime(client))

def generate_csv(client):
	s = sched.scheduler(time.time, time.sleep)
	s.enter(1, 1, cycle_csv, (client,s,))
	s.run()

def exit_practica(client):
	print 'Bye!!!'
	exit()

# Main function
if __name__ == '__main__':
	# Obtenemos un cliente
	_client = get_client()
	menu = [
		{'text': 'Settear fecha', 'function': set_fecha},
		{'text': 'Sincronizar fecha', 'function': set_fecha_auto},
		{'text': 'Empezar a generar CSV', 'function': generate_csv},
		{'text': 'Salir', 'function': exit_practica}
	]
	value = True
	while value:
		opt = print_menu(menu, _client)
		choice = menu[opt - 1]
		if 'function' in choice:
			choice['function'](client=_client)

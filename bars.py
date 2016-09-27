import json
import math


def load_from_json(filepath):
    with open(filepath, 'r') as data:
        return json.load(data)


def get_biggest_bar(data):
	help_dictionary=dict()	
	for bar in data:
		help_dictionary.update([(bar['Cells']['SeatsCount'],bar['Cells']['Name'])])
	print('Bar with biggest area:')	
	print(max(help_dictionary.keys()))
	print(help_dictionary.get(max(help_dictionary.keys())))


def get_smallest_bar(data):
	help_dictionary=dict()	
	for bar in data:
		help_dictionary.update([(bar['Cells']['SeatsCount'],bar['Cells']['Name'])])
	print('Bar with smallest area:')	
	print(min(help_dictionary.keys()))
	print(help_dictionary.get(min(help_dictionary.keys())))


def get_closest_bar(data):
	try:
    		latitude = float(input('Enter latitude:  '))
	except ValueError:
    		latitude = None

	if latitude is None:
    		print('Sorry, there are no data!')

	try:
    		longitude = float(input('Enter longitude: '))
	except ValueError:
    		latitude = None

	if longitude is None:
    		print('Sorry, there are no data!')
	
	help_dictionary=dict()	
	for bar in data:
		help_dictionary.update([(math.sqrt((bar['Cells']['geoData']['coordinates'][0]-longitude)*(bar['Cells']['geoData']['coordinates'][0]-longitude)+(bar['Cells']['geoData']['coordinates'][1]-latitude)*(bar['Cells']['geoData']['coordinates'][1]-latitude)),bar['Cells']['Name'])])
	print(min(help_dictionary.keys()))
	print(help_dictionary.get(min(help_dictionary.keys())))




if __name__ == '__main__':
	data = load_from_json('bar.json')
	#print(data[1]['PublicPhone'])
	get_biggest_bar(data)
	get_smallest_bar(data)
	get_closest_bar(data)


    

import json
import sys

def import_data(filename):
	data = []
	business_categories = set([])
	with open(filename) as f:
		for line in f:
			line_as_dict = json.loads(line)
			if line_as_dict['type'] == 'business' and 'Stanford University' in line_as_dict['schools']:
				data.append(line_as_dict)
			if line_as_dict['type'] == 'business':
				for item in line_as_dict['categories']:
					business_categories.add(item)
	return data

def write_list_to_file(json_as_list, stanford_file):
	for item in json_as_list:
		stanford_file.write('%s\n' % item)

def calculate_area_dimensions(json_as_list):
	min_latitute = sys.maxint
	min_longitude = sys.maxint
	max_latitute = -sys.maxint - 1
	max_longitude = -sys.maxint - 1
	for item in json_as_list:
		if item['latitude'] < min_latitute:
			min_latitute = item['latitude']
		if item['latitude'] > max_latitute:
			max_latitute = item['latitude']
		if item['longitude'] < min_longitude:
			min_longitude = item['longitude']
		if item['longitude']  > max_longitude:
			max_longitude = item['longitude']
	return min_latitute, max_latitute, min_longitude, max_longitude

def divide_area(min_latitute, max_latitute, min_longitude, max_longitude):
	areas = []
	lat_offset = (max_latitute - min_latitute) / 5
	long_offset = (max_longitude - min_longitude) / 5

	for lat in range(5):
		for lon in range(5):
			areas.append((min_latitute + lat * lat_offset, min_latitute + (lat+1) * lat_offset, min_longitude + lon * long_offset, min_longitude + (lon + 1) * long_offset))

	return areas

def parse():
	(json_as_list, all_business_categories) = import_data('yelp_academic_dataset.json')
	stanford_file = open('stanford_businesses.txt', 'w')
	(min_latitute, max_latitute, min_longitude, max_longitude) = calculate_area_dimensions(json_as_list)
	neighborhoods = divide_area(min_latitute, max_latitute, min_longitude, max_longitude)
	print neighborhoods

parse()

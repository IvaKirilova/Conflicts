# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 11:10:24 2018

@author: Iva
"""
import json
import csv

with open ('conflict_data_full_lined.json') as file:
    data = json.load(file)

Bosnia = []
for fatality in data:
    if fatality["country"] == "Bosnia-Herzegovina":
        Bosnia.append(fatality)
        
Croatia = []
for fatality in data:
    if fatality["country"] == "Croatia":
        Croatia.append(fatality)
        
with open ('Bosnia.csv', 'w', newline = '') as file:
    csvwriter = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    csvwriter.writerow(['country', 'year', 'active_year', 'type_of_violence', 'side_a', 'side_b', 'latitude', 'longitude', 'deaths_a', 'deaths_b', 'deaths_civilians', 'best'])
    for item in Bosnia:
        csvwriter = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        csvwriter.writerow([item['country'], item['year'], item['active_year'], item['type_of_violence'], item['side_a'], item['side_b'], item['latitude'], item['longitude'], item['deaths_a'], item['deaths_b'], item['deaths_civilians'], item['best']])
 
with open ('Croatia.csv', 'w', newline = '') as file:
    csvwriter = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    csvwriter.writerow(['country', 'year', 'active_year', 'type_of_violence', 'side_a', 'side_b', 'latitude', 'longitude', 'deaths_a', 'deaths_b', 'deaths_civilians', 'best'])
    for item in Croatia:
        csvwriter = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        csvwriter.writerow([item['country'], item['year'], item['active_year'], item['type_of_violence'], item['side_a'], item['side_b'], item['latitude'], item['longitude'], item['deaths_a'], item['deaths_b'], item['deaths_civilians'], item['best']])
    
total_deaths_bosnia = 0
for item in Bosnia:
    total_deaths_bosnia += item['best']
    
deaths_civilians_bosnia = 0
for item in Bosnia:
    deaths_civilians_bosnia += item['deaths_civilians']

total_deaths_croatia = 0
for item in Croatia:
    total_deaths_croatia += item['best']
    
deaths_civilians_croatia = 0
for item in Croatia:
    deaths_civilians_croatia += item['deaths_civilians']
    

#!/usr/bin/env python3
import os 
import pprint
import csv
from datetime import datetime
import requests
from urls_utils import gen_from_urls


def main():
    print(os.getcwd())
    # read_dictionary()
    generators()





def generators():
    urls =('http://google.com', 'http://oreilly.com', 'http://x.com')
    
    for resp_len, status, url in gen_from_urls(urls):
        print(f"{resp_len} -> {status} -> {url}")

def convert_to_ampm(time24: str) -> str:
    return datetime.strptime(time24,'%H:%M').strftime('%I:%M%p')


def read_csv():
    print(os.getcwd())

    with open('buzzers.csv') as raw_data:
        for line in csv.DictReader(raw_data):
            pprint.pprint(line)
    
def read_dictionary():
    with open('buzzers.csv') as raw_data: 
        ignore = raw_data.readline()
        flights = {}
        for line in raw_data:
            k,v = line.strip().split(',')
            flights[k] = v
        pprint.pprint(flights)
        
def comprehension():
    
    with open('buzzers.csv') as data:
        ignore_header = data.readline()
        flights = {}
        for line in data:
            k, v = line.strip().split(',')
            flights[k] = v 

    flight_times = [convert_to_ampm(times) for times in flights.keys()]    
    destinations = [destination.title() for destination in flights.values() ]
        
    pprint.pprint(flight_times)
    pprint.pprint(destinations)
    
        
        
        
        
        

if __name__ == "__main__":
    main()
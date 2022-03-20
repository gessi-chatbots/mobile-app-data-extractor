import json
import os

from google_play_scraper import app

from serpapi import GoogleSearch

import utils

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-a', dest='package_name', type=str, help="Package name of the app to be searched for")
parser.add_argument('-f', dest='file', type=str, help="Name of the file to save the results")
parser.add_argument('-k', dest='api_key', type=str, help="API key for SERP API")
parser.add_argument('-c', dest='keys', type=str, help="File where the keys are located")

args = parser.parse_args()
api_key = args.api_key
package = args.package_name
destination_file = args.file

params = {
    "engine": "google_play_product",
    "store": "apps",
    "product_id": package,
    "api_key": api_key
}


search = GoogleSearch(params)
results = search.get_dict()
# flatten dict
flat_dict = utils.flatten_dict(results)

# get gps results
gps_results = app(package)

key_file = open(os.getcwd() + "\\" + args.keys, 'r')
keys = []
for line in key_file:
    key = line.split()
    keys.append(tuple(key))
merged_dict = utils.combine_dicts(gps_results, flat_dict, keys)
key_file.close()
with open(os.getcwd() + "/" + destination_file, 'w') as file:
    json_object = json.dumps(merged_dict)
    print(json_object, file=file)

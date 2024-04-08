"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path='data/neos.csv'):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    # TODO: Load NEO data from the given CSV file.
    with open(neo_csv_path, mode='r', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        next(reader)
        '''
            name: row[4].strip() - Removes white space from name
            designation: row[3]
            diameter: row[15]
            hazardous: row[7]
        '''
        neos = [NearEarthObject(designation=row[3].strip(), name=row[4].strip(), diameter = row[15], hazardous = row[7]) for row in reader]
    return neos


def load_approaches(cad_json_path='data/cad.json'):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    # TODO: Load close approach data from the given JSON file.
    with open(cad_json_path, mode = 'r', encoding = 'utf-8') as infile:
        json_data = json.load(infile)
        clas = [CloseApproach(designation = entry[json_data['fields'].index("des")], time = entry[json_data['fields'].index("cd")], distance = entry[json_data['fields'].index("dist")], velocity = entry[json_data['fields'].index("v_rel")]) for entry in json_data['data']]
    return clas

# data = load_neos('data/neos.csv')
# cla_data = load_approaches('data/cad.json')
# print(cla_data[:3])
# print(cla_data[0])
# print(cla_data[1])
# print(cla_data[2])
# print(cla_data[3])
# print('' in cla_data)
# print(len(cla_data))
# print(data[:3])
# print(data[0])
# print(data[1])
# print(data[2])
# print(data[3])
# print(data[4])

import json
import sys
import pymongo
import argparse

'''
Created to parse, and load the JSON files available in the Facebook profile download into a MongoDB instance.
Requires a default mongodb instance to be installed and running.
Test the existance of the mongo instance by typing 'mongod' into the command line.
'''
'''todo add argparse functionality'''
class DataLoader(object):
    def __init__(self):
        try:
            # Attempt to read the file included in the command line arguments.
            self._fb_folder_root_path = sys.argv[1]
        except IndexError as e:
            print("{0}.".format(e) + " Error indexing the command line path variable. Likely the path was not included.")

        try:
            # Attempt to connect to a running MongoDB instance running on IP: localhost and port: 27017.
            self._mongo_client = pymongo.MongoClient()
        except pymongo.errors.ConnectionFailure as e:
            print(e)

    def _load_file(self, file_path):
        '''Reads the file at the provided file path if possible. Returns an IOError if not successful.'''
        try:
            # Attempt to read and return the file at the provided file_path.
            return json.load(open(file_path))
        except IOError as e:
            print("IOError({0}): {1}.".format(e.errno, e.strerror))



import datetime
import os
import csv
import time
import glob

# Path to the file
path = r"/Users/gamerman2/Documents/"

# Convert time to ISO 8601 format
def iso_time(time2):
    iso = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(time2))
    return str(iso)

def getMetadata(path):
    # returns a tuple of the path, size, modified time, created time, accessed time, is file, is directory, is link, is mount, exists
    return path, os.path.getsize(path), iso_time(os.path.getmtime(path)), iso_time(os.path.getctime(path)), iso_time(os.path.getatime(path)), int(os.path.isfile(path)), int(os.path.isdir(path)), int(os.path.islink(path)), int(os.path.ismount(path))

# Recursively list files in home directory
def list_files(path):
    files_list = []

    for file in glob.glob(path + "**", recursive=True):
        files_list.append(file)

    return files_list

files = list_files(path)
metadata = []
for file in files:
    metadata.append(getMetadata(file))

#write code to push getMetadata to csv file.
with(open('system32.csv', 'w')) as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['path', 'size', 'modified', 'created', 'accessed', 'is file', 'is directory', 'is link', 'is mount'])
    for meta in metadata:
        csvwriter.writerow(meta)
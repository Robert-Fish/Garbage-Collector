import glob
import os
import shutil
from variables import path, basePath

print('Welcome to WatchDog Cleanup 🗑')
print('Running cleanup... 🛠')
os.chdir(path)


def handleFile(file, path):
    shutil.move(file, path)


for file in glob.glob("*"):
    if file.endswith('.app'):
        print('Moving file ', file)
        handleFile(file, basePath + '/Compactor')

    elif file.endswith('.zip'):
        print('Moving file ', file)
        handleFile(file, basePath + '/Compactor')

    elif file.endswith('.pdf'):
        print('Moving file ', file)
        handleFile(file, basePath + '/Documents')

    elif file.endswith('.jpg'):
        print('Moving file ', file)
        handleFile(file, basePath + '/Pictures'

print('Clean up complete 😃')

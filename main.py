import glob
import os
import shutil
from variables import path, basePath

print('Welcome to WatchDog Cleanup 🗑')
print('Running cleanup... 🛠')
os.chdir(path)

for file in glob.glob("*"):
    if file.endswith('.app'):
        print('Moving file ', file)
        shutil.move(file, basePath + '/Compactor')

    elif file.endswith('.zip'):
        print('Moving file ', file)
        shutil.move(file, basePath + '/Compactor')

    elif file.endswith('.pdf'):
        print('Moving file ', file)
        shutil.move(file, basePath + '/Documents')

    elif file.endswith('.jpg'):
        print('Moving file ', file)
        shutil.move(file, basePath + '/Pictures')

print('Clean up complete 😃')

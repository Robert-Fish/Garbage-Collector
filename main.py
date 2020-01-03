import glob, os
import shutil
from variables import path, basePath

print('Welcome to WatchDog Cleanup 🗑')
print('Running cleanup... 🛠')
os.chdir(path)

for file in glob.glob("*.zip"):
    print('Moving file ', file)
    shutil.move(file, basePath + '/Compactor')

for file in glob.glob("*.app"):
    print('Moving file ', file)
    shutil.move(file, basePath + '/Compactor')

for file in glob.glob("*.pdf"):
    print("Moving file ", file)
    shutil.move(file, basePath + '/Documents')

for file in glob.glob("*.jpg"):
    print("Moving file ", file)
    shutil.move(file, basePath + '/Pictures')

print('Clean up complete 😃')

import os
source_dir = "C:\\Users\\User\\Downloads"
with os.scandir(source_dir) as entries:
    for entry in entries:
        print(entry.name)
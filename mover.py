from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time 


def write_log(message):
    file_path = "/Users/sockless/mover.log"
    file_ref = open(file_path, "a+")
    file_ref.write(message + "\n")
    file_ref.close()


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        subfolder = "undef"

        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            # new_destination = folder_destination + "/" + filename

            if "sv_" in filename:
                subfolder = "sv"
            elif "en_" in filename: 
                subfolder = "en"

            elif "boi_" in filename: 
                subfolder = "boi"
            
            new_destination = folder_destination + "/" + subfolder + "/" + filename
            os.rename(src, new_destination)
            
            print(src + " >> " + new_destination)
            write_log(src + " >> " + new_destination)
            
            

folder_to_track = "/Users/sockless/Desktop/Sort"
folder_destination = "/Users/sockless/Documents/Sorted"

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
except KeyboardInterrupt:
    observer.stop()

observer.join()
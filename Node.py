while True:
    file = open("Launch.txt", "r")
    Command = file.read()
    if Command == "Launch":
        for i in range (5):
            file = open("JunkFile1.txt", "a")
            file.write("10000000000000000000000000000000000000")
            file.close()
    elif Command == "Kill":
            print("Kill Success")
    file.close()

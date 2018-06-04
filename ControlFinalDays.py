def Prime():
    print("Primed")
    file = open("Launch.txt", "w")
    file.close()
def Launch():
    print("Launching")
    file = open("Launch.txt", "w")
    file.write("Launch")
    file.close()
def Kill():
    print("Killing")
    file = open("Launch.txt", "w")
    file.write("Kill")
    file.close()

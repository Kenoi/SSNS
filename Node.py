while True:
    file = open("Launch.txt", "r")
    Command = file.read()
    if Command == "Launch":
            BProgress = 0
            num = 999
            while True:
                for i in range(2,num):
                    if (num % i) == 0:
                        num += 2
                        BProgress += 1
                else:
                        print(num)
                        num += 2
                        BProgress += 1
                    
                if BProgress >= 1000:
                    print("Block complete")
                    BProgress = 0
                    num += 2000
    elif Command == "Kill":
            print("Kill Success")
    file.close()

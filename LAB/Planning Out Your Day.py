def part1():
    print("PART1: Arrived to lab and turned on laptop")#
    part2()
    print("Exiting PART1: Turned off laptop and left lab")
    
def part2():
    print("PART2: Logged into Edstem")
    lab = input("Which lab assignment are you attempting? (Lab1/Lab2/...): ")
    part3(lab)
    print("Exiting PART2: Logged out of Edstem")
    
def part3(lab):
    print("PART3: Started " + lab)
    msg = input("Lab is over! What is the status of your lab? Complete/Incomplete?: ")
    if msg == 'Complete':
        print("Exiting PART3: Completed " + lab)
    else:
        print("Exiting PART3: Didn't complete " + lab)
    
print("START: Time to conquer the day!")
part1()
print("END: I'm done!")
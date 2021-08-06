from time import sleep
import winsound


def beepbeep():
            Fr = 750
            d = 120
            winsound.Beep(Fr, d)
            sleep(0.1)
            winsound.Beep(Fr, d)
            sleep(0.5)
print("--------------------------------------------------------------------------------")
print("\t\t\t\tWelcome to Timer")
print()
print("--------------------------------------------------------------------------------")
print("by - ShubhamProgmer(https://github.com/ShubhamProgmer/ShubhamProgmer)")
print()
print()
print("Please press \'ctrl+c\' to terminate timer at any instant!")
print()
print()
while True:
    try:
        i = int(input("Please Enter Timer in second: "))
        break
    except Exception as e:
        print("Please enter a valid INTEGER")
        continue
while True:
    if i == 0:
        print("Press \'ctrl+c\' to stop the alarm!\nThan you for using Timmer!")
        while True:
            Fr = 750
            d = 120
            winsound.Beep(Fr, d)
            sleep(0.1)
            winsound.Beep(Fr, d)
            sleep(0.5)

    else:
        print(f"{i} secs")
        sleep(1)
        i -= 1


# imports (keyboard writing, waiting, pressing with immediate releasing and system)
from keyboard import write, wait, press_and_release
from os import system


# inputting integers (error checking)
def int_input(prompt: str):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid value.")


# main loop
while True:
    # asking for repeated message
    message = input("Enter the message: ")
    # asking for the amount of times to repeat the message
    repeat = int_input("Enter the amount of times the message should be repeated: ")
    # asking for the delay between each message
    delay = int_input("Enter the delay between each message (0 can be used): ")

    # waiting for 't' to be entered (removing the 't' once entered)
    wait("t")
    press_and_release("backspace")

    # sending loop
    for _ in range(repeat):
        write(text = message, delay = delay)

    # when finished
    input("All done! (press enter to continue)")
    # cleanup
    system("cls")

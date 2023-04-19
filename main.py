import time
import pyautogui

# Wait for 5 seconds before starting the script
time.sleep(5)

# Open the file containing the birthday wishes
with open('birthday_wishes.txt', 'r') as file:
    # Read the lines of the file
    wishes = file.readlines()

thank_you_message = "Thank you so much for your birthday wishes!"
pyautogui.typewrite(thank_you_message)

# Extract the names of the friends who wished by looping through the wishes
for wish in wishes:
    friend_name = wish[wish.index("]") + 2 : wish.index(": ")]
    pyautogui.typewrite(f"{friend_name}\n")

import pyautogui, keyboard, random

count = 10
wordList = ["monkey", "donkey", "dog", "cat", "fool", "blunder"]

while True:
    if keyboard.is_pressed("Ctrl+Shift+z"):
        break
    else:
        continue

for i in range(count):
    pyautogui.write(f"You are a {random.choice(wordList)}!")
    pyautogui.press("Enter")
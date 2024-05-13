import pyautogui
from pdfminer.high_level import extract_pages, extract_text
import re
import sys, os

text_body = extract_text("2023-2024-SHOPPING-LIST-FOR-UPLOAD.pdf")
#print(text_body)

# JAMB regnumber regex
jamb_number_pattern = re.compile(r'\b\d{12}[A-Z]{2}\b')

jamb_numbers = jamb_number_pattern.findall(text_body)
# Array of values to iterate over
values = jamb_numbers
files = os.listdir("./saved/2")
trimmed_list = [s[:-4] for s in files]

filtered_list = [item for item in values if item not in trimmed_list]
# print(len(filtered_list))
# navigate to your browser with the UNN portal already opened to avoid writing excessive code to achieve that.


for value in filtered_list:
    pyautogui.sleep(5)
# These coordinates are based on my PC resolution. Please adjust to your own system
# use this to get coordinates print(pyautogui.position())

    pyautogui.click(1216, 1026)
    pyautogui.sleep(1)
    pyautogui.write(value)
    # pyautogui.sleep(1)
    pyautogui.click(1665, 1170)
    # You can reduce every other sleep but this line require more time because of internet speed variation
    pyautogui.sleep(15)
    
    pyautogui.click(828, 1366)
    pyautogui.sleep(5)
    pyautogui.click(2003, 1318)
    # remember to set the print option to "print to pdf" before running this script
    # Also remember to set the destination of the download if you want
    pyautogui.sleep(1)
    pyautogui.write(value)
    pyautogui.sleep(3)
    pyautogui.click(905, 909)
    pyautogui.sleep(2)

    pyautogui.press('enter')
    pyautogui.press('esc')
    pyautogui.press('esc')

    pyautogui.sleep(2)
    pyautogui.click(1000, 186)
    pyautogui.write("https://unnportal.unn.edu.ng/putme_login")
    pyautogui.press('enter')



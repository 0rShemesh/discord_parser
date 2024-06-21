#!/bin/env python3
# Author: 0rShemesh
# This script used to get all the messages in slected discord chat.
# Tested on Python 3.8.2
# Little guide: 
#   1. just open the chat with Ctrl+shift+I.
#   2. scroll up to load all the messages. 
#   3. press right click on the HTML tag and  "edit as HTML"
#   4. save all the HTML page to file
#   5. run the script ( you should change the "XXXX.html" to your favorite discord chat)
# have fun!
from bs4 import BeautifulSoup
from pathlib import Path
import re
from datetime import datetime
CURRENT_TIME = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

html_page = Path("XXXX.html").read_bytes()
soup = BeautifulSoup(html_page)
all_msg = soup.find_all("ol",{"class":"scrollerInner_e2e187"})[0].find_all(["div","li"])

result = []
current_subarray = []

def get_message(li:list):
    text = ""
    for element in li:
        for span in element.find_all("span"):
            if len(span.attrs) == 0:
                text = text + span.text

    return text

for element in all_msg:
    if element.name == 'div':
        if current_subarray:
            result.append(current_subarray)
        current_subarray = []
    elif element.name == 'li':
        current_subarray.append(element)
    
if current_subarray:
    result.append(current_subarray)


print(f"Amount of scraped messages:{len(result)}")

save_to_file = Path(f"{CURRENT_TIME}_message_dump.txt")
save_to_file.write_bytes(b"")

for elements in result:
    print("message:")
    
    message = get_message(elements)
    print(message)
    mesage_to_save = b"MESSAGE:\r\n"
    mesage_to_save = mesage_to_save + message.encode()
    mesage_to_save = mesage_to_save + b"\r\n"
    save_to_file.write_bytes(save_to_file.read_bytes() + mesage_to_save)
    

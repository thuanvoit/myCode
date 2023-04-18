import os

try:
  import rumps
  print("rumps imported sucessfully")
except ImportError:
  print("Install required module: rumps")
  os.system('python3 -m pip install rumps')

try:
  import imessage_reader
  print("imessage_reader imported sucessfully")
except ImportError:
  print("Install required module: imessage_reader")
  os.system('python3 -m pip install imessage_reader')
  
try:
  import pyperclip
  print("pyperclip imported sucessfully")
except ImportError:
  print("Install required module: pyperclip")
  os.system('python3 -m pip install pyperclip')


import rumps
from imessage_reader import fetch_data
from datetime import datetime
import re
import pyperclip as pp

class myCode(rumps.App):
    
    version = 'v1.0'
    
    def __init__(self):
        super(myCode, self).__init__("myCode")
        self.menu = ["myCode" + self.version]
    
    @rumps.clicked("Copy myCode")
    def copy_code(self, _):
        pp.copy(self.get_code())
            
    def fetch_msg(self):
      print("fetching all messages...")
      fd = fetch_data.FetchData()
      return fd.get_messages()

    
    
    def get_code(self):
        my_data = self.fetch_msg()
        my_data.sort(key=lambda x: (datetime.strptime(x[2], '%Y-%m-%d %H:%M:%S')), reverse=True)
        for data in my_data:
            if data is not None and data[1] is not None:
                msg_content = data[1].lower()
                if ("code" in msg_content or "verification" in msg_content):
                    if bool(re.findall(r"\d{4,}", msg_content)):
                        out = re.findall(r"\d{4,}", msg_content)
                        print(f"{msg_content}: {out[0]}")
                        return out[0]
        return -1

if __name__ == "__main__":
    myCode().run()

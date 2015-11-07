#Copyright 2015 Scott Scheiner
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.

__module_name__ = "CleanPaste"
__module_version__ = "1.0"
__module_description__ = "Pastes your clipboard without colour"

import hexchat
import ctypes

# Windows only
def getClipboard():
    ctypes.windll.user32.OpenClipboard(0)
    pcontents = ctypes.windll.user32.GetClipboardData(1) # 1 is CF_TEXT
    data = ctypes.c_char_p(pcontents).value
    ctypes.windll.user32.CloseClipboard()

    if type(data) == bytes:
        data = data.decode()
    return data

def strip(text):
	return hexchat.strip(text,-1,3).replace("\010", "") # \010 = Hidden text

def onKeyPress(word, word_eol, userdata):
	if word[0] == '86' and word[1] == '5':
		hexchat.command("settext " + hexchat.get_info("inputbox") + strip(getClipboard()))
		hexchat.command("setcursor " + str(len(hexchat.get_info("inputbox"))))

hexchat.hook_print("Key Press", onKeyPress)
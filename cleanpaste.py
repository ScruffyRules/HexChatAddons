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
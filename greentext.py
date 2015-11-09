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

import hexchat

__module_name__ = 'Green Text'
__module_version__ = '1.0'
__module_description__ = 'When you type > it turns it into green text'

def keypress_cb(word, word_eol, userdata):
	if hexchat.get_info("inputbox") == "" and word[2] == ">":
		hexchat.command("settext \00303")
		hexchat.command("setcursor 4")
	return hexchat.EAT_NONE

hexchat.hook_print("Key Press", keypress_cb)

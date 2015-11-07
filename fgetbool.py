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

__module_name__ = 'FGETBOOL'
__module_version__ = '1.0'
__module_description__ = 'FGETBOOL'

def fgetbool_cb(word, word_eol, userdata):
	if word_eol[1][-1:] == "0":
		pass
	elif word_eol[1][-1:] == "1":
		hexchat.command(word_eol[1][:-1])
	else:
		print("What?")
	return hexchat.EAT_ALL

hexchat.hook_command("FGETBOOL", fgetbool_cb)
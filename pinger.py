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

__module_name__ = 'Pinger'
__module_version__ = '1.0'
__module_description__ = 'Later'

channels = ["#spigot-irc-staff","#oresomecraft-admin","#ausfrag","#scruffyrules"]

def pinger_cb(word, word_eol, userdata):
	for i in channels:
		if hexchat.get_info("channel").lower() == i:
			hexchat.command("gui flash")
			hexchat.command("gui color 3")
			beep()
	return hexchat.EAT_NONE

def beep():
	hexchat.command("QUERY -nofocus !PING!")
	context = hexchat.find_context(channel="!PING!")
	context.prnt("\007")
	context.command("close")

hexchat.hook_print("Channel Message", pinger_cb)
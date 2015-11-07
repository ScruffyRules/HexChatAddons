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

__module_name__ = "AikarStream"
__module_version__ = "1.1"
__module_description__ = "Improves chat view for AikarStream in #aikar on Spigot"

def chanmessage_cb(word, word_eol, userdata):
    nick = hexchat.strip(word[0])
    if nick == "AikarStream":
        message = word[1]
        nick = message.split(" ")[0]
        message = message.replace(nick + " ", "")
        user = message.split(" ")[0]
        message = message.replace(user, user + ":")
        hexchat.prnt(nick + "\t" + message)
        return hexchat.EAT_ALL
    return hexchat.EAT_NONE

hexchat.hook_print("Channel Message", chanmessage_cb),
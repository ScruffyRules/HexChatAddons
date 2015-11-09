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
import urllib.error as urllib_error
import urllib.request as urllib_request
import os
import json

__module_name__ = 'Scruff\'s Scripts'
__module_version__ = '1.0'
__module_description__ = 'Downloads and loads Scruff\'s Python scripts'
__module_shortname__ = "\002\00300,01SS\017"

cache_list = []
dlss_list = []

addon_dir = os.path.join(hexchat.get_info('configdir'), 'addons')
ss_dir = os.path.join(addon_dir, 'ss')

raw = "https://raw.github.com/ScruffyRules/HexChatAddons/master/"
contents = "https://api.github.com/repos/ScruffyRules/HexChatAddons/contents/"
apicallsleft = 60

onstartload = bool(False if hexchat.get_pluginpref("ss_onstartload") == None else hexchat.get_pluginpref("ss_onstartload"))

# Make ss folder in HexChat's addon folder
if not os.path.isdir(ss_dir):
	os.makedirs(ss_dir)

# Load all scripts Or add them to dlss_list
for i in os.listdir(ss_dir):
	dlss_list.append(i)
	if onstartload:
		hexchat.command("py load " + os.path.join(ss_dir, i))

def pprefix(string):
	print(__module_shortname__ + "\t" + string)

def ss_cb(word, word_eol, userdata):
	if len(word) < 2:
		word.append("help")
	if word[1].lower() == "list":
		callCacheList()
		
		colourlist = []
		for i in cache_list:
			if (i + ".py") in dlss_list:
				colourlist.append("\00303" + i + "\017")
			else:
				colourlist.append(i)
		
		pprefix("List of Scripts: " + ", ".join(colourlist))
	elif word[1].lower() == "get":
		if not len(word) == 3:
			pprefix("Usage: /SS GET <script[.py]>")
			return hexchat.EAT_HEXCHAT
		
		script = word[2]
		if script[-3:] == ".py":
			script = script[:-3]
		
		if (script + ".py") in dlss_list:
			hexchat.hook_timer(0, pyunload_timer, script + ".py")
		
		callCacheList()
		if script in cache_list:
			dlss_list.append(script + ".py")
			hexchat.hook_timer(0, download, [script + ".py", True])
		else:
			pprefix("\"{0}\" is not a known script!".format(word[2]))
	elif word[1].lower() == "startup":
		if not len(word) == 3:
			pprefix("Usage: /SS STARTUP <True/False>")
			return hexchat.EAT_HEXCHAT
		
		onstartload = bool(False if word[2].lower() == "false" else True)
		hexchat.set_pluginpref("ss_onstartload", onstartload)
		pprefix("On startup load plugins is set to\002\0030" + ("3" if onstartload else "4"), onstartload, "\017")
	elif word[1].lower() == "update":
		callCacheList()
		for i in dlss_list:
			if i[:-3] in cache_list:
				hexchat.hook_timer(0, pyunload_timer, i)
				hexchat.hook_timer(0, download, [i])
	else:
		pprefix("/SS HELP -- Shows this help message")
		pprefix("/SS LIST -- Lists all SS Scripts you can get")
		pprefix("/SS GET <script[.py]> -- Downloads and loads <script>")
		pprefix("/SS STARTUP <True/False> -- Loads scripts on startup")
		pprefix("/SS UPDATE -- Updates all SS Scripts")
		pprefix("You have \00304{}\017 API Calls left!".format("~"+str(apicallsleft) if apicallsleft == 60 else apicallsleft))
	return hexchat.EAT_HEXCHAT

def download(stuff):
	global apicallsleft
	script = stuff[0]
	verbose = True if len(stuff) >1 else False
	try:
		if verbose:
			pprefix("Downloading {}...".format(script))
		urllib_request.urlretrieve(raw + script, os.path.join(ss_dir, script))
	except urllib_error.HTTPError as err:
		pprefix("Error downloading {} ({})".format(script, err))
	else:
		if verbose:
			pprefix("Download complete, loading script...")
		hexchat.hook_timer(0, pyload_timer, script)
	return False #For Timer

def pyload_timer(script):
	hexchat.command("py load {}".format(os.path.join(ss_dir, script)))
	return False

def pyunload_timer(script):
	hexchat.command("py unload {}".format(script))
	return False

def callCacheList():
	if not len(cache_list) > 0:
		updateCacheList()

def updateCacheList():
	global cache_list, apicallsleft
	httpresponse = urllib_request.urlopen(contents)
	apicallsleft = httpresponse.info()["X-RateLimit-Remaining"]
	
	cache_list = []
	for i in json.loads(httpresponse.read().decode()):
		if i["path"][-3:] == ".py":
			if not i["path"] in ["ss.py", "loader.py"]:
				cache_list.append(i["path"][:-3])

def unload_cb(userdata):
	for i in dlss_list:
		hexchat.command("py unload {}".format(i))

hexchat.hook_command("SS", ss_cb)
hexchat.hook_unload(unload_cb)
hexchat.prnt(__module_name__ + ' script loaded!')
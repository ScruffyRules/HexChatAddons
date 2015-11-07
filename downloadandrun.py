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
import urllib.parse
import os

__module_name__ = 'DownloadAndRun'
__module_version__ = '1.0'
__module_description__ = 'Downloads and loads python scripts'
__module_shortname__ = "00,01DNR"

addon_dir = os.path.join(hexchat.get_info('configdir'), 'addons')

def download_cb(word, word_eol, userdata):
        if isURL(word[1]):
                hexchat.hook_timer(0, download_timer, word[1])
        else:
                print(__module_shortname__ + "\tNot a valid URL!")
        return hexchat.EAT_HEXCHAT

def download(url):
        split = url.split("/")
        filename = split[len(split)-1].split(".")[0]
        extention = split[len(split)-1].split(".")[1]
        filention = filename + "." + extention
        if not extention == "py":
                hexchat.emit_print("Channel Message", __module_name__, "Not a python script.", "")
                return
        hexchat.emit_print("Channel Message", __module_name__, "Downloading {}...".format(filention), "")
        try:
                urllib_request.urlretrieve(url, os.path.join(addon_dir, filention))
        except urllib_error.HTTPError as err:
                hexchat.emit_print("Channel Message", __module_name__, "Error downloading {} ({})".format(filention, err), "")
        else:
                hexchat.emit_print("Channel Message", __module_name__, "Download complete, loading script...", "")
                hexchat.hook_timer(0, loadpy_timer, filention)
        return

def download_timer(url):
        download(url)
        return False

def loadpy_timer(script):
        hexchat.command("py load {}".format(script))
        return False

def isURL(url):
        parsedurl = urllib.parse.urlparse(url)

        if parsedurl.netloc:
                return True
        return False

hexchat.hook_command("download", download_cb)
hexchat.prnt(__module_name__ + ' script loaded')
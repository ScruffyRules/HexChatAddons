#
# Copyright 2015 Johannes Donath <johannesd@torchmind.com>
# and other copyright owners as documented in the project's IP log.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
__module_name__ = "git.io"
__module_version__ = "1.0"
__module_description__ = "Provides automatic shortening of GitHub links."

# integrate with hexchat & http
# urllib requires Python 3.x
import hexchat
import http.client
import re
import urllib.parse

urlRegex = re.compile('(https?://(gist.)?github.com[\S]+)')

# Called when you send a message
def replace_url(word, word_eol, userdata):
	# Skip replacement if string does not match
	if urlRegex.search(word_eol[0]) == None:
		return hexchat.EAT_NONE
	
	converted = []
	# List through all words
	for e in word:
		# Match if e is a gist/github url
		if urlRegex.match(e):
			converted.append(gitio(e))
		else:
			converted.append(e)
	
	hexchat.command('SAY {}'.format(" ".join(converted)))
	return hexchat.EAT_ALL

# Converts gist/github urls to git.io ones
def gitio(url):
	try:
		params = urllib.parse.urlencode({ 'url': url })
		headers = {'Content-type': 'application/x-www-form-urlencoded'}
		
		connection = http.client.HTTPConnection("git.io")
		connection.request('POST', '', params, headers)
		response = connection.getresponse()
		return response.getheader('Location', '<invalid>')
	except:
		return url.replace("github", "git\017hub")

hexchat.hook_command("", replace_url)
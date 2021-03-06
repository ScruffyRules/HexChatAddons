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
from os.path import join
from glob import glob

__module_name__ = 'ExtPlugins Loader'
__module_version__ = '1.0'
__module_description__ = 'Loads Python scripts in an external directory'


extdir = join(join(hexchat.get_info("configdir"), "addons"), "extplugins")

for i in glob(join(extdir, "*.py")):
	if not "loader.py" in i:
		hexchat.command("py load " + i)

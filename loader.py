import hexchat
from os.path import join
from glob import glob

__module_name__ = 'ExtPlugins Loader'
__module_version__ = '1.0'
__module_description__ = 'Later'


extdir = join(join(hexchat.get_info("configdir"), "addons"), "extplugins")

for i in glob(join(extdir, "*.py")):
	if not i == "loader.py":
		hexchat.command("py load " + i)

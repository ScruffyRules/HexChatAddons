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
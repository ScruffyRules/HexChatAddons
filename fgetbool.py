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
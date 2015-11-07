import hexchat

__module_name__ = 'AutoInvite'
__module_version__ = '1.1'
__module_description__ = 'Automatically invites if a channel is invite only and accepts any invites'

listlist = ["#spigot-irc-staff", "#oresomecraft-admin"]
blacklist = []
usrblacklist = []

def invite_callback(word, word_eol, user_data):
	hexchat.command('msg ChanServ invite {0}'.format(word[0]))
	return hexchat.EAT_HEXCHAT

def invited_callback(word, word_eol, user_data):
	if not word[1] in usrblacklist:
		if not word[0] in blacklist:
			#hexchat.command('join {0}'.format(word[0]))
			#hexchat.hook_timer(500, doprnt, word[0]+"|Invite\tYou have been intvited to this channel by " + word[1])
			if word[0] in listlist:
				hexchat.command("JOIN " + word[0])
				return hexchat.EAT_NONE
			hexchat.command("getbool \"FGETBOOL JOIN " + word[0] + "\" \"Incoming invite!\" Do you want to join " + word[0] + "?\nYou were invited by: " + word[1])
		else:
			print("Invite\t" + word[1] + " attempted to invite you to " + word[0] + " but it's on the blacklist!")
	else:
		print("Invite\t" + word[1] + " attempted to invite you but they're on the blacklist!")
	return hexchat.EAT_NONE


hexchat.hook_print('Invite', invite_callback)
hexchat.hook_print('Invited', invited_callback)

hexchat.prnt('AutoInvite script loaded')
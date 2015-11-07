import hexchat

__module_name__ = 'Same Channel Colour'
__module_version__ = '1.0'
__module_description__ = 'Later'

colour = "7"
Halt = False

def whoischan_cb(word, word_eol, userdata):
	global Halt
	if Halt:
		return hexchat.EAT_NONE
	chans = {}
	watwat = ""
	if word[1].lower() == "is an IRC Operator".lower():
		return hexchat.EAT_NONE
	words = word[1][:-1].split(" ")
	mchans = getchannels()
	for i in words:
		if i[0] != "#":
			chans[i[1:]] = i[0]
		else:
			chans[i] = ""
	
	for i in chans:
		if i in mchans:
			watwat += chans[i]+"\003"+colour+i + "\017 "
		else:
			watwat += chans[i]+i + " "
	Halt = True
	hexchat.emit_print("WhoIs Channel/Oper Line", word[0], watwat, "")
	#print(watwat)
	Halt = False
	return hexchat.EAT_ALL

def getchannels():
	channels = []
	network = hexchat.get_info("network")
	for i in hexchat.get_list("channels"):
		if i.network == network:
			if i.type == 2:
				channels.append(i.channel)
	return channels

hexchat.hook_print("WhoIs Channel/Oper Line", whoischan_cb)
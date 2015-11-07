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
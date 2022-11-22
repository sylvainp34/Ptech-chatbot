from rivescript import RiveScript

bot = RiveScript()
bot.load_directory("./eg/brain")
bot.sort_replies()


while True:
    msg = input('Vous> ')
    if msg == '/quit':
        quit()

    reply = bot.reply("localuser", msg)
    print('Bot>', reply)

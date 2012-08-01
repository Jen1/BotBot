from botClass import BotBot

bot = BotBot()
FIRST_CONNECT = True
bot.connect()
while(1):
    line = bot.response()

    if(line[0:4] == 'PING'):
        bot.request('PONG ' + line.rstrip().split()[1])
    if(FIRST_CONNECT == True):
        bot.joinChannels()
        bot.log('Join Successful')
        print('SERVER: ' + bot.HOST + ' ' + str(bot.PORT))
        print('JOINED: ' + bot.CHANNELS[0])
        FIRST_CONNECT = False


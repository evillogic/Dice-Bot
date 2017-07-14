# EvilLogic's Dice-Bot
A more intuitive Discord Dice Bot

# Why?
Most bots that include dice rolling functionality require a !roll command or convoluted syntax. This bot bypasses that and simply uses a channel for rolling with simple sintax, making it much easier to roll any kind of dice (any number of times!) and consolidating it all to one channel.

# Use
To add the bot to your server, authorize it with <br />
https://discordapp.com/oauth2/authorize?client_id=332292348950347777&scope=bot&permissions=0 <br />
and make a channel named rolz. This name can be reconfigured easily if you host your own version of the bot.<br />
Any message in rolz will be treated as a dice command if it starts with a number, and should be in the format of #(operator)#.<br />

## Example<br />
3d6 will roll 3d6 and output the result<br />
3d6d6 will roll a d6 3d6 times<br />
3d6+1 will roll 3d6 and add 1<br />
3d6+1 20d20 will roll 3d6 and add 1, then roll 20d20 and output each as separate rolls<br />

Math operators +, -, *, and / are also accepted

# Installation
The bot requires python3 and the discord.py library.
After you install both, make a discord bot with a user over at
https://discordapp.com/developers/docs/intro
and give the bot a token on line 66, the last line.
Now all that's left is to add the bot to your server. Copy the link above and replace the number after "id=" with your bot's Client ID.
Have fun!

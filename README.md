# botstore

So I created this script when I was 14 and 15 years old (2021 - 2022), with the intention to have all the commands from a complete discord bot working sepparately, so I could sell parts of it in my discord bot store as fast as possible.
For the store, I created basically a menu so my clients could choose what commands they would buy, each one costing around BRL$0,75, it depended of the command, some were more complex, so more expensive as well.

*This code does not have the intention of being clean. I created it just so I could ctrl V + ctrl C and sell chunks of it sepparately. I was 14 when I wrote it too, so disregard stupid code or features*

Features:
* It has his own ecconomy system with his own currencies:
     Users could transfer coins to each other
     Users could buy cool things with the coins
     All the currencies have dollar-backed value using requests
* marry users, same as divorcing
* send cute photos of animals by command
* ban/kick, give roles, unban users
* Track users activities
* Create ASCII art with the photo of choice of users or profile avatar 
* kiss, punch, hug, slap, pet users
* request any price of some currencies around the world
* lock/unlock and clear chats

Dependencies:
* discord.py
* requests
* PIL

How to run:
git clone https://github.com/leonardogtcruz1/botstore.git
cd botstore
pip install -r requirements.txt
python bot.py

DISCLAIMER -> You need to create a new bot in discord website and paste your token as it shown in the line 1610: client.run(TOKEN)

Leonardo Cruz - leogtdacruz@gmail.com

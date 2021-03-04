from DiscordLib import *


now = datetime.now()

def command_aide():
    bot.write("heure => retourne l'heure (H:M:S)")
    bot.write("zizi => retourne une blague")
    bot.write("about => information de création")

def logout():
    bot.write("Ma journée est finie. Bye bye")
    exit

def about():
    bot.write("Developpé par Sl00x ce bot n'a besoin d'aucun droit")

#Création du bot
bot = DiscordBot("neutrom.inc@gmail.com", "Anonymes1245!")

bot.haveNSFW(True);
bot.mainServer("417615269108776960/754079824460513360")
bot.connectToGuild("447057765903368197/783061289597140992")

bot.triggerSign("::")

#Init des commandes du bot
bot.command("aide", command_aide)
bot.command("zizi", bot.write, ["Mon gros chibrax et léve, tel le chapito du cirque Pinder"])
bot.command("heure", bot.write, ["Il est actuellement: " + now.strftime("%H:%M:%S")])
bot.command("exit", logout)
bot.command("about", about)


#Connexion
bot.Connect()

#HandleReceivedMessage
while(bot.isLog):
    bot.ReceiveMessage()


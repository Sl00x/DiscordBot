from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from colorama import Fore, Back, Style 


class DiscordBot:
    
    def __init__(self, user, passw):
        self.password = passw
        self.username = user
        self.uri = "https://discord.com/login"
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        #self.driver.set_window_position(-10000,0)
        self.islog = False
        self.commands = {}
        self.args = {}
        self.nfsw = False
        self.endpointMain = None
        self.guildChat = None
        self.trigger = "!"

    def mainServer(self, endpoint):
        self.endpointMain = endpoint

    def connectToGuild(self, chat):
        self.guildChat = chat

    def triggerSign(self, trigger):
        self.trigger = trigger


    def haveNSFW(self, bool):
        self.nfsw = bool

    def Connect(self):
        now = datetime.now()
        self.driver.get(self.uri)
        time.sleep(3)
        print('{'+now.strftime("%H:%M:%S")+'} - Init credentials of BOT')
        self.driver.find_element_by_name("email").click()
        self.driver.find_element_by_name("email").click()
        self.driver.find_element_by_name("email").send_keys(self.username)
        self.driver.find_element_by_name("password").click()
        self.driver.find_element_by_name("password").send_keys(self.password)
        time.sleep(2)
        print('{'+now.strftime("%H:%M:%S")+'} - Credentials entered & validated')
        #element = self.driver.find_element_by_xpath("//button[@class='marginBottom8-AtZOdT button-3k0cO7 button-38aScr lookFilled-1Gx00P colorBrand-3pXr91 sizeLarge-1vSeWK fullWidth-1orjjo grow-q77ONN']")
        #self.driver.execute_script("arguments[0].removeAttribute('disabled');", element)
        self.driver.find_element_by_xpath("//button[@class='marginBottom8-AtZOdT button-3k0cO7 button-38aScr lookFilled-1Gx00P colorBrand-3pXr91 sizeLarge-1vSeWK fullWidth-1orjjo grow-q77ONN']").click()
        time.sleep(10)
        self.driver.get("https://discord.com/channels/" + self.endpointMain)
        print(Fore.GREEN + '{'+now.strftime("%H:%M:%S")+'} - Access to server main')
        
        if(self.nfsw):
            time.sleep(5)
            self.driver.find_element_by_xpath("//button[@class='action-yrVND8 button-38aScr lookFilled-1Gx00P actionRed-gYn8D3 sizeLarge-1vSeWK grow-q77ONN']").click()
        
        time.sleep(5)
        print('{'+now.strftime("%H:%M:%S")+'} - NSFW Bypass')
        self.driver.get("https://discord.com/channels/" + self.guildChat)
        time.sleep(5)
        print('{'+now.strftime("%H:%M:%S")+'} - Access to channel botworking...')
        self.isLog = True;
        print('{'+now.strftime("%H:%M:%S")+'} - Logged In')

    def ReceiveMessage(self):
        time.sleep(1)
        msgs = self.driver.find_elements_by_css_selector(".message-2qnXI6")
        try:
            last = msgs[len(msgs) - 1].text
            keys = self.commands.keys()
            for key in keys:
                if key in last:
                    if(self.commands[key] != None):
                        if(self.args[key] != None):
                            self.commands[key](*self.args[key])
                            print('{'+now.strftime("%H:%M:%S")+'} - ' + key + ' executed')
                        else:
                            self.commands[key]()
                            print('{'+now.strftime("%H:%M:%S")+'} - ' + key + ' executed')
        except:
            print("")
        

    def command(self, command, functionlinked = None, args =None):
        self.commands[self.trigger+command] = functionlinked
        self.args[self.trigger+command] = args


    def write(self, message):
        inputBox = self.driver.find_elements_by_xpath('.//span[@data-slate-zero-width = "z"]')
        inputBox[0].send_keys(message)
        inputBox[0].send_keys(Keys.RETURN)

   

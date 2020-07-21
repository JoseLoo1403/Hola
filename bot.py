from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import Utils
import random

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.instagram.com/p/CC2f7-6Dq5h/")


Helper = Utils.ListHelper('@sampineda18','@clementeramost ','@jair.abdul','@jaysonerazo','@fredyjmunoz')
XpathHelper = Utils.XpathObjects


UsersList = list()

def FillUsers():
    UsersList.clear()

    for p in range(20):
        UsersList.append(Helper.GetRandom_User_Order())
    
    print("Combinaciones hechas")
    

sleep(6)

LogBtn = driver.find_element_by_xpath(XpathHelper.LoginButton)
LogBtn.click()


def MakeComments():
    for x in UsersList:
        TextBox = driver.find_element_by_xpath(XpathHelper.textBox)
        TextBox.send_keys(x)
        sleep(2)

        Publish = driver.find_element_by_xpath(XpathHelper.PublishBtn)
        Publish.click()
        sleep(random.randint(5,15))

    print("Compltado!")


verificator = "1"
 
while(verificator == "1"):
    Selector = input("Que desea hacer?")

    if Selector == "1":

        try:
            FillUsers()
            MakeComments()
        except:
            print("Error al publicar")
    
    verificator = input("Quiere seguir?")
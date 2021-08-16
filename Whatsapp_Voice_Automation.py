from selenium import webdriver
from time import sleep
import speech_recognition as sr

#Connect you to whatsapp web and prompt for the contact name you saved.
driver = webdriver.Chrome('''PATH_of_chromedriver''')
driver.get("https://web.whatsapp.com/")
wait = input('Press Enter after scanning QR Code: ')
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak the name of the person you want to send message :")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)
name=[text]

#Listen to the message you want to deliver and covert it to text.
m = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak the message you want to send :")
    audio = m.listen(source)
    text2 = m.recognize_google(audio)
    print(text2)
msg = text2
count = len(name)

#The message converted into text will be automaticallly written in message box
#Search for the send button and click it virtually at given time
n = 0
for i in range(count):
    search = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    search.send_keys(name[n])
    sleep(1)
    
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name[n]))
    user.click()
    n += 1

    msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    msg_box.send_keys(msg)
    button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]')
    sleep(1)
    button.click()
    print("Sent message to {}".format(name))
    

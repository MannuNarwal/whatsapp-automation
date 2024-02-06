import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from csv import reader

contacts =[]

def readContacts():
	with open('contacts.csv',"r") as f:
		csv_reader = reader(f)
		for row in csv_reader:
			contacts.append(row[0])

def sendMessage():
	driver=webdriver.Chrome()   
	driver.get("https://web.whatsapp.com/")
	while True:
		for name in contacts:
			try:
				user = driver.find_element(By.XPATH, "//span[@title='{}']".format(name))
				print(user)
				user.click()

				text_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p')
				text_box.send_keys("Hello ",name)

				
				sendbtn= driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')
				sendbtn.click()
			except Exception as e:
				pass
			else :
				print('Successfully msg sent to',name)
				print(len(contacts)-1, 'more msgs left to send')
				contacts.remove(name)

		if(len(contacts)==0):
			break
		
	time.sleep(10)
	driver.close()


readContacts()
sendMessage()

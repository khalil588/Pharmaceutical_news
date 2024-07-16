import os
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import pyautogui
import constant as cnst
import time
import pandas as pd

class Scrapper (webdriver.Chrome):

    def __init__(self,driver_path=cnst.path, teardown = False):
        self.driver_path=driver_path
        self.teardown=teardown
        os.environ['PATH'] +=self.driver_path
        super(Scrapper,self).__init__()
        self.implicitly_wait(0)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown :
            self.quit()

#Lnading to first page 
    def land_first_page(self):
        self.get("https://www.visualcapitalist.com/cp/worlds-50-largest-pharmaceutical-companies/")
        #time.sleep(60)
    
# Extracting Data 
    def extracting_data(self):
        try : 
            dropdown_element = self.find_element(By.XPATH, '//*[@id="tablepress-3837_length"]/label/select')
            dropdown = Select(dropdown_element)
            dropdown.select_by_value("100")
            time.sleep(5)
            table = self.find_element(By.XPATH, '//*[@id="tablepress-3837"]')
            table_data = []
            for row in table.find_elements(By.TAG_NAME, "tr"):
                row_data = {}
                title = []
                cnt = 1
                """for cellth in  row.find_elements(By.TAG_NAME, "th"):
                    title.append(cellth.text.strip()) 

                cnttd= 1"""
                title= ['Ranking', 'Company Name', 'Symbol',   'Market Cap','country']
                cnttd =  0 
                for cell in row.find_elements(By.TAG_NAME, "td") :
                    #print(title[str(cnttd)])
                    ttl = title[cnttd]
                    print(ttl)
                    #row_data.append(cell.text.strip())  # Remove leading/trailing whitespace
                    row_data[ttl] = cell.text.strip()
                    cnttd+=1
                    print(row_data)
                table_data.append(row_data)
            return pd.DataFrame(table_data)
        except : 
            return pd.DataFrame()
        

        





    def scrape_paginated_data(self):
        next_button = self.find_element(By.XPATH, '//*[@id="main"]/div/div/nav/button[2]')
        #close_pop_up = self.find_element(By.XPATH, '/html/body/div/div[2]/div/button')
        data_collected = pd.DataFrame()
        data_collected = data_collected._append(self.extracting_data()) 
        i = 0       
        while True:
#/html/body/div/div[2]/div/div/form/div/input 
            try:
                """time.sleep(5)
                pyautogui.moveTo(96, 237)
                # Left-click the mouse at the current position
                pyautogui.click()"""

                i +=1 
                print(i)
                WebDriverWait(self, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div/nav/button[2]')))
 
                next_button.click()
                print("Clicked the next button!")
                #data_collected = pd.DataFrame()
                #popup start
                popups = self.window_handles  # Get a list of all window handles
                if len(popups) > 1:  # If there are popups:
                    for handle in popups[1:]:  # Iterate through each popup handle
                        self.switch_to.window(handle)  # Switch to the popup window
                        try:
                            close_button = WebDriverWait(self, 60).until(
                                EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div > div.fixed.left-0.top-0.z-\[99\].flex.h-screen.w-screen.items-center.justify-center.bg-gray-500\/50 > div > button'))
                            )  # Find the "Close" button
                            close_button.click()  # Click the "Close" button
                        except:
                            self.close()  # Close the popup window if no "Close" button found
                        self.switch_to.window(popups[0])  # Switch back to the main window
 
                #popup ends




                data_collected = data_collected._append(self.extracting_data())   # Call data collection function after successful click
            except :

                data_collected = data_collected._append(self.extracting_data()) 
                print('non cliquable')
                break
        return data_collected
        # Close the browser after the loop finishes


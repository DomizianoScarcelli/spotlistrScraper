from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
from passwords import secret_password
from passwords import secret_username

#Define month mapping
month_mapping = dict({
    "1" : "Gennaio",
    "2" : "Febbraio",
    "3" : "Marzo",
    "4" : "Aprile",
    "5" : "Maggio",
    "6" : "Giugno",
    "7" : "Luglio",
    "8" : "Agosto",
    "9" : "Settembre",
    "10" : "Ottobre",
    "11" : "Novembre",
    "12" : "Dicembre"
})

month_days_mapping = dict({
    "1": "31",
    "2": "28",
    "3": "31",
    "4": "30",
    "5": "31",
    "6": "30",
    "7": "31",
    "8": "31",
    "9": "30",
    "10": "31",
    "11": "30",
    "12": "31",
})

#Get first and last day of the month
actual_date = datetime.today().date()
if len(str(actual_date.month)) == 1:
    first_day_month = "0{}/{}/{}".format(actual_date.month, "01", actual_date.year)
    last_day_month = "0{}/{}/{}".format(actual_date.month, month_days_mapping.get(str(actual_date.month)), actual_date.year)
else:
    first_day_month = "{}/{}/{}".format(actual_date.month, "01", actual_date.year)
    last_day_month = "{}/{}/{}".format(actual_date.month, month_days_mapping.get(str(actual_date.month)), actual_date.year)

#Get the webpage
driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver")

#Login to Spotify
driver.get("https://spotlistr.com/.netlify/functions/routes/login")
username = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")
login_button = driver.find_element_by_id("login-button")
username.send_keys(secret_username)
password.send_keys(secret_password)
login_button.click()
time.sleep(3)
driver.get("https://www.spotlistr.com/search/lastfm-top-for-time-period")

#Select time period
username = driver.find_element_by_class_name("ui input")
username.send_keys("dovi666")
start_date = driver.find_element_by_id("start-date")
start_date.send_keys(first_day_month)
end_date = driver.find_element_by_id("end-date")
end_date.send_keys(last_day_month)
track_number = driver.find_elements_by_class_name("ui input")[3]
track_number.clear()
track_number.send_keys("20")
search = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div[2]/div[2]/div[2]/div/div/div/form[1]/div/div[4]/div/div/button')
search.click()

#Name and create the playlist
time.sleep(5)
playlist_name = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div[2]/div[2]/div[2]/div/div/div/form[2]/div[2]/div[1]/div/input')
playlist_name.send_keys("Preferiti di {} {}".format(month_mapping.get(str(actual_date.month)), str(actual_date.year)))
create_playlist = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div[2]/div[2]/div[2]/div/div/div/form[2]/div[3]/div/button[1]')
create_playlist.click()
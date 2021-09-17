import time #To implement delays
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities #to log network traffic
from playsound import playsound


Surrey_driver_licensing_label = "/html/body/div/div[1]/div/mat-dialog-container/app-search-modal/div[2]/div/div[3]/div[2]"
Surrey_claim_centre_label = "/html/body/div/div[1]/div/mat-dialog-container/app-search-modal/div[2]/div/div[4]/div"

Label = Surrey_claim_centre_label # Change this for different locations

# Chrome Profiles
options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:/Users/sshao/AppData/Local/Google/Chrome/User Data')
options.add_argument('--profile-directory=Profile 1')
#implement capabilities
capabilities = DesiredCapabilities.CHROME
# capabilities["loggingPrefs"] = {"performance": "ALL"}  # chromedriver < ~75
capabilities["goog:loggingPrefs"] = {"performance": "ALL"}  # chromedriver 75+

browser = webdriver.Chrome('C:\webdrivers\chromedriver', 
options=options, desired_capabilities=capabilities) #Open Browser
browser.get("https://onlinebusiness.icbc.com/webdeas-ui/home") #Open ICBC Website

playsound('C:/Users/sshao/Desktop/icbc bot/ohyeah.mp3')

def scrape_date():
    # Click the Surrey label to refresh the data
    Surrey_label = browser.find_element_by_xpath(Label) 
    Surrey_label.click()
    
    try:
        WebDriverWait(browser, 600).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.date-title"))
        )
        print("waiting")
    finally:
        print("Date Located. Returning data: ")

    # Find earliest date
    earliest_date = browser.find_element_by_css_selector("div.date-title")
    date1 = earliest_date.text
    return(date1)
def press_next():
    nextbutton_location = "/html/body/app-root/app-home/mat-card/div[3]/div[2]/button"
    nextbutton = browser.find_element_by_xpath(nextbutton_location)
    nextbutton.click()
def getting_to_searching():
    # Fill in Last Name
    lastname_box_location = "/html/body/app-root/app-login/mat-card/mat-card-content/form/span[1]/div[1]/mat-form-field/div/div[1]/div[3]/input"
    Lastname = "Shao"
    lastnamebox = browser.find_element_by_xpath(lastname_box_location)
    lastnamebox.clear()
    lastnamebox.send_keys(Lastname)

    # Fill in Drivers License Number
    driverlicensenumber = "nah"
    licensebox_location = "/html/body/app-root/app-login/mat-card/mat-card-content/form/span[1]/div[2]/mat-form-field/div/div[1]/div[3]/input"
    licensebox = browser.find_element_by_xpath(licensebox_location)
    licensebox.clear()
    licensebox.send_keys(driverlicensenumber)

    # Fill in Keyword (Password)
    keyword = "nah"
    keywordbox_location = "/html/body/app-root/app-login/mat-card/mat-card-content/form/span[2]/div[1]/mat-form-field/div/div[1]/div[3]/input"
    keywordbox = browser.find_element_by_xpath(keywordbox_location)
    keywordbox.clear()
    keywordbox.send_keys(keyword)

    #check box
    checkbox = browser.find_element_by_xpath("/html/body/app-root/app-login/mat-card/mat-card-content/form/span[2]/div[3]/mat-checkbox/label/div")
    checkbox.click()

    #Sign in 
    signinbox = browser.find_element_by_xpath("/html/body/app-root/app-login/mat-card/mat-card-content/form/div[3]/button[2]")
    signinbox.click()

    try:
        WebDriverWait(browser, 600).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-driver/div/mat-card/div[5]/div[1]/app-appointments/div/div[2]/div/div[4]/button[1]"))
    )
    finally:
        print("Reschedule appointment button located. Delaying 0.1s, then pressing.")
    time.sleep(0.1)
    #reschedule appointmnet
    reschedule_button = browser.find_element_by_xpath("/html/body/app-root/app-driver/div/mat-card/div[5]/div[1]/app-appointments/div/div[2]/div/div[4]/button[1]")
    reschedule_button.click()
    
    try:
        WebDriverWait(browser, 600).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div/mat-dialog-container/app-cancel/div/div/div[2]/button[2]"))
    )
    finally:
        print("Confirm button located. Delaying 0.1s, then pressing.")
    time.sleep(0.1)
    #confirm
    confirm_button = browser.find_element_by_xpath("/html/body/div/div[2]/div/mat-dialog-container/app-cancel/div/div/div[2]/button[2]")
    confirm_button.click()
   
    try:
        WebDriverWait(browser, 600).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div/mat-dialog-container/app-search-modal/div/div/form/div[1]/div[1]/mat-form-field/div/div[1]/div[3]/input"))
    )
    finally:
        print("Page Loaded. Delaying 0.1s, then entering data.")
    time.sleep(0.1)

    #Fill in Location
    surrey_location_first_letter = "S"
    surrey_location_second_letter = "u"
    surrey_location_third_letter = "r"
    surrey_location_fifth_letter = "e"
    location_box = browser.find_element_by_xpath("/html/body/div/div[1]/div/mat-dialog-container/app-search-modal/div/div/form/div[1]/div[1]/mat-form-field/div/div[1]/div[3]/input")
    location_box.clear()
    location_box.send_keys(surrey_location_first_letter)
    time.sleep(0.1)
    location_box.send_keys(surrey_location_second_letter)
    time.sleep(0.1)
    location_box.send_keys(surrey_location_third_letter)
    time.sleep(0.1)
    location_box.send_keys(surrey_location_third_letter)
    time.sleep(0.1)
    location_box.send_keys(surrey_location_fifth_letter)
    time.sleep(1)
    
    #click dropdown
    try:
        WebDriverWait(browser, 600).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div/div"))
    )
    finally:
        print("Dropdown located. Delaying 0.1s, then pressing.")
    time.sleep(0.1)
    dropdown_result = browser.find_element_by_xpath("/html/body/div/div[2]/div/div")
    dropdown_result.click()
    
    #Search
    time.sleep(0.5)
    search_button = browser.find_element_by_xpath("/html/body/div/div/div/mat-dialog-container/app-search-modal/div/div/form/div[2]/button")
    search_button.click()

    time.sleep(3)
    #Check Surrey
    try:
        WebDriverWait(browser, 600).until(
        EC.presence_of_element_located((By.XPATH,Label))
    )
    finally:
        print("Surrey location located. Delaying 0.1s, then parsing.")
    time.sleep(0.1)
    Surrey_label = browser.find_element_by_xpath(Label)
    Surrey_label.click()

press_next()
getting_to_searching()

time.sleep(0.2)
#Collecting Reference Date (most likely today's date)
try:
    WebDriverWait(browser, 60).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div.date-title"))
    )
    print("waiting")
finally:
    print("Element located. Delaying 0.1s, then parsing.")
time.sleep(0.1)
reference_date = browser.find_element_by_css_selector("div.date-title").text
print("This is the reference date: ")
print(reference_date)

# Random status condition
is_same_thing = False

while not is_same_thing:
    new_date = scrape_date()
    if new_date == reference_date:
        print("No change.")
    else:
        print("NEW DATE FOUND!")
        print(new_date)
        is_same_thing = True
        playsound('C:/Users/sshao/Desktop/icbc bot/ohyeah.mp3')
    time.sleep(5) # Wait 5 seconds then check again

print("Go register")

# Find later dates, change the 1 at the end in span
#browser.find_element_by_xpath("/html/body/div/div[2]/div/mat-dialog-container/app-eligible-tests/div/div[2]/mat-button-toggle-group/div/span[1]/div")

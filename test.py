from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import time
# Path to the Brave browser executable
brave_path = "/usr/bin/brave-browser"

# Path to the Brave profile directory
brave_profile_path = "profiles/1/Brave-Browser"

# Set up the ChromeOptions object to use the Brave browser and the profile
options = Options()
options.binary_location = brave_path
options.add_argument("--user-data-dir=" + brave_profile_path)

# Set up the ChromeService object with the Brave binary and options
service = Service(executable_path='/usr/bin/brave-browser')

# Launch the Brave browser with the last tabs that were open
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.google.com/")
time.sleep(50)
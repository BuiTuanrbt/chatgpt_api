from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Path to the Brave browser executable
brave_path = "/usr/bin/brave-browser"

# List of profile names, user data directories, and last pages for each instance of Brave
profiles = [
    {"name": "Brave 1", "user_data_dir": "profiles/1", "last_page": "https://www.google.com/"},
    {"name": "Brave 2", "user_data_dir": "profiles/2", "last_page": "https://www.facebook.com/"},
    {"name": "Brave 3", "user_data_dir": "profiles/3", "last_page": "https://www.youtube.com/"},
]

# Loop over the profiles to create and launch each instance of Brave
for profile in profiles:
    # Set up the ChromeOptions object to use the Brave browser and the user data directory
    options = Options()
    options.binary_location = brave_path
    options.add_argument("--user-data-dir=" + profile["user_data_dir"])
    
    # Set up the ChromeService object with the Brave binary and options
    service = Service(executable_path='/usr/bin/brave-browser')

    # Launch the Brave browser with the last page that was open in the previous session
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(profile["last_page"])
    
    # Do whatever you need to do with the instance of Brave here
    # For example, you could use the driver to navigate to other pages, interact with the page, etc.

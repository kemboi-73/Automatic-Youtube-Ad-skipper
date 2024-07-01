from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open YouTube
driver.get("https://www.youtube.com")

# Function to skip ads
def skip_ad():
    try:
       
        skip_button = driver.find_element(By.CLASS_NAME, "ytp-ad-skip-button")
        skip_button.click()
        print("Ad skipped")
    except Exception as e:
        print("No ad to skip:", e)

# Play a video
search_box = driver.find_element(By.NAME, "search_query")
search_box.send_keys("Kenya")
search_box.send_keys(Keys.RETURN)

time.sleep(3)  # Wait for the search results to load

first_video = driver.find_element(By.ID, "video-title")
first_video.click()

# Continuously check for ads and attempt to skip them
while True:
    skip_ad()
    time.sleep(5)  # Check every 5 seconds

# Cleanup
driver.quit()

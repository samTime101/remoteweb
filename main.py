# required for opening the links and responding (chrome is used here)
from selenium import webdriver

# for adding the headless option because I am running this on Google Shell and I have not downloaded it locally
from selenium.webdriver.chrome.options import Options

# for alerts as we are working with prompts and alerts
from selenium.webdriver.common.alert import Alert

# for searching elements in HTML
from selenium.webdriver.common.by import By

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ensure GUI is not required

# Set up the WebDriver
driver = webdriver.Chrome(options=chrome_options)

# our target site for now let's work with mine
driver.get("https://samip101.web.app/project.html")

# finding the button
driver.find_element(by=By.TAG_NAME, value="button").click()

# alerts
prompt_alert = driver.switch_to.alert

# printing the alert content
print(prompt_alert.text)

# what we want to type on the prompt menu
prompt_alert.send_keys("test")

# clicking the OK button of the prompt, simply confirming
prompt_alert.accept()

# searching the body element
body_content = driver.find_element(by=By.TAG_NAME, value="body").text

# displaying the body of HTML after the prompt entry
print(body_content)

# quitting Chrome (headless)
driver.quit()

from selenium_recaptcha_solver import RecaptchaSolver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Set up Chrome options
options = Options()
options.add_argument("--headless")  # Remove this if you want to see the browser (Headless makes the chromedriver not have a GUI)
options.add_argument("--window-size=1920,1080")
options.add_argument(f'--user-agent=Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36')
options.add_argument('--no-sandbox')
options.add_argument("--disable-extensions")

# Initialize the Chrome driver without specifying the path to ChromeDriver
test_driver = webdriver.Chrome(options=options)

try:
    # Initialize the RecaptchaSolver
    solver = RecaptchaSolver(driver=test_driver)

    # Open the webpage with reCAPTCHA
    test_driver.get('https://www.google.com/recaptcha/api2/demo')

    # Find the reCAPTCHA iframe
    recaptcha_iframe = test_driver.find_element(By.XPATH, '//iframe[@title="reCAPTCHA"]')

    # Click the reCAPTCHA checkbox
    solver.click_recaptcha_v2(iframe=recaptcha_iframe)

    # Take a screenshot after solving reCAPTCHA
    test_driver.save_screenshot('screenshot.png')
    print("Screenshot saved as 'screenshot.png'")
    
finally:
    # Clean up
    test_driver.quit()

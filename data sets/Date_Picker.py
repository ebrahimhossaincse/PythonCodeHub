from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Function to convert month name to index
def month_name_to_index(month_name):
    months = {
        "January": 0, "February": 1, "March": 2, "April": 3,
        "May": 4, "June": 5, "July": 6, "August": 7,
        "September": 8, "October": 9, "November": 10, "December": 11
    }
    return months.get(month_name, -1)

# Initialize WebDriver
driver = webdriver.Chrome()

def select_date_time(desired_day, desired_month, desired_year, desired_hour, desired_minute, am_pm):
    try:
        # Open the URL
        driver.get("https://www.tutorialspoint.com/selenium/practice/date-picker.php")

        # Maximize the browser window
        driver.maximize_window()
        time.sleep(2)
        # Locate the date picker input field and click to open the calendar
        date_input = driver.find_element(By.ID, "datepicker")
        date_input.click()
        time.sleep(2)
        # Select the year
        while True:
            year_input = driver.find_element(By.CSS_SELECTOR, ".numInput.cur-year")
            displayed_year = year_input.get_attribute("value")
            if displayed_year == desired_year:
                break
            if int(displayed_year) < int(desired_year):
                driver.find_element(By.CSS_SELECTOR, ".flatpickr-next-month").click()
            else:
                driver.find_element(By.CSS_SELECTOR, ".flatpickr-prev-month").click()

        time.sleep(2)
        # Select the month
        while True:
            month_dropdown = driver.find_element(By.CSS_SELECTOR, ".flatpickr-monthDropdown-months")
            displayed_month = int(month_dropdown.get_attribute("value"))
            desired_month_index = month_name_to_index(desired_month)

            if displayed_month == desired_month_index:
                break
            if displayed_month < desired_month_index:
                driver.find_element(By.CSS_SELECTOR, ".flatpickr-next-month").click()
            else:
                driver.find_element(By.CSS_SELECTOR, ".flatpickr-prev-month").click()

        time.sleep(2)
        # Select the desired day
        day_element = driver.find_element(By.XPATH, f"//span[contains(@class, 'flatpickr-day') and text()='{desired_day}']")
        day_element.click()

        # Select the time
        # Set the hour
        hour_input = driver.find_element(By.CSS_SELECTOR, ".flatpickr-hour")
        hour_input.clear()
        hour_input.send_keys(desired_hour)
        time.sleep(2)
        # Set the minute
        minute_input = driver.find_element(By.CSS_SELECTOR, ".flatpickr-minute")
        minute_input.clear()
        minute_input.send_keys(desired_minute)
        time.sleep(2)
        # Set AM/PM
        am_pm_button = driver.find_element(By.CSS_SELECTOR, ".flatpickr-am-pm")
        if am_pm_button.text != am_pm:
            am_pm_button.click()
        time.sleep(2)
        # Ensure the date and time are set
        date_input.send_keys(Keys.TAB)
        time.sleep(1)  # Allow the input field to update
        time.sleep(2)
        # Verify the selected date and time in the input field
        selected_date_time = date_input.get_attribute("value")
        print("Selected Date and Time:", selected_date_time)

    except Exception as e:
        print("An error occurred:", e)

    finally:
        # Close the browser
        driver.quit()

# Call the function with desired date and time
select_date_time("15", "February", "2025", "10", "30", "AM")

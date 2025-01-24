from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from urllib.parse import urljoin

# Global variables
visited_urls = set()  # To track visited URLs and avoid duplicates
broken_links = set()  # To store broken links

def crawl_website(driver, base_url):
    """
    Recursively crawl the website starting from the base URL.
    """
    if base_url in visited_urls:
        return

    # Mark the URL as visited
    visited_urls.add(base_url)
    print(f"Crawling: {base_url}")

    # Navigate to the URL
    driver.get(base_url)

    # Find all links on the page
    links = driver.find_elements(By.TAG_NAME, "a")

    for link in links:
        href = link.get_attribute("href")

        if href and href not in visited_urls:
            # Check if the link is internal (same domain)
            if is_internal_link(href, base_url):
                # Recursively crawl internal links
                crawl_website(driver, href)
            else:
                # Check external links for broken status
                check_link_status(href)

def is_internal_link(link, base_url):
    """
    Check if the link belongs to the same domain as the base URL.
    """
    return link.startswith(base_url) or link.startswith("/")

def check_link_status(url):
    """
    Check the HTTP status code of the link.
    """
    try:
        response = requests.head(url, timeout=5)
        if response.status_code >= 400:
            broken_links.add(f"{url} (Response Code: {response.status_code})")
    except requests.exceptions.RequestException as e:
        broken_links.add(f"{url} (Error: {e})")

def main():
    # Set up Selenium WebDriver (e.g., Chrome)
    driver = webdriver.Chrome()  # Ensure chromedriver is in your PATH

    # Base URL of the website to crawl
    base_url = "https://staging.college-bridge.achievetestprep.com/"  # Replace with your website URL

    try:
        # Start crawling from the base URL
        crawl_website(driver, base_url)
    finally:
        # Close the WebDriver
        driver.quit()

    # Print broken links
    if broken_links:
        print("\nBroken links found:")
        for link in broken_links:
            print(link)
    else:
        print("\nNo broken links found.")

if __name__ == "__main__":
    main()
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


def get_glassdoor_salaries(company_name):
    chrome_options = webdriver.Chrome()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    url = f"https://www.glassdoor.co.in/Salaries/{company_name}-data-engineer-salary-SRCH_KO0,14.htm"
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    salaries = soup.find_all("div", {"class": "col-2 d-none d-md-flex flex-row justify-content-end"})
    salaries = [s.text.strip() for s in salaries]
    driver.quit()
    return salaries


def get_ambitionbox_salaries(company_name):
    url = f"https://www.ambitionbox.com/salaries/{company_name}-salaries/data-engineer-salaries"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    salaries = soup.find_all("div", {"class": "salary-cell"})
    salaries = [s.text.strip() for s in salaries]
    return salaries


company_name = input("Enter the company name: ")
glassdoor_salaries = get_glassdoor_salaries(company_name)
ambitionbox_salaries = get_ambitionbox_salaries(company_name)

print(f"Glassdoor salaries for {company_name}: {glassdoor_salaries}")
print(f"AmbitionBox salaries for {company_name}: {ambitionbox_salaries}")

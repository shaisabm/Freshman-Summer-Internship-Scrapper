import time
from selenium.webdriver.common.by import By
from selenium import webdriver
import requests
from bs4 import BeautifulSoup

from api import gemini
import json
from selenium.webdriver.common.keys import Keys

url = 'https://github.com/SimplifyJobs/Summer2025-Internships/blob/dev/README.md'

with open('data.json') as file:
    data = json.load(file)
    last_visited = data['last_visited']

html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
job_rows = list(soup.find_all('tr'))[1:]
print(job_rows)
driver = webdriver.Firefox()
print("Starting the job scrapper...")
for job in job_rows:
    try:
        title = list(job.find_all('td'))[1].text
        print(title)
        if title == last_visited:
            first_row = job_rows[0]
            data['last_visited'] = first_row.find_all('td')[1].text
            with open('data.json', 'w') as file:
                json.dump(data, file, indent=4)
            break

        job_link = list(job.find_all('td'))[3].a['href']
        driver.get(job_link)
        time.sleep(3)
        job_description = driver.find_element(By.TAG_NAME, 'body').text
        response = gemini(job_description)
        print(json.loads(response[7:len(response)-5]))
        body = driver.find_element(By.TAG_NAME, 'body')
    except Exception as e:
        print(f"Error: {e}")
driver.quit()
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup
from api import gemini
import json
from send_update import send_update
url = 'https://github.com/SimplifyJobs/Summer2025-Internships/blob/dev/README.md'

with open('data.json') as file:
    data = json.load(file)
    last_visited = data['last_visited']

def main():
    # html = requests.get(url).text
    driver = webdriver.Firefox()
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    job_rows = list(soup.find_all('tr'))[1:]
    print(job_rows)
    time.sleep(4)
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
            job_info = json.loads(response[7:len(response)-5])
            print(job_info)
            if job_info['hiring_freshman'] and job_info['posted_days_ago'] <= 15:
                print("Sending the job to telegram...")
                send_update(f"Title: {title}\nLink: {job_link}")
                print("Job sent!")


        except Exception as e:
            print(f"Error: {e}")
            continue
    driver.quit()

if __name__ == '__main__':
    while True:
        main()
        time.sleep(10)

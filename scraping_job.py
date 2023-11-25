import requests
from bs4 import BeautifulSoup
import time


def job_jobs():
    ls_job = []
    for i in range(1, 17):  # job posting pages
        URL = 'http://www.job.am/jobs?p=' + str(i)  # url in page
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")

        job_elements = soup.find_all("div", class_="col pl-2 my-auto jobcard-desc")
        for job_element in job_elements:
            title_element = job_element.find("a", class_="text-dark font-weight-bold wordBreak jttl media-size16 scale-link")
            company_element = job_element.find("a", class_="font-weight-bold job-muthed fontSize16 scale-link")
            location_element = job_element.find("span", class_="pl-1 va-middle")
            ls_job.append("Job Title _ " + str(title_element.text.strip()))
            ls_job.append("Company Name _ " + str(company_element.text.strip()))
            ls_job.append("Location _ " + str(location_element.text.strip()))
            url = 'http://www.job.am' + job_element.find("a", class_="text-dark font-weight-bold wordBreak jttl media-size16 scale-link")['href']
            page1 = requests.get(url)

            soup = BeautifulSoup(page1.content, "html.parser")
            job_elements1 = soup.find_all('div', class_="about-container job--descr")
            for job_element1 in job_elements1:
                try:
                    des_text = job_element1.find('p')
                    ls_job.append("Job Description _ " + str(des_text.text.strip()))
                except AttributeError:
                    ls_job.append("This job has not description section")
            ls_job.append("URL to the job posting _ " + str(url))
            ls_job.append("\n")

            with open('job_am.txt', "w", encoding="utf-8") as f:
                for i in ls_job:
                    f.write(i)
                    f.write('\n')


while __name__ == "__main__":
    job_jobs()
    time.sleep(172800)  # will be updated every two days

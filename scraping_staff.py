import requests
from bs4 import BeautifulSoup
import time


def staff_jobs(*jobs):
    ls_job = []
    for i in range(1, 13):  # job posting pages
        URL = 'http://www.staff.am/am/jobs?page=' + str(i) + "&per-page=100"  # url in page
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find(id="search_list_block")
        job_elements = results.find_all("div", class_=jobs)
        for job_element in job_elements:
            title_element = job_element.find("p", class_="font_bold")
            company_element = job_element.find("p", class_="job_list_company_title")
            location_element = job_element.find("p", class_="job_location")
            ls_job.append("* Job Title _ " + str(title_element.text.strip()))
            ls_job.append("* Company Name _ " + str(company_element.text.strip()))
            ls_job.append("* Location _ " + str(location_element.text.strip()))
            url = 'http://www.staff.am' + job_element.find("a", class_="load-more btn width100 job_load_more radius_changes")['href']
            page = requests.get(url)

            soup = BeautifulSoup(page.content, "html.parser")
            results = soup.find(id="job-post")
            job_elements1 = results.find_all("div", class_="job-list-content-desc hs_line_break")
            for job_element1 in job_elements1:
                desciption_element = job_element1.find('p')
                ls_job.append("* Job Description _ " + str(desciption_element.text.strip()))
            ls_job.append("* URL to the job posting _ " + str(url.strip()))
            ls_job.append("\n")

            with open('staff_am.txt', "w", encoding="utf-8") as f:
                for i in ls_job:
                    f.write(i)
                    f.write('\n')


while __name__ == "__main__":
    staff_jobs("right_radius_change hb_list_item clearfix featured-job", "right_radius_change hb_list_item clearfix")
    time.sleep(172800)  # will be updated every two days

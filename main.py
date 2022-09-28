from bs4 import BeautifulSoup
import requests
import csv

# Retrieve top 50 results
url = "https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors"
url2 = "https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/2"

response = requests.get(url)
contents = response.text

response2 = requests.get(url2)
contents2 = response2.text

soup = BeautifulSoup(contents, 'html.parser')
soup2 = BeautifulSoup(contents2, 'html.parser')

html = soup.find_all('span', class_="data-table__value")
html2 = soup2.find_all('span', class_="data-table__value")

# Majors column
majors_html = html[1::6]
majors_html2 = html2[1::6]
majors_html += majors_html2
majors = [item.text for item in majors_html]

# Starting median salary
start_salary_html = html[3::6]
start_salary_html2 = html2[3::6]
start_salary_html += start_salary_html2
start_salary = [int(item.text[1:].replace(',', '')) for item in start_salary_html]

# Mid-career median salary
med_salary_html = html[4::6]
med_salary_html2 = html2[4::6]
med_salary_html += med_salary_html2
med_salary = [int(item.text[1:].replace(',', '')) for item in med_salary_html]

# Create CSV
export_data = zip(majors, start_salary, med_salary)

with open('2021_data.csv', 'x') as file:
    wr = csv.writer(file)
    wr.writerow(("Undergraduate Major", "Starting Median Salary", "Mid-Career Median Salary"))
    wr.writerows(export_data)
# This is a python script to find out exam times without having to search through 100s of exams
# Uses Textwarp for parsing input and bs4 for http request
# Create by Alex Wilson


from textwrap import wrap
from bs4 import BeautifulSoup as bs
import requests
import sys

my_url = "https://www.dal.ca/academics/exam_schedule/halifax_campus_exam_schedule.html"

r = requests.get(my_url)
page = (r.text)
soup = bs(page, 'html.parser')

args = sys.argv
args.pop(0)


faculty = args[0]
faculty = faculty.upper()
args.pop(0)

codes = ""

for arg in args:
    codes += arg
# Separating course numbers
codes =codes.replace(" ", "")
codes = codes.replace(",", "")


counter = 1
codes = wrap(codes, 4)

# Going through html soup to find courses and if found displaying exam times.
date = soup.find_all('h1')

print(date[0].text)
for match in soup.find_all('td', text=faculty):

    courseID = match.find_next_sibling("td")
    if any(code in courseID for code in codes):
        print("Exam " + str(counter) + "\nCourse number:" + match.find_next_sibling("td").text)
        print("Section: " + match.find_next_sibling("td").find_next_sibling("td").text)
        print("Date: " + match.find_next_sibling("td").find_next_sibling("td").find_next_sibling("td").text)
        print(
            "Time: " + match.find_next_sibling("td").find_next_sibling("td").find_next_sibling("td").find_next_sibling(
                "td").text)

        print(
            "Place: " + match.find_next_sibling("td").find_next_sibling("td").find_next_sibling("td").find_next_sibling(
                "td").find_next_sibling("td").text)
        counter = counter + 1


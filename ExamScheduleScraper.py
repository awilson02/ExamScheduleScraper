# This is a python script to find out exam times without having to search through 100s of exams
# Uses Textwarp for parsing input and bs4 for http request
# Create by Alex Wilson


from textwrap import wrap
from bs4 import BeautifulSoup as bs
import requests

my_url = "https://www.dal.ca/academics/exam_schedule/halifax_campus_exam_schedule.html"

r = requests.get(my_url)
page = (r.text)
soup = bs(page, 'html.parser')

print("\n\n\n This scraper can return Dalhousie Halifax exam schedule \n\n\n")

# Getting inputs from user
print('Input faculty 4 letter string')
faculty = input("Enter Faculty: ")
faculty = faculty.upper()

print('\nInput Class codes')
codes = input("Class Codes: ")

# Separating course numbers
codes.replace(" ", "")
codes.replace(",", "")

counter = 1
codes = wrap(codes, 4)

# Going through html soup to find courses and if found displaying exam times.
for match in soup.find_all('td', text=faculty):

    courseID = match.find_next_sibling("td")
    if any(code in courseID for code in codes):
        print("\n\n Exam " + str(counter) + "\n\nCourse number:" + match.find_next_sibling("td").text)
        print("Section: " + match.find_next_sibling("td").find_next_sibling("td").text)
        print("Date: " + match.find_next_sibling("td").find_next_sibling("td").find_next_sibling("td").text)
        print(
            "Time: " + match.find_next_sibling("td").find_next_sibling("td").find_next_sibling("td").find_next_sibling(
                "td").text)
        print(
            "Place: " + match.find_next_sibling("td").find_next_sibling("td").find_next_sibling("td").find_next_sibling(
                "td").find_next_sibling("td").text)
        counter = counter + 1

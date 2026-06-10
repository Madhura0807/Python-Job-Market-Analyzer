import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.python.org/jobs/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

jobs = soup.find_all("h2")

with open("jobs.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(["Job Title"])

    for job in jobs:
        writer.writerow([job.text.strip()])

print("Data saved successfully!")
import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Fetch the page
URL = "https://github.com/trending"
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

# Step 2: Parse top 5 repositories
repos = soup.find_all('article', class_='Box-row')[:5]

# Step 3: Extract repo name and link
data = []
for repo in repos:
    anchor = repo.h2.a
    name = anchor.text.strip().replace('\n', '').replace(' ', '')
    link = f"https://github.com{anchor['href']}"
    data.append([name, link])

# Step 4: Write to CSV
with open('trending_repos.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Repository Name', 'Link'])
    writer.writerows(data)

print("✅ Top 5 trending repositories saved to trending_repos.csv")

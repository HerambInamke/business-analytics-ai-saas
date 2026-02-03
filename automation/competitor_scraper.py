import requests
from bs4 import BeautifulSoup
import csv

urls = {
    "ToolA": "https://example.com",
    "ToolB": "https://example.com"
}

with open("competitor_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Tool", "Title"])
    
    for tool, url in urls.items():
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.title.text if soup.title else "N/A"
        writer.writerow([tool, title])

print("Competitor data scraped successfully.")
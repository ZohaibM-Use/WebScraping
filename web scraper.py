import pandas as pd
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from bs4 import BeautifulSoup

driver_path = "C:/Users/zohai/OneDrive/Documents/Class 37/Mod 3/CIS 403/Week 17/msedgedriver.exe"  # Replace with the actual path

service = Service(driver_path)
driver = webdriver.Edge(service=service)

url = "https://oxylabs.io/blog"
driver.get(url)

results = []
content = driver.page_source
soup = BeautifulSoup(content)
driver.quit()

headings = soup.find_all(['p'])

for heading in headings:
    title = heading.get_text(strip=True)
    if title not in results:
        results.append(title)

df = pd.DataFrame({'All Text': results})
df.to_csv('text.csv', index=False, encoding='utf-8')

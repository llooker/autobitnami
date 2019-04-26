import re
import urllib.request
from bs4 import BeautifulSoup


page = urllib.request.urlopen('https://bitnami.com/stack/lamp/installer')
page_bytes = page.read()

page_html = page_bytes.decode('utf-8')

soup = BeautifulSoup(page_html, 'html.parser')

links = soup.find_all('a', class_='indirect_download_link')

for link in links: 
  target_link = re.match(r'.*bitnami-lampstack-7.2.[0-9]+-[0-9].*-installer.run.*', link['href'])
  if target_link:
    download_link = 'https://bitnami.com' + target_link.group()
    urllib.request.urlretrieve(download_link, download_link.split('/')[-1])

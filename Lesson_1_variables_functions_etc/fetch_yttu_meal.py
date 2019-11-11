# pip install beautifulsoup4
# pip install requests
import requests
from bs4 import BeautifulSoup

ytuyemekurl="http://www.sks.yildiz.edu.tr/"
yemektendonensonuc = requests.get(ytuyemekurl)
soup = BeautifulSoup(yemektendonensonuc.text)

ogleyemeginial = soup.findAll("div", {"class": "one_lunchMainMenu"})
aksamyemeginial = soup.findAll("div", {"class": "one_dinnerMainMenu"})
print("Öğle Yemeği")
print(ogleyemeginial)
print("---------------------------------")
print("Akşam Yemeği:")
print(aksamyemeginial)
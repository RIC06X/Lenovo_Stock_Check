from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
url_p1 = "https://www.lenovo.com/us/en/laptops/thinkpad/thinkpad-p/P1-Gen-2/p/22WS2WPP102"
url_x1 = "https://www.lenovo.com/us/en/laptops/thinkpad/thinkpad-x/X1-Carbon-Gen-7/p/22TP2TXX17G"
url_x1e = "https://www.lenovo.com/us/en/laptops/thinkpad/thinkpad-x/X1-Extreme-Gen-2/p/22TP2TXX1E2"
html = urlopen(url_p1).read().decode('utf=8')
soup = BeautifulSoup(html, features='lxml')
Computer_Name = soup.find('h1',{'class':'desktopHeader', 'itemprop':'name'} or {'class': 'mobileHeader','itemprop':'name'}).string
print(Computer_Name)
items = soup.find_all('li', {'class':'tabbedBrowse-productListing-container only-allow-small-pricingSummary'})
for item in items:
    try:
        partNumber  = re.sub(r'\s*',"",item.find('div', {'class':'partNumber'}).string)
    except:
        partNumber = 'PartNumber:Customize'
    salePrice = item.find('dd',{'class': 'saleprice pricingSummary-details-final-price'}).string
    inStock = 'Unavailable' if item.find('div',{'class': 'rci-esm'}) == None else 'in Stock'
    print(partNumber, salePrice, inStock)
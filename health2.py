import requests
from bs4 import BeautifulSoup

url="http://vizhub.healthdata.org/gbd-compare/api/data?year=1990.1995.2000.2005.2010.2015&chart=top&value=observed&data=cause&metric=2&unit=3&location=6.11.22.36.51.63.67.71.81.97.102.109.123.130.135.141.163.168.180.196.207&age=22&sex=3&cause=294&paf=0&version=142&context=cause&base=single"
req = requests.get(url)
html = req.content
soup = BeautifulSoup(html, 'html.parser')

with open("Causes", "w") as out:
    for result in soup.find_all("tr", "cause_item"):
        year = result.find("td", "cause").contents[0]
        id_number = result["id"].split("-")[2]
        out.write("{} {}\n".format(year, id_number))

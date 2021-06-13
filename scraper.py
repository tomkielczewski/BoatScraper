from bs4 import BeautifulSoup
from urllib.request import urlopen
import time
import pandas as pd

def download_pages(url1, url2, path1, path2):
        for i in range(1,15):
            # url = "https://www.clickandboat.com/pl/czarter-jacht%C3%B3w/szukaj?where=Polska&_nbKm=1000&_tri=Selection&TypeNavigation=With%20or%20without%20captain&LongueurMin=0&LongueurMax=60&PrixJourMin=0&PrixJourMax=1005&ProduitTypeId=Sailboat;&_page="+ str(i) +"&hasDiscount=0"
            url = url1 + str(i) + url2
            page = urlopen(url)
            html = page.read().decode("utf-8")
            soup = BeautifulSoup(html, "html.parser")
            
            # file_name = "clickandboat/clickandboat_polska_zaglowe_" + str(i) + ".html"
            file_name = path1 + str(i) + path2
            with open(file_name, 'w', encoding = 'utf-8') as file:
                file.write(str(soup))
            
            time.sleep(10)

#TODO:
def verify_details(columns):
    for column in columns:
        pass
    
def scrap_data(offer_url):
    dataframe = pd.DataFrame()
    with open(offer_url, 'r', encoding = 'utf-8') as file:

        soup = BeautifulSoup(file, "html.parser")
        boatDetails = soup.find("div", {"class": "boatDetails__list"})
        children = boatDetails.findChildren("div" , recursive=False)
        for child in children:
            # child.string
            print(child.contents[0].strip().replace(':', ''))
            span = child.find("span")
            print(span.contents[0].strip())

        localisation = soup.find(class_='map__text')
        span = localisation.find("span")
        print(span.contents[0].strip())

        equipment = soup.find("div", {"class": "itemsList"})
        children = equipment.find_all("div", {"class": "itemsList__text"})
        equipment = ''
        for child in children:
            equipment = equipment + child.contents[0].strip() + ', '

        print("wyposażenie: " + equipment)
    return dataframe

if __name__ == "__main__":
    df = scrap_data('clickandboat_example_page.html')
    

        # for a in a_elems:
        #     print(a['href'])
        # url = a_elems[0]['href']
        # page = urlopen(url)
        # html = page.read().decode("utf-8")
        # soup = BeautifulSoup(html, "html.parser")
        # file_name = "clickandboat_example_page.html"
        # with open(file_name, 'w', encoding = 'utf-8') as file:
        #     file.write(str(soup))

        



        


    # url = url1 + str(i) + url2
    # page = urlopen(url)
    # html = page.read().decode("utf-8")
    # soup = BeautifulSoup(html, "html.parser")
    # download_pages(
    #     "https://www.clickandboat.com/pl/czarter-jacht%C3%B3w/szukaj?where=Polska&_nbKm=1000&_tri=Selection&TypeNavigation=With%20or%20without%20captain&LongueurMin=0&LongueurMax=60&PrixJourMin=0&PrixJourMax=1005&ProduitTypeId=Sailboat;&_page="
    #     , "&hasDiscount=0"
    #     , "clickandboat/clickandboat_polska_zaglowe_"
    #     ,".html")
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time

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

if __name__ == "__main__":

    with open('clickandboat/clickandboat_example_page.html', 'r', encoding = 'utf-8') as file:

        soup = BeautifulSoup(file, "html.parser")
        a_elems = soup.find_all("div", {"class": "boatDetails__list"})
        # for a in a_elems:
        #     print(a['href'])
        url = a_elems[0]['href']
        page = urlopen(url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        file_name = "clickandboat_example_page.html"
        with open(file_name, 'w', encoding = 'utf-8') as file:
            file.write(str(soup))

        



        


    # url = url1 + str(i) + url2
    # page = urlopen(url)
    # html = page.read().decode("utf-8")
    # soup = BeautifulSoup(html, "html.parser")
    # download_pages(
    #     "https://www.clickandboat.com/pl/czarter-jacht%C3%B3w/szukaj?where=Polska&_nbKm=1000&_tri=Selection&TypeNavigation=With%20or%20without%20captain&LongueurMin=0&LongueurMax=60&PrixJourMin=0&PrixJourMax=1005&ProduitTypeId=Sailboat;&_page="
    #     , "&hasDiscount=0"
    #     , "clickandboat/clickandboat_polska_zaglowe_"
    #     ,".html")
from lxml import html
from time import sleep
import os,json, requests,datetime


def AmazonProducts(url):

    ProductPage = requests.get(url )

    PageInfo = html.fromstring(ProductPage.content)

    XPathProductName = '//h1[@id="title" ]//text()'
    #print(PageInfo.xpath(XPathProductName))
    XPathProductSalePrice = '//span[contains(@id,"ourprice") or contains(@id,"dealprice")]/text()'
    XPathProductPrice = '//td[contains(text(),"List Price") or contains(text(),"price") or contains(text(),"ListPrice") or contains(text(),"M.R.P") or contains(text(),"Price")]/following-sibling::td/text()'

    Name = ' '.join(''.join(PageInfo.xpath(XPathProductName)).split())
    SalePrice  = ' '.join(''.join(PageInfo.xpath(XPathProductSalePrice)).split())
    ProductPrice  = ' '.join(''.join(PageInfo.xpath(XPathProductPrice)).split())

    print(Name)
    print(" URL:               "+ url)
    print(" Current Price:     "+ SalePrice)
    print(" Actual Price:      "+ ProductPrice)

def WatchStationProducts(url):

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

    ProductPage = requests.get(url, headers = headers )

    PageInfo = html.fromstring(ProductPage.content)
    XPathProductName = '//h1[@class="pdpTitle"] //text() '
    XPathProductPrice = '//span[contains(@class,"price") or  contains(@id,"priceOld")]/text()'
    XPathProductSalePrice = '//span[contains(@class,"newPrice")]/text()'

    Name = ' '.join(''.join(PageInfo.xpath(XPathProductName)).split())
    SalePrice  = ' '.join(''.join(PageInfo.xpath(XPathProductSalePrice)).split())
    ProductPrice  = ' '.join(''.join(PageInfo.xpath(XPathProductPrice)).split())

    print(Name)
    print(" URL:               "+ url)
    print("")
    print( ProductPrice )

    if SalePrice != "":
        print("Current Price       " + SalePrice )

while True:
    print("Updated Time:")
    print(datetime.datetime.now())
    print("")

    AmazonBaseurl= "https://www.amazon.ca/dp/"
    ASIN = {'B01ETRGE68','B07KPXGQLQ','B00M77HLII'} #'B07KPXGQLQ'
    ProductNum = 1

    print("Amazon Products")

    for i in ASIN:
        print(ProductNum)
        AmazonProductsURL = AmazonBaseurl + i
        print("")
        AmazonProducts(AmazonProductsURL)
        ProductNum+=1

    WatchURL = {'http://www.watchstation.com/en_US/shop/mens/shop_by_brand/view_all/aix_mens_three_hand_black_stainless_steel_watch-ax2701p.html?parent_category_rn=288124&departmentCategoryId=287583&solrMetaData=Y2FzX2YxN19udGtfY3M6IkFybWFuaSBFeGNoYW5nZSI%3D&N=cas_f17_ntk_cs%3AArmani+Exchange&No=20&Nf=p_min_price%7CBTWN+0+1995&pn=c&rec=2&imagePath=AX2701',
                'http://www.watchstation.com/en_US/shop/mens_sale/shop_mens_sale/view_all_sale/retro-ar1749p.html?parent_category_rn=425585&departmentCategoryId=425086&N=0&pn=c&rec=2&imagePath=AR1749'}

    #https://www.thebay.com/main/ProductDetail.jsp?FOLDER%3C%3Efolder_id=2534374302025903&PRODUCT%3C%3Eprd_id=845524441841782
    print("")
    print("")

    print("Watch Products")
    for i in WatchURL:
        print(ProductNum)
        WatchStationProducts(i)
        ProductNum+=1

    print("")
    print("")
    print("-----------------------------------------------------------------------------")
    sleep(60)

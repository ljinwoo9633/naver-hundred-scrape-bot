from urllib.request import urlopen
from urllib.request import urlretrieve
from urllib.error import HTTPError
from urllib.error import URLError

from PIL import Image

from bs4 import BeautifulSoup

import os
import csv
import time

categoryURLs = {
    'fashion_cloth': 'https://search.shopping.naver.com/best100v2/detail.nhn?catId=50000000',
    'fashion_miscellaneous_goods': 'https://search.shopping.naver.com/best100v2/detail.nhn?catId=50000001',
    'cosmetics': 'https://search.shopping.naver.com/best100v2/detail.nhn?catId=50000002',
    'digital': 'https://search.shopping.naver.com/best100v2/detail.nhn?catId=50000003',
    'furniture': 'https://search.shopping.naver.com/best100v2/detail.nhn?catId=50000004',
    'baby': 'https://search.shopping.naver.com/best100v2/detail.nhn?catId=50000005',
    'sports': 'https://search.shopping.naver.com/best100v2/detail.nhn?catId=50000007',
    'foods': 'https://search.shopping.naver.com/best100v2/detail.nhn?catId=50000006',
    'healty': 'https://search.shopping.naver.com/best100v2/detail.nhn?catId=50000008'
}

downloadDirectory = 'downloaded'

def printProductCategory():
    print('1. fashion_cloth')
    print('2. fashion_miscellaneous_goods')
    print('3. cosmetics')
    print('4. digital')
    print('5. furniture')
    print('6. baby')
    print('7. sports')
    print('8. foods')
    print('9. healty')

    

#다운로드할 경로 설정
def getDownloadPath(number, absoluteUrl, downloadDirectory):
    path = downloadDirectory + '/img/{}.jpg'.format(number)
    directory = os.path.dirname(path)
    
    if not os.path.exists(directory):
        os.makedirs(directory)

    return path

# 카테고리 가지고 오기
def getHundredTitleInNaver(categoryURL):
    try:
        html = urlopen(categoryURL)
    except HTTPError:
        return None
    except URLError:
        return None
    else:
        bs = BeautifulSoup(html, 'html.parser')
        title = bs.find('div', {'class': 'summary_area'}).findAll('a')[1].get_text()
        return title

# 물건 이름 가지고 오기
def getHundredNameInNaver(categoryURL):
    try:
        html = urlopen(categoryURL)
    except HTTPError:
        return None
    except URLError:
        return None
    else:
        product_names = []
        bs = BeautifulSoup(html, 'html.parser')
        name_sections = bs.findAll('p', {'class': 'cont'})
        for name_section in name_sections:
            name = name_section.find('a')['title']
            product_names.append(name)
        return product_names
        
        
# 물건 이미지 가지고 오기
def getHundredImageInNaver(categoryURL):
    try:
        html = urlopen(categoryURL)
    except HTTPError:
        return None
    except URLError:
        return None
    else:
        image_rating = 0
        image_urls = []

        bs = BeautifulSoup(html, 'html.parser')
        thumb_sections = bs.findAll('div', {'class': 'thumb_area'})
        for thumb_section in thumb_sections:
            image_rating = image_rating + 1
            image_url = thumb_section.find('img')['data-original']
            urlretrieve(image_url, getDownloadPath(image_rating, image_url, downloadDirectory))
            image_urls.append(image_url)
        return image_urls

#물건 가격 가지고 오기
def getHundredPriceInNaver(categoryURL):
    try:
        html = urlopen(categoryURL)
    except HTTPError:
        return None
    except URLError:
        return None
    else:
        prices = []
        bs = BeautifulSoup(html, 'html.parser')
        price_sections = bs.findAll('div', {'class': 'price'})
        for price_section in price_sections:
            price = price_section.find('span', {'class': 'num'}).get_text()
            prices.append(price)
        return prices

def getCsvFile(product_names, product_image_urls, product_prices):
    csvFile = open('text.csv', 'w+')
    try:
        writer = csv.writer(csvFile)
        writer.writerow(("이름", "이미지URL", "가격"))
        for i in range(100):
            writer.writerow((product_names[i], product_image_urls[i], product_prices[i]))
    finally:
        csvFile.close()

def resizeImage():
    for i in range(100):
        image = Image.open('./downloaded/img/{}.jpg'.format(i+1))
        resize_image = image.resize((250, 250))
        resize_image.save('./downloaded/img/{}.jpg'.format(i+1))
    

def main(printProductCategory, getHundredNameInNaver, getHundredImageInNaver, getHundredPriceInNaver, getCsvFile, resizeImage):
    while True:
        print("Naver Hundred Bot")
        print('Made By LeeJinwoo')
        printProductCategory()
        print('10. Close This Bot')
        number = int(input('Choose The Number: '))
        if number == 1:
            print('...loading')
            category = categoryURLs['fashion_cloth']
            product_names = getHundredNameInNaver(category)
            product_image_urls = getHundredImageInNaver(category)
            product_prices = getHundredPriceInNaver(category)
            getCsvFile(product_names, product_image_urls, product_prices)
            resizeImage()
            print('[+]Done!')
        elif number == 2:
            print('...loading')
            category = categoryURLs['fashion_miscellaneous_goods']
            product_names = getHundredNameInNaver(category)
            product_image_urls = getHundredImageInNaver(category)
            product_prices = getHundredPriceInNaver(category)
            getCsvFile(product_names, product_image_urls, product_prices)
            resizeImage()
            print('[+]Done!')
        elif number == 3:
            print('...loading')
            category = categoryURLs['cosmetics']
            product_names = getHundredNameInNaver(category)
            product_image_urls = getHundredImageInNaver(category)
            product_prices = getHundredPriceInNaver(category)
            getCsvFile(product_names, product_image_urls, product_prices)
            resizeImage()
            print('[+]Done!')
        elif number == 4:
            print('..loading')
            category = categoryURLs['digital']
            product_names = getHundredNameInNaver(category)
            product_image_urls = getHundredImageInNaver(category)
            product_prices = getHundredPriceInNaver(category)
            getCsvFile(product_names, product_image_urls, product_prices)
            resizeImage()
            print('[+]Done!')
        elif number == 5:
            print('..loading')
            category = categoryURLs['furniture']
            product_names = getHundredNameInNaver(category)
            product_image_urls = getHundredImageInNaver(category)
            product_prices = getHundredPriceInNaver(category)
            getCsvFile(product_names, product_image_urls, product_prices)
            resizeImage()
            print('[+]Done!')
        elif number == 6:
            print('..loading')
            category = categoryURLs['baby']
            product_names = getHundredNameInNaver(category)
            product_image_urls = getHundredImageInNaver(category)
            product_prices = getHundredPriceInNaver(category)
            getCsvFile(product_names, product_image_urls, product_prices)
            resizeImage()
            print('[+]Done!')
        elif number == 7:
            print('..loading')
            category = categoryURLs['sports']
            product_names = getHundredNameInNaver(category)
            product_image_urls = getHundredImageInNaver(category)
            product_prices = getHundredPriceInNaver(category)
            getCsvFile(product_names, product_image_urls, product_prices)
            resizeImage()
            print('[+]Done!')
        elif number == 8:
            print('..loading')
            category = categoryURLs['foods']
            product_names = getHundredNameInNaver(category)
            product_image_urls = getHundredImageInNaver(category)
            product_prices = getHundredPriceInNaver(category)
            getCsvFile(product_names, product_image_urls, product_prices)
            resizeImage()
            print('[+]Done!')
        elif number == 9:
            print('..loading')
            category = categoryURLs['healty']
            product_names = getHundredNameInNaver(category)
            product_image_urls = getHundredImageInNaver(category)
            product_prices = getHundredPriceInNaver(category)
            getCsvFile(product_names, product_image_urls, product_prices)
            resizeImage()
            print('[+]Done!')
        elif number == 10:
            print('Close This Bot...')
            print('[+]Good Bye~')
            return
        else:
            print('[-]Unknown Number Please Try Again!')

        print("-"*50)


main(printProductCategory, getHundredNameInNaver, getHundredImageInNaver, getHundredPriceInNaver, getCsvFile, resizeImage)
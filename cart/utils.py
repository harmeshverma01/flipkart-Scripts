from bs4 import BeautifulSoup
import requests

def product_details(divs, list_of_product):
    for div in divs:
        product_name = div.find('div', {"class" : "_4rR01T"})
        product_rating = div.find('div', {"class": "_3LWZlK"})
        if product_rating:
            product_rating
        else:
            return None    
        product_discription = div.find('div',{"class" : "fMghEO"})
        product_price = div.find('div', {"class":"nlI3QM"})
        
        product = {
            'name' : product_name.text,
            'rating' : product_rating.text,
            'discription' : product_discription.text,
            'price' : product_price.text,
        }
        list_of_product.append(product)
    return list_of_product
        

def html_content(url):
    content = requests.get(url)
    htmlContent = content.content
    soup = BeautifulSoup(htmlContent, 'html5lib')
    return soup


def get_next_page(url):
    soup = html_content(url)
    
    nextpage = soup.find('a', {'class' : '_1LKTO3'})
    if not nextpage.find('span',{'class' : '_22Tduf'}):
        url = 'http://www.flipkart.com' + nextpage.attrs['href'] 
        return (url)
    else:
        return
    

    
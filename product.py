import bs4
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'

#opening up connection, grabbing the page
uClient = ureq(my_url)

#downloads the content into a variable
page_html = uClient.read()

#close connection
uClient.close()

page_soup = soup(page_html, "html.parser")

#grabs each product
containers = page_soup.findAll("div", {"class" : "item-container" })

filename = "product.csv"
f = open(filename, "w")

headers = "brand, product_name, shipping\n"

f.write(headers)

for container in containers:

    count = container.find("div", "item-info")
    brand = count.div.a.img["title"]

    title_container = container.findAll("a", {"class" : "item-title"})
    product_name = title_container[0].text

    shipping_container = container.findAll("li", {"class" : "price-ship"})
    shipping = shipping_container[0].text.strip()


    print("brand: " + brand)
    print("product_name: " + product_name)
    print("shipping: " + shipping)

    f.write(brand + "," + product_name + "," + shipping + "\n")

f.close()
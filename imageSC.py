import requests 
from bs4 import BeautifulSoup
import os



# def imagedown(url, folder): 
    # try: 
    #     os.mkdir(os.path.join(os.getcwd(), folder))
    # except: 
    #     print("in pass")
    #     pass
    # os.chdir(os.path.join(os.getcwd(), folder))


url = 'https://www.pinterest.com/search/pins/?q=muffin&rs=typed'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')


images = soup.find_all("img")

for image in images: 
    name = image['alt']
    link = image['src']
    # if(len(name) < 20): 
    with open(name.replace(' ', '-').replace('/', '') + '.jpg', 'wb') as f:
        im = requests.get(link)
        f.write(im.content)
        print('Writing ', name)

# imagedown('https://www.pinterest.com/search/pins/?q=muffin&rs=typed', 'trying1')
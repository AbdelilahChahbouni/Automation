import requests
import shutil
from bs4 import BeautifulSoup
url = input("Enter The An Image Url : ")
image_name = input("Save Image with Name : ")



def get_html_content(url):
    response = requests.get(url)
    return response.text

html_string = get_html_content(url)



def get_attribute_content(html_string, element, attribute):
    soup = BeautifulSoup(html_string, 'html.parser')
    elements = soup.find_all(element)
    attribute_content = []

    for elem in elements:
        if attribute in elem.attrs:
            attribute_content.append(elem[attribute])

    return attribute_content


element = 'img'
attribute = 'src'
content = get_attribute_content(html_string, element, attribute)
for new_url in content:
    req = requests.get(url , stream = True)
    print(new_url)
    if req.status_code == 200 and new_url.startswith("http") == True:
        with open(image_name , "wb") as f:
            shutil.copyfileobj(req.raw , f)
        print("Image Downloaded .." , image_name)

    else:
        print("Image could not downloaded ..")





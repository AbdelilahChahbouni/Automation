from bs4 import BeautifulSoup

import requests

def get_html_content(url):
    response = requests.get(url)
    return response.text

# Example usage
url = input("enter url : ")
html_string = get_html_content(url)
#print(html_content)



def get_attribute_content(html_string, element, attribute):
    soup = BeautifulSoup(html_string, 'html.parser')
    elements = soup.find_all(element)
    attribute_content = []

    for elem in elements:
        if attribute in elem.attrs:
            attribute_content.append(elem[attribute])

    return attribute_content

# Example usage

element = 'img'
attribute = 'src'
#html_string = input("enter the url image")
content = get_attribute_content(html_string, element, attribute)
#print(content)
for x in content:
    print(x)






import requests
from bs4 import BeautifulSoup
import json


def get_html():
    url = 'https://www.google.com'
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    title = soup.select_one('title').text
    body = soup.select_one('body').text
    script = soup.select_one('script').text

    data = {
        'title': title,
        'body': body,
        'script': script,
    }

    with open('jsons/data.json', 'w') as f:
        json.dump(data, f)


if __name__ == '__main__':
    get_html()

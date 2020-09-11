import requests
import parsel
import time


src_html = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Document</title>

</head>
<body>
    {content}
</body>
</html>
'''
headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
}


def download_one_page(page_url):
    response = requests.get(url=page_url, headers=headers)
    html = response.text
    print("open url:" + str(page_url))


def down_all_url(index_url):
    index_response = requests.get(url=index_url,headers=headers)
    index_selector = parsel.Selector(index_response.text)
    urls = index_selector.css('.article-list h4 a::attr(href)').getall()
    for url in urls:
        download_one_page(url)
        time.sleep(5)


if __name__ == '__main__':
    while True:
        time.sleep(2)
        for index in [1, 2, 3]:
            url = 'https://blog.csdn.net/weixin_36628778/article/list/' + str(index)
            down_all_url(url)

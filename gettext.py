from bs4 import BeautifulSoup
import urllib.request


# version: Python 3.5
# 需要安装BeautifulSoup、html5lib第三方库
def gettext(url):
    res = urllib.request.urlopen(url).read()
    data = res.decode()
    soup = BeautifulSoup(data, "html5lib")  # 将html代码用Bs进行处理
    author = soup.select(".fb")[0].text  # 获取class为fb第一个元素的text
    print("作者：" + author)
    title = soup.select("h1")[0].text
    print("书名：" + title)
    author = soup.find("a", {"class": "fb"}).get_text()
    print("作者:"+author)
    title = soup.find("h1").get_text()
    print("书名:"+title)


if __name__ == "__main__":
    url = "http://book.zongheng.com/showchapter/342974.html"
    gettext(url)

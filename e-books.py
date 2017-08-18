from bs4 import BeautifulSoup
import urllib.request


# author: MGZ
# version: Python 3.5
# 需要安装BeautifulSoup、html5lib第三方库
def taonvlang(url):
    res = urllib.request.urlopen(url).read()
    data = res.decode()
    soup = BeautifulSoup(data, "html5lib")  # 将html代码用Bs进行处理
    author = soup.find("a", {"class": "fb"}).get_text()
    print("作者:" + author)
    title = soup.find("h1").get_text()
    print("书名:" + title)
    for list in soup.find_all("div", {"class": "booklist tomeBean"}):
        dict = list.attrs
        tomeid = dict['tomeid']
        tomename = dict['tomename']
        print("卷Id:" + tomeid)
        print("卷名:" + tomename)
        for children in list.find_all("td", {"class": "chapterBean"}):
            chapter = children.attrs
            chapterurl = "http://book.zongheng.com/chapter/342974/" + chapter['chapterid'] + ".html"
            chaptername = chapter['chaptername']
            print("章节名:" + chaptername)
            print("url:" + chapterurl)


if __name__ == "__main__":
    url = "http://book.zongheng.com/showchapter/342974.html"
    taonvlang(url)

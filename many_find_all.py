from bs4 import BeautifulSoup
import urllib.request


# version: Python 3.5
# 需要安装BeautifulSoup、html5lib第三方库
def many_find_all(url):
    res = urllib.request.urlopen(url).read()
    data = res.decode()
    soup = BeautifulSoup(data, "html5lib")  # 将html代码用Bs进行处理
    # 分析网页找到正确的元素
    for list in soup.find_all("div", {"class": "booklist tomeBean"}):  # 获取class为booklist tomeBean的div
        dict = list.attrs  # 转换成字典
        tomeid = dict['tomeid']  # 取得卷名id利于将相同卷的小说分组
        tomename = dict['tomename']  # 取得卷名
        print("卷Id:" + tomeid)
        print("卷名:" + tomename)
        # 将div再次遍历获得所有的章节（这里选择的是class为chapterBean的td)
        # 也可以选择遍历出所有的a标签，但是a标签转换成字典时会丢失text
        # url可以拼接，也可以直接再次find_all获得a标签的href获得
        for children in list.find_all("td", {"class": "chapterBean"}):
            chapter = children.attrs  # 将转换成字典更方便获取值
            # chapterurl = "http://book.zongheng.com/chapter/342974/" + chapter['chapterid'] + ".html"
            chaptername = chapter['chaptername']
            print("章节名:" + chaptername)
            # print("url:" + chapterurl)
            for childa in children.find_all("a"):
                print("url:" + childa.attrs["href"])


if __name__ == "__main__":
    url = "http://book.zongheng.com/showchapter/342974.html"
    many_find_all(url)

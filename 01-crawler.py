from bs4 import BeautifulSoup as bs
import requests
import json

START_URL = "https://movie.douban.com/subject/26363254/comments"
HEADERS = {
'Accept-Encoding':'gzip, deflate, sdch, br',
'Accept-Language':'en-US,en;q=0.8',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Referer':'https://www.douban.com/accounts/login?source=movie',
'Cookie':'',
'Connection':'keep-alive Cache-Control: max-age=0'
}

def find_next(dom):
    next_button = dom.find('a', {'class': 'next'})
    if next_button:
        href = next_button.attrs['href']
        return START_URL + href
    else:
        return

def parse_comment(comment):
    cid = comment.attrs['data-cid']
    vote = comment.find('span', {'class': 'votes'}).text
    star = comment.find('span', {'class': 'rating'})
    star = star.attrs['title'] if star else "未评分"
    content = comment.find('p').text
    return {
        "comment": content,
        "vote": vote,
        "star": star,
        "cid": cid
    }

def parse_comments(dom):
    comments = dom.find_all('div', {'class': 'comment-item'})
    return [parse_comment(comment) for comment in comments]


def crawler(url, n=0):
    req = requests.get(url, headers=HEADERS)
    print("Crawling {}".format(url))
    if req.status_code == 200:
        dom = bs(req.text, 'lxml')
        next_button = find_next(dom)
        comments = parse_comments(dom)
        with open("result/comment_{}.json".format(n), 'w') as fp:
            fp.write(json.dumps(comments, ensure_ascii=False, indent=4))
        n = n + 1
        if next_button:
            crawler(next_button, n)
    else:
        print("Fail")

if __name__ == "__main__":
    print(crawler(START_URL))

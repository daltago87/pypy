'''
thread.py
2018/02/07
by daltago87
'''

#threading 모듈을 사용
#1. 쓰레드가 실행할 함수 혹은 메서드를 작성  또는 2.threading.Thread 로부터 파생된 파생클래스를 작성

import threading, requests, time
 
def getHtml(url):
    resp = requests.get(url)
    time.sleep(1)
    print(url, len(resp.text), ' chars')
 
t1 = threading.Thread(target=getHtml, args=('http://google.com',))
t1.start()
 
print("### End ###")

 
class HtmlGetter (threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self) 
        self.url = url
 
    def run(self):
        resp = requests.get(self.url)
        time.sleep(1)
        print(self.url, len(resp.text), ' chars')
 
t = HtmlGetter('http://google.com')
t.start()
 
print("### End ###")
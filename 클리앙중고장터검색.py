# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

for n in range(1,10):
        #클리앙의 중고장터 주소 
        # data ='https://www.clien.net/service/board/sold?&od=T31&po=' + str(n)
        data ='https://www.inven.co.kr/board/lostark/4821?p=' + str(n)
        print(data)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)
        data = urllib.request.urlopen(req).read()
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')
        list = soup.findAll('a', attrs={'class':'subject-link'})

        # <div class="text-wrap">
        #                         <div>
        #                                 <span class="user-icon"><img src="https://upload2.inven.co.kr/upload/2015/07/27/icon/i13598720059.jpg" alt="유저 아이콘" loading="lazy"></span>                                <a class="subject-link" href="https://www.inven.co.kr/board/lostark/4821/94974?p=2">
        #                                 <span class="category">[일반]</span>
        #                                                                                                         1415 시작하는 모코코분들을 위한 tip                                </a>
        #                         </div>
        #                         <span data-opinion-bbs-comeidx="4821" data-opinion-bbs-uid="94974" data-opinion-bbs-opi="35" class="con-comment">[35]</span>                                                        <span class="con-icon board-img photo">사진</span>                                                                                                            </div>

        for item in list:
                try:
                        title = item.text.strip()
                        print(title)
                        # if (re.search('아이폰', title)):
                        #         print(title.strip())
                        #         print('https://www.clien.net'  + item['href'])
                except:
                        pass
        

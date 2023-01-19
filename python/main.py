# pip install bs4
# pip install schedule
# pip install python-telegram-bot
# pip install telegram
# pip install asyncio
####################

##############################################
#################  Module  ###################
from urllib.request import Request,urlopen  ##
from bs4 import BeautifulSoup               ##
import schedule,time,telegram               ##
import asyncio                              ##
##############################################
##########################################################
#####################  News_Bot  #########################

# Send News
async def send_news(txt):
    Bot_token = "Bot_token"  ##### BOT API
    id = "id"           ##### BOT API
    News_bot = telegram.Bot(token=Bot_token) # HTTP token

    try:
        await News_bot.sendMessage(chat_id=id,text=txt)
    except :
        time.sleep(2)
        await News_bot.sendMessage(chat_id=id,text=txt)

# Stock News 
def send_stock_news():
    # Crawling url, html
    url = Request("https://finance.naver.com/news/",headers={'User-Agent':'Mozilla/5.0'})
    html = urlopen(url)
    soup = BeautifulSoup(html,'html.parser',from_encoding='cp949')
    temp = "https://finance.naver.com"
    s = " ==== P가장 많이 본 주식 관련 뉴스 ==== \n\n"
    for href in soup.find("ul", class_="right_list_1_2").find_all("li"):
        try :
            s += ('[' + href.find("a")["title"] + ']' + '\n') + (temp + href.find("a")["href"]) + '\n\n'
        except TypeError:
            pass
    s += "====== 주식 관련 기사 확인!!!! ======"
    asyncio.run(send_news(s))


# Coin News
def send_coin_news():
    # Crawling url, html
    url = Request("https://www.coinreaders.com/",headers={'User-Agent':'Mozilla/5.0'})
    html = urlopen(url)
    soup = BeautifulSoup(html,'html.parser')
    temp = "https://www.coinreaders.com/"
    s = " ==== 가장 많이 본 코인 관련 뉴스 ==== \n\n"
    for href in soup.find("div", class_="list_area").find_all("a"):
        try :
            s += ('[' + href.text + ' ] \n' + temp + href["href"] + '\n\n' )
        except TypeError:
            pass
    s += "====== 코인 관련 기사 확인!!!! ======"
    asyncio.run(send_news(s))


"""
# 10초에 한번씩 실행
schedule.every(10).second.do(send_news)
# 10분에 한번씩 실행
schedule.every(10).minutes.do(send_news)
# 매 시간 실행
schedule.every().hour.do(send_news)
# 매일 10:30 에 실행
schedule.every().day.at("10:30").do(send_news)
# 매주 월요일 실행
schedule.every().monday.do(send_news)
# 매주 수요일 13:15 에 실행
schedule.every().wednesday.at("13:15").do(send_news)
"""
send_stock_news()
send_coin_news()

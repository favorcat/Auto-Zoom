from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()

prefs = {
    'protocol_handler.excluded_schemes': {
        'zoommtg': False
    }
}
chrome_options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(r'/Applications/chromedriver', options=chrome_options)


# 회의에 암호가 걸려있을 경우 &pwd=암호 를 입력해준다.
driver.get('zoommtg://zoom.us/join?confno=회의ID&pwd=비밀번호')

# 로그
print(datetime.today().strftime("%Y.%m.%d %H:%M:%S"))
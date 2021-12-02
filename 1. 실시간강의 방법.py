import time
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

# 강의동 로그인 페이지
driver.get('https://lms.sunmoon.ac.kr/ilos/main/member/login_form.acl')
driver.find_element_by_name('usr_id').send_keys('아이디')
driver.find_element_by_name('usr_pwd').send_keys('비밀번호')
driver.find_element_by_xpath('//*[@id="myform"]/div/div/div/fieldset/input[3]').click()
time.sleep(1)

# 강의실 들어가기 css selector 이용
driver.find_element_by_css_selector('.sub_open[title="과목명 강의실 들어가기"]').click()

# 실시간 강의 페이지 들어가기
driver.find_element_by_xpath('//*[@id="menu_zoom"]').click()

# 현재 날짜 및 시간 확인
today = datetime.today().strftime("%Y.%m.%d")
time = datetime.today().strftime("%I")

# 해당 실시간 강의 페이지에서 링크 가져오는 함수
def zoom():
    pwd = (driver.find_element_by_xpath('//*[@id="content_text"]/table/tbody/tr[6]/td').text)
    confno = (driver.find_element_by_xpath('//*[@id="content_text"]/table/tbody/tr[5]/td').text)
    link = 'zoommtg://zoom.us/join?confno='+ confno + '&pwd=' + pwd
    driver.get(link)

print('=============result============')

# 해당 수업을 찾는 반복문
rows = driver.find_elements_by_css_selector('tr')
for tr in rows:
    data = tr.find_elements_by_css_selector('td.center.number')
    for value in data:
        if value.text[:10] == today :
            # 10시 ~ 12시인 경우
            if time[0] != '0' :
                if value.text[14:16] == time:
                    td = tr.find_elements_by_css_selector('td[onclick]')
                    td[0].click()
                    zoom()
                    break
            # 오전 9시 or 오후 1시 ~ 인 경우
            else:
                if value.text[14:15] == time[1] :
                    td = tr.find_elements_by_css_selector('td[onclick]')
                    td[0].click()
                    zoom()
                    break

# 로그
print(datetime.today().strftime("%Y.%m.%d %H:%M:%S"))
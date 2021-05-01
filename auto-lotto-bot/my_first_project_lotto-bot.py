# 셀레니움 까는데도 오래걸림... pip3 install selenium 으로 설치함.
from selenium import webdriver
# 셀레늄에서 셀렉트 불러오기
from selenium.webdriver.support.select import Select


# ID, PW 입력
ID = 'weston0713'
PW = 'q1w2e3r4!@#'

# 웹드라이버는 설치하면 땡이 아니고 폴더안에 넣어주고 매번 실행하는거더라,, 몰랐음.
DRIVER_PATH = '/Users/heechankang/projects/pythonworkspace/auto-lotto-bot/chromedriver' # 크롬드라이버 위치 지정
driver = webdriver.Chrome(executable_path=DRIVER_PATH) # DRIVER_PATH에 있는 크롬드라이버를 켜라는건가?

# 동행복권 로그인 창 접속
LOTTO_URL = 'https://dhlottery.co.kr/user.do?method=login&returnUrl=' # 크롬드라이버로 열 사이트 지정
driver.get(LOTTO_URL) #이걸로 드라이버를 통해 LOTTO_URL을 열라는 뜻인듯.

# 동행복권 아이디 입력
elem_login = driver.find_element_by_id('userId')
elem_login.send_keys(ID)

# 동행복권 비밀번호 입력
elem_login = driver.find_element_by_name('password')
elem_login.clear()
elem_login.send_keys(PW)

# 로그인 버튼 클릭
LOGIN_XPATH = '//*[@id="article"]/div[2]/div/form/div/div[1]/fieldset/div[1]/a'
driver.find_element_by_xpath(LOGIN_XPATH).click()

# 로또 구매창 이동
BUY_LOTTO_URL = 'https://el.dhlottery.co.kr/game/TotalGame.jsp?LottoId=LO40'
driver.get(BUY_LOTTO_URL)

# 자동번호발급 버튼 클릭
driver.switch_to_frame('ifrm_tab')
driver.find_element_by_xpath('//*[@id="num2"]').click()

# 로또 구매 개수 선택
select = Select(driver.find_element_by_xpath('//*[@id="amoundApply"]'))
select.select_by_value('5')

# 확인 버튼 누르기
BTN_XPATH = '//*[@id="btnSelectNum"]'
driver.find_element_by_xpath(BTN_XPATH).click()

# 구매하기 버튼 누르기
BUY_BTN_XPATH = '//*[@id="btnBuy"]'
driver.find_element_by_xpath(BUY_BTN_XPATH).click()

# 확인 버튼
alert = driver.switch_to.alert
alert.accept()

# 크롬 브라우저 종료
driver.close()
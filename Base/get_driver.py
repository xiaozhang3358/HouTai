from selenium import webdriver


def get_driver():
    #     创建浏览器驱动对象并返回
    driver = webdriver.Chrome()
    #     窗口最大化
    driver.maximize_window()
    #     设置隐式等待时间
    driver.implicitly_wait(30)
    #     获取url
    driver.get('http://192.168.3.110:8080/P2P/a')
    return driver
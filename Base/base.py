from time import sleep

from selenium import webdriver

import Page


class Base():
    # 初始化方法
    def __init__(self, driver):
        self.driver = driver

    # 查找元素方法封装
    def base_find_element(self, loc):
        return self.driver.find_element(*loc)

    # 获取一组元素方法封装
    def base_find_elements(self, loc):
        return self.driver.find_elements(*loc)

    # 输入框方法封装
    def base_input_text(self, loc, input_value):
        el = self.base_find_element(loc)
        # 清空内容
        el.clear()
        # 输入内容
        el.send_keys(input_value)

    #   点击方法封装
    def base_click_btn(self, loc):
        self.base_find_element(loc).click()

    #   切换表单方法封装
    def base_frame(self, frame_name):
        self.driver.switch_to.frame(frame_name)

    # 切换表单之后返回
    def base_frame_back(self):
        self.driver.switch_to.default_content()

    # 滚动条滚动到最底部、
    def base_scroll_bar_di(self):
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)

    # 滚动条滚动到最顶部
    def base_scroll_bar_ding(self):
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    # 选择时间日期方法封装
    def base_date(self):
        # 创建时间
        # 开始查询时间
        self.driver.find_element_by_css_selector('#startTime').click()
        self.driver.switch_to.default_content()
        # 切换表单
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('html/body/div[2]/iframe'))
        # 选择时间
        self.driver.find_element_by_xpath('html/body/div[1]/div[3]/table/tbody/tr[2]/td[5]').click()
        # 选择时间(今天）
        # self.driver.find_element_by_css_selector('#dpTodayInput').click()
        # 点击确定
        self.driver.find_element_by_css_selector('#dpOkInput').click()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('mainFrame')
        # 点击结束查询时间
        self.driver.find_element_by_css_selector('#endTime').click()
        self.driver.switch_to.default_content()
        # 切换表单
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/div[2]/iframe'))
        # 选择时间
        self.driver.find_element_by_css_selector('#dpTodayInput').click()
        # 点击确定
        # self.driver.find_element_by_css_selector('#dpOkInput').click()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('mainFrame')

    # 切换表单点击之后在切换表单方法封装
    def base_iframe(self, loc1, loc2):
        # 返回主页
        self.base_frame_back()
        # 先切换
        self.base_frame(Page.menuframe)
        # 点击
        self.base_click_btn(loc1)
        sleep(1)
        # 再次点击
        self.base_click_btn(loc2)
        # 返回主页
        self.base_frame_back()
        # 再次切换表单
        self.base_frame(Page.mainframe)

    def base_aframe(self, loc):
        # 返回主页
        self.base_frame_back()
        # 先切换
        self.base_frame(Page.menuframe)
        # 点击
        self.base_click_btn(loc)
        # 返回主页
        self.base_frame_back()
        # 再次切换表单
        self.base_frame(Page.mainframe)

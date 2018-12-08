import Page
from Base.base import Base


class PageLogin(Base):
    # 输入用户名
    def page_login_username(self,username):
        self.base_input_text(Page.username,username)

    # 输入密码
    def page_login_pwd(self,pwd):
        self.base_input_text(Page.pwd,pwd)

    # 点击登录
    def page_login_btn(self):
        self.base_click_btn(Page.login_btn)

    # 封装登录方法
    def page_login(self):
        self.page_login_username('admini')
        self.page_login_pwd('admin')
        self.page_login_btn()
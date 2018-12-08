from Base.get_driver import get_driver
from Page.caiwuguanli import PageCaiWu
from Page.dianxiaozhongxin import PageDianxiao
from Page.dingdanzhongxin import PageDingDan
from Page.fengkongzhongxin import PageFengKong
from Page.login import PageLogin
from Page.shujukanban import PageShuJu
from Page.xitongshezhi import PageXiTong
from Page.yunyingguanli import PageYunYing
from Page.zhaiwuguanli import PageZhaiWu


class PageIn():
    def __init__(self):
        self.driver = get_driver()

    # 登录页面对象
    def page_get_login(self):
        return PageLogin(self.driver)

    # 获取电销中心页面对象
    def page_get_dianxiao(self):
        return PageDianxiao(self.driver)

    # 获取订单中心页面对象
    def page_get_dingdan(self):
        return PageDingDan(self.driver)

    # 获取风控中心页面对象
    def page_get_fengkong(self):
        return PageFengKong(self.driver)

    # 获取债务管理页面对象
    def page_get_zhaiwu(self):
        return PageZhaiWu(self.driver)

    # 获取数据看板页面对象
    def page_get_shuju(self):
        return PageShuJu(self.driver)

    # 获取运营管理页面对象
    def page_get_yunying(self):
        return PageYunYing(self.driver)

    # 获取财务管理页面对象
    def page_get_caiwu(self):
        return PageCaiWu(self.driver)

    # 获取系统设置页面对象
    def page_get_xitong(self):
        return PageXiTong(self.driver)

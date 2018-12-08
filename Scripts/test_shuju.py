import sys, os

sys.path.append(os.getcwd())
import pytest

from Base.read_yaml import ReadYAML
from Page.page_in import PageIn


# 读取参数函数封装
def get_data():
    # 定义一个空列表
    arrs = []
    for data in ReadYAML('shuju_data.yaml').read_yaml().values():
        arrs.append((data.get('phone')))
    return arrs


class TestShuJu():
    def setup_class(self):
        # 统一化入口类
        self.page = PageIn()
        # 调用封装的登录方法
        self.page.page_get_login().page_login()
        # 实例化债务管理页面对象
        self.shuju = self.page.page_get_shuju()

    def teardown_class(self):
        # 关闭浏览器驱动对象
        self.shuju.driver.quit()

    # 点击数据看板
    @pytest.mark.parametrize('phone', get_data())
    def test_shuju_kb(self,phone):
        # 点击财务总量统计
        self.shuju.page_click_cwzltj()
        # 点击贷后统计
        self.shuju.page_click_dhtj()
        # 点击注册用户统计
        self.shuju.page_click_zcyhtj(phone)
        # 点击统计报表
        self.shuju.page_click_tjbb()
        # 点击业务数据统计
        self.shuju.page_click_ywsjtj()
        # 点击渠道统计
        self.shuju.page_click_qdtj()
        # 点击催收统计
        self.shuju.page_click_cstj()
        # 点击电销统计
        self.shuju.page_click_dxtj()

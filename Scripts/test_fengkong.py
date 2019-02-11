import sys, os

sys.path.append(os.getcwd())
import pytest

from Base.read_yaml import ReadYAML
from Page.page_in import PageIn


# 读取参数函数封装
def get_data():
    # 定义一个空列表
    arrs = []
    for data in ReadYAML('fengkong_data.yaml').read_yaml().values():
        arrs.append(
            (data.get('fk_zh_fysx'), data.get('fk_hmd_nr'), data.get('fk_hmdk_tj_day'), data.get('fk_hmdk_tj_nrxx'), data.get('fk_hmdk_tj_lhyy'),
             data.get('fk_kh_phone')))
    return arrs


class TestFengKong():
    def setup_class(self):
        # 实例化统一入口类
        self.page = PageIn()
        # 调用封装的登录方法
        self.page.page_get_login().page_login()
        # 实例化风控中心页面对象
        self.fengkong = self.page.page_get_fengkong()

    def teardown_class(self):
        # 关闭浏览器驱动对象
        self.fengkong.driver.quit()

    # 点击风控中心
    @pytest.mark.parametrize('fk_zh_fysx,fk_hmd_nr,fk_hmdk_tj_day,fk_hmdk_tj_nrxx, fk_hmdk_tj_lhyy, fk_kh_phone', get_data())
    def test_fengkong_fkjcgl(self, fk_zh_fysx, fk_hmd_nr, fk_hmdk_tj_day, fk_hmdk_tj_nrxx, fk_hmdk_tj_lhyy, fk_kh_phone):
        # 点击风控决策管理
        self.fengkong.page_click_fhjc()
        # 点击接口管理
        self.fengkong.page_click_jkgl()
        # 点击账户管理
        self.fengkong.page_click_zhgl(fk_zh_fysx)
        # 点击调用日志管理
        # 点击黑名单管理
        self.fengkong.page_click_hmdgl(fk_hmd_nr, fk_hmdk_tj_day, fk_hmdk_tj_nrxx, fk_hmdk_tj_lhyy)
        # 点击客户管理
        self.fengkong.page_click_khgl(fk_kh_phone)

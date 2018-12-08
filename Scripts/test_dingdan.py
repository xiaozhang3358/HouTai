import sys, os
sys.path.append(os.getcwd())

from Base.read_yaml import ReadYAML
import pytest
from Page.page_in import PageIn


# 读取参数函数封装
def get_data():
    # 定义一个空列表
    arrs = []
    for data in ReadYAML('dingdan_data.yaml').read_yaml().values():
        arrs.append((data.get('ddlb_ddbh'), data.get('ddlb_name'), data.get('ddlb_phone'), data.get('ddlb_khly'),
                     data.get('ddsh_ddbh'), data.get('ddsh_name'), data.get('ddsh_phone'), data.get('zgsh_ddbh'),
                     data.get('zgsh_name'), data.get('zgsh_phone'), data.get('dqy_ddbh'), data.get('dqy_name'),
                     data.get('dqy_phone')))
    return arrs


class TestDingDan():
    def setup_class(self):
        # 实例化统一入口类
        self.page = PageIn()
        # 调用封装的登录方法
        self.page.page_get_login().page_login()
        # 实例化订单中心页面对象
        self.dingdan = self.page.page_get_dingdan()

    def teardown_class(self):
        # 关闭浏览器驱动对象
        self.dingdan.driver.quit()

    # 订单中心
    @pytest.mark.parametrize('ddlb_ddbh,ddlb_name,ddlb_phone,ddlb_khly,ddsh_ddbh,ddsh_name,ddsh_phone,zgsh_ddbh,zgsh_name,zgsh_phone,dqy_ddbh,dqy_name,dqy_phone',get_data())
    def test_dingdan_ddsh(self,ddlb_ddbh,ddlb_name,ddlb_phone,ddlb_khly,ddsh_ddbh,ddsh_name,ddsh_phone,zgsh_ddbh,zgsh_name,zgsh_phone,dqy_ddbh,dqy_name,dqy_phone):
        # 点击订单列表
        self.dingdan.page_click_ddlb(ddlb_ddbh,ddlb_name,ddlb_phone,ddlb_khly)
        # 点击订单审核
        self.dingdan.page_click_ddsh(ddsh_ddbh,ddsh_name,ddsh_phone)
        # 点击主管审核
        self.dingdan.page_click_zgsh(zgsh_ddbh,zgsh_name,zgsh_phone)
        # 点击待签约客户
        self.dingdan.page_click_dd_dqy(dqy_ddbh,dqy_name,dqy_phone)
        # 点击订单管理
        self.dingdan.page_click_ddgl()

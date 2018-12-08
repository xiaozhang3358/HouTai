import sys, os

sys.path.append(os.getcwd())
from Page.page_in import PageIn
from Base.read_yaml import ReadYAML
import pytest


# 读取参数函数封装
def get_data():
    # 定义一个空列表
    arrs = []
    for data in ReadYAML('dianxiao_data.yaml').read_yaml().values():
        arrs.append((data.get('khdr_pch'), data.get('khdr_czy'), data.get('khdr_phone'), data.get('khgl_dxy'),
                     data.get('khgl_bfcs'), data.get('khgl_drly'), data.get('khgl_zcly'), data.get('dqy_name'),
                     data.get('dqy_phone'), data.get('sq_name'), data.get('sq_phone'), data.get('sq_bfcs'),
                     data.get('sq_drly'), data.get('sq_zcly'), data.get('lkh_name'), data.get('lkh_phone'),
                     data.get('lkh_day'), data.get('yx_name'), data.get('yx_phone'), data.get('yx_czy')))
    return arrs


class TestDiaoxiao():
    def setup_class(self):
        # 实例化统一入口类
        self.page = PageIn()
        # 调用封装的登录方法
        self.page.page_get_login().page_login()
        # 实例化电销中心页面对象
        self.dianxiao = self.page.page_get_dianxiao()

    def teardown_class(self):
        # 关闭浏览器驱动对象
        self.dianxiao.driver.quit()

    # 客户导入
    @pytest.mark.parametrize(
        'khdr_pch, khdr_czy, khdr_phone, khgl_dxy, khgl_bfcs, khgl_drly, khgl_zcly, dqy_name, dqy_phone, sq_name, sq_phone,sq_bfcs, sq_drly, sq_zcly, lkh_name, lkh_phone, lkh_day, yx_name, yx_phone,yx_czy',
        get_data())
    def test_dianxiao_khdr(self, khdr_pch, khdr_czy, khdr_phone, khgl_dxy, khgl_bfcs, khgl_drly, khgl_zcly, dqy_name,
                           dqy_phone, sq_name, sq_phone,
                           sq_bfcs, sq_drly, sq_zcly, lkh_name, lkh_phone, lkh_day, yx_name, yx_phone,
                           yx_czy):
        # 点击客户导入
        self.dianxiao.page_click_khdr(khdr_pch, khdr_czy, khdr_phone)
        # 点击客户管理
        self.dianxiao.page_click_khgl(khgl_dxy, khgl_bfcs, khgl_drly, khgl_zcly)
        # 点击待签约客户
        self.dianxiao.page_click_dqy(dqy_name, dqy_phone)
        # 点击售前营销
        self.dianxiao.page_click_sqyx(sq_name, sq_phone, sq_bfcs, sq_drly, sq_zcly)
        # 点击老客户唤醒营销
        self.dianxiao.page_click_lkh(lkh_name, lkh_phone, lkh_day)
        # 点击营销记录
        self.dianxiao.page_click_yxjl(yx_name, yx_phone, yx_czy)

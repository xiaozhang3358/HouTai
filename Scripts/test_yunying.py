import sys, os

sys.path.append(os.getcwd())
import pytest

from Base.read_yaml import ReadYAML
from Page.page_in import PageIn


# 读取参数函数封装
def get_data():
    # 定义一个空列表
    arrs = []
    for data in ReadYAML('yunying_data.yaml').read_yaml().values():
        arrs.append((data.get('yy_qdgl_tg_mc'), data.get('yy_qdgl_tg_phone'), data.get('yy_qdgl_qdzc_phone'),
                     data.get('yy_qdgl_zcyh_name'), data.get('yy_qdgl_zcyh_phone'), data.get('yy_qdgl_zcyh_tjqd'),
                     data.get('yy_qdgl_zcyh_num'), data.get('yy_yhgl_zcyh_name'), data.get('yy_yhgl_zcyh_phone'),
                     data.get('yy_yhgl_zcyh_tjr_phone'), data.get('yy_yhgl_zcyh_tjr_name'), data.get('yy_dcgl_pt_mc'),
                     data.get('yy_dcgl_pt_ip')))
    return arrs


class TestYunYing():
    def setup_class(self):
        # 统一化入口类
        self.page = PageIn()
        # 调用封装的登录方法
        self.page.page_get_login().page_login()
        # 实例化债务管理页面对象
        self.yunying = self.page.page_get_yunying()

    def teardown_class(self):
        # 关闭浏览器驱动对象
        self.yunying.driver.quit()

    # 点击运营管理
    @pytest.mark.parametrize(
        'yy_qdgl_tg_mc, yy_qdgl_tg_phone, yy_qdgl_qdzc_phone, yy_qdgl_zcyh_name,yy_qdgl_zcyh_phone, yy_qdgl_zcyh_tjqd,'
        'yy_qdgl_zcyh_num,yy_yhgl_zcyh_name, yy_yhgl_zcyh_phone, yy_yhgl_zcyh_tjr_phone, yy_yhgl_zcyh_tjr_name,'
        'yy_dcgl_pt_mc, yy_dcgl_pt_ip', get_data())
    def test_yunying_gl(self, yy_qdgl_tg_mc, yy_qdgl_tg_phone, yy_qdgl_qdzc_phone, yy_qdgl_zcyh_name,
                        yy_qdgl_zcyh_phone, yy_qdgl_zcyh_tjqd, yy_qdgl_zcyh_num, yy_yhgl_zcyh_name, yy_yhgl_zcyh_phone,
                        yy_yhgl_zcyh_tjr_phone, yy_yhgl_zcyh_tjr_name, yy_dcgl_pt_mc, yy_dcgl_pt_ip):
        # 点击渠道管理
        self.yunying.page_click_qdgl(yy_qdgl_tg_mc, yy_qdgl_tg_phone, yy_qdgl_qdzc_phone, yy_qdgl_zcyh_name,
                                     yy_qdgl_zcyh_phone, yy_qdgl_zcyh_tjqd, yy_qdgl_zcyh_num)
        # 点击用户管理
        self.yunying.page_click_yyyhgl(yy_yhgl_zcyh_name, yy_yhgl_zcyh_phone, yy_yhgl_zcyh_tjr_phone,
                                       yy_yhgl_zcyh_tjr_name)
        # 点击渠道统计
        self.yunying.page_click_yyqdtj()
        # 点击贷超管理
        self.yunying.page_click_yydcgl(yy_dcgl_pt_mc, yy_dcgl_pt_ip)
        # 点击业务数据统计
        self.yunying.page_click_yyywsjtj()

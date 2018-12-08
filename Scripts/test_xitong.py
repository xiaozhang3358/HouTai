import sys, os

sys.path.append(os.getcwd())
import pytest

from Base.read_yaml import ReadYAML
from Page.page_in import PageIn


# 读取参数函数封装
def get_data():
    # 定义一个空列表
    arrs = []
    for data in ReadYAML('xitong_data.yaml').read_yaml().values():
        arrs.append((data.get('xt_qxgl_cdgl_xg_px'), data.get('xt_qxgl_cdgl_tj_mc'), data.get('xt_qxgl_cdgl_tj_px'),
                     data.get('xt_qxgl_rygl_dlm'), data.get('xt_qxgl_rygl_name'), data.get('xt_qxgl_lzgl_dlm'),
                     data.get('xt_qxgl_lzgl_name'), data.get('xt_xtrz_yhid'), data.get('xt_xtrz_url'),
                     data.get('xt_xtrz_dxrz_phone'), data.get('xt_xtrz_dxrz_dxnr'), data.get('xt_xtrz_dxrz_id'),
                     data.get('xt_xtrz_dxrz_ip'), data.get('xt_xtrz_jskhdx_phone'), data.get('xt_xtrz_jskhdx_ip'),
                     data.get('xt_sjzd_zdgl_ms'), data.get('xt_sjzd_zdgl_tj_jz'), data.get('xt_sjzd_zdgl_tj_bq'),
                     data.get('xt_sjzd_zdgl_tj_lx'), data.get('xt_sjzd_zdgl_tj_ms'), data.get('xt_sjzd_zdgl_tj_px'),
                     data.get('xt_sjzd_dhkgl_lb_gspt'), data.get('xt_sjzd_dhkgl_lb_phone'),
                     data.get('xt_llgl_dq_lb_szll_qs'), data.get('xt_llgl_dq_lb_szll_ll'),
                     data.get('xt_llgl_qll_lb_qs'), data.get('xt_llgl_qll_tj_qs'), data.get('xt_llgl_qll_tj_ll')))
    return arrs


class TestXiTong():
    def setup_class(self):
        # 统一化入口类
        self.page = PageIn()
        # 调用封装的登录方法
        self.page.page_get_login().page_login()
        # 实例化债务管理页面对象
        self.xitong = self.page.page_get_xitong()

    def teardown_class(self):
        # 关闭浏览器驱动对象
        self.xitong.driver.quit()

    # 点击系统设置
    @pytest.mark.parametrize('xt_qxgl_cdgl_xg_px, xt_qxgl_cdgl_tj_mc, xt_qxgl_cdgl_tj_px, xt_qxgl_rygl_dlm,'
                             'xt_qxgl_rygl_name, xt_qxgl_lzgl_dlm, xt_qxgl_lzgl_name, xt_xtrz_yhid, xt_xtrz_url,'
                             'xt_xtrz_dxrz_phone, xt_xtrz_dxrz_dxnr, xt_xtrz_dxrz_id, xt_xtrz_dxrz_ip, xt_xtrz_jskhdx_phone,'
                             'xt_xtrz_jskhdx_ip, xt_sjzd_zdgl_ms, xt_sjzd_zdgl_tj_jz, xt_sjzd_zdgl_tj_bq, xt_sjzd_zdgl_tj_lx,'
                             'xt_sjzd_zdgl_tj_ms, xt_sjzd_zdgl_tj_px, xt_sjzd_dhkgl_lb_gspt, xt_sjzd_dhkgl_lb_phone,'
                             'xt_llgl_dq_lb_szll_qs, xt_llgl_dq_lb_szll_ll, xt_llgl_qll_lb_qs, xt_llgl_qll_tj_qs,xt_llgl_qll_tj_ll',
                             get_data())
    def test_xitong_sz(self, xt_qxgl_cdgl_xg_px, xt_qxgl_cdgl_tj_mc, xt_qxgl_cdgl_tj_px, xt_qxgl_rygl_dlm,
                       xt_qxgl_rygl_name, xt_qxgl_lzgl_dlm, xt_qxgl_lzgl_name, xt_xtrz_yhid, xt_xtrz_url,
                       xt_xtrz_dxrz_phone, xt_xtrz_dxrz_dxnr, xt_xtrz_dxrz_id, xt_xtrz_dxrz_ip, xt_xtrz_jskhdx_phone,
                       xt_xtrz_jskhdx_ip, xt_sjzd_zdgl_ms, xt_sjzd_zdgl_tj_jz, xt_sjzd_zdgl_tj_bq, xt_sjzd_zdgl_tj_lx,
                       xt_sjzd_zdgl_tj_ms, xt_sjzd_zdgl_tj_px, xt_sjzd_dhkgl_lb_gspt, xt_sjzd_dhkgl_lb_phone,
                       xt_llgl_dq_lb_szll_qs, xt_llgl_dq_lb_szll_ll, xt_llgl_qll_lb_qs, xt_llgl_qll_tj_qs,
                       xt_llgl_qll_tj_ll):
        # 点击权限管理
        self.xitong.page_click_xtqxgl(xt_qxgl_cdgl_xg_px, xt_qxgl_cdgl_tj_mc, xt_qxgl_cdgl_tj_px, xt_qxgl_rygl_dlm,
                                      xt_qxgl_rygl_name, xt_qxgl_lzgl_dlm, xt_qxgl_lzgl_name)
        # 点击系统日志
        self.xitong.page_click_xtrz(xt_xtrz_yhid, xt_xtrz_url, xt_xtrz_dxrz_phone, xt_xtrz_dxrz_dxnr, xt_xtrz_dxrz_id,
                                    xt_xtrz_dxrz_ip, xt_xtrz_jskhdx_phone, xt_xtrz_jskhdx_ip)
        # 点击数据字典
        self.xitong.page_click_xtsjzd(xt_sjzd_zdgl_ms, xt_sjzd_zdgl_tj_jz, xt_sjzd_zdgl_tj_bq, xt_sjzd_zdgl_tj_lx,
                                      xt_sjzd_zdgl_tj_ms, xt_sjzd_zdgl_tj_px, xt_sjzd_dhkgl_lb_gspt,
                                      xt_sjzd_dhkgl_lb_phone)
        # 点击利率管理
        self.xitong.page_click_xtllgl(xt_llgl_dq_lb_szll_qs, xt_llgl_dq_lb_szll_ll, xt_llgl_qll_lb_qs,
                                      xt_llgl_qll_tj_qs, xt_llgl_qll_tj_ll)

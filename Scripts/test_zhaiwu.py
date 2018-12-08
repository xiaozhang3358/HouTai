import sys, os

sys.path.append(os.getcwd())

import pytest
from Base.read_yaml import ReadYAML
from Page.page_in import PageIn


# 读取参数函数封装
def get_data():
    # 定义一个空列表
    arrs = []
    for data in ReadYAML('zhaiwu_data.yaml').read_yaml().values():
        arrs.append((data.get('zw_dz_hktx_name'), data.get('zw_dz_hktx_phone'), data.get('zw_dz_hktx_ddbh'),
                     data.get('zw_dz_txjl_name'), data.get('zw_dz_txjl_phone'), data.get('zw_dh_kh_ddbh'),
                     data.get('zw_dh_kh_name'), data.get('zw_dh_kh_phone'), data.get('zw_dhcs_yqkhc_name'),
                     data.get('zw_dhcs_yqkhc_phone'), data.get('zw_dhcs_yqkhc_ddbh'), data.get('zw_dhcs_yqcs_name'),
                     data.get('zw_dhcs_yqcs_phone'), data.get('zw_dhcs_csjlgl_name'), data.get('zw_dhcs_csjlgl_phone'),
                     data.get('zw_dhcs_wapcgl_pch'), data.get('zw_dhcs_wapcgl_jgmc'), data.get('zw_dhcs_waajzx_name'),
                     data.get('zw_dhcs_waajzx_phone'), data.get('zw_dhcs_waajzx_ddbh'), data.get('zw_dhcs_waajzx_ajpc'),
                     data.get('zw_dhcs_hkmx_name'), data.get('zw_dhcs_hkmx_phone'), data.get('zw_dhcs_hkmx_wapch'),
                     data.get('zw_dhcs_hkmx_ddbh'), data.get('zw_jggl_jgmc'), data.get('zw_rygl_name'),
                     data.get('zw_rygl_phone'), data.get('zw_rbbb_csyrb_csy'), data.get('zw_rbbb_csygcrb_csy'),
                     data.get('zw_ybbb_csyyjyb_name'), data.get('zw_ybbb_csyyjyb_zl'), data.get('zw_ybbb_wwjgyb_wwjg')))
    return arrs


class TestZhaiWu():
    def setup_class(self):
        # 统一化入口类
        self.page = PageIn()
        # 调用封装的登录方法
        self.page.page_get_login().page_login()
        # 实例化债务管理页面对象
        self.zhaiwu = self.page.page_get_zhaiwu()

    def teardown_class(self):
        # 关闭浏览器驱动对象
        self.zhaiwu.driver.quit()

    # 点击债务管理
    @pytest.mark.parametrize(
        'zw_dz_hktx_name, zw_dz_hktx_phone, zw_dz_hktx_ddbh,zw_dz_txjl_name, zw_dz_txjl_phone,zw_dh_kh_ddbh,'
        'zw_dh_kh_name, zw_dh_kh_phone,zw_dhcs_yqkhc_name, zw_dhcs_yqkhc_phone, zw_dhcs_yqkhc_ddbh,zw_dhcs_yqcs_name,'
        'zw_dhcs_yqcs_phone,zw_dhcs_csjlgl_name, zw_dhcs_csjlgl_phone,zw_dhcs_wapcgl_pch, zw_dhcs_wapcgl_jgmc,'
        'zw_dhcs_waajzx_name, zw_dhcs_waajzx_phone, zw_dhcs_waajzx_ddbh, zw_dhcs_waajzx_ajpc,zw_dhcs_hkmx_name,'
        'zw_dhcs_hkmx_phone,zw_dhcs_hkmx_wapch, zw_dhcs_hkmx_ddbh,zw_jggl_jgmc,zw_rygl_name, zw_rygl_phone,'
        'zw_rbbb_csyrb_csy, zw_rbbb_csygcrb_csy, zw_ybbb_csyyjyb_name, zw_ybbb_csyyjyb_zl, zw_ybbb_wwjgyb_wwjg',
        get_data())
    def test_zhaiwu_gl(self, zw_dz_hktx_name, zw_dz_hktx_phone, zw_dz_hktx_ddbh, zw_dz_txjl_name, zw_dz_txjl_phone,
                       zw_dh_kh_ddbh, zw_dh_kh_name, zw_dh_kh_phone, zw_dhcs_yqkhc_name, zw_dhcs_yqkhc_phone,
                       zw_dhcs_yqkhc_ddbh, zw_dhcs_yqcs_name, zw_dhcs_yqcs_phone, zw_dhcs_csjlgl_name,
                       zw_dhcs_csjlgl_phone, zw_dhcs_wapcgl_pch, zw_dhcs_wapcgl_jgmc, zw_dhcs_waajzx_name,
                       zw_dhcs_waajzx_phone, zw_dhcs_waajzx_ddbh, zw_dhcs_waajzx_ajpc, zw_dhcs_hkmx_name,
                       zw_dhcs_hkmx_phone, zw_dhcs_hkmx_wapch, zw_dhcs_hkmx_ddbh, zw_jggl_jgmc, zw_rygl_name,
                       zw_rygl_phone, zw_rbbb_csyrb_csy, zw_rbbb_csygcrb_csy, zw_ybbb_csyyjyb_name, zw_ybbb_csyyjyb_zl,
                       zw_ybbb_wwjgyb_wwjg):
        # 点击贷中管理
        self.zhaiwu.page_click_dzgl(zw_dz_hktx_name, zw_dz_hktx_phone, zw_dz_hktx_ddbh)
        # 点击提醒记录管理
        self.zhaiwu.page_click_txjlgl(zw_dz_txjl_name, zw_dz_txjl_phone)
        # 点击待还管理
        self.zhaiwu.page_click_dhgl(zw_dh_kh_ddbh, zw_dh_kh_name, zw_dh_kh_phone)
        # 点击贷后催收
        self.zhaiwu.page_click_dhcs(zw_dhcs_yqkhc_name, zw_dhcs_yqkhc_phone, zw_dhcs_yqkhc_ddbh)
        # 点击逾期催收
        self.zhaiwu.page_click_yqcs(zw_dhcs_yqcs_name, zw_dhcs_yqcs_phone)
        # 点击催收记录管理
        self.zhaiwu.page_click_csjlgl(zw_dhcs_csjlgl_name, zw_dhcs_csjlgl_phone)
        # 点击委案批次管理
        self.zhaiwu.page_click_wapcgl(zw_dhcs_wapcgl_pch, zw_dhcs_wapcgl_jgmc)
        # 点击委外案件中心
        self.zhaiwu.page_click_waajzx(zw_dhcs_waajzx_name, zw_dhcs_waajzx_phone, zw_dhcs_waajzx_ddbh,
                                      zw_dhcs_waajzx_ajpc)
        # 点击回款明细
        self.zhaiwu.page_click_hkmx(zw_dhcs_hkmx_name, zw_dhcs_hkmx_phone, zw_dhcs_hkmx_wapch, zw_dhcs_hkmx_ddbh)
        # 点击委外机构管理
        self.zhaiwu.page_click_wwjggl(zw_jggl_jgmc)
        # 点击人员管理
        self.zhaiwu.page_click_rygl(zw_rygl_name, zw_rygl_phone)
        # 点击日报报表
        self.zhaiwu.page_click_rbbb(zw_rbbb_csyrb_csy, zw_rbbb_csygcrb_csy)
        # 点击月报报表
        self.zhaiwu.page_click_ybbb(zw_ybbb_csyyjyb_name, zw_ybbb_csyyjyb_zl, zw_ybbb_wwjgyb_wwjg)

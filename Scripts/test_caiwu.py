import sys, os

sys.path.append(os.getcwd())
import pytest
from Base.read_yaml import ReadYAML
from Page.page_in import PageIn


# 读取参数函数封装
def get_data():
    # 定义一个空列表
    arrs = []
    for data in ReadYAML('caiwu_data.yaml').read_yaml().values():
        arrs.append((data.get('cw_dfgl_jygl_ddbh'), data.get('cw_dfgl_jygl_name'), data.get('cw_dfgl_jygl_phone'),
                     data.get('cw_dfgl_jygl_jydh'), data.get('cw_dfgl_zjzhgl_jydh'), data.get('cw_dfgl_hkjygl_ddbh'),
                     data.get('cw_dfgl_hkjygl_jydh'), data.get('cw_dfgl_hkjygl_yhmc'), data.get('cw_dfgl_hkjygl_yhdh'),
                     data.get('cw_hkgl_dhzdgl_ddbh'), data.get('cw_hkgl_dhzdgl_name'), data.get('cw_hkgl_dhzdgl_phone'),
                     data.get('cw_hkgl_zdgl_yhmc'), data.get('cw_hkgl_zdgl_yhdh'), data.get('cw_hkgl_zdgl_ddbh'),
                     data.get('cw_hkgl_dhzd_ddbh'), data.get('cw_hkgl_dhzd_yhmc'), data.get('cw_hkgl_dhzd_yhdh'),
                     data.get('cw_daikgl_jyjl_ddbh'), data.get('cw_daikgl_jyjl_yhm'), data.get('cw_daikgl_jyjl_khh'),
                     data.get('cw_daikgl_jyjl_yhkh'), data.get('cw_zjzhgl_baby_jydh'), data.get('cw_zjgl_dsbdb_ddbh'),
                     data.get('cw_zjgl_dsbdb_name'), data.get('cw_zjgl_ysbdb_ddbh'), data.get('cw_zjgl_ysbdb_name'),
                     data.get('cw_zjgl_sjsb_xmmc'), data.get('cw_zjgl_sjsb_ym'), data.get('cw_zjgl_sjsb_mysj'),
                     data.get('cw_zjgl_yjqdb_gjz'), data.get('cw_dkgl_wdk_ddbh'), data.get('cw_dkgl_wdk_name'),
                     data.get('cw_dkgl_ydk_ddbh'), data.get('cw_dkgl_ydk_name'), data.get('cw_dkgl_dktj_dkzh'),
                     data.get('cw_hkjy_baby_name'), data.get('cw_hkjy_baby_shjyh'), data.get('cw_zdmx_yqgl_yhmc'),
                     data.get('cw_zdmx_yqgl_ddbh'), data.get('cw_zdmx_baby_yhmc'), data.get('cw_zdmx_dhmx_yhmc'),
                     data.get('cw_zdmx_zdgl_name'), data.get('cw_zdmx_zdgl_phone'), data.get('cw_zdmx_zdgl_ddbh'),
                     data.get('cw_zdmx_hkmx_yhmc'), data.get('cw_zdmx_yqmx_yhmc'), data.get('cw_zdmx_hkdz_ddbh'),
                     data.get('cw_zdmx_hkdz_jydh'), data.get('cw_zdmx_hkdz_name'), data.get('cw_zdmx_hkdz_phone'),
                     data.get('cw_zdmx_dhzd_ddbh'), data.get('cw_zdmx_dhzd_yhmc'), data.get('cw_zdmx_dhzd_yhdh'),
                     data.get('cw_zqdz_mbxm_name'), data.get('cw_zqdz_mbhkz_name'), data.get('cw_zqdz_mbhkwc_name'),
                     data.get('cw_zqdz_hkdzzd_name'), data.get('cw_zqdz_jkdz_name'), data.get('cw_zqdz_bzjfh_name'),
                     data.get('cw_zqdz_jywljl_lsh')))
    return arrs


class TestCaiWu():
    def setup_class(self):
        # 统一化入口类
        self.page = PageIn()
        # 调用封装的登录方法
        self.page.page_get_login().page_login()
        # 实例化债务管理页面对象
        self.caiwu = self.page.page_get_caiwu()

    def teardown_class(self):
        # 关闭浏览器驱动对象
        self.caiwu.driver.quit()

    # 点击财务管理
    @pytest.mark.parametrize(
        'cw_dfgl_jygl_ddbh, cw_dfgl_jygl_name, cw_dfgl_jygl_phone, cw_dfgl_jygl_jydh, cw_dfgl_zjzhgl_jydh, cw_dfgl_hkjygl_ddbh, cw_dfgl_hkjygl_jydh,'
        'cw_dfgl_hkjygl_yhmc, cw_dfgl_hkjygl_yhdh, cw_hkgl_dhzdgl_ddbh, cw_hkgl_dhzdgl_name,cw_hkgl_dhzdgl_phone, cw_hkgl_zdgl_yhmc, cw_hkgl_zdgl_yhdh,'
        'cw_hkgl_zdgl_ddbh, cw_hkgl_dhzd_ddbh, cw_hkgl_dhzd_yhmc, cw_hkgl_dhzd_yhdh, cw_daikgl_jyjl_ddbh,cw_daikgl_jyjl_yhm, cw_daikgl_jyjl_khh,'
        'cw_daikgl_jyjl_yhkh, cw_zjzhgl_baby_jydh, cw_zjgl_dsbdb_ddbh, cw_zjgl_dsbdb_name,cw_zjgl_ysbdb_ddbh, cw_zjgl_ysbdb_name, cw_zjgl_sjsb_xmmc,'
        'cw_zjgl_sjsb_ym, cw_zjgl_sjsb_mysj, cw_zjgl_yjqdb_gjz, cw_dkgl_wdk_ddbh, cw_dkgl_wdk_name,cw_dkgl_ydk_ddbh, cw_dkgl_ydk_name, cw_dkgl_dktj_dkzh,'
        'cw_hkjy_baby_name, cw_hkjy_baby_shjyh, cw_zdmx_yqgl_yhmc, cw_zdmx_yqgl_ddbh, cw_zdmx_baby_yhmc,cw_zdmx_dhmx_yhmc, cw_zdmx_zdgl_name, cw_zdmx_zdgl_phone, cw_zdmx_zdgl_ddbh, cw_zdmx_hkmx_yhmc,'
        'cw_zdmx_yqmx_yhmc, cw_zdmx_hkdz_ddbh, cw_zdmx_hkdz_jydh, cw_zdmx_hkdz_name,cw_zdmx_hkdz_phone, cw_zdmx_dhzd_ddbh, cw_zdmx_dhzd_yhmc, cw_zdmx_dhzd_yhdh, cw_zqdz_mbxm_name,'
        'cw_zqdz_mbhkz_name, cw_zqdz_mbhkwc_name, cw_zqdz_hkdzzd_name, cw_zqdz_jkdz_name,cw_zqdz_bzjfh_name, cw_zqdz_jywljl_lsh',
        get_data())
    def test_caiwu_gl(self, cw_dfgl_jygl_ddbh, cw_dfgl_jygl_name, cw_dfgl_jygl_phone, cw_dfgl_jygl_jydh,
                      cw_dfgl_zjzhgl_jydh, cw_dfgl_hkjygl_ddbh, cw_dfgl_hkjygl_jydh,
                      cw_dfgl_hkjygl_yhmc, cw_dfgl_hkjygl_yhdh, cw_hkgl_dhzdgl_ddbh, cw_hkgl_dhzdgl_name,
                      cw_hkgl_dhzdgl_phone, cw_hkgl_zdgl_yhmc, cw_hkgl_zdgl_yhdh,
                      cw_hkgl_zdgl_ddbh, cw_hkgl_dhzd_ddbh, cw_hkgl_dhzd_yhmc, cw_hkgl_dhzd_yhdh, cw_daikgl_jyjl_ddbh,
                      cw_daikgl_jyjl_yhm, cw_daikgl_jyjl_khh,
                      cw_daikgl_jyjl_yhkh, cw_zjzhgl_baby_jydh, cw_zjgl_dsbdb_ddbh, cw_zjgl_dsbdb_name,
                      cw_zjgl_ysbdb_ddbh, cw_zjgl_ysbdb_name, cw_zjgl_sjsb_xmmc,
                      cw_zjgl_sjsb_ym, cw_zjgl_sjsb_mysj, cw_zjgl_yjqdb_gjz, cw_dkgl_wdk_ddbh, cw_dkgl_wdk_name,
                      cw_dkgl_ydk_ddbh, cw_dkgl_ydk_name, cw_dkgl_dktj_dkzh,
                      cw_hkjy_baby_name, cw_hkjy_baby_shjyh, cw_zdmx_yqgl_yhmc, cw_zdmx_yqgl_ddbh, cw_zdmx_baby_yhmc,
                      cw_zdmx_dhmx_yhmc, cw_zdmx_zdgl_name, cw_zdmx_zdgl_phone, cw_zdmx_zdgl_ddbh, cw_zdmx_hkmx_yhmc,
                      cw_zdmx_yqmx_yhmc, cw_zdmx_hkdz_ddbh, cw_zdmx_hkdz_jydh, cw_zdmx_hkdz_name,
                      cw_zdmx_hkdz_phone, cw_zdmx_dhzd_ddbh, cw_zdmx_dhzd_yhmc, cw_zdmx_dhzd_yhdh, cw_zqdz_mbxm_name,
                      cw_zqdz_mbhkz_name, cw_zqdz_mbhkwc_name, cw_zqdz_hkdzzd_name, cw_zqdz_jkdz_name,
                      cw_zqdz_bzjfh_name, cw_zqdz_jywljl_lsh):
        # 点击代付管理
        self.caiwu.page_click_cwdfgl(cw_dfgl_jygl_ddbh, cw_dfgl_jygl_name, cw_dfgl_jygl_phone, cw_dfgl_jygl_jydh,
                                     cw_dfgl_zjzhgl_jydh, cw_dfgl_hkjygl_ddbh, cw_dfgl_hkjygl_jydh, cw_dfgl_hkjygl_yhmc,
                                     cw_dfgl_hkjygl_yhdh)
        # 点击代扣管理
        self.caiwu.page_click_cwdkgl(cw_daikgl_jyjl_ddbh, cw_daikgl_jyjl_yhm, cw_daikgl_jyjl_khh, cw_daikgl_jyjl_yhkh)

        # 点击还款管理
        self.caiwu.page_click_cwhkgl(cw_hkgl_dhzdgl_ddbh, cw_hkgl_dhzdgl_name,
                                     cw_hkgl_dhzdgl_phone, cw_hkgl_zdgl_yhmc, cw_hkgl_zdgl_yhdh,
                                     cw_hkgl_zdgl_ddbh, cw_hkgl_dhzd_ddbh, cw_hkgl_dhzd_yhmc, cw_hkgl_dhzd_yhdh)

        # 点击资金账户管理
        self.caiwu.page_click_cwzjzhgl(cw_zjzhgl_baby_jydh)
        # 点击资金管理
        self.caiwu.page_click_cwzjgl(cw_zjgl_dsbdb_ddbh, cw_zjgl_dsbdb_name, cw_zjgl_ysbdb_ddbh, cw_zjgl_ysbdb_name,
                                     cw_zjgl_sjsb_xmmc, cw_zjgl_sjsb_ym, cw_zjgl_sjsb_mysj, cw_zjgl_yjqdb_gjz)
        # 点击打款管理
        self.caiwu.page_click_cwdakgl(cw_dkgl_wdk_ddbh, cw_dkgl_wdk_name, cw_dkgl_ydk_ddbh, cw_dkgl_ydk_name,
                                     cw_dkgl_dktj_dkzh)
        # 点击还款交易
        self.caiwu.page_click_cwhkjy(cw_hkjy_baby_name, cw_hkjy_baby_shjyh)
        # 点击账单明细
        self.caiwu.page_click_cwzdmx(cw_zdmx_yqgl_yhmc, cw_zdmx_yqgl_ddbh, cw_zdmx_baby_yhmc, cw_zdmx_dhmx_yhmc,
                                     cw_zdmx_zdgl_name, cw_zdmx_zdgl_phone, cw_zdmx_zdgl_ddbh, cw_zdmx_hkmx_yhmc,
                                     cw_zdmx_yqmx_yhmc, cw_zdmx_hkdz_ddbh, cw_zdmx_hkdz_jydh, cw_zdmx_hkdz_name,
                                     cw_zdmx_hkdz_phone, cw_zdmx_dhzd_ddbh, cw_zdmx_dhzd_yhmc, cw_zdmx_dhzd_yhdh)
        # 点击债权对账
        self.caiwu.page_click_cwzqdz(cw_zqdz_mbxm_name, cw_zqdz_mbhkz_name, cw_zqdz_mbhkwc_name, cw_zqdz_hkdzzd_name,
                                     cw_zqdz_jkdz_name, cw_zqdz_bzjfh_name, cw_zqdz_jywljl_lsh)

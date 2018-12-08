from time import sleep

import Page
from Base.base import Base
from selenium.webdriver.support.select import Select


class PageZhaiWu(Base):
    # 点击贷中管理
    def page_click_dzgl(self, zw_dz_hktx_name, zw_dz_hktx_phone, zw_dz_hktx_ddbh):
        self.base_frame_back()
        # 点击债务管理
        self.base_click_btn(Page.zwgl)
        # 点击还款提醒
        self.base_aframe(Page.zw_dz_hktx)
        # 输入客户姓名
        self.base_input_text(Page.zw_dz_hktx_name, zw_dz_hktx_name)
        # 输入客户电话
        self.base_input_text(Page.zw_dz_hktx_phone, zw_dz_hktx_phone)
        # 输入订单编号
        self.base_input_text(Page.zw_dz_hktx_ddbh, zw_dz_hktx_ddbh)
        # 选择用户状态
        select1 = Select(self.base_find_element(Page.zw_dz_hktx_yhzt))
        # select1.select_by_visible_text(text4)
        select1.select_by_index(1)
        # 选择剩余天数
        select2 = Select(self.base_find_element(Page.zw_dz_hktx_syts))
        # select2.select_by_visible_text(text5)
        select2.select_by_index(2)
        # 点击查询
        self.base_click_btn(Page.zw_dz_hktx_cx)
        sleep(5)

    # 点击提醒记录管理
    def page_click_txjlgl(self, zw_dz_txjl_name, zw_dz_txjl_phone):
        # 点击提醒记录管理
        self.base_aframe(Page.zw_dz_txjl)
        # 输入客户姓名
        self.base_input_text(Page.zw_dz_txjl_name, zw_dz_txjl_name)
        # 输入手机号
        self.base_input_text(Page.zw_dz_txjl_phone, zw_dz_txjl_phone)
        # 点击查询
        self.base_click_btn(Page.zw_dz_txjl_cx)
        sleep(5)

    # 点击待还管理
    def page_click_dhgl(self, zw_dh_kh_ddbh, zw_dh_kh_name, zw_dh_kh_phone):
        # 点击待还款客户
        self.base_iframe(Page.zw_dhgl, Page.zw_dh_kh)
        # 输入订单编号
        self.base_input_text(Page.zw_dh_kh_ddbh, zw_dh_kh_ddbh)
        # 输入客户姓名
        self.base_input_text(Page.zw_dh_kh_name, zw_dh_kh_name)
        # 输入客户电话
        self.base_input_text(Page.zw_dh_kh_phone, zw_dh_kh_phone)
        # 点击查询
        self.base_click_btn(Page.zw_dh_kh_cx)
        sleep(5)

    # 点击贷后催收
    def page_click_dhcs(self, zw_dhcs_yqkhc_name, zw_dhcs_yqkhc_phone, zw_dhcs_yqkhc_ddbh):
        # 点击逾期客户池
        self.base_iframe(Page.zw_dhcs, Page.zw_dhcs_yqkhc)
        # 输入客户姓名
        self.base_input_text(Page.zw_dhcs_yqkhc_name, zw_dhcs_yqkhc_name)
        # 输入手机号
        self.base_input_text(Page.zw_dhcs_yqkhc_phone, zw_dhcs_yqkhc_phone)
        # 输入订单编号
        self.base_input_text(Page.zw_dhcs_yqkhc_ddbh, zw_dhcs_yqkhc_ddbh)
        # 点击查询
        self.base_click_btn(Page.zw_dhcs_yqkhc_cx)
        sleep(5)

    # 点击逾期催收
    def page_click_yqcs(self, zw_dhcs_yqcs_name, zw_dhcs_yqcs_phone):
        # 点击逾期催收
        self.base_aframe(Page.zw_dhcs_yqcs)
        # 输入客户姓名
        self.base_input_text(Page.zw_dhcs_yqcs_name, zw_dhcs_yqcs_name)
        # 输入客户电话
        self.base_input_text(Page.zw_dhcs_yqcs_phone, zw_dhcs_yqcs_phone)
        # 点击查询
        self.base_click_btn(Page.zw_dhcs_yqcs_cx)
        sleep(5)

    # 点击催收记录管理
    def page_click_csjlgl(self, zw_dhcs_csjlgl_name, zw_dhcs_csjlgl_phone):
        # 点击催收记录管理
        self.base_aframe(Page.zw_dhcs_csjlgl)
        # 输入客户姓名
        self.base_input_text(Page.zw_dhcs_csjlgl_name, zw_dhcs_csjlgl_name)
        # 输入客户电话
        self.base_input_text(Page.zw_dhcs_csjlgl_phone, zw_dhcs_csjlgl_phone)
        # 点击查询
        self.base_click_btn(Page.zw_dhcs_csjlgl_cx)
        sleep(5)

    # 点击委案批次管理
    def page_click_wapcgl(self, zw_dhcs_wapcgl_pch, zw_dhcs_wapcgl_jgmc):
        # 点击委案批次管理
        self.base_aframe(Page.zw_dhcs_wapcgl)
        # 输入委案批次号
        self.base_input_text(Page.zw_dhcs_wapcgl_pch, zw_dhcs_wapcgl_pch)
        # 输入机构名称
        self.base_input_text(Page.zw_dhcs_wapcgl_jgmc, zw_dhcs_wapcgl_jgmc)
        # 点击查询
        self.base_click_btn(Page.zw_dhcs_wapcgl_cx)
        sleep(5)

    # 点击委外案件中心
    def page_click_waajzx(self, zw_dhcs_waajzx_name, zw_dhcs_waajzx_phone, zw_dhcs_waajzx_ddbh, zw_dhcs_waajzx_ajpc):
        # 点击委外案件中心
        self.base_aframe(Page.zw_dhcs_waajzx)
        # 输入客户姓名
        self.base_input_text(Page.zw_dhcs_waajzx_name, zw_dhcs_waajzx_name)
        # 输入客户电话
        self.base_input_text(Page.zw_dhcs_waajzx_phone, zw_dhcs_waajzx_phone)
        # 输入订单编号
        self.base_input_text(Page.zw_dhcs_waajzx_ddbh, zw_dhcs_waajzx_ddbh)
        # 输入案件批次
        self.base_input_text(Page.zw_dhcs_waajzx_ajpc, zw_dhcs_waajzx_ajpc)
        # 点击查询
        self.base_click_btn(Page.zw_dhcs_waajzx_cx)
        sleep(5)

    # 点击回款明细
    def page_click_hkmx(self, zw_dhcs_hkmx_name, zw_dhcs_hkmx_phone, zw_dhcs_hkmx_wapch, zw_dhcs_hkmx_ddbh):
        # 点击回款明细
        self.base_aframe(Page.zw_dhcs_hkmx)
        # 输入客户姓名
        self.base_input_text(Page.zw_dhcs_hkmx_name, zw_dhcs_hkmx_name)
        # 输入客户电话
        self.base_input_text(Page.zw_dhcs_hkmx_phone, zw_dhcs_hkmx_phone)
        # 输入委案批次号
        self.base_input_text(Page.zw_dhcs_hkmx_wapch, zw_dhcs_hkmx_wapch)
        # 输入订单编号
        self.base_input_text(Page.zw_dhcs_hkmx_ddbh, zw_dhcs_hkmx_ddbh)
        # 点击查询
        self.base_click_btn(Page.zw_dhcs_hkmx_cx)
        sleep(5)

    # 点击委外机构管理
    def page_click_wwjggl(self, zw_jggl_jgmc):
        # 点击机构管理
        self.base_iframe(Page.zw_wwjggl, Page.zw_jggl)
        # 输入机构名称
        self.base_input_text(Page.zw_jggl_jgmc, zw_jggl_jgmc)
        # 点击检索
        self.base_click_btn(Page.zw_jggl_js)
        sleep(5)

    # 点击人员管理
    def page_click_rygl(self, zw_rygl_name, zw_rygl_phone):
        # 点击人员管理
        self.base_aframe(Page.zw_rygl)
        # 输入人员姓名
        self.base_input_text(Page.zw_rygl_name, zw_rygl_name)
        # 输入联系电话
        self.base_input_text(Page.zw_rygl_phone, zw_rygl_phone)
        # 点击查询
        self.base_click_btn(Page.zw_rygl_cx)
        sleep(5)

    # 点击日报报表
    def page_click_rbbb(self, zw_rbbb_csyrb_csy, zw_rbbb_csygcrb_csy):
        # 点击委外机构日报
        self.base_iframe(Page.zw_rbbb, Page.zw_rbbb_wwjgrb)
        # 选择委外机构
        self.base_click_btn(Page.zw_rbbb_wwjgrb_wwjg)
        sleep(1)
        self.base_click_btn(Page.zw_rbbb_wwjgrb_wwjg_xz)
        sleep(1)
        # 选择日期
        self.base_click_btn(Page.zw_rbbb_wwjgrb_rq)
        sleep(1)
        self.base_click_btn(Page.zw_rbbb_wwjgrb_rq_xz)
        sleep(1)
        # 点击查询
        self.base_click_btn(Page.zw_rbbb_wwjgrb_cx)
        sleep(3)

        # 点击中期
        self.base_click_btn(Page.zw_rbbb_wwjgrb_zq)
        # 选择委外机构
        self.base_click_btn(Page.zw_rbbb_wwjgrb_wwjg)
        sleep(1)
        self.base_click_btn(Page.zw_rbbb_wwjgrb_wwjg_xz)
        sleep(1)
        # 选择日期
        self.base_click_btn(Page.zw_rbbb_wwjgrb_rq)
        sleep(1)
        self.base_click_btn(Page.zw_rbbb_wwjgrb_rq_xz)
        sleep(1)
        # 点击查询
        self.base_click_btn(Page.zw_rbbb_wwjgrb_cx)
        sleep(3)

        # 点击高期
        self.base_click_btn(Page.zw_rbbb_wwjgrb_gq)
        # 选择委外机构
        self.base_click_btn(Page.zw_rbbb_wwjgrb_wwjg)
        sleep(1)
        self.base_click_btn(Page.zw_rbbb_wwjgrb_wwjg_xz)
        sleep(1)
        # 选择日期
        self.base_click_btn(Page.zw_rbbb_wwjgrb_rq)
        sleep(1)
        self.base_click_btn(Page.zw_rbbb_wwjgrb_rq_xz)
        sleep(1)
        # 点击查询
        self.base_click_btn(Page.zw_rbbb_wwjgrb_cx)
        sleep(3)

        # 点击催收员日报
        self.base_aframe(Page.zw_rbbb_csyrb)
        # 输入催收员
        self.base_input_text(Page.zw_rbbb_csyrb_csy, zw_rbbb_csyrb_csy)
        # 选择账龄
        self.base_click_btn(Page.zw_rbbb_csyrb_zl)
        sleep(1)
        self.base_click_btn(Page.zw_rbbb_csyrb_zl_xz)
        sleep(1)
        # 选择日期
        self.base_click_btn(Page.zw_rbbb_csyrb_rq)
        sleep(1)
        self.base_click_btn(Page.zw_rbbb_csyrb_rq_xz)
        sleep(1)
        # 点击查询
        self.base_click_btn(Page.zw_rbbb_csyrb_cx)
        sleep(3)

        # 点击催收员过程日报
        self.base_aframe(Page.zw_rbbb_csygcrb)
        # 输入催收员
        self.base_input_text(Page.zw_rbbb_csygcrb_csy, zw_rbbb_csygcrb_csy)
        sleep(1)
        # 选择账龄
        self.base_click_btn(Page.zw_rbbb_csygcrb_zl)
        sleep(1)
        self.base_click_btn(Page.zw_rbbb_csygcrb_zl_xz)
        # 选择日期
        self.base_click_btn(Page.zw_rbbb_csygcrb_rq)
        sleep(1)
        self.base_click_btn(Page.zw_rbbb_csygcrb_rq_xz)
        # 点击查询
        self.base_click_btn(Page.zw_rbbb_csygcrb_cx)
        sleep(3)

        # 点击委外机构过程日报
        self.base_aframe(Page.zw_rbbb_wwjggcrb)
        # 选择委外机构
        self.base_click_btn(Page.zw_rbbb_wwjggcrb_wwjg)
        sleep(1)
        self.base_click_btn(Page.zw_rbbb_wwjggcrb_wwjg_xz)
        # 选择账龄
        self.base_click_btn(Page.zw_rbbb_wwjggcrb_zl)
        sleep(1)
        self.base_click_btn(Page.zw_rbbb_wwjggcrb_zl_xz)
        # 选择日期
        self.base_click_btn(Page.zw_rbbb_wwjggcrb_rq)
        sleep(1)
        self.base_click_btn(Page.zw_rbbb_wwjggcrb_rq_xz)
        # 点击查询
        self.base_click_btn(Page.zw_rbbb_wwjggcrb_cx)
        sleep(3)


    # 点击月报报表
    def page_click_ybbb(self,zw_ybbb_csyyjyb_name, zw_ybbb_csyyjyb_zl, zw_ybbb_wwjgyb_wwjg):
        # 点击催收员业绩月报
        self.base_iframe(Page.zw_ybbb,Page.zw_ybbb_csyyjyb)
        # 输入名字
        self.base_input_text(Page.zw_ybbb_csyyjyb_name, zw_ybbb_csyyjyb_name)
        # 输入账龄
        self.base_input_text(Page.zw_ybbb_csyyjyb_zl, zw_ybbb_csyyjyb_zl)
        # 点击查询
        self.base_click_btn(Page.zw_ybbb_csyyjyb_cx)
        sleep(3)

        # 点击委外机构月报
        self.base_aframe(Page.zw_ybbb_wwjgyb)
        # 输入委外机构
        self.base_input_text(Page.zw_ybbb_wwjgyb_wwjg, zw_ybbb_wwjgyb_wwjg)
        # 点击查询
        self.base_click_btn(Page.zw_ybbb_wwjgyb_cx)
        sleep(3)

        # 资产月报
        self.base_aframe(Page.zw_ybbb_zcyb)
        # 点击查询
        self.base_click_btn(Page.zw_ybbb_zcyb_cx)
        sleep(3)
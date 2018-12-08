from time import sleep

import Page
from Base.base import Base
from selenium.webdriver.support.select import Select


class PageFengKong(Base):
    # 点击风控决策管理
    def page_click_fhjc(self):
        self.base_frame_back()
        # 点击风控中心
        self.base_click_btn(Page.fkzx)
        # 点击风控规则命中率
        self.base_aframe(Page.fk_fkgzmzl)
        # 选择策略名称
        self.base_click_btn(Page.fk_gzmzl_clmc)
        sleep(1)
        self.base_click_btn(Page.fk_gzmzl_clmc_xz)
        # 选择时间
        self.base_click_btn(Page.fk_gzmzl_sj)
        sleep(1)
        self.base_click_btn(Page.fk_gzmzl_sj_xz)
        # 点击查询
        self.base_click_btn(Page.fk_gzmzl_cx)
        sleep(5)

    # 点击接口管理
    def page_click_jkgl(self):
        # 点击接口调用记录
        self.base_iframe(Page.jkgl, Page.fk_jkdyjl)
        # 输入申请时间
        self.base_click_btn(Page.fk_jk_sqsj)
        sleep(1)
        self.base_click_btn(Page.fk_jk_sqsj_xz)
        # 选择接口名称
        select = Select(self.base_find_element(Page.fk_jk_jkmc))
        # select.select_by_visible_text(text)
        select.select_by_index(2)
        # 清空
        self.base_click_btn(Page.fk_jk_qk)
        # 筛选
        self.base_click_btn(Page.fk_jk_sx)
        sleep(5)

    # 点击账户管理
    def page_click_zhgl(self, fk_zh_fysx):
        # 点击交易记录
        self.base_iframe(Page.zhgl, Page.fk_jyjl)
        # 输入费用事项
        self.base_input_text(Page.fk_zh_fysx, fk_zh_fysx)
        # 选择申请时间
        self.base_click_btn(Page.fk_zh_sqsj)
        sleep(1)
        self.base_click_btn(Page.fk_zh_sqsj_xz)
        # 点击清空
        # self.base_click_btn(Page.fk_zh_qk)
        # 点击筛选
        self.base_click_btn(Page.fk_zh_sx)
        sleep(5)

    # 点击黑名单管理
    def page_click_hmdgl(self, fk_hmd_nr, fk_hmdk_tj_nrxx, fk_hmdk_tj_lhyy):
        # 点击黑名单库
        self.base_iframe(Page.hmdgl, Page.fk_hmdk)
        # 输入内容
        self.base_input_text(Page.fk_hmd_nr, fk_hmd_nr)
        # 选择来源
        self.base_click_btn(Page.fk_hmd_ly)
        sleep(1)
        self.base_click_btn(Page.fk_hmd_ly_xz)
        # 选择黑（灰）名单
        self.base_click_btn(Page.fk_hmd_md)
        sleep(1)
        self.base_click_btn(Page.fk_hmd_md_xz)
        # 点击查询
        self.base_click_btn(Page.fk_hmd_cx)
        sleep(3)
        # 点击黑名单添加
        self.base_click_btn(Page.fk_hmdk_tj)
        # 选择黑灰名单类型
        self.base_click_btn(Page.fk_hmd_mdlx)
        sleep(1)
        self.base_click_btn(Page.fk_hmd_mdlx_xz)
        # 选择黑灰名单
        self.base_click_btn(Page.fk_hmdk_tj_lmd)
        sleep(1)
        self.base_click_btn(Page.fk_hmdk_tj_lmd_xz)
        # 输入内容信息
        self.base_input_text(Page.fk_hmdk_tj_nrxx, fk_hmdk_tj_nrxx)
        # 选择来源
        self.base_click_btn(Page.fk_hmdk_tj_ly)
        sleep(1)
        self.base_click_btn(Page.fk_hmdk_tj_ly_xz)
        # 输入拉黑原因
        self.base_input_text(Page.fk_hmdk_tj_lhyy, fk_hmdk_tj_lhyy)
        # 点击保存
        self.base_click_btn(Page.fk_hmdk_tj_save)
        sleep(5)


    # 点击客户管理
    def page_click_khgl(self, fk_kh_phone):
        # 点击资质认证管理
        self.base_iframe(Page.khgl, Page.fk_zzrzgl)
        # 输入客户联系方式
        self.base_input_text(Page.fk_kh_phone, fk_kh_phone)
        # 点击检索
        self.base_click_btn(Page.fk_kh_js)
        sleep(5)

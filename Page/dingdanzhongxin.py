from time import sleep

import Page
from Base.base import Base


class PageDingDan(Base):

    # 点击订单列表
    def page_click_ddlb(self, text1, text2, text3, text4):
        self.base_frame_back()
        # 点击订单中心
        self.base_click_btn(Page.ddzx)
        # 点击订单列表
        self.base_iframe(Page.dd_ddsh,Page.dd_ddlb)
        # 输入订单编号
        self.base_input_text(Page.dd_lb_ddbh, input_value=text1)
        # 输入客户姓名
        self.base_input_text(Page.dd_lb_name, input_value=text2)
        # 输入手机号
        self.base_input_text(Page.dd_lb_phone, input_value=text3)
        # 点击客户来源
        self.base_input_text(Page.dd_lb_ly, input_value=text4)
        # 点击查询
        self.base_click_btn(Page.dd_lb_cx)
        sleep(5)

    # 点击主管审核
    def page_click_zgsh(self, text1, text2, text3):
        # 点击主管审核
        self.base_aframe(Page.dd_zgsh)
        # 输入订单编号
        self.base_input_text(Page.dd_zg_ddbh, input_value=text1)
        # 输入客户姓名
        self.base_input_text(Page.dd_zg_name, input_value=text2)
        # 输入手机号
        self.base_input_text(Page.dd_zg_phone, input_value=text3)
        # 点击查询
        self.base_click_btn(Page.dd_zg_cx)
        sleep(5)

    # 点击订单审核
    def page_click_ddsh(self, text1, text2, text3):
        # 点击订单审核
        self.base_aframe(Page.dd_ddsh)
        # 输入订单编号
        self.base_input_text(Page.dd_ddsh_ddbh, input_value=text1)
        # 输入客户姓名
        self.base_input_text(Page.dd_ddsh_name, input_value=text2)
        # 输入手机号
        self.base_input_text(Page.dd_ddsh_phone, input_value=text3)
        # 点击查询
        self.base_click_btn(Page.dd_ddsh_cx)
        sleep(5)

    # 点击待签约客户
    def page_click_dd_dqy(self, text1, text2, text3):
        # 点击待签约客户
        self.base_aframe(Page.dd_dqy)
        # 输入订单编号
        self.base_input_text(Page.dd_dqy_ddbh, input_value=text1)
        # 输入用户姓名
        self.base_input_text(Page.dd_dqy_name, input_value=text2)
        # 输入手机号
        self.base_input_text(Page.dd_dqy_phone, input_value=text3)
        # 点击查询
        self.base_click_btn(Page.dd_dqy_cx)
        sleep(5)

    # 点击订单管理
    def page_click_ddgl(self):
        # 点击处理量监控
        self.base_iframe(Page.ddgl,Page.dd_clljk)
        # 选择订单创建时间
        self.base_click_btn(Page.dd_ddcjsj)
        sleep(1)
        self.base_click_btn(Page.dd_ddcjsj_xz)
        # 选择订单完成时间
        self.base_click_btn(Page.dd_ddwcsj)
        sleep(1)
        self.base_click_btn(Page.dd_ddwcsj_xz)
        # 点击查询
        self.base_click_btn(Page.dd_cll_cx)
        sleep(5)
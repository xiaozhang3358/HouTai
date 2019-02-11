from time import sleep

import Page
from Base.base import Base


class PageDingDan(Base):
    # 点击订单列表
    def page_click_ddlb(self, ddlb_ddbh, ddlb_name, ddlb_phone, ddlb_khly):
        self.base_frame_back()
        # 点击订单中心
        self.base_click_btn(Page.ddzx)
        # 点击订单列表
        self.base_iframe(Page.dd_ddsh, Page.dd_ddlb)
        # 输入订单编号
        self.base_input_text(Page.dd_lb_ddbh, ddlb_ddbh)
        # 订单状态
        self.base_click_btn(Page.dd_lb_ddzt)
        sleep(1)
        self.base_click_btn(Page.dd_lb_shtg)
        # 输入客户姓名
        self.base_input_text(Page.dd_lb_name, ddlb_name)
        # 输入手机号
        self.base_input_text(Page.dd_lb_phone, ddlb_phone)
        # 点击客户来源
        self.base_input_text(Page.dd_lb_ly, ddlb_khly)
        # 点击查询
        self.base_click_btn(Page.dd_lb_cx)
        sleep(5)

    # 点击主管审核
    def page_click_zgsh(self, zgsh_ddbh, zgsh_name, zgsh_phone):
        # 点击主管审核
        self.base_aframe(Page.dd_zgsh)
        # 输入订单编号
        self.base_input_text(Page.dd_zg_ddbh, zgsh_ddbh)
        # 输入客户姓名
        self.base_input_text(Page.dd_zg_name, zgsh_name)
        # 输入手机号
        self.base_input_text(Page.dd_zg_phone, zgsh_phone)
        # 点击查询
        self.base_click_btn(Page.dd_zg_cx)
        sleep(5)

    # 点击订单审核
    def page_click_ddsh(self, ddsh_ddbh, ddsh_name, ddsh_phone):
        # 点击订单审核
        self.base_aframe(Page.dd_ddsh)
        # 输入订单编号
        self.base_input_text(Page.dd_ddsh_ddbh, ddsh_ddbh)
        # 输入客户姓名
        self.base_input_text(Page.dd_ddsh_name, ddsh_name)
        # 输入手机号
        self.base_input_text(Page.dd_ddsh_phone, ddsh_phone)
        # 点击查询
        self.base_click_btn(Page.dd_ddsh_cx)
        sleep(5)

    # 点击待签约客户
    def page_click_dd_dqy(self, dqy_ddbh, dqy_name, dqy_phone):
        # 点击待签约客户
        self.base_aframe(Page.dd_dqy)
        # 输入订单编号
        self.base_input_text(Page.dd_dqy_ddbh, dqy_ddbh)
        # 输入用户姓名
        self.base_input_text(Page.dd_dqy_name, dqy_name)
        # 输入手机号
        self.base_input_text(Page.dd_dqy_phone, dqy_phone)
        # 点击查询
        self.base_click_btn(Page.dd_dqy_cx)
        sleep(5)

    # 点击订单管理
    def page_click_ddgl(self):
        # 点击处理量监控
        self.base_iframe(Page.ddgl, Page.dd_clljk)
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

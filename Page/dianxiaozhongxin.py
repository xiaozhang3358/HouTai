from time import sleep

import Page
from Base.base import Base


class PageDianxiao(Base):
    # 点击客户导入
    def page_click_khdr(self, khdr_pch, khdr_czy, khdr_phone):
        # 点击电销中心
        self.base_frame_back()
        self.base_click_btn(Page.dxzx)
        # 点击客户导入
        self.base_iframe(Page.dx_khgl, Page.khdr)
        # 输入批次号
        self.base_input_text(Page.pch, khdr_pch)
        # 输入操作员
        self.base_input_text(Page.czy, khdr_czy)
        # 输入电话号码
        self.base_input_text(Page.phone, khdr_phone)
        # 创建时间
        self.base_date()
        # 点击查询
        self.base_click_btn(Page.cx)
        # 电话号码导入
        # self.base_click_btn(Page.dhdr)
        # 下载txt模板
        # self.base_click_btn(Page.downtxt)
        # 下载excel模板
        # self.base_click_btn(Page.downexcel)
        # 点击数字页码或下一页
        sleep(5)

    # 点击客户管理
    def page_click_khgl(self, khgl_dxy, khgl_bfcs, khgl_drly, khgl_zcly):
        # 点击客户管理
        self.base_aframe(Page.dx_khgl)
        # 选择客户状态
        self.base_click_btn(Page.dx_gl_khzt)
        sleep(1)
        self.base_click_btn(Page.dx_gl_ddywc)
        # 点击拜访状态
        self.base_click_btn(Page.dx_gl_bfzt)
        sleep(1)
        self.base_click_btn(Page.dx_gl_dhkh)
        # 输入电销员
        self.base_input_text(Page.dxy, khgl_dxy)
        # 输入拜访次数
        self.base_input_text(Page.bfcs, khgl_bfcs)
        # 导入来源
        self.base_input_text(Page.drly, khgl_drly)
        # 注册来源
        self.base_input_text(Page.zcly, khgl_zcly)
        # 时间筛选
        self.base_click_btn(Page.dx_gl_sxsj)
        sleep(1)
        self.base_click_btn(Page.dx_gl_sxsj_dr)
        # 选择日期
        # 点击查询
        self.base_click_btn(Page.cx_gl)
        sleep(5)

    # 点击待签约客户
    def page_click_dqy(self, dqy_name, dqy_phone):
        # 点击待签约客户
        self.base_aframe(Page.dqy)
        # 输入客户姓名
        self.base_input_text(Page.dqy_name, dqy_name)
        # 输入电话号码
        self.base_input_text(Page.dqy_phone, dqy_phone)
        # 点击查询
        self.base_click_btn(Page.dqy_cx)
        sleep(5)

    # 点击售前营销
    def page_click_sqyx(self, sq_name, sq_phone, sq_bfcs, sq_drly, sq_zcly):
        # 点击售前营销
        self.base_aframe(Page.sqyx)
        # 输入客户姓名
        self.base_input_text(Page.sqyx_name, sq_name)
        # 输入电话号码
        self.base_input_text(Page.sqyx_phone, sq_phone)
        # 输入拜访次数
        self.base_input_text(Page.sqyx_bfcs, sq_bfcs)
        # 导入来源
        self.base_input_text(Page.sqyx_drly, sq_drly)
        # 注册来源
        self.base_input_text(Page.sqyx_zcly, sq_zcly)
        # 点击查询
        self.base_click_btn(Page.sqyx_cx)
        sleep(5)

    # 点击老客户唤醒营销
    def page_click_lkh(self, lkh_name, lkh_phone, lkh_day):
        # 点击老客户唤醒营销
        self.base_aframe(Page.lkh)
        # 输入客户姓名
        self.base_input_text(Page.lkh_name, lkh_name)
        # 输入电话号码
        self.base_input_text(Page.lkh_phone, lkh_phone)
        # 点击客户状态
        self.base_click_btn(Page.lkh_khzt)
        sleep(1)
        # 选择订单废弃
        self.base_click_btn(Page.lkh_khzt_xz)
        # 点击距离完结时间
        self.base_click_btn(Page.dx_lkh_jl)
        sleep(1)
        # 选择距离完结天数
        self.base_click_btn(Page.dx_lkh_dy)
        # 输入天数
        self.base_input_text(Page.dx_lkh_day, lkh_day)
        # 点击拜访状态
        self.base_click_btn(Page.dx_lkh_bfzt)
        # 选择有意向
        self.base_click_btn(Page.dx_lkh_yyx)
        # 选择拜访时间
        self.base_date()
        # 点击查询
        self.base_click_btn(Page.lkh_cx)
        sleep(5)

    # 点击营销记录
    def page_click_yxjl(self, yx_name, yx_phone, yx_czy):
        # 点击营销记录
        self.base_aframe(Page.yxjl)
        # 输入客户姓名
        self.base_input_text(Page.yxjl_name, yx_name)
        # 输入电话号码
        self.base_input_text(Page.yxjl_phone, yx_phone)
        # 输入操作员
        self.base_input_text(Page.yxjl_czy, yx_czy)
        # 点击查询
        self.base_click_btn(Page.yxjl_cx)
        sleep(5)

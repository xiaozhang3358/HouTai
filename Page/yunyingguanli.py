from time import sleep

import Page
from Base.base import Base


class PageYunYing(Base):
    # 点击渠道管理
    def page_click_qdgl(self, yy_qdgl_tg_mc, yy_qdgl_tg_phone, yy_qdgl_qdzc_phone, yy_qdgl_zcyh_name,
                        yy_qdgl_zcyh_phone, yy_qdgl_zcyh_tjqd, yy_qdgl_zcyh_num):
        self.base_frame_back()
        # 点击运营管理
        self.base_click_btn(Page.yygl)
        # 点击推广渠道管理
        self.base_aframe(Page.yy_qdgl_tg)
        # 输入渠道名称
        self.base_input_text(Page.yy_qdgl_tg_mc, yy_qdgl_tg_mc)
        # 输入渠道手机号
        self.base_input_text(Page.yy_qdgl_tg_phone, yy_qdgl_tg_phone)
        # 点击查询
        self.base_click_btn(Page.yy_qdgl_tg_cx)
        sleep(5)

        # 点击渠道监控
        self.base_aframe(Page.yy_qdgl_jk)
        sleep(1)
        # 点击渠道
        self.base_click_btn(Page.yy_qdgl_jk_qd)
        sleep(1)
        # 选择渠道
        self.base_click_btn(Page.yy_qdgl_jk_zx)
        # 点击选择日期
        # 查询
        self.base_click_btn(Page.yy_qdgl_jk_cx)
        sleep(5)

        # 点击渠道注册用户统计
        self.base_aframe(Page.yy_qdgl_qdzc)
        # 选择最近30天
        self.base_click_btn(Page.yy_qdgl_qdzc_sst)
        # 选择按月查询
        # self.base_click_btn(Page.yy_qdgl_qdzc_yue)
        # 输入推荐人手机号
        self.base_input_text(Page.yy_qdgl_qdzc_phone, yy_qdgl_qdzc_phone)
        # 选择认证通过人数
        self.base_click_btn(Page.yy_qdgl_qdzc_rztgrs)
        # 选择订单申请数
        self.base_click_btn(Page.yy_qdgl_qdzc_ddsqs)
        # 选择订单通过数量
        self.base_click_btn(Page.yy_qdgl_qdzc_ddtgsl)
        # 选择成功放款本金
        self.base_click_btn(Page.yy_qdgl_qdzc_cgfkbj)
        # 点击查询
        self.base_click_btn(Page.yy_qdgl_qdzc_cx)
        sleep(5)

        # 点击渠道注册用户
        self.base_aframe(Page.yy_qdgl_zcyh)
        # 输入用户姓名
        self.base_input_text(Page.yy_qdgl_zcyh_name, yy_qdgl_zcyh_name)
        # 输入用户电话
        self.base_input_text(Page.yy_qdgl_zcyh_phone, yy_qdgl_zcyh_phone)
        # 输入推荐渠道
        self.base_input_text(Page.yy_qdgl_zcyh_tjqd, yy_qdgl_zcyh_tjqd)
        # 输入渠道编号
        self.base_input_text(Page.yy_qdgl_zcyh_num, yy_qdgl_zcyh_num)
        # 点击是否扣重
        self.base_click_btn(Page.yy_qdgl_zcyh_iskz)
        sleep(1)
        # 选择是否扣重
        self.base_click_btn(Page.yy_qdgl_zcyh_zc)
        # 点击开始时间
        # 点击结束时间
        # 点击筛选
        self.base_click_btn(Page.yy_qdgl_zcyh_sx)
        sleep(5)

    # 点击用户管理
    def page_click_yyyhgl(self, yy_yhgl_zcyh_name, yy_yhgl_zcyh_phone, yy_yhgl_zcyh_tjr_phone, yy_yhgl_zcyh_tjr_name):
        # 点击注册用户
        self.base_iframe(Page.yy_yhgl, Page.yy_yhgl_zcyh)
        # 输入注册人姓名
        self.base_input_text(Page.yy_yhgl_zcyh_name, yy_yhgl_zcyh_name)
        # 输入注册人电话
        self.base_input_text(Page.yy_yhgl_zcyh_phone, yy_yhgl_zcyh_phone)
        # 输入推荐人电话
        self.base_input_text(Page.yy_yhgl_zcyh_tjr_phone, yy_yhgl_zcyh_tjr_phone)
        # 输入推荐人姓名
        self.base_input_text(Page.yy_yhgl_zcyh_tjr_name, yy_yhgl_zcyh_tjr_name)
        # 点击注册来源
        self.base_click_btn(Page.yy_yhgl_zcyh_zcly)
        sleep(1)
        # 选择注册来源
        self.base_click_btn(Page.yy_yhgl_zcyh_zcly_xz)
        # 点击是否扣重
        self.base_click_btn(Page.yy_yhgl_zcyh_iskz)
        sleep(1)
        # 选择是否扣重
        self.base_click_btn(Page.yy_yhgl_zcyh_zc)
        # 点击查询
        self.base_click_btn(Page.yy_yhgl_zcyh_cx)
        # 点击导出
        # self.base_click_btn(Page.yy_yhgl_zcyh_dc)
        sleep(5)
        # 点击详情
        # self.base_click_btn(Page.yy_yhgl_zcyh_xq)
        # sleep(5)

        # 点击用户监控
        self.base_aframe(Page.yy_yhgl_yhjk)
        # 选择时间查询
        # 查询
        self.base_click_btn(Page.yy_yhgl_yhjk_cx)
        sleep(5)

    # 点击渠道统计
    def page_click_yyqdtj(self):
        # 点击渠道统计
        self.base_iframe(Page.yy_qdtj, Page.yy_qdtj_baby)
        sleep(1)
        # 点击渠道
        self.base_click_btn(Page.yy_qdtj_baby_qd)
        sleep(1)
        # 选择渠道
        self.base_click_btn(Page.yy_qdtj_baby_qd_zx)
        # 选择日期
        # 点击查询
        self.base_click_btn(Page.yy_qdtj_baby_cx)
        # 点击导出数据
        # self.base_click_btn(Page.yy_qdtj_baby_dcsj)
        sleep(5)

    # 点击贷超管理
    def page_click_yydcgl(self, yy_dcgl_pt_mc, yy_dcgl_pt_ip):
        # 点击平台管理
        self.base_iframe(Page.yy_dcgl, Page.yy_dcgl_pt)
        # 输入名称
        self.base_input_text(Page.yy_dcgl_pt_mc, yy_dcgl_pt_mc)
        # 点击超市类型
        self.base_click_btn(Page.yy_dcgl_pt_lx)
        sleep(1)
        # 选择超市类型
        self.base_click_btn(Page.yy_dcgl_pt_lx_xz)
        # 点击上下架
        self.base_click_btn(Page.yy_dcgl_pt_sxj)
        sleep(1)
        # 选择上下架
        self.base_click_btn(Page.yy_dcgl_pt_sj)
        # 选择创建时间
        # 点击排序方式
        # self.base_click_btn(Page.yy_dcgl_pt_px)
        # # 选择排序方式
        # self.base_click_btn(Page.yy_dcgl_pt_sx)
        # 查询
        self.base_click_btn(Page.yy_dcgl_pt_cx)
        sleep(5)
        # 点击访问记录
        self.base_click_btn(Page.yy_dcgl_pt_fwjl)
        # 输入用户ip
        self.base_input_text(Page.yy_dcgl_pt_ip, yy_dcgl_pt_ip)
        # ip查询
        self.base_click_btn(Page.yy_dcgl_pt_ipcx)
        sleep(5)

        # 点击客户转换情况
        self.base_aframe(Page.yy_dcgl_kh)
        # 选择注册时间
        # 查询
        self.base_click_btn(Page.yy_dcgl_kh_cx)
        sleep(5)

    # 点击业务数据统计
    def page_click_yyywsjtj(self):
        # 点击业务数据统计
        self.base_iframe(Page.yy_ywsjtj, Page.yy_ywsjtj_baby)
        # 点击导出
        # self.base_click_btn(Page.yy_ywsjtj_baby_dc)
        sleep(5)

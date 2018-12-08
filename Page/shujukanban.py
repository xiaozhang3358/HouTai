from time import sleep

import Page
from Base.base import Base


class PageShuJu(Base):
    # 点击财务总量统计
    def page_click_cwzltj(self):
        self.base_frame_back()
        # 点击数据看板
        self.base_click_btn(Page.sjkb)
        # 点击财务总量
        self.base_aframe(Page.sj_cwtj_zl)
        # 点击项目名称
        self.base_click_btn(Page.sj_cwtj_zl_name)
        sleep(1)
        # 选择项目名称
        self.base_click_btn(Page.sj_cwtj_zl_name_xz)
        # 点击查询
        self.base_click_btn(Page.sj_cwtj_zl_fkezs_cx)
        sleep(5)
        # 点击债务数据统计
        self.base_click_btn(Page.sj_cwtj_zl_zwsjtj)
        # 点击业务类型
        self.base_click_btn(Page.sj_cwtj_zl_zwsjtj_ywlx)
        sleep(1)
        # 选择业务类型
        self.base_click_btn(Page.sj_cwtj_zl_zwsjtj_ywlx_xz)
        # 点击查询
        self.base_click_btn(Page.sj_cwtj_zl_zwsjtj_cx)
        sleep(3)

    # 点击贷后统计
    def page_click_dhtj(self):
        # 点击还款数据统计
        self.base_iframe(Page.sj_dhtj,Page.sj_dhtj_hksj)
        # 点击客户类型
        self.base_click_btn(Page.sj_dhtj_hksj_khlx)
        sleep(1)
        # 选择客户类型
        self.base_click_btn(Page.sj_dhtj_hksj_khlx_xz)
        # 点击查询
        self.base_click_btn(Page.sj_dhtj_hksj_cx)
        # 点击导出
        # self.base_click_btn(Page.sj_dhtj_hksj_dc)
        sleep(5)

        # 点击逾期数据统计
        self.base_aframe(Page.sj_dhtj_yqsj)
        # 点击客户类型
        self.base_click_btn(Page.sj_dhtj_yqsj_khlx)
        sleep(1)
        # 选择客户类型
        self.base_click_btn(Page.sj_dhtj_yqsj_khlx_xz)
        # 点击导出数据
        # self.base_click_btn(Page.sj_dhtj_yqsj_dcsj)
        # 点击查询
        self.base_click_btn(Page.sj_dhtj_yqsj_cx)
        sleep(5)

        # 点击首逾统计
        self.base_aframe(Page.sj_dhtj_sytj)
        # 点击客户类型
        self.base_click_btn(Page.sj_dhtj_sytj_khlx)
        sleep(1)
        # 选择客户类型
        self.base_click_btn(Page.sj_dhtj_sytj_khlx_xz)
        # 点击查询
        self.base_click_btn(Page.sj_dhtj_sytj_cx)
        sleep(3)
        # 点击图标
        self.base_click_btn(Page.sj_dhtj_sytj_tb)
        # 点击导出
        # self.base_click_btn(Page.sj_dhtj_sytj_dc)
        sleep(5)

    # 点击注册用户统计
    def page_click_zcyhtj(self, phone):
        # 点击注册用户统计
        self.base_iframe(Page.sj_zcyh, Page.sj_zcyh_tj)
        # 点击最近30天
        self.base_click_btn(Page.sj_zcyh_tj_sst)
        sleep(1)
        # 点击按月查询
        # self.base_click_btn(Page.sj_zcyh_tj_yue)
        # 输入推荐人手机号
        self.base_input_text(Page.sj_zcyh_tj_phone, phone)
        # 点击注册人数
        self.base_click_btn(Page.sj_zcyh_tj_zcrs)
        sleep(1)
        # 点击认证通过人数
        self.base_click_btn(Page.sj_zcyh_tj_rztgrs)
        sleep(1)
        # 点击订单申请数
        self.base_click_btn(Page.sj_zcyh_tj_ddsqs)
        sleep(1)
        # 点击订单通过数量
        self.base_click_btn(Page.sj_zcyh_tj_ddtgsl)
        sleep(1)
        # 点击查询
        self.base_click_btn(Page.sj_zcyh_tj_cx)
        sleep(5)

    # 点击统计报表
    def page_click_tjbb(self):
        # 点击资产报表统计
        self.base_iframe(Page.sj_tjbb, Page.sj_tjbb_zcbb)
        # 点击选择日期
        # 点击查询
        self.base_click_btn(Page.sj_tjbb_zcbb_cx)
        # 点击导出数据
        # self.base_click_btn(Page.sj_tjbb_zcbb_dcsj)
        sleep(5)
        # 点击贷中逾期统计
        self.base_aframe(Page.sj_tjbb_dzyq)
        # 点击选择日期
        # 点击查询
        self.base_click_btn(Page.sj_tjbb_dzyq_cx)
        # 点击导出数据
        # self.base_click_btn(Page.sj_tjbb_dzyq_dcsj)
        sleep(5)
        # 点击贷前渠道统计
        self.base_aframe(Page.sj_tjbb_dqqd)
        # 点击选择日期
        # 点击渠道
        self.base_click_btn(Page.sj_tjbb_dqqd_qd)
        # 选择渠道
        self.base_click_btn(Page.sj_tjbb_dqqd_xzqd)
        # 点击查询
        self.base_click_btn(Page.sj_tjbb_dqqd_cx)
        # 点击导出数据
        # self.base_click_btn(Page.sj_tjbb_dqqd_dcsj)
        sleep(5)

    # 点击业务数据统计
    def page_click_ywsjtj(self):
        # 点击业务数据统计
        self.base_iframe(Page.sj_ywsj, Page.sj_ywsj_tj)
        # 点击导出
        # self.base_click_btn(Page.sj_ywsj_tj_dc)
        sleep(5)

    # 点击渠道统计
    def page_click_qdtj(self):
        # 点击渠道贷后统计
        self.base_iframe(Page.sj_qdtj, Page.sj_qdtj_dh)
        # 点击客户类型
        self.base_click_btn(Page.sj_qdtj_dh_khlx)
        sleep(1)
        # 选择客户类型
        self.base_click_btn(Page.sj_qdtj_dh_khlx_xz)
        # 点击导出数据
        # self.base_click_btn(Page.sj_qdtj_dh_dcsj)
        # 点击查询
        self.base_click_btn(Page.sj_qdtj_dh_cx)
        sleep(5)

    # 点击催收统计
    def page_click_cstj(self):
        # 点击催收考核统计
        self.base_iframe(Page.sj_cstj, Page.sj_cstj_kh)
        # 点击导出当月
        # self.base_click_btn(Page.sj_cstj_kh_dcdy)
        # 点击导出历史
        # self.base_click_btn(Page.sj_cstj_kh_dcls)
        sleep(5)

    # 点击电销统计
    def page_click_dxtj(self):
        # 点击渠道电销统计
        self.base_iframe(Page.sj_dxtj, Page.sj_dxtj_qddx)
        # 点击电销员
        self.base_click_btn(Page.sj_dxtj_qddx_dxy)
        sleep(1)
        # 选择电销员
        self.base_click_btn(Page.sj_dxtj_qddx_dxy_xz)
        # 点击统计类型
        self.base_click_btn(Page.sj_dxtj_qddx_tjlx)
        sleep(1)
        # 选择统计类型
        self.base_click_btn(Page.sj_dxtj_qddx_tjlx_xz)
        # 点击注册/导入时间
        self.base_click_btn(Page.sj_dxtj_qddx_zc)
        sleep(1)
        # 选择注册/导入时间
        self.base_click_btn(Page.sj_dxtj_qddx_zc_xz)
        # 点击查询
        self.base_click_btn(Page.sj_dxtj_qddx_cx)
        sleep(5)

        # 点击人员电销统计
        self.base_aframe(Page.sj_dxtj_rydx)
        # 点击注册/导入时间
        self.base_click_btn(Page.sj_dxtj_rydx_zc)
        sleep(1)
        # 选择注册/导入时间
        self.base_click_btn(Page.sj_dxtj_rydx_zc_xz)
        # 点击渠道/导入标签
        self.base_click_btn(Page.sj_dxtj_rydx_qd)
        sleep(1)
        # 选择渠道/导入标签
        self.base_click_btn(Page.sj_dxtj_rydx_qd_xz)
        # 点击导出数据
        # self.base_click_btn(Page.sj_dxtj_rydx_dcsj)
        # 点击查询
        self.base_click_btn(Page.sj_dxtj_rydx_cx)
        sleep(5)

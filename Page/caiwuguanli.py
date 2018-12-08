from time import sleep

import Page
from Base.base import Base


class PageCaiWu(Base):
    # 点击代付管理
    def page_click_cwdfgl(self, cw_dfgl_jygl_ddbh, cw_dfgl_jygl_name, cw_dfgl_jygl_phone, cw_dfgl_jygl_jydh,
                          cw_dfgl_zjzhgl_jydh, cw_dfgl_hkjygl_ddbh, cw_dfgl_hkjygl_jydh,
                          cw_dfgl_hkjygl_yhmc, cw_dfgl_hkjygl_yhdh):
        self.base_frame_back()
        # 点击财务管理
        self.base_click_btn(Page.cwgl)
        # 点击代付交易管理
        self.base_aframe(Page.cw_dfgl_jygl)
        # 输入订单编号
        self.base_input_text(Page.cw_dfgl_jygl_ddbh, cw_dfgl_jygl_ddbh)
        # 输入客户姓名
        self.base_input_text(Page.cw_dfgl_jygl_name, cw_dfgl_jygl_name)
        # 输入客户电话
        self.base_input_text(Page.cw_dfgl_jygl_phone, cw_dfgl_jygl_phone)
        # 输入交易单号
        self.base_input_text(Page.cw_dfgl_jygl_jydh, cw_dfgl_jygl_jydh)
        # 点击出款账号
        self.base_click_btn(Page.cw_dfgl_jygl_ckzh)
        sleep(1)
        # 选择出款账号
        self.base_click_btn(Page.cw_dfgl_jygl_xzzh)
        # 点击财务类型
        self.base_click_btn(Page.cw_dfgl_jygl_cwlx)
        sleep(1)
        # 选择财务类型
        self.base_click_btn(Page.cw_dfgl_jygl_xzlx)
        # 交易时间
        # 点击查询
        self.base_click_btn(Page.cw_dfgl_jygl_cx)
        # 点击导出数据
        # self.base_click_btn(Page.cw_dfgl_jygl_dcsj)
        sleep(5)

        # 点击资金账户管理
        self.base_aframe(Page.cw_dfgl_zjzhgl)
        # 点击资金账户
        self.base_click_btn(Page.cw_dfgl_zjzhgl_zjzh)
        sleep(1)
        # 选择资金账户
        self.base_click_btn(Page.cw_dfgl_zjzhgl_xzzjzh)
        # 点击财务类型
        self.base_click_btn(Page.cw_dfgl_zjzhgl_cwlx)
        sleep(1)
        # 选择财务类型
        self.base_click_btn(Page.cw_dfgl_zjzhgl_xzcwlx)
        # 输入交易单号
        self.base_input_text(Page.cw_dfgl_zjzhgl_jydh, cw_dfgl_zjzhgl_jydh)
        # 选择收支类型
        self.base_click_btn(Page.cw_dfgl_zjzhgl_sr)
        sleep(1)
        self.base_click_btn(Page.cw_dfgl_zjzhgl_zc)
        # 中心交易时间
        # 点击添加交易
        # self.base_click_btn(Page.cw_dfgl_zjzhgl_tjjy)
        # 点击新增账户
        # self.base_click_btn(Page.cw_dfgl_zjzhgl_xzzh)
        # 点击导出数据
        # self.base_click_btn(Page.cw_dfgl_zjzhgl_dcsj)
        # 点击查看
        # self.base_click_btn(Page.cw_dfgl_zjzhgl_ck)
        # 点击关闭
        # self.base_click_btn(Page.cw_dfgl_zjzhglc_gb)
        # 点击查询
        self.base_click_btn(Page.cw_dfgl_zjzhgl_cx)
        sleep(5)

        # 点击还款交易管理
        self.base_aframe(Page.cw_dfgl_hkjygl)
        # 输入订单编号
        self.base_input_text(Page.cw_dfgl_hkjygl_ddbh, cw_dfgl_hkjygl_ddbh)
        # 输入交易单号
        self.base_input_text(Page.cw_dfgl_hkjygl_jydh, cw_dfgl_hkjygl_jydh)
        # 输入用户名称
        self.base_input_text(Page.cw_dfgl_hkjygl_yhmc, cw_dfgl_hkjygl_yhmc)
        # 输入用户电话
        self.base_input_text(Page.cw_dfgl_hkjygl_yhdh, cw_dfgl_hkjygl_yhdh)
        # 点击所属省份
        self.base_click_btn(Page.cw_dfgl_hkjygl_sssf)
        sleep(1)
        # 选择所属省份
        self.base_click_btn(Page.cw_dfgl_hkjygl_xzsf)
        # 点击所属城市
        self.base_click_btn(Page.cw_dfgl_hkjygl_sscs)
        sleep(1)
        # 选择所属城市
        self.base_click_btn(Page.cw_dfgl_hkjygl_xzcs)
        # 点击时间类型
        self.base_click_btn(Page.cw_dfgl_hkjygl_sjlx)
        sleep(1)
        # 选择时间类型
        self.base_click_btn(Page.cw_dfgl_hkjygl_xzlx)
        # 点击查询
        self.base_click_btn(Page.cw_dfgl_hkjygl_cx)
        # 点击重置
        self.base_click_btn(Page.cw_dfgl_hkjygl_cz)
        # 点击查询
        self.base_click_btn(Page.cw_dfgl_hkjygl_cx)
        # 点击导出数据
        # self.base_click_btn(Page.cw_dfgl_hkjygl_dcsj)
        sleep(5)

    # 点击代扣管理
    def page_click_cwdkgl(self, cw_daikgl_jyjl_ddbh, cw_daikgl_jyjl_yhm, cw_daikgl_jyjl_khh, cw_daikgl_jyjl_yhkh):
        # 点击代扣交易记录
        self.base_iframe(Page.cw_daikgl, Page.cw_daikgl_jyjl)
        # 输入订单编号
        self.base_input_text(Page.cw_daikgl_jyjl_ddbh, cw_daikgl_jyjl_ddbh)
        # 输入用户名
        self.base_input_text(Page.cw_daikgl_jyjl_yhm, cw_daikgl_jyjl_yhm)
        # 输入开户行
        self.base_input_text(Page.cw_daikgl_jyjl_khh, cw_daikgl_jyjl_khh)
        # 输入银行卡号
        self.base_input_text(Page.cw_daikgl_jyjl_yhkh, cw_daikgl_jyjl_yhkh)
        # 点击代扣状态
        self.base_click_btn(Page.cw_daikgl_jyjl_dkzt)
        sleep(1)
        # 选择代扣状态
        self.base_click_btn(Page.cw_daikgl_jyjl_xzdkzt)
        # 代扣时间
        # 点击查询
        self.base_click_btn(Page.cw_daikgl_jyjl_cx)
        # 点击导出数据
        # self.base_click_btn(Page.cw_daikgl_jyjl_dcsj)
        sleep(5)

    # 点击还款管理
    def page_click_cwhkgl(self, cw_hkgl_dhzdgl_ddbh, cw_hkgl_dhzdgl_name,
                          cw_hkgl_dhzdgl_phone, cw_hkgl_zdgl_yhmc, cw_hkgl_zdgl_yhdh,
                          cw_hkgl_zdgl_ddbh, cw_hkgl_dhzd_ddbh, cw_hkgl_dhzd_yhmc, cw_hkgl_dhzd_yhdh):
        # 点击待还账单管理
        self.base_iframe(Page.cw_hkgl, Page.cw_hkgl_dhzdgl)
        # 输入订单编号
        self.base_input_text(Page.cw_hkgl_dhzdgl_ddbh, cw_hkgl_dhzdgl_ddbh)
        # 输入客户姓名
        self.base_input_text(Page.cw_hkgl_dhzdgl_name, cw_hkgl_dhzdgl_name)
        # 输入客户电话
        self.base_input_text(Page.cw_hkgl_dhzdgl_phone, cw_hkgl_dhzdgl_phone)
        # 点击业务类型
        self.base_click_btn(Page.cw_hkgl_dhzdgl_ywlx)
        sleep(1)
        # 选择业务类型
        self.base_click_btn(Page.cw_hkgl_dhzdgl_ywlx_xz)
        # 账单日
        # 点击查询
        self.base_click_btn(Page.cw_hkgl_dhzdgl_cx)
        # 点击导出数据
        # self.base_click_btn(Page.cw_hkgl_dhzdgl_dcsj)
        # 点击销账
        # 点击减免
        sleep(5)

        # 点击账单管理
        self.base_aframe(Page.cw_hkgl_zdgl)
        # 输入用户名称
        self.base_input_text(Page.cw_hkgl_zdgl_yhmc, cw_hkgl_zdgl_yhmc)
        # 输入用户电话
        self.base_input_text(Page.cw_hkgl_zdgl_yhdh, cw_hkgl_zdgl_yhdh)
        # 输入订单编号
        self.base_input_text(Page.cw_hkgl_zdgl_ddbh, cw_hkgl_zdgl_ddbh)
        # 点击查询
        self.base_click_btn(Page.cw_hkgl_zdgl_cx)
        sleep(5)

        # 点击待还账单
        self.base_aframe(Page.cw_hkgl_dhzd)
        # 输入订单编号
        self.base_input_text(Page.cw_hkgl_dhzd_ddbh, cw_hkgl_dhzd_ddbh)
        # 输入用户名称
        self.base_input_text(Page.cw_hkgl_dhzd_yhmc, cw_hkgl_dhzd_yhmc)
        # 输入用户电话
        self.base_input_text(Page.cw_hkgl_dhzd_yhdh, cw_hkgl_dhzd_yhdh)
        # 点击账单日
        # 点击所属省份
        self.base_click_btn(Page.cw_hkgl_dhzd_sssf)
        sleep(1)
        # 选择所属省份
        self.base_click_btn(Page.cw_hkgl_dhzd_sssf_xz)
        # 点击所属城市
        self.base_click_btn(Page.cw_hkgl_dhzd_sscs)
        sleep(1)
        # 选择所属城市
        self.base_click_btn(Page.cw_hkgl_dhzd_sscs_xz)
        # 点击查询
        self.base_click_btn(Page.cw_hkgl_dhzd_cx)
        # 点击重置
        self.base_click_btn(Page.cw_hkgl_dhzd_cz)
        sleep(5)

    # 点击资金账户管理
    def page_click_cwzjzhgl(self, cw_zjzhgl_baby_jydh):
        # 点击资金账户管理
        self.base_iframe(Page.cw_zjzhgl, Page.cw_zjzhgl_baby)
        # 点击资金账户
        self.base_click_btn(Page.cw_zjzhgl_baby_zjzh)
        sleep(1)
        # 选择资金账户
        self.base_click_btn(Page.cw_zjzhgl_baby_zjzh_xz)
        # 点击财务类型
        self.base_click_btn(Page.cw_zjzhgl_baby_cwlx)
        sleep(1)
        # 选择财务类型
        self.base_click_btn(Page.cw_zjzhgl_baby_cwlx_xz)
        # 输入交易单号
        self.base_input_text(Page.cw_zjzhgl_baby_jydh, cw_zjzhgl_baby_jydh)
        # 点击收支类型
        self.base_click_btn(Page.cw_zjzhgl_baby_sr)
        sleep(1)
        # 点击支出
        self.base_click_btn(Page.cw_zjzhgl_baby_zc)
        # 交易时间
        # 点击添加交易
        # self.base_click_btn(Page.cw_zjzhgl_baby_tjjy)
        # 点击新增账户
        # self.base_click_btn(Page.cw_zjzhgl_baby_xzzh)
        # 点击查询
        self.base_click_btn(Page.cw_zjzhgl_baby_cx)
        # 点击导出数据
        # self.base_click_btn(Page.cw_zjzhgl_baby_dcsj)
        # 点击查看
        # self.base_click_btn(Page.cw_zjzhgl_baby_ck)
        sleep(5)

    # 点击资金管理
    def page_click_cwzjgl(self, cw_zjgl_dsbdb_ddbh, cw_zjgl_dsbdb_name, cw_zjgl_ysbdb_ddbh, cw_zjgl_ysbdb_name,
                          cw_zjgl_sjsb_xmmc, cw_zjgl_sjsb_ym, cw_zjgl_sjsb_mysj, cw_zjgl_yjqdb_gjz):
        # 点击待上标订单
        self.base_iframe(Page.cw_zjgl, Page.cw_zjgl_dsbdb)
        # 输入订单编号
        self.base_input_text(Page.cw_zjgl_dsbdb_ddbh, cw_zjgl_dsbdb_ddbh)
        # 输入客户姓名
        self.base_input_text(Page.cw_zjgl_dsbdb_name, cw_zjgl_dsbdb_name)
        # 点击产品类型
        self.base_click_btn(Page.cw_zjgl_dsbdb_cplx)
        sleep(1)
        # 选择产品类型
        self.base_click_btn(Page.cw_zjgl_dsbdb_cplx_xz)
        # 单击分期数
        self.base_click_btn(Page.cw_zjgl_dsbdb_fqs)
        sleep(1)
        # 选择分期数
        self.base_click_btn(Page.cw_zjgl_dsbdb_fqs_xz)
        # 点击排序方式
        self.base_click_btn(Page.cw_zjgl_dsbdb_pxfs)
        sleep(1)
        # 选择排序方式
        self.base_click_btn(Page.cw_zjgl_dsbdb_pxfs_xz)
        # 点击查询
        self.base_click_btn(Page.cw_zjgl_dsbdb_cx)
        # 点击查看详情
        # self.base_click_btn(Page.cw_zjgl_dsbdb_ckxq)
        sleep(5)

        # 点击已上标订单
        self.base_aframe(Page.cw_zjgl_ysbdb)
        # 输入订单编号
        self.base_input_text(Page.cw_zjgl_ysbdb_ddbh, cw_zjgl_ysbdb_ddbh)
        # 输入客户姓名
        self.base_input_text(Page.cw_zjgl_ysbdb_name, cw_zjgl_ysbdb_name)
        # 点击产品类型
        self.base_click_btn(Page.cw_zjgl_ysbdb_cplx)
        sleep(1)
        # 选择产品类型
        self.base_click_btn(Page.cw_zjgl_ysbdb_cplx_xz)
        # 点击上标平台
        self.base_click_btn(Page.cw_zjgl_ysbdb_sbpt)
        sleep(1)
        # 选择上标平台
        self.base_click_btn(Page.cw_zjgl_ysbdb_sbpt_xz)
        # 点击是否打款
        self.base_click_btn(Page.cw_zjgl_ysbdb_sfdk)
        sleep(1)
        # 选择是否打款
        self.base_click_btn(Page.cw_zjgl_ysbdb_sfdk_xz)
        # 点击排序方式
        self.base_click_btn(Page.cw_zjgl_ysbdb_pxfs)
        sleep(1)
        # 选择排序方式
        self.base_click_btn(Page.cw_zjgl_ysbdb_pxfs_xz)
        # 点击分期数
        self.base_click_btn(Page.cw_zjgl_ysbdb_fqs)
        sleep(1)
        # 选择分期数
        self.base_click_btn(Page.cw_zjgl_ysbdb_fqs_xz)
        # 点击是否已导出
        self.base_click_btn(Page.cw_zjgl_ysbdb_sfydc)
        sleep(1)
        # 选择是否已导出
        self.base_click_btn(Page.cw_zjgl_ysbdb_sfydc_xz)
        # 点击查询
        self.base_click_btn(Page.cw_zjgl_ysbdb_cx)
        # 点击查看详情
        # self.base_click_btn(Page.cw_zjgl_ysbdb_ckxq)
        # 点击返回
        # self.base_click_btn(Page.cw_zjgl_ysbdb_back)
        sleep(5)

        # 点击实际上标
        self.base_aframe(Page.cw_zjgl_sjsb)
        # 输入项目名称
        self.base_input_text(Page.cw_zjgl_sjsb_xmmc, cw_zjgl_sjsb_xmmc)
        # 点击上标日期
        # 输入页码
        self.base_input_text(Page.cw_zjgl_sjsb_ym, cw_zjgl_sjsb_ym)
        # 输入每页数据
        self.base_input_text(Page.cw_zjgl_sjsb_mysj, cw_zjgl_sjsb_mysj)
        # 点击查询
        self.base_click_btn(Page.cw_zjgl_sjsb_cx)
        sleep(5)

        # 点击已结清订单
        self.base_aframe(Page.cw_zjgl_yjqdb)
        # 点击筛选时间类型
        self.base_click_btn(Page.cw_zjgl_yjqdb_sxsjlx)
        sleep(1)
        # 选择筛选时间类型
        self.base_click_btn(Page.cw_zjgl_yjqdb_sxsjlx_xz)
        # 点击回款来源
        self.base_click_btn(Page.cw_zjgl_yjqdb_hkly)
        sleep(1)
        # 选择回款来源
        self.base_click_btn(Page.cw_zjgl_yjqdb_hkly_xz)
        # 输入关键字
        self.base_input_text(Page.cw_zjgl_yjqdb_gjz, cw_zjgl_yjqdb_gjz)
        # 点击查询
        self.base_click_btn(Page.cw_zjgl_yjqdb_cx)
        sleep(5)

    # 点击打款管理
    def page_click_cwdakgl(self, cw_dkgl_wdk_ddbh, cw_dkgl_wdk_name, cw_dkgl_ydk_ddbh, cw_dkgl_ydk_name,
                           cw_dkgl_dktj_dkzh):
        # 点击未打款
        self.base_iframe(Page.cw_dkgl, Page.cw_dkgl_wdk)
        # 输入订单编号
        self.base_input_text(Page.cw_dkgl_wdk_ddbh, cw_dkgl_wdk_ddbh)
        # 输入客户姓名
        self.base_input_text(Page.cw_dkgl_wdk_name, cw_dkgl_wdk_name)
        # 选择审核通过日期
        # 点击查询
        self.base_click_btn(Page.cw_dkgl_wdk_cx)
        # 点击导出数据
        # self.base_click_btn(Page.cw_dkgl_wdk_dcsj)
        sleep(5)

        # 点击已打款
        self.base_aframe(Page.cw_dkgl_ydk)
        # 输入订单编号
        self.base_input_text(Page.cw_dkgl_ydk_ddbh, cw_dkgl_ydk_ddbh)
        # 输入客户姓名
        self.base_input_text(Page.cw_dkgl_ydk_name, cw_dkgl_ydk_name)
        # 点击审核通过日期
        # 点击查询
        self.base_click_btn(Page.cw_dkgl_ydk_cx)
        # 点击导出数据
        # self.base_click_btn(Page.cw_dkgl_ydk_dcsj)
        sleep(5)

        # 点击打款统计
        self.base_aframe(Page.cw_dkgl_dktj)
        # 打款时间
        # 输入打款账号
        self.base_input_text(Page.cw_dkgl_dktj_dkzh, cw_dkgl_dktj_dkzh)
        # 点击查询
        self.base_click_btn(Page.cw_dkgl_dktj_cx)
        sleep(5)

    # 点击还款交易
    def page_click_cwhkjy(self, cw_hkjy_baby_name, cw_hkjy_baby_shjyh):
        # 点击还款交易
        self.base_iframe(Page.cw_hkjy, Page.cw_hkjy_baby)
        # 输入用户名称
        self.base_input_text(Page.cw_hkjy_baby_name, cw_hkjy_baby_name)
        # 时间
        # 输入商户交易号
        self.base_input_text(Page.cw_hkjy_baby_shjyh, cw_hkjy_baby_shjyh)
        # 点击支付渠道
        self.base_click_btn(Page.cw_hkjy_baby_zfqd)
        sleep(1)
        # 选择支付渠道
        self.base_click_btn(Page.cw_hkjy_baby_zfqd_xz)
        # 点击查询
        self.base_click_btn(Page.cw_hkjy_baby_cx)
        # 点击导出
        # self.base_click_btn(Page.cw_hkjy_baby_dc)
        sleep(5)

    # 点击账单明细
    def page_click_cwzdmx(self, cw_zdmx_yqgl_yhmc, cw_zdmx_yqgl_ddbh, cw_zdmx_baby_yhmc, cw_zdmx_dhmx_yhmc,
                          cw_zdmx_zdgl_name, cw_zdmx_zdgl_phone, cw_zdmx_zdgl_ddbh, cw_zdmx_hkmx_yhmc,
                          cw_zdmx_yqmx_yhmc, cw_zdmx_hkdz_ddbh, cw_zdmx_hkdz_jydh, cw_zdmx_hkdz_name,
                          cw_zdmx_hkdz_phone, cw_zdmx_dhzd_ddbh, cw_zdmx_dhzd_yhmc, cw_zdmx_dhzd_yhdh):
        # 点击逾期管理
        self.base_iframe(Page.cw_zdmx, Page.cw_zdmx_yqgl)
        # 输入用户名单
        self.base_input_text(Page.cw_zdmx_yqgl_yhmc, cw_zdmx_yqgl_yhmc)
        # 还款日
        # 输入订单编号
        self.base_input_text(Page.cw_zdmx_yqgl_ddbh, cw_zdmx_yqgl_ddbh)
        # 点击查询
        self.base_click_btn(Page.cw_zdmx_yqgl_cx)
        # 点击导出
        # self.base_click_btn(Page.cw_zdmx_yqgl_dc)
        # 点击查看
        # self.base_click_btn(Page.cw_zdmx_yqgl_ck)
        sleep(5)

        # 点击账单明细
        self.base_aframe(Page.cw_zdmx_baby_zdmx)
        # 输入用户名称
        self.base_input_text(Page.cw_zdmx_baby_yhmc, cw_zdmx_baby_yhmc)
        # 点击还款日
        self.base_click_btn(Page.cw_zdmx_baby_hkr)
        sleep(1)
        # 选择还款日
        self.base_click_btn(Page.cw_zdmx_baby_hkr_xz)
        # 输入订单编号
        self.base_input_text(Page.cw_zdmx_baby_ddbh)
        # 点击查询
        self.base_click_btn(Page.cw_zdmx_baby_cx)
        # 点击重置
        self.base_click_btn(Page.cw_zdmx_baby_cz)
        # 点击返回
        self.base_click_btn(Page.cw_zdmx_baby_fh)
        # 点击导出
        # self.base_click_btn(Page.cw_zdmx_baby_dc)
        sleep(5)

        # 点击待还明细
        self.base_aframe(Page.cw_zdmx_dhmx)
        # 输入用户名称
        self.base_input_text(Page.cw_zdmx_dhmx_yhmc, cw_zdmx_dhmx_yhmc)
        # 点击还款日
        self.base_click_btn(Page.cw_zdmx_dhmx_hkr)
        sleep(1)
        # 选择还款日
        self.base_click_btn(Page.cw_zdmx_dhmx_hkr_xz)
        # 输入订单编号
        self.base_input_text(Page.cw_zdmx_dhmx_ddbh)
        # 点击查询
        self.base_click_btn(Page.cw_zdmx_dhmx_cx)
        # 点击重置
        self.base_click_btn(Page.cw_zdmx_dhmx_cz)
        # 点击返回
        self.base_click_btn(Page.cw_zdmx_dhmx_fh)
        # 点击导出
        # self.base_click_btn(Page.cw_zdmx_dhmx_dc)
        sleep(5)

        # 点击账单管理
        self.base_aframe(Page.cw_zdmx_zdgl)
        # 输入用户名
        self.base_input_text(Page.cw_zdmx_zdgl_name, cw_zdmx_zdgl_name)
        # 输入用户电话
        self.base_input_text(Page.cw_zdmx_zdgl_phone, cw_zdmx_zdgl_phone)
        # 输入订单编号
        self.base_input_text(Page.cw_zdmx_zdgl_ddbh, cw_zdmx_zdgl_ddbh)
        # 点击查询
        self.base_click_btn(Page.cw_zdmx_zdgl_cx)
        sleep(5)

        # 点击还款明细
        self.base_aframe(Page.cw_zdmx_hkmx)
        # 输入用户名称
        self.base_input_text(Page.cw_zdmx_hkmx_yhmc, cw_zdmx_hkmx_yhmc)
        # 点击还款日
        self.base_click_btn(Page.cw_zdmx_hkmx_hkr)
        sleep(1)
        # 选择还款日
        self.base_click_btn(Page.cw_zdmx_hkmx_hkr_xz)
        # 输入订单编号
        self.base_input_text(Page.cw_zdmx_hkmx_ddbh)
        # 点击查询
        self.base_click_btn(Page.cw_zdmx_hkmx_cx)
        # 点击重置
        self.base_click_btn(Page.cw_zdmx_hkmx_cz)
        # 点击返回
        self.base_click_btn(Page.cw_zdmx_hkmx_fh)
        # 点击导出
        # self.base_click_btn(Page.cw_zdmx_hkmx_dc)
        sleep(5)

        # 点击逾期明细
        self.base_aframe(Page.cw_zdmx_yqmx)
        # 输入用户名称
        self.base_input_text(Page.cw_zdmx_yqmx_yhmc, cw_zdmx_yqmx_yhmc)
        # 点击还款日
        self.base_click_btn(Page.cw_zdmx_yqmx_hkr)
        sleep(1)
        # 选择还款日
        self.base_click_btn(Page.cw_zdmx_yqmx_hkr_xz)
        # 输入订单编号
        self.base_input_text(Page.cw_zdmx_yqmx_ddbh)
        # 点击查询
        self.base_click_btn(Page.cw_zdmx_yqmx_cx)
        # 点击逾期未还
        self.base_click_btn(Page.cw_zdmx_yqmx_yqwh)
        # 点击逾期已还
        self.base_click_btn(Page.cw_zdmx_yqmx_yqyh)
        # 点击重置
        self.base_click_btn(Page.cw_zdmx_yqmx_cz)
        # 点击返回
        self.base_click_btn(Page.cw_zdmx_yqmx_fh)
        # 点击导出
        # self.base_click_btn(Page.cw_zdmx_yqmx_dc)
        sleep(5)

        # 点击还款对账
        self.base_aframe(Page.cw_zdmx_hkdz)
        # 输入订单编号
        self.base_input_text(Page.cw_zdmx_hkdz_ddbh, cw_zdmx_hkdz_ddbh)
        # 输入交易单号
        self.base_input_text(Page.cw_zdmx_hkdz_jydh, cw_zdmx_hkdz_jydh)
        # 输入用户名称
        self.base_input_text(Page.cw_zdmx_hkdz_name, cw_zdmx_hkdz_name)
        # 输入用户电话
        self.base_input_text(Page.cw_zdmx_hkdz_phone, cw_zdmx_hkdz_phone)
        # 点击所属省份
        self.base_click_btn(Page.cw_zdmx_hkdz_sssf)
        sleep(1)
        # 选择所属省份
        self.base_click_btn(Page.cw_zdmx_hkdz_sssf_xz)
        # 点击所属城市
        self.base_click_btn(Page.cw_zdmx_hkdz_sscs)
        sleep(1)
        # 选择所属城市
        self.base_click_btn(Page.cw_zdmx_hkdz_sscs_xz)
        # 点击时间类型
        self.base_click_btn(Page.cw_zdmx_hkdz_sjlx)
        sleep(1)
        # 选择数据类型
        self.base_click_btn(Page.cw_zdmx_hkdz_sjlx_xz)
        # 点击查询
        self.base_click_btn(Page.cw_zdmx_hkdz_cx)
        # 点击重置
        self.base_click_btn(Page.cw_zdmx_hkdz_cz)
        # 点击导出数据
        # self.base_click_btn(Page.cw_zdmx_hkdz_dcsj)
        sleep(5)

        # 点击待还账单
        self.base_aframe(Page.cw_zdmx_dhzd)
        # 输入订单编号
        self.base_input_text(Page.cw_zdmx_dhzd_ddbh, cw_zdmx_dhzd_ddbh)
        # 输入用户名称
        self.base_input_text(Page.cw_zdmx_dhzd_yhmc, cw_zdmx_dhzd_yhmc)
        # 输入用户电话
        self.base_input_text(Page.cw_zdmx_dhzd_yhdh, cw_zdmx_dhzd_yhdh)
        # 账单日
        # 点击所属省份
        self.base_click_btn(Page.cw_zdmx_dhzd_sssf)
        sleep(1)
        # 选择所属省份
        self.base_click_btn(Page.cw_zdmx_dhzd_sssf_xz)
        # 点击所属城市
        self.base_click_btn(Page.cw_zdmx_dhzd_sscs)
        sleep(1)
        # 选择所属城市
        self.base_click_btn(Page.cw_zdmx_dhzd_sscs_xz)
        # 点击查询
        self.base_click_btn(Page.cw_zdmx_dhzd_cx)
        # 点击重置
        self.base_click_btn(Page.cw_zdmx_dhzd_cz)
        sleep(5)

    # 点击债权对账
    def page_click_cwzqdz(self, cw_zqdz_mbxm_name, cw_zqdz_mbhkz_name, cw_zqdz_mbhkwc_name, cw_zqdz_hkdzzd_name,
                          cw_zqdz_jkdz_name, cw_zqdz_bzjfh_name, cw_zqdz_jywljl_lsh):
        # 点击满标项目
        self.base_iframe(Page.cw_zqdz, Page.cw_zqdz_mbxm)
        # 输入项目名称
        self.base_input_text(Page.cw_zqdz_mbxm_name, cw_zqdz_mbxm_name)
        # 点击状态
        self.base_click_btn(Page.cw_zqdz_mbxm_zt)
        sleep(1)
        # 选择状态
        self.base_click_btn(Page.cw_zqdz_mbxm_xzzt)
        # 满标日期
        # 点击查询
        self.base_click_btn(Page.cw_zqdz_mbxm_cx)
        sleep(5)

        # 点击满标还款中
        self.base_aframe(Page.cw_zqdz_mbhkz)
        # 输入项目名称
        self.base_input_text(Page.cw_zqdz_mbhkz_name, cw_zqdz_mbhkz_name)
        # 点击状态
        self.base_click_btn(Page.cw_zqdz_mbhkz_jkzt)
        sleep(1)
        # 选择状态
        self.base_click_btn(Page.cw_zqdz_mbhkz_jkzt_xz)
        # 满标日期
        # 点击查询
        self.base_click_btn(Page.cw_zqdz_mbhkz_cx)
        sleep(5)

        # 点击满标还款完成
        self.base_aframe(Page.cw_zqdz_mbhkwc)
        # 输入项目名称
        self.base_input_text(Page.cw_zqdz_mbhkwc_name, cw_zqdz_mbhkwc_name)
        # 点击保证金状态
        self.base_click_btn(Page.cw_zqdz_mbhkwc_bzjzt)
        sleep(1)
        # 选择保证金状态
        self.base_click_btn(Page.cw_zqdz_mbhkwc_bzjzt_xz)
        # 满标日期
        # 点击查询
        self.base_click_btn(Page.cw_zqdz_mbhkwc_cx)
        # 点击账单明细
        self.base_click_btn(Page.cw_zqdz_mbhkwc_zdmx)
        sleep(5)
        # 点击返回
        self.base_click_btn(Page.cw_zqdz_mbhkwc_zdmx_back)
        # 点击保证金返还
        sleep(5)

        # 点击还款对账账单
        self.base_aframe(Page.cw_zqdz_hkdzzd)
        # 项目名称
        self.base_input_text(Page.cw_zqdz_hkdzzd_name, cw_zqdz_hkdzzd_name)
        # 点击账单状态
        self.base_click_btn(Page.cw_zqdz_hkdzzd_zdzt)
        sleep(1)
        # 选择账单状态
        self.base_click_btn(Page.cw_zqdz_hkdzzd_zdzt_xz)
        # 点击账单日
        self.base_click_btn(Page.cw_zqdz_hkdzzd_zdr)
        sleep(1)
        # 选择账单日
        self.base_click_btn(Page.cw_zqdz_hkdzzd_zdr_xz)
        # 点击查询
        self.base_click_btn(Page.cw_zqdz_hkdzzd_cx)
        sleep(5)

        # 点击借款到账
        self.base_aframe(Page.cw_zqdz_jkdz)
        # 输入项目名称
        self.base_input_text(Page.cw_zqdz_jkdz_name, cw_zqdz_jkdz_name)
        # 点击到账日期
        self.base_click_btn(Page.cw_zqdz_jkdz_dzrq)
        sleep(1)
        # 选择到账日期
        self.base_click_btn(Page.cw_zqdz_jkdz_dzrq_xz)
        # 点击查询
        self.base_click_btn(Page.cw_zqdz_jkdz_cx)
        sleep(5)

        # 点击提现记录
        self.base_aframe(Page.cw_zqdz_txjl)
        # 点击转入银行卡
        self.base_click_btn(Page.cw_zqdz_txjl_zryhk)
        sleep(1)
        # 选择转入银行卡
        self.base_click_btn(Page.cw_zqdz_txjl_zryhk_xz)
        # 交易时间
        # 点击查询
        self.base_click_btn(Page.cw_zqdz_txjl_cx)
        sleep(5)

        # 点击充值记录
        self.base_aframe(Page.cw_zqdz_czjl)
        # 点击充值方式
        self.base_click_btn(Page.cw_zqdz_czjl_czfs)
        sleep(1)
        # 选择充值方式
        self.base_click_btn(Page.cw_zqdz_czjl_czfs_xz)
        # 交易时间
        # 点击查询
        self.base_click_btn(Page.cw_zqdz_czjl_cx)
        sleep(5)

        # 点击保证金返还
        self.base_aframe(Page.cw_zqdz_bzjfh)
        # 输入项目名称
        self.base_input_text(Page.cw_zqdz_bzjfh_name, cw_zqdz_bzjfh_name)
        # 点击返还日期
        self.base_click_btn(Page.cw_zqdz_bzjfh_fhrq)
        sleep(1)
        # 选择返还日期
        self.base_click_btn(Page.cw_zqdz_bzjfh_fhrq_xz)
        # 点击查询
        self.base_click_btn(Page.cw_zqdz_bzjfh_cx)
        sleep(5)

        # 点击交易往来记录
        self.base_aframe(Page.cw_zqdz_jywljl)
        # 点击交易类型
        self.base_click_btn(Page.cw_zqdz_jywljl_jylx)
        sleep(1)
        # 选择交易类型
        self.base_click_btn(Page.cw_zqdz_jywljl_jylx_xz)
        # 输入流水号
        self.base_input_text(Page.cw_zqdz_jywljl_lsh, cw_zqdz_jywljl_lsh)
        # 交易时间
        # 点击查询
        self.base_click_btn(Page.cw_zqdz_jywljl_cx)
        sleep(5)

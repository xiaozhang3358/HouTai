from time import sleep

import Page
from Base.base import Base


class PageXiTong(Base):
    # 点击权限管理
    def page_click_xtqxgl(self, xt_qxgl_cdgl_xg_px, xt_qxgl_cdgl_tj_mc, xt_qxgl_cdgl_tj_px, xt_qxgl_rygl_dlm,
                          xt_qxgl_rygl_name, xt_qxgl_lzgl_dlm, xt_qxgl_lzgl_name):
        self.base_frame_back()
        # 点击系统设置
        self.base_click_btn(Page.xtsz)
        # 点击菜单管理
        self.base_aframe(Page.xt_qxgl_cdgl)
        # 点击修改
        self.base_click_btn(Page.xt_qxgl_cdgl_lb_xg)
        # 点击修改排序
        self.base_input_text(Page.xt_qxgl_cdgl_xg_px, xt_qxgl_cdgl_xg_px)
        # 点击修改是否可见
        self.base_click_btn(Page.xt_qxgl_cdgl_xg_kj)
        # 是否同步到工作流
        self.base_click_btn(Page.xt_qxgl_cdgl_xg_tb)
        # 点击保存
        # self.base_click_btn(Page.xt_qxgl_cdgl_xg_save)
        # 点击返回
        self.base_click_btn(Page.xt_qxgl_cdgl_xg_back)
        sleep(1)
        # 点击菜单添加
        self.base_click_btn(Page.xt_qxgl_cdgl_tj)
        # 选择上级菜单
        # 输入名称
        self.base_input_text(Page.xt_qxgl_cdgl_tj_mc, xt_qxgl_cdgl_tj_mc)
        # 选择排序
        self.base_input_text(Page.xt_qxgl_cdgl_tj_px, xt_qxgl_cdgl_tj_px)
        # 是否可见
        self.base_click_btn(Page.xt_qxgl_cdgl_tj_kj)
        # 是否同步
        self.base_click_btn(Page.xt_qxgl_cdgl_tj_tb)
        # 点击保存
        # self.base_click_btn(Page.xt_qxgl_cdgl_tj_save)
        # 点击返回
        self.base_click_btn(Page.xt_qxgl_cdgl_tj_back)

        # 点击删除
        # 添加下级菜单
        # 保存排序
        # 同步工作流权限
        sleep(5)
        # 点击角色管理
        self.base_aframe(Page.xt_qxgl_jsgl)
        sleep(1)
        # 点击人员管理
        self.base_aframe(Page.xt_qxgl_rygl)
        # 输入登录名
        self.base_input_text(Page.xt_qxgl_rygl_dlm, xt_qxgl_rygl_dlm)
        # 输入姓名
        self.base_input_text(Page.xt_qxgl_rygl_name, xt_qxgl_rygl_name)
        # 点击角色
        self.base_click_btn(Page.xt_qxgl_rygl_js)
        sleep(1)
        # 选择角色
        self.base_click_btn(Page.xt_qxgl_rygl_xzjs)
        # 点击查询
        self.base_click_btn(Page.xt_qxgl_rygl_cx)
        # 点击导出
        # self.base_click_btn(Page.xt_qxgl_rygl_dc)
        sleep(5)

        # 点击离职管理
        self.base_aframe(Page.xt_qxgl_lzgl)
        # 输入登录名
        self.base_input_text(Page.xt_qxgl_lzgl_dlm, xt_qxgl_lzgl_dlm)
        # 输入姓名
        self.base_input_text(Page.xt_qxgl_lzgl_name, xt_qxgl_lzgl_name)
        # 点击角色
        self.base_click_btn(Page.xt_qxgl_lzgl_js)
        sleep(1)
        # 选择角色
        self.base_click_btn(Page.xt_qxgl_lzgl_xzjs)
        # 点击查询
        self.base_click_btn(Page.xt_qxgl_lzgl_cx)
        # 点击导出
        # self.base_click_btn(Page.xt_qxgl_lzgl_dc)
        sleep(5)

    # 点击系统日志
    def page_click_xtrz(self, xt_xtrz_yhid, xt_xtrz_url, xt_xtrz_dxrz_phone, xt_xtrz_dxrz_dxnr, xt_xtrz_dxrz_id,
                        xt_xtrz_dxrz_ip, xt_xtrz_jskhdx_phone, xt_xtrz_jskhdx_ip):
        # 点击操作日志
        self.base_iframe(Page.xt_xtrz, Page.xt_xtrz_czrz)
        # 输入用户id
        self.base_input_text(Page.xt_xtrz_yhid, xt_xtrz_yhid)
        # 输入url
        self.base_input_text(Page.xt_xtrz_url, xt_xtrz_url)
        # 日期
        # 点击异常信息
        self.base_click_btn(Page.xt_xtrz_ycxx)
        # 点击查询
        self.base_click_btn(Page.xt_xtrz_cx)
        sleep(5)

        # 点击短信日志
        self.base_aframe(Page.xt_xtrz_dxrz)
        # 输入手机号
        self.base_input_text(Page.xt_xtrz_dxrz_phone, xt_xtrz_dxrz_phone)
        # 输入短信内容
        self.base_input_text(Page.xt_xtrz_dxrz_dxnr, xt_xtrz_dxrz_dxnr)
        # 输入短信id
        self.base_input_text(Page.xt_xtrz_dxrz_id, xt_xtrz_dxrz_id)
        # 输入ip地址
        self.base_input_text(Page.xt_xtrz_dxrz_ip, xt_xtrz_dxrz_ip)
        # 点击回执状态
        self.base_click_btn(Page.xt_xtrz_dxrz_hzzt)
        sleep(1)
        # 选择回执状态
        self.base_click_btn(Page.xt_xtrz_dxrz_xzzt)
        # 发送时间
        # 点击查询
        self.base_click_btn(Page.xt_xtrz_dxrz_cx)
        # 催收短信发送
        sleep(5)

        # 点击接收客户短信
        self.base_aframe(Page.xt_xtrz_jskhdx)
        # 输入手机号
        self.base_input_text(Page.xt_xtrz_jskhdx_phone, xt_xtrz_jskhdx_phone)
        # 输入请求ip
        self.base_input_text(Page.xt_xtrz_jskhdx_ip, xt_xtrz_jskhdx_ip)
        # 发送时间
        # 点击状态
        self.base_click_btn(Page.xt_xtrz_jskhdx_zt)
        sleep(1)
        # 选择状态
        self.base_click_btn(Page.xt_xtrz_jskhdx_xzzt)
        # 点击查询
        self.base_click_btn(Page.xt_xtrz_jskhdx_cx)
        # 点击阅读
        # self.base_click_btn(Page.xt_xtrz_jskhdx_yd)
        sleep(5)

        # 点击定时任务日志
        self.base_aframe(Page.xt_xtrz_dsrwrz)
        # 点击任务描述
        self.base_click_btn(Page.xt_xtrz_dsrwrz_rwms)
        sleep(1)
        # 选择任务描述
        self.base_click_btn(Page.xt_xtrz_dsrwrz_rwms_xz)
        # 选择时间
        # 点击查询
        self.base_click_btn(Page.xt_xtrz_dsrwrz_cx)
        sleep(5)

    # 点击数据字典
    def page_click_xtsjzd(self, xt_sjzd_zdgl_ms, xt_sjzd_zdgl_tj_jz, xt_sjzd_zdgl_tj_bq, xt_sjzd_zdgl_tj_lx,
                          xt_sjzd_zdgl_tj_ms, xt_sjzd_zdgl_tj_px, xt_sjzd_dhkgl_lb_gspt, xt_sjzd_dhkgl_lb_phone):
        # 点击字典管理
        self.base_iframe(Page.xt_sjzd, Page.xt_sjzd_zdgl)
        # 点击类型
        self.base_click_btn(Page.xt_sjzd_zdgl_lx)
        sleep(1)
        # 选择类型
        self.base_click_btn(Page.xt_sjzd_zdgl_xzlx)
        # 输入描述
        self.base_input_text(Page.xt_sjzd_zdgl_ms, xt_sjzd_zdgl_ms)
        # 点击查询
        self.base_click_btn(Page.xt_sjzd_zdgl_cx)
        # 修改
        # self.base_click_btn(Page.xt_sjzd_zdgl_lb_xg)
        # self.base_click_btn(Page.xt_sjzd_zdgl_xg_back)
        # 删除
        # 添加键值对
        sleep(5)

        # 点击字典添加
        self.base_click_btn(Page.xt_sjzd_zdgl_tj)
        # 输入键值
        self.base_input_text(Page.xt_sjzd_zdgl_tj_jz, xt_sjzd_zdgl_tj_jz)
        # 输入标签
        self.base_input_text(Page.xt_sjzd_zdgl_tj_bq, xt_sjzd_zdgl_tj_bq)
        # 输入类型
        self.base_input_text(Page.xt_sjzd_zdgl_tj_lx, xt_sjzd_zdgl_tj_lx)
        # 输入描述
        self.base_input_text(Page.xt_sjzd_zdgl_tj_ms, xt_sjzd_zdgl_tj_ms)
        # 输入排序
        self.base_input_text(Page.xt_sjzd_zdgl_tj_px, xt_sjzd_zdgl_tj_px)
        # 点击保存
        # self.base_click_btn(Page.xt_sjzd_zdgl_tj_save)
        # 点击返回
        self.base_click_btn(Page.xt_sjzd_zdgl_tj_back)
        sleep(2)

        # 点击电话库管理
        self.base_aframe(Page.xt_sjzd_dhkgl)
        # 库列表--归属平台
        self.base_input_text(Page.xt_sjzd_dhkgl_lb_gspt, xt_sjzd_dhkgl_lb_gspt)
        # 点击归属类型
        self.base_click_btn(Page.xt_sjzd_dhkgl_lb_gslx)
        sleep(1)
        # 选择归属类型
        self.base_click_btn(Page.xt_sjzd_dhkgl_lb_xzlx)
        # 输入电话号码
        self.base_input_text(Page.xt_sjzd_dhkgl_lb_phone, xt_sjzd_dhkgl_lb_phone)
        # 点击查询
        self.base_click_btn(Page.xt_sjzd_dhkgl_lb_cx)
        # 点击修改
        self.base_click_btn(Page.xt_sjzd_dhkgl_lb_xg)
        # 点击修改页面返回
        self.base_click_btn(Page.xt_sjzd_dhkgl_xg_back)
        # 点击删除
        sleep(2)

        # 点击机构管理
        self.base_aframe(Page.xt_sjzd_jggl)
        sleep(2)
        # 点击区域管理
        self.base_aframe(Page.xt_sjzd_qygl)
        sleep(5)

    # 点击利率管理
    def page_click_xtllgl(self, xt_llgl_dq_lb_szll_qs, xt_llgl_dq_lb_szll_ll, xt_llgl_qll_lb_qs, xt_llgl_qll_tj_qs,
                          xt_llgl_qll_tj_ll):
        # 点击地区利率
        self.base_iframe(Page.xt_llgl, Page.xt_llgl_dq)
        # 点击状态
        self.base_click_btn(Page.xt_llgl_dq_lb_zt)
        sleep(1)
        # 选择状态
        self.base_click_btn(Page.xt_llgl_dq_lb_zc)
        # 点击查询
        self.base_click_btn(Page.xt_llgl_dq_lb_cx)
        # 点击更新缓存中
        self.base_click_btn(Page.xt_llgl_dq_lb_gx)
        sleep(5)
        # 点击地区利率添加
        self.base_click_btn(Page.xt_llgl_dq_tj)
        sleep(2)
        # 点击添加页面返回
        self.base_click_btn(Page.xt_llgl_dq_tj_back)
        sleep(3)
        self.base_click_btn(Page.xt_llgl_dq_lb_x)
        # 点击列表页面设置利率
        self.base_click_btn(Page.xt_llgl_dq_lb_szll)
        # 输入期数
        self.base_input_text(Page.xt_llgl_dq_lb_szll_qs, xt_llgl_dq_lb_szll_qs)
        # 点击利率类型
        self.base_click_btn(Page.xt_llgl_dq_lb_szll_lllx)
        sleep(1)
        # 选择利率类型
        self.base_click_btn(Page.xt_llgl_dq_lb_szll_lllx_xz)
        # 输入利率
        self.base_input_text(Page.xt_llgl_dq_lb_szll_ll, xt_llgl_dq_lb_szll_ll)
        # 点击保存
        # self.base_click_btn(Page.xt_llgl_dq_lb_szll_save)
        # 点击返回
        self.base_click_btn(Page.xt_llgl_dq_lb_szll_back)
        sleep(3)
        self.base_click_btn(Page.xt_llgl_dq_lb_x)
        # 点击查看利率
        self.base_click_btn(Page.xt_llgl_dq_lb_ckll)
        sleep(1)
        # 点击查看利率返回
        self.base_click_btn(Page.xt_llgl_dq_lb_ckll_back)
        # 点击删除
        sleep(3)


        # 点击期利率
        self.base_aframe(Page.xt_llgl_qll)
        # 输入期数
        self.base_input_text(Page.xt_llgl_qll_lb_qs, xt_llgl_qll_lb_qs)
        # 点击利率类型
        self.base_click_btn(Page.xt_llgl_qll_lb_lx)
        sleep(1)
        # 选择利率类型
        self.base_click_btn(Page.xt_llgl_qll_lb_lhq)
        # 点击状态
        self.base_click_btn(Page.xt_llgl_qll_lb_zt)
        sleep(1)
        # 选择状态
        self.base_click_btn(Page.xt_llgl_qll_lb_zc)
        # 点击查询
        self.base_click_btn(Page.xt_llgl_qll_lb_cx)
        # 点击修改
        self.base_click_btn(Page.xt_llgl_qll_lb_xg)
        # 点击修改-返回
        self.base_click_btn(Page.xt_llgl_qll_xg_back)
        # 点击删除
        sleep(2)
        # 点击期利率添加
        self.base_click_btn(Page.xt_llgl_qll_tj)
        # 输入期数
        self.base_input_text(Page.xt_llgl_qll_tj_qs, xt_llgl_qll_tj_qs)
        # 点击利率类型
        self.base_click_btn(Page.xt_llgl_qll_tj_lx)
        sleep(1)
        # 选择利率类型
        self.base_click_btn(Page.xt_llgl_qll_tj_lhq)
        # 输入利率
        self.base_input_text(Page.xt_llgl_qll_tj_ll, xt_llgl_qll_tj_ll)
        # 点击保存
        # self.base_click_btn(Page.xt_llgl_qll_tj_save)
        # 点击返回
        self.base_click_btn(Page.xt_llgl_qll_tj_back)

"""
表单元素
"""
# 导航栏表单
from selenium.webdriver.common.by import By

menuframe = 'menuFrame'
# 功能表单
mainframe = 'mainFrame'

"""
功能元素
"""
# 电销中心
dxzx = By.XPATH, 'html/body/div[1]/div[2]/div/div[2]/ul[1]/li[1]/a'
# 订单中心
ddzx = By.XPATH, 'html/body/div[1]/div[2]/div/div[2]/ul[1]/li[2]/a'
# 风控中心
fkzx = By.XPATH, 'html/body/div[1]/div[2]/div/div[2]/ul[1]/li[3]/a'
# 债务管理
zwgl = By.XPATH, 'html/body/div[1]/div[2]/div/div[2]/ul[1]/li[4]/a'
# 数据看板
sjkb = By.XPATH, 'html/body/div[1]/div[2]/div/div[2]/ul[1]/li[5]/a'
# 运营管理
yygl = By.XPATH, 'html/body/div[1]/div[2]/div/div[2]/ul[1]/li[6]/a'
# 财务管理
cwgl = By.XPATH, 'html/body/div[1]/div[2]/div/div[2]/ul[1]/li[7]/a'
# 系统设置
xtsz = By.XPATH, 'html/body/div[1]/div[2]/div/div[2]/ul[1]/li[8]/a'

"""
登录页面元素
"""
# 账户名
username = By.ID, 'username'
# 密码
pwd = By.ID, 'password'
# 登录按钮
login_btn = By.CSS_SELECTOR, '.btn.btn-primary'

# 获取电销中心的元素
#     电销管理
dx = By.XPATH, 'html/body/div[1]/div/div[1]/a'
# 客户导入
khdr = By.XPATH, "html/body/div[1]/div/div[2]/div/ul/li[1]/a"
# 客户管理
dx_khgl = By.XPATH, "html/body/div[1]/div/div[2]/div/ul/li[2]/a"
# 售前营销
sqyx = By.XPATH, "html/body/div[1]/div/div[2]/div/ul/li[4]/a"
# 老客户唤醒营销
lkh = By.XPATH, "html/body/div[1]/div/div[2]/div/ul/li[5]/a"
# 营销记录
yxjl = By.XPATH, "html/body/div[1]/div/div[2]/div/ul/li[6]/a"
# 待签约客户
dqy = By.XPATH, 'html/body/div[1]/div/div[2]/div/ul/li[3]/a'

"""
客户导入页面元素
"""
# 批次号
pch = By.CSS_SELECTOR, '#batch'
# 操作员
czy = By.CSS_SELECTOR, '#workName'
# 电话号码
phone = By.CSS_SELECTOR, '#phone'
# 创建时间
# 开始时间
startTime = By.CSS_SELECTOR, '#startTime'
# 表单名称
iframe = By.XPATH, 'html/body/div[2]/iframe'
# 选择今天
today = By.CSS_SELECTOR, '#dpTodayInput'
# 结束时间
endTime = By.CSS_SELECTOR, '#endTime'
# 查询
cx = By.CSS_SELECTOR, '[value="查询"]'
# 电话号码导入
dhdr = By.CSS_SELECTOR, '[value="电话号码导入"]'
# 下载TXT模板
downtxt = By.CSS_SELECTOR, '[value="下载TXT模板"]'
# 下载Excel模板
downexcel = By.CSS_SELECTOR, '[value="下载Excel模板"]'
"""
客户管理页面元素
"""
# 客户状态
dx_gl_khzt = By.XPATH, 'html/body/div[1]/form/div[1]/div/a'
# 选择未下单
dx_gl_ddywc = By.XPATH, 'html/body/div[10]/ul/li[3]/div'
# 拜访状态
dx_gl_bfzt = By.XPATH, 'html/body/div[1]/form/div[2]/div/a'
# 选择拜访状态（电话空号）
dx_gl_dhkh = By.XPATH, 'html/body/div[11]/ul/li[6]/div'
# 电销员
dxy = By.XPATH, 'html/body/div[1]/form/div[3]/input'
# 拜访次数
bfcs = By.XPATH, 'html/body/div[1]/form/div[4]/input'
# 导入来源
drly = By.XPATH, 'html/body/div[1]/form/div[5]/input'
# 注册来源
zcly = By.XPATH, 'html/body/div[1]/form/div[6]/input'
# 时间筛选
dx_gl_sxsj = By.XPATH, 'html/body/div[1]/form/div[7]/div/a'
# 选择导入时间
dx_gl_sxsj_dr = By.XPATH, 'html/body/div[12]/ul/li[3]/div'
# 查询
cx_gl = By.XPATH, 'html/body/div[1]/form/div[8]/input'
# 全选
dx_gl_qx = By.CSS_SELECTOR, '#revCheck'
# 批量提取
dx_gl_pltq = By.CSS_SELECTOR, '#extractGroup'
# 批量分配
dx_gl_plfp = By.CSS_SELECTOR, '#distributionGroup'

"""
售前营销页面元素
"""
# 客户状态
dx_sq_kh = By.XPATH, 'html/body/div[1]/form/div[1]/div/a'
# 选择未下单
dx_sq_wxd = By.XPATH, 'html/body/div[8]/ul/li[4]/div'
# 客户姓名
sqyx_name = By.CSS_SELECTOR, '#name'
# 电话号码
sqyx_phone = By.CSS_SELECTOR, '#phone'
# 拜访次数
sqyx_bfcs = By.CSS_SELECTOR, '#callTimes'
# 导入来源
sqyx_drly = By.XPATH, 'html/body/div[1]/form/div[5]/input'
# 注册来源
sqyx_zcly = By.CSS_SELECTOR, '#regChannelName'
# 拜访来源
dx_sq_bfzt = By.XPATH, 'html/body/div[1]/form/div[7]/div/a'
# 选择有意向
dx_sq_yyx = By.XPATH, 'html/body/div[9]/ul/li[2]/div'
# 时间筛选
dx_sq_sjsx = By.XPATH, 'html/body/div[1]/form/div[8]/div/a'
# 选择注册时间
dx_sq_zcsj = By.XPATH, 'html/body/div[10]/ul/li[2]/div'

# 查询
sqyx_cx = By.CSS_SELECTOR, '#btnSubmit'

"""
老客户唤醒营销页面元素
"""
# 客户姓名
lkh_name = By.CSS_SELECTOR, '#name'
# 电话号码
lkh_phone = By.CSS_SELECTOR, '#phone'
# 点击客户状态
lkh_khzt = By.XPATH, 'html/body/div[1]/form/div[3]/div/a'
# 选择客户状态（订单废弃）
lkh_khzt_xz = By.XPATH, 'html/body/div[8]/ul/li[3]/div'
# 选择距离完结时间
dx_lkh_jl = By.XPATH, 'html/body/div[1]/form/div[4]/div/a'
# 选择大于
dx_lkh_dy = By.XPATH, 'html/body/div[9]/ul/li[2]/div'
# 输入天数
dx_lkh_day = By.XPATH, 'html/body/div[1]/form/div[4]/input'
# 拜访状态
dx_lkh_bfzt = By.XPATH, 'html/body/div[1]/form/div[5]/div/a'
# 选择有意向
dx_lkh_yyx = By.XPATH, 'html/body/div[10]/ul/li[2]/div'
# 查询
lkh_cx = By.XPATH, 'html/body/div[1]/form/div[7]/input'

"""
营销记录页面元素
"""
# 客户姓名
yxjl_name = By.CSS_SELECTOR, '#name'
# 电话号码
yxjl_phone = By.CSS_SELECTOR, '#phone'
# 操作员
yxjl_czy = By.CSS_SELECTOR, '#workName'
# 查询
yxjl_cx = By.CSS_SELECTOR, '#btnSubmit'

"""
待签约客户页面元素
"""
# 客户姓名
dqy_name = By.XPATH, 'html/body/div[1]/form/div[1]/input'
# 电话号码
dqy_phone = By.XPATH, 'html/body/div[1]/form/div[2]/input'
# 提醒状态
dqy_tx = By.XPATH, 'html/body/div[1]/form/div[3]/div/a'
# 选择稍后签约
dqy_tx_sh = By.XPATH, 'html/body/div[8]/ul/li[2]/div'
# 查询
dqy_cx = By.XPATH, 'html/body/div[1]/form/div[4]/input'

"""
订单中心页面元素
"""
# 订单审核
ddsh = By.XPATH, 'html/body/div[1]/div[1]/div[1]/a'

# 订单列表
dd_ddlb = By.XPATH, 'html/body/div[1]/div[1]/div[2]/div/ul/li[1]/a'
"""
订单列表页面元素
"""
# 订单编号
dd_lb_ddbh = By.CSS_SELECTOR, '#sn'
# 订单状态
dd_lb_ddzt = By.XPATH, 'html/body/div[1]/form/div[2]/div/a'
# 选择待审核
dd_lb_dsh = By.XPATH, 'html/body/div[9]/ul/li[2]/div'
# 客户姓名
dd_lb_name = By.CSS_SELECTOR, '#username'
# 手机号
dd_lb_phone = By.CSS_SELECTOR, '#phone'
# 所属省份
dd_lb_sf = By.XPATH, 'html/body/div[1]/form/div[5]/div[1]/a'
# 选择河南省
dd_lb_hn = By.XPATH, 'html/body/div[10]/ul/li[4]/div'
# 所属城市
dd_lb_cs = By.XPATH, 'html/body/div[1]/form/div[5]/div[2]/a'
# 选择郑州市
dd_lb_zzs = By.XPATH, 'html/body/div[11]/ul/li[3]/div'
# 客户来源
dd_lb_ly = By.CSS_SELECTOR, '#reg_form'
# 初审人
dd_lb_csr = 'cpath', 'html/body/div[1]/form/div[8]/div[1]/a'
# 选择王世斌
dd_lb_wsb = By.XPATH, 'html/body/div[12]/ul/li[2]/div'
# 终审人
dd_lb_zsr = By.XPATH, 'html/body/div[1]/form/div[8]/div[2]/a'
# 选择年临泽
dd_lb_nlz = By.XPATH, 'html/body/div[13]/ul/li[3]/div'
# 查询
dd_lb_cx = By.CSS_SELECTOR, '.btn.btn-success'


# 主管审核
dd_zgsh = By.XPATH, 'html/body/div[1]/div[1]/div[2]/div/ul/li[3]/a'
"""
主管审核页面元素
"""
# 订单编号
dd_zg_ddbh = By.CSS_SELECTOR, '#sn'
# 客户姓名
dd_zg_name = By.CSS_SELECTOR, '#username'
# 手机号
dd_zg_phone = By.CSS_SELECTOR, '#phone'
# 查询
dd_zg_cx = By.CSS_SELECTOR, '.btn.btn-success'

# 订单审核
dd_ddsh = By.XPATH, 'html/body/div[1]/div[1]/div[2]/div/ul/li[2]/a'
"""
订单审核页面元素
"""
# 订单编号
dd_ddsh_ddbh = By.CSS_SELECTOR, '#sn'
# 客户姓名
dd_ddsh_name = By.CSS_SELECTOR, '#username'
# 手机号
dd_ddsh_phone = By.CSS_SELECTOR, '#phone'
# 查询
dd_ddsh_cx = By.CSS_SELECTOR, '.btn.btn-success'

# 待签约客户
dd_dqy = By.XPATH, 'html/body/div[1]/div[1]/div[2]/div/ul/li[4]/a'
"""
待签约客户页面元素
"""
# 订单编号
dd_dqy_ddbh = By.XPATH, 'html/body/div[1]/form/div[1]/input'
# 用户姓名
dd_dqy_name = By.XPATH, 'html/body/div[1]/form/div[2]/input'
# 手机号
dd_dqy_phone = By.XPATH, 'html/body/div[1]/form/div[3]/input'
# 查询
dd_dqy_cx = By.XPATH, 'html/body/div[1]/form/input[2]'

# 订单管理
ddgl = By.XPATH, 'html/body/div[1]/div[2]/div[1]/a'
# 处理量监控
dd_clljk = By.XPATH, 'html/body/div[1]/div[2]/div[2]/div/ul/li[1]/a'
# 点击选择订单创建时间
dd_ddcjsj = By.XPATH, 'html/body/div[2]/div[1]/div[2]/div/input[1]'
# 选择上个月
dd_ddcjsj_xz = By.XPATH, 'html/body/div[3]/div[1]/ul/li[5]'
# 点击订单完成时间
dd_ddwcsj = By.XPATH, 'html/body/div[2]/div[1]/div[3]/div/input[1]'
# 选择上个月
dd_ddwcsj_xz= By.XPATH, 'html/body/div[4]/div[1]/ul/li[5]'
# 点击查询
dd_cll_cx = By.XPATH, 'html/body/div[2]/div[1]/div[4]/button'

# 订单调度
dd_dddd = By.XPATH, 'html/body/div[1]/div[2]/div[2]/div/ul/li[2]/a'



"""
风控中心页面
"""
# 风控决策管理
fkjcgl = By.XPATH, 'html/body/div[1]/div[1]/div[1]/a'
# 决策管理
fk_jcgl = By.XPATH, 'html/body/div[1]/div[1]/div[2]/div/ul/li[1]/a'
# 调用记录管理
fk_dyjlgl = By.XPATH, 'html/body/div[1]/div[1]/div[2]/div/ul/li[2]/a'

# 风控规则命中率
fk_fkgzmzl = By.XPATH, 'html/body/div[1]/div[1]/div[2]/div/ul/li[3]/a'
# 策略名称
fk_gzmzl_clmc = By.XPATH, 'html/body/div[2]/div[1]/div[2]/div/span/span[1]/span/span[1]'
# 选择策略名称
fk_gzmzl_clmc_xz = By.XPATH, 'html/body/span/span/span[2]/ul/li[2]'
# 点击时间
fk_gzmzl_sj = By.XPATH, 'html/body/div[2]/div[1]/div[3]/div/input[1]'
# 选择上个月
fk_gzmzl_sj_xz = By.XPATH, 'html/body/div[3]/div[1]/ul/li[5]'
# 查询
fk_gzmzl_cx = By.XPATH, 'html/body/div[2]/div[1]/div[4]/button'


# 接口管理
jkgl = By.XPATH, 'html/body/div[1]/div[2]/div[1]/a'
# 接口配置
fk_jkpz = By.XPATH, 'html/body/div[1]/div[2]/div[2]/div/ul/li[1]/a'
# 接口调用记录
fk_jkdyjl = By.XPATH, 'html/body/div[1]/div[2]/div[2]/div/ul/li[2]/a'
# 申请时间
fk_jk_sqsj = By.XPATH, 'html/body/div[1]/div[1]/form/div/div/div[1]/div/input[1]'
# 选择申请事件
fk_jk_sqsj_xz = By.XPATH, 'html/body/div[2]/div[1]/ul/li[5]'
# 接口名称
fk_jk_jkmc = By.XPATH, 'html/body/div[1]/div[1]/form/div/div/div[2]/div/select'
# 清空
fk_jk_qk = By.XPATH, 'html/body/div[1]/div[1]/form/div/div/div[3]/button[1]'
# 筛选
fk_jk_sx = By.XPATH, 'html/body/div[1]/div[1]/form/div/div/div[3]/button[2]'

# 账户管理
zhgl = By.XPATH, 'html/body/div[1]/div[3]/div[1]/a'
# 交易记录
fk_jyjl = By.XPATH, 'html/body/div[1]/div[3]/div[2]/div/ul/li/a'
# 费用事项
fk_zh_fysx = By.XPATH, 'html/body/div[1]/div[1]/form/div/div/div[1]/div/input'
# 申请时间
fk_zh_sqsj = By.XPATH, 'html/body/div[1]/div[1]/form/div/div/div[2]/div/input[1]'
# 选择申请时间
fk_zh_sqsj_xz = By.XPATH, 'html/body/div[2]/div[1]/ul/li[5]'
# 清空
fk_zh_qk = By.XPATH, 'html/body/div[1]/div[1]/form/div/div/div[3]/button[1]'
# 筛选
fk_zh_sx = By.XPATH, 'html/body/div[1]/div[1]/form/div/div/div[3]/button[2]'

# 调用日志管理
dyrzgl = By.XPATH, 'html/body/div[1]/div[4]/div[1]/a'

# 黑名单管理
hmdgl = By.XPATH, 'html/body/div[1]/div[5]/div[1]/a'
# 黑名单库
fk_hmdk = By.XPATH, 'html/body/div[1]/div[5]/div[2]/div/ul/li[1]/a'
# 黑名单列表
# 内容
fk_hmd_nr = By.XPATH, 'html/body/div[1]/form/div[1]/input'
# 点击来源
fk_hmd_ly = By.XPATH, 'html/body/div[1]/form/div[2]/div/a'
# 选择来源
fk_hmd_ly_xz = By.XPATH, 'html/body/div[5]/ul/li[2]/div'
# 点击黑灰名单
fk_hmd_md = By.XPATH, 'html/body/div[1]/form/div[3]/div/a'
# 选择黑灰名单
fk_hmd_md_xz = By.XPATH, 'html/body/div[6]/ul/li[2]/div'
# 查询
fk_hmd_cx = By.XPATH, 'html/body/div[1]/form/div[4]/input'
# 黑名单添加
fk_hmdk_tj = By.XPATH, 'html/body/div[1]/div/ul/li[2]/a'
# 点击黑灰名单类型
fk_hmd_mdlx = By.XPATH, 'html/body/div[1]/form/div[1]/div/div/a'
# 选择黑灰名单类型
fk_hmd_mdlx_xz = By.XPATH, 'html/body/div[3]/ul/li[2]/div'
# 点击拉黑灰名单
fk_hmdk_tj_lmd = By.XPATH, 'html/body/div[1]/form/div[2]/div/div/a'
# 选择拉黑灰名单
fk_hmdk_tj_lmd_xz = By.XPATH, 'html/body/div[4]/ul/li[1]/div'
# 输入内容信息
fk_hmdk_tj_nrxx = By.XPATH, 'html/body/div[1]/form/div[4]/div/input'
# 点击来源
fk_hmdk_tj_ly = By.XPATH, 'html/body/div[1]/form/div[5]/div/div/a'
# 选择来源
fk_hmdk_tj_ly_xz = By.XPATH, 'html/body/div[5]/ul/li[1]/div'
# 输入拉黑原因
fk_hmdk_tj_lhyy = By.XPATH, 'html/body/div[1]/form/div[6]/div/textarea'
# 点击保存
fk_hmdk_tj_save = By.XPATH, 'html/body/div[1]/form/div[7]/input[1]'
# 点击返回
fk_hmdk_tj_back = By.XPATH, 'html/body/div[1]/form/div[7]/input[2]'


# 客户管理
khgl = By.XPATH, 'html/body/div[1]/div[6]/div[1]/a'
# 资质认证管理
fk_zzrzgl = By.XPATH, 'html/body/div[1]/div[6]/div[2]/div/ul/li/a'
# 客户联系方式
fk_kh_phone = By.XPATH, 'html/body/div[1]/form/div[1]/input'
# 检索
fk_kh_js = By.XPATH, 'html/body/div[1]/form/div[2]/input'

"""
债务管理页面元素
"""
# 贷中管理
zw_dzgl = By.XPATH, 'html/body/div[1]/div[1]/div[1]/a'
# 还款提醒
zw_dz_hktx = By.XPATH, 'html/body/div[1]/div[1]/div[2]/div/ul/li[1]/a'
# 客户姓名
zw_dz_hktx_name = By.XPATH, 'html/body/div[2]/div[1]/div[2]/input'
# 客户电话
zw_dz_hktx_phone = By.XPATH, 'html/body/div[2]/div[1]/div[3]/input'
# 订单编号
zw_dz_hktx_ddbh = By.XPATH, 'html/body/div[2]/div[1]/div[4]/input'
# 用户状态
zw_dz_hktx_yhzt = By.XPATH, 'html/body/div[2]/div[1]/div[5]/select'
# 账单状态
zw_dz_hktx_zdzt = By.XPATH, 'html/body/div[2]/div[1]/div[6]/select'
# 剩余天数
zw_dz_hktx_syts = By.XPATH, 'html/body/div[2]/div[1]/div[7]/select'
# 提醒结果
zw_dz_hktx_txjg = By.XPATH, 'html/body/div[2]/div[1]/div[8]/select'
# 点击责任人
zw_dz_hktx_zrr = By.XPATH, 'html/body/div[2]/div[1]/div[9]/span/span[1]/span/span[1]'
# 选择责任人
zw_dz_hktx_zrr_xz = By.XPATH, 'html/body/span/span/span[2]/ul/li[2]'
# 输入提醒次数
zw_dz_hktx_txcs = By.XPATH, 'html/body/div[2]/div[1]/div[10]/input'
# 点击下次跟进时间
zw_dz_hktx_xcgjsj = By.XPATH, 'html/body/div[2]/div[1]/div[11]/div/input[1]'
# 选择下次跟进时间
zw_dz_hktx_xcgjsj_xz = By.XPATH, 'html/body/div[3]/div[1]/ul/li[5]'
# 点击账单日
zw_dz_hktx_zdr = By.XPATH, 'html/body/div[2]/div[1]/div[12]/div/input[1]'
# 选择账单日
zw_dz_hktx_zdr_xz = By.XPATH, 'html/body/div[4]/div[1]/ul/li[3]'
# 查询
zw_dz_hktx_cx = By.XPATH, 'html/body/div[2]/div[1]/div[13]/button'
# 点击全选
# 点击已分配
# 点击批量分配
# 点击一键分配

# 提醒记录管理
zw_dz_txjl = By.XPATH, 'html/body/div[1]/div[1]/div[2]/div/ul/li[2]/a'
# 客户姓名
zw_dz_txjl_name = By.XPATH, 'html/body/div[1]/form/div[1]/input'
# 客户电话
zw_dz_txjl_phone = By.XPATH, 'html/body/div[1]/form/div[2]/input'
# 操作时间
# 提醒结果
# 用户状态
# 查询
zw_dz_txjl_cx = By.XPATH, 'html/body/div[1]/form/div[6]/input'


# 贷后催收
zw_dhcs = By.XPATH, 'html/body/div[1]/div[3]/div[1]/a'
# 逾期客户池
zw_dhcs_yqkhc = By.XPATH, 'html/body/div[1]/div[3]/div[2]/div/ul/li[1]/a'
# 客户姓名
zw_dhcs_yqkhc_name = By.XPATH, 'html/body/div[1]/form/div[1]/input'
# 客户电话
zw_dhcs_yqkhc_phone = By.XPATH, 'html/body/div[1]/form/div[2]/input'
# 订单编号
zw_dhcs_yqkhc_ddbh = By.XPATH, 'html/body/div[1]/form/div[3]/input'
# 账单状态
# 委案状态
# 责任人
# 账单日
# 查询
zw_dhcs_yqkhc_cx = By.XPATH, 'html/body/div[1]/form/div[8]/input'

# 逾期催款
zw_dhcs_yqcs = By.XPATH, 'html/body/div[1]/div[3]/div[2]/div/ul/li[2]/a'
# 客户姓名
zw_dhcs_yqcs_name = By.XPATH, 'html/body/div[2]/form/div[1]/input'
# 客户电话
zw_dhcs_yqcs_phone = By.XPATH, 'html/body/div[2]/form/div[2]/input'
# 查询
zw_dhcs_yqcs_cx = By.XPATH, 'html/body/div[2]/form/div[7]/input'

# 催收记录管理
zw_dhcs_csjlgl = By.XPATH, 'html/body/div[1]/div[3]/div[2]/div/ul/li[3]/a'
# 客户姓名
zw_dhcs_csjlgl_name = By.XPATH, 'html/body/div[2]/form/div[1]/input'
# 客户电话
zw_dhcs_csjlgl_phone = By.XPATH, 'html/body/div[2]/form/div[2]/input'
# 查询
zw_dhcs_csjlgl_cx = By.XPATH, 'html/body/div[2]/form/div[6]/input'

# 委案批次管理
zw_dhcs_wapcgl = By.XPATH, 'html/body/div[1]/div[3]/div[2]/div/ul/li[4]/a'
# 委案批次号
zw_dhcs_wapcgl_pch = By.XPATH, 'html/body/div[1]/form/div[1]/input'
# 机构名称
zw_dhcs_wapcgl_jgmc = By.XPATH, 'html/body/div[1]/form/div[2]/input'
# 查询
zw_dhcs_wapcgl_cx = By.XPATH, 'html/body/div[1]/form/div[4]/input'

# 委案案件中心
zw_dhcs_waajzx = By.XPATH, 'html/body/div[1]/div[3]/div[2]/div/ul/li[5]/a'
# 客户姓名
zw_dhcs_waajzx_name = By.XPATH, 'html/body/div[1]/form/div[1]/input'
# 客户电话
zw_dhcs_waajzx_phone = By.XPATH, 'html/body/div[1]/form/div[2]/input'
# 订单编号
zw_dhcs_waajzx_ddbh = By.XPATH, 'html/body/div[1]/form/div[3]/input'
# 案件批次
zw_dhcs_waajzx_ajpc = By.XPATH, 'html/body/div[1]/form/div[4]/input'
# 查询
zw_dhcs_waajzx_cx = By.XPATH, 'html/body/div[1]/form/div[7]/input'

# 回款明细
zw_dhcs_hkmx = By.XPATH, 'html/body/div[1]/div[3]/div[2]/div/ul/li[6]/a'
# 客户姓名
zw_dhcs_hkmx_name = By.XPATH, 'html/body/div[1]/form/div[1]/input'
# 客户电话
zw_dhcs_hkmx_phone = By.XPATH, 'html/body/div[1]/form/div[2]/input'
# 委案批次号
zw_dhcs_hkmx_wapch = By.XPATH, 'html/body/div[1]/form/div[3]/input'
# 订单编号
zw_dhcs_hkmx_ddbh = By.XPATH, 'html/body/div[1]/form/div[4]/input'
# 查询
zw_dhcs_hkmx_cx = By.XPATH, 'html/body/div[1]/form/div[7]/input'


# 待还管理
zw_dhgl = By.XPATH, 'html/body/div[1]/div[2]/div[1]/a'
# 待还款客户
zw_dh_kh = By.XPATH, 'html/body/div[1]/div[2]/div[2]/div/ul/li/a'
# 订单编号
zw_dh_kh_ddbh = By.XPATH, 'html/body/div[1]/form/div[1]/input'
# 客户姓名
zw_dh_kh_name = By.XPATH, 'html/body/div[1]/form/div[2]/input'
# 客户电话
zw_dh_kh_phone = By.XPATH, 'html/body/div[1]/form/div[3]/input'
# 业务类型
# 账单日
# 查询
zw_dh_kh_cx = By.XPATH, 'html/body/div[1]/form/div[6]/input[1]'
# 导出数据
zw_dh_kh_dc = By.XPATH, 'html/body/div[1]/form/div[6]/input[2]'



# 委外机构管理
zw_wwjggl = By.XPATH, 'html/body/div[1]/div[4]/div[1]/a'
# 机构管理
zw_jggl = By.XPATH, 'html/body/div[1]/div[4]/div[2]/div/ul/li[1]/a'
# 机构列表
zw_jggl_jglb = By.XPATH, 'html/body/div[2]/div/ul/li[1]/a'
# 添加机构
zw_jggl_tjjg = By.XPATH, 'html/body/div[2]/div/ul/li[2]/a'
# 机构名称
zw_jggl_jgmc = By.XPATH, 'html/body/div[2]/form/div[1]/input'
# 机构状态
# 创建时间
# 检索
zw_jggl_js = By.XPATH, 'html/body/div[2]/form/div[4]/input'

# 人员管理
zw_rygl = By.XPATH, 'html/body/div[1]/div[4]/div[2]/div/ul/li[2]/a'
# 人员列表
zw_rygl_rylb = By.XPATH, 'html/body/div[2]/div/ul/li[1]/a'
# 人员添加
zw_rygl_rytj = By.XPATH, 'html/body/div[2]/div/ul/li[2]/a'
# 人员姓名
zw_rygl_name = By.XPATH, 'html/body/div[2]/form/div[1]/input'
# 联系电话
zw_rygl_phone = By.XPATH, 'html/body/div[2]/form/div[2]/input'
# 人员状态
# 催收机构
# 人员角色
# 查询
zw_rygl_cx = By.XPATH, 'html/body/div[2]/form/div[6]/input'

# 日报报表
zw_rbbb = By.XPATH, 'html/body/div[1]/div[5]/div[1]/a'
# 委外机构日报
zw_rbbb_wwjgrb = By.XPATH, 'html/body/div[1]/div[5]/div[2]/div/ul/li[1]/a'
# 初期
zw_rbbb_wwjgrb_cq = By.XPATH, 'html/body/div[2]/div[1]/div[1]/ul/li[1]'
# 中期
zw_rbbb_wwjgrb_zq = By.XPATH, 'html/body/div[2]/div[1]/div[1]/ul/li[2]'
# 高期
zw_rbbb_wwjgrb_gq = By.XPATH, 'html/body/div[2]/div[1]/div[1]/ul/li[3]'
# 委外机构
zw_rbbb_wwjgrb_wwjg = By.XPATH, 'html/body/div[2]/div[1]/div[2]/span/span[1]/span/span[1]'
zw_rbbb_wwjgrb_wwjg_xz = By.XPATH, 'html/body/span/span/span[2]/ul/li[3]'
# 日期
zw_rbbb_wwjgrb_rq = By.XPATH, 'html/body/div[2]/div[1]/div[3]/div/input[1]'
zw_rbbb_wwjgrb_rq_xz = By.XPATH, 'html/body/div[3]/div[1]/ul/li[2]'
# 查询
zw_rbbb_wwjgrb_cx = By.XPATH, 'html/body/div[2]/div[1]/div[4]/button'

# 催收员日报
zw_rbbb_csyrb = By.XPATH, 'html/body/div[1]/div[5]/div[2]/div/ul/li[2]/a'
# 催收员
zw_rbbb_csyrb_csy = By.XPATH, 'html/body/div[2]/div[1]/div[2]/input'
# 账龄
zw_rbbb_csyrb_zl = By.XPATH, 'html/body/div[2]/div[1]/div[3]/span/span[1]/span/span[1]'
zw_rbbb_csyrb_zl_xz = By.XPATH, 'html/body/span/span/span[2]/ul/li[3]'
# 日期
zw_rbbb_csyrb_rq = By.XPATH, 'html/body/div[2]/div[1]/div[4]/div/input[1]'
zw_rbbb_csyrb_rq_xz = By.XPATH, 'html/body/div[3]/div[1]/ul/li[2]'
# 查询
zw_rbbb_csyrb_cx = By.XPATH, 'html/body/div[2]/div[1]/div[5]/button'

# 催收员过程日报
zw_rbbb_csygcrb = By.XPATH, 'html/body/div[1]/div[5]/div[2]/div/ul/li[3]/a'
# 催收员
zw_rbbb_csygcrb_csy = By.XPATH, 'html/body/div[2]/div[1]/div[2]/input'
# 账龄
zw_rbbb_csygcrb_zl = By.XPATH, 'html/body/div[2]/div[1]/div[3]/span/span[1]/span/span[1]'
zw_rbbb_csygcrb_zl_xz = By.XPATH, 'html/body/span/span/span[2]/ul/li[3]'
# 日期
zw_rbbb_csygcrb_rq = By.XPATH, 'html/body/div[2]/div[1]/div[4]/div/input[1]'
zw_rbbb_csygcrb_rq_xz = By.XPATH, 'html/body/div[3]/div[1]/ul/li[2]'
# 查询
zw_rbbb_csygcrb_cx = By.XPATH, 'html/body/div[2]/div[1]/div[5]/button'

# 委外机构过程日报
zw_rbbb_wwjggcrb = By.XPATH, 'html/body/div[1]/div[5]/div[2]/div/ul/li[4]/a'
# 委外机构
zw_rbbb_wwjggcrb_wwjg = By.XPATH, 'html/body/div[2]/div[1]/div[2]/span/span[1]/span/span[1]'
zw_rbbb_wwjggcrb_wwjg_xz = By.XPATH, 'html/body/span/span/span[2]/ul/li[3]'
# 账龄
zw_rbbb_wwjggcrb_zl = By.XPATH, 'html/body/div[2]/div[1]/div[3]/span/span[1]/span/span[1]'
zw_rbbb_wwjggcrb_zl_xz = By.XPATH, 'html/body/span/span/span[2]/ul/li[3]'
# 日期
zw_rbbb_wwjggcrb_rq = By.XPATH, 'html/body/div[2]/div[1]/div[4]/div/input[1]'
zw_rbbb_wwjggcrb_rq_xz = By.XPATH, 'html/body/div[3]/div[1]/ul/li[2]'
# 查询
zw_rbbb_wwjggcrb_cx = By.XPATH, 'html/body/div[2]/div[1]/div[5]/button'


# 月报报表
zw_ybbb = By.XPATH, 'html/body/div[1]/div[6]/div[1]/a'
# 催收员业绩月报
zw_ybbb_csyyjyb = By.XPATH, 'html/body/div[1]/div[6]/div[2]/div/ul/li[1]/a'
# 月份
zw_ybbb_csyyjyb_yf = By.XPATH, 'html/body/div[1]/div[1]/div[2]/input'
# 名字
zw_ybbb_csyyjyb_name = By.XPATH, 'html/body/div[1]/div[1]/div[3]/input'
# 账龄
zw_ybbb_csyyjyb_zl = By.XPATH, 'html/body/div[1]/div[1]/div[4]/input'
# 查询
zw_ybbb_csyyjyb_cx = By.XPATH, 'html/body/div[1]/div[1]/div[5]/button'

# 委外机构月报
zw_ybbb_wwjgyb = By.XPATH, 'html/body/div[1]/div[6]/div[2]/div/ul/li[2]/a'
# 月份
zw_ybbb_wwjgyb_yf = By.XPATH, 'html/body/div[1]/div[1]/div[2]/input'
# 委外机构
zw_ybbb_wwjgyb_wwjg = By.XPATH, 'html/body/div[1]/div[1]/div[3]/input'
# 查询
zw_ybbb_wwjgyb_cx = By.XPATH, 'html/body/div[1]/div[1]/div[4]/button'

# 资产月报
zw_ybbb_zcyb = By.XPATH, 'html/body/div[1]/div[6]/div[2]/div/ul/li[3]/a'
# 月份
zw_ybbb_zcyb_yf = By.XPATH, 'html/body/div[1]/div[1]/div[2]/input'
# 查询
zw_ybbb_zcyb_cx = By.XPATH, 'html/body/div[1]/div[1]/div[3]/button'

"""
数据看板页面元素
"""
# 财务总量统计
sj_cwzltj = By.XPATH, 'html/body/div[1]/div[1]/div[1]/a'
# 财务总量
sj_cwtj_zl = By.XPATH, 'html/body/div[1]/div[1]/div[2]/div/ul/li/a'
# 放款额走势
sj_cwtj_zl_fkezs = By.XPATH, 'html/body/div[1]/div/ul/li[1]/a'
# 债务数据统计
sj_cwtj_zl_zwsjtj = By.XPATH, 'html/body/div[1]/div/ul/li[2]/a'
# 项目名称
sj_cwtj_zl_name = By.XPATH, 'html/body/div[1]/form/div[1]/div/a'
# 选择项目名称
sj_cwtj_zl_name_xz = By.XPATH, 'html/body/div[4]/ul/li[3]/div'
# 日期
# 查询
sj_cwtj_zl_fkezs_cx = By.XPATH, 'html/body/div[1]/form/div[3]/input'
# 业务类型
sj_cwtj_zl_zwsjtj_ywlx = By.XPATH, 'html/body/div[1]/form/div[1]/div/a'
# 选择业务类型
sj_cwtj_zl_zwsjtj_ywlx_xz = By.XPATH, 'html/body/div[5]/ul/li[3]/div'
# 查询
sj_cwtj_zl_zwsjtj_cx = By.XPATH, 'html/body/div[1]/form/div[4]/input'

# 贷后统计
sj_dhtj = By.XPATH, 'html/body/div[1]/div[2]/div[1]/a'
# 还款数据统计
sj_dhtj_hksj = By.XPATH, 'html/body/div[1]/div[2]/div[2]/div/ul/li[1]/a'
# 客户类型
sj_dhtj_hksj_khlx = By.XPATH, 'html/body/div[2]/div[2]/div[1]/div/a'
# 选择客户类型
sj_dhtj_hksj_khlx_xz = By.XPATH, 'html/body/div[6]/ul/li[3]/div'
# 时间段
# 查询
sj_dhtj_hksj_cx = By.XPATH, 'html/body/div[2]/div[2]/div[3]/input[1]'
# 导出
sj_dhtj_hksj_dc = By.XPATH, 'html/body/div[2]/div[2]/div[3]/input[2]'

# 逾期数据统计
sj_dhtj_yqsj = By.XPATH, 'html/body/div[1]/div[2]/div[2]/div/ul/li[2]/a'
# 客户类型
sj_dhtj_yqsj_khlx = By.XPATH, 'html/body/div[1]/form/div[1]/div/a'
# 选择客户类型
sj_dhtj_yqsj_khlx_xz = By.XPATH, 'html/body/div[6]/ul/li[3]/div'
# 导出数据
sj_dhtj_yqsj_dcsj = By.XPATH, 'html/body/div[1]/form/div[3]/input[1]'
# 查询
sj_dhtj_yqsj_cx = By.XPATH, 'html/body/div[1]/form/div[3]/input[2]'

# 首逾统计
sj_dhtj_sytj = By.XPATH, 'html/body/div[1]/div[2]/div[2]/div/ul/li[3]/a'
# 客户类型
sj_dhtj_sytj_khlx = By.XPATH, 'html/body/div[1]/div[2]/div/a'
# 选择客户类型
sj_dhtj_sytj_khlx_xz = By.XPATH, 'html/body/div[5]/ul/li[2]/div'
# 时间段
# 查询
sj_dhtj_sytj_cx = By.XPATH, 'html/body/div[1]/div[4]/input[1]'
# 图表
sj_dhtj_sytj_tb = By.XPATH, 'html/body/div[1]/div[4]/input[2]'
# 导出
sj_dhtj_sytj_dc = By.XPATH, 'html/body/div[1]/div[4]/input[3]'

# 注册用户统计
sj_zcyh = By.XPATH, 'html/body/div[1]/div[4]/div[1]/a'
# 注册用户统计
sj_zcyh_tj = By.XPATH, 'html/body/div[1]/div[4]/div[2]/div/ul/li/a'
# 最近7天
sj_zcyh_tj_qi = By.XPATH, 'html/body/div[1]/form/div[1]/label[1]'
# 最近30天
sj_zcyh_tj_sst = By.XPATH, 'html/body/div[1]/form/div[1]/label[2]'
# 按月查询
sj_zcyh_tj_yue = By.XPATH, 'html/body/div[1]/form/div[1]/label[3]'
# 注册人数
sj_zcyh_tj_zcrs = By.XPATH, 'html/body/div[1]/form/div[3]/label[1]'
# 认证通过人数
sj_zcyh_tj_rztgrs = By.XPATH, 'html/body/div[1]/form/div[3]/label[2]'
# 订单申请数
sj_zcyh_tj_ddsqs = By.XPATH, 'html/body/div[1]/form/div[3]/label[3]'
# 订单通过数量
sj_zcyh_tj_ddtgsl = By.XPATH, 'html/body/div[1]/form/div[3]/label[4]'
# 成功放款本金
sj_zcyh_tj_cgfkbj = By.XPATH, 'html/body/div[1]/form/div[3]/label[5]'
# 推荐人手机号码
sj_zcyh_tj_phone = By.XPATH, 'html/body/div[1]/form/div[2]/input'
# 查询
sj_zcyh_tj_cx = By.XPATH, 'html/body/div[1]/form/div[4]/input'

# 统计报表
sj_tjbb = By.XPATH, 'html/body/div[1]/div[3]/div[1]/a'
# 资产报表统计
sj_tjbb_zcbb = By.XPATH, 'html/body/div[1]/div[3]/div[2]/div/ul/li[1]/a'
# 日期
# 查询
sj_tjbb_zcbb_cx = "xpath", 'html/body/div[2]/div[1]/div[3]/button'
# 导出数据
sj_tjbb_zcbb_dcsj = By.XPATH, 'html/body/div[2]/div[1]/div[3]/a'

# 贷中逾期统计
sj_tjbb_dzyq = By.XPATH, 'html/body/div[1]/div[3]/div[2]/div/ul/li[2]/a'
# 日期
# 查询
sj_tjbb_dzyq_cx = By.XPATH, 'html/body/div[2]/div[1]/div[3]/button'
# 导出数据
sj_tjbb_dzyq_dcsj = By.XPATH, 'html/body/div[2]/div[1]/div[3]/a'

# 贷前渠道统计
sj_tjbb_dqqd = By.XPATH, 'html/body/div[1]/div[3]/div[2]/div/ul/li[3]/a'
# 日期
# 渠道
sj_tjbb_dqqd_qd = By.XPATH, 'html/body/div[2]/div[1]/div[3]/div/span/span[1]/span/span[1]'
# 选择渠道
sj_tjbb_dqqd_xzqd = By.XPATH, 'html/body/span/span/span[2]/ul/li[4]'
# 查询
sj_tjbb_dqqd_cx = By.XPATH, 'html/body/div[2]/div[1]/div[4]/button'
# 导出数据\
sj_tjbb_dqqd_dcsj = By.XPATH, 'html/body/div[2]/div[1]/div[4]/a'

# 业务数据统计
sj_ywsj = By.XPATH, 'html/body/div[1]/div[5]/div[1]/a'
# 业务数据统计
sj_ywsj_tj = By.XPATH, 'html/body/div[1]/div[5]/div[2]/div/ul/li/a'
# 查询
sj_ywsj_tj_dc = By.XPATH, 'html/body/div[1]/div[1]/a'

# 渠道统计
sj_qdtj = By.XPATH, 'html/body/div[1]/div[6]/div[1]/a'
# 渠道贷后统计
sj_qdtj_dh = By.XPATH, 'html/body/div[1]/div[6]/div[2]/div/ul/li/a'
# 客户类型
sj_qdtj_dh_khlx = By.XPATH, 'html/body/div[1]/form/dev/div/a'
# 选择客户类型
sj_qdtj_dh_khlx_xz = By.XPATH, 'html/body/div[6]/ul/li[3]/div'
# 导出数据
sj_qdtj_dh_dcsj = By.XPATH, 'html/body/div[1]/form/div[2]/input[1]'
# 查询
sj_qdtj_dh_cx = By.XPATH, 'html/body/div[1]/form/div[2]/input[2]'

# 催收统计
sj_cstj = By.XPATH, 'html/body/div[1]/div[7]/div[1]/a'
# 催收考核统计
sj_cstj_kh = By.XPATH, 'html/body/div[1]/div[7]/div[2]/div/ul/li/a'
# 导出当月
sj_cstj_kh_dcdy = By.XPATH, 'html/body/div[1]/div/div/a[1]'
# 导出历史
sj_cstj_kh_dcls = By.XPATH, 'html/body/div[1]/div/div/a[2]'

# 电销统计
sj_dxtj = By.XPATH, 'html/body/div[1]/div[8]/div[1]/a'
# 渠道电销统计
sj_dxtj_qddx = By.XPATH, 'html/body/div[1]/div[8]/div[2]/div/ul/li[1]/a'
# 末次跟进时间
# 电销员
sj_dxtj_qddx_dxy = By.XPATH, 'html/body/div[1]/form/div[2]/div/a'
# 选择电销员
sj_dxtj_qddx_dxy_xz = By.XPATH, 'html/body/div[5]/ul/li[5]/div'
# 统计类型
sj_dxtj_qddx_tjlx = By.XPATH, 'html/body/div[1]/form/div[3]/div/a'
# 选择统计类型
sj_dxtj_qddx_tjlx_xz = By.XPATH, 'html/body/div[6]/ul/li[2]/div'
# 注册/导入时间
sj_dxtj_qddx_zc = By.XPATH, 'html/body/div[1]/form/div[4]/div/a'
# 选择注册/导入时间
sj_dxtj_qddx_zc_xz = By.XPATH, 'html/body/div[7]/ul/li[2]/div'
# 查询
sj_dxtj_qddx_cx = By.XPATH, 'html/body/div[1]/form/div[5]/input'

# 人员电销统计
sj_dxtj_rydx = By.XPATH, 'html/body/div[1]/div[8]/div[2]/div/ul/li[2]/a'
# 注册/导入时间
sj_dxtj_rydx_zc = By.XPATH, 'html/body/div[1]/form/div[2]/div/a'
# 选择注册/导入时间
sj_dxtj_rydx_zc_xz = By.XPATH, 'html/body/div[4]/ul/li[2]/div'
# 渠道/导入标签
sj_dxtj_rydx_qd = By.XPATH, 'html/body/div[1]/form/div[3]/div/a'
# 选择渠道/导入标签
sj_dxtj_rydx_qd_xz = By.XPATH, 'html/body/div[5]/ul/li[2]/div'
# 导出数据
sj_dxtj_rydx_dcsj = By.XPATH, 'html/body/div[1]/form/div[4]/input[1]'
# 查询
sj_dxtj_rydx_cx = By.XPATH, 'html/body/div[1]/form/div[4]/input[2]'

"""
运营管理页面元素
"""
# 渠道管理
yy_qdgl = By.XPATH, 'html/body/div[1]/div[1]/div[1]/a'
# 推广渠道管理
yy_qdgl_tg = By.XPATH, 'html/body/div[1]/div[1]/div[2]/div/ul/li[1]/a'
# 渠道名称
yy_qdgl_tg_mc = By.XPATH, 'html/body/div[1]/form/div[1]/input'
# 渠道手机号
yy_qdgl_tg_phone = By.XPATH, 'html/body/div[1]/form/div[2]/input'
# 查询
yy_qdgl_tg_cx = By.XPATH, 'html/body/div[1]/form/div[3]/input'

# 渠道注册用户统计
yy_qdgl_qdzc = By.XPATH, 'html/body/div[1]/div[1]/div[2]/div/ul/li[3]/a'
# 最近7天
yy_qdgl_qdzc_qi = By.XPATH, 'html/body/div[1]/form/div[1]/label[1]'
# 选择最近30天
yy_qdgl_qdzc_sst = By.XPATH, 'html/body/div[1]/form/div[1]/label[2]'
# 按月查询
yy_qdgl_qdzc_yue = By.XPATH, 'html/body/div[1]/form/div[1]/label[3]'
# 输入推荐人手机号
yy_qdgl_qdzc_phone = By.XPATH, 'html/body/div[1]/form/div[2]/input'
# 选择注册人数
yy_qdgl_qdzc_zcrs = By.XPATH, 'html/body/div[1]/form/div[3]/label[1]'
# 认证通过人数
yy_qdgl_qdzc_rztgrs = By.XPATH, 'html/body/div[1]/form/div[3]/label[2]'
# 选择订单申请数
yy_qdgl_qdzc_ddsqs = By.XPATH, 'html/body/div[1]/form/div[3]/label[3]'
# 订单通过数量
yy_qdgl_qdzc_ddtgsl = By.XPATH, 'html/body/div[1]/form/div[3]/label[4]'
# 成功放款本金
yy_qdgl_qdzc_cgfkbj = By.XPATH, 'html/body/div[1]/form/div[3]/label[5]'
# 查询
yy_qdgl_qdzc_cx = By.XPATH, 'html/body/div[1]/form/div[4]/input'

# 渠道监控
yy_qdgl_jk = By.XPATH, 'html/body/div[1]/div[1]/div[2]/div/ul/li[2]/a'
# 渠道
yy_qdgl_jk_qd = By.XPATH, 'html/body/div[2]/div[1]/div[2]/div/span/span[1]/span/span[1]'
# 选择征信查询1
yy_qdgl_jk_zx = By.XPATH, 'html/body/span/span/span[2]/ul/li[3]'
# 点击下周日期
# 查询
yy_qdgl_jk_cx = By.XPATH, 'html/body/div[2]/div[1]/div[4]/button'

# 渠道注册用户
yy_qdgl_zcyh = By.XPATH, 'html/body/div[1]/div[1]/div[2]/div/ul/li[4]/a'
# 用户姓名
yy_qdgl_zcyh_name = By.XPATH, 'html/body/div[1]/form/div[1]/input'
# 用户电话
yy_qdgl_zcyh_phone = By.XPATH, 'html/body/div[1]/form/div[2]/input'
# 推荐渠道
yy_qdgl_zcyh_tjqd = By.XPATH, 'html/body/div[1]/form/div[3]/input'
# 渠道编号
yy_qdgl_zcyh_num = By.XPATH, 'html/body/div[1]/form/div[4]/input'
# 是否扣量
yy_qdgl_zcyh_iskz = By.XPATH, 'html/body/div[1]/form/div[5]/div/a'
# 选择正常
yy_qdgl_zcyh_zc = By.XPATH, 'html/body/div[5]/ul/li[2]/div'
# 开始时间
# 结束时间
# 筛选
yy_qdgl_zcyh_sx = By.XPATH, 'html/body/div[1]/form/div[7]/input'
# 扣重
yy_qdgl_zcyh_kz = By.XPATH, 'html/body/div[2]/table/tbody/tr[1]/td[8]/button[2]'

# 用户管理
yy_yhgl = By.XPATH, 'html/body/div[1]/div[2]/div[1]/a'
# 注册用户
yy_yhgl_zcyh = By.XPATH, 'html/body/div[1]/div[2]/div[2]/div/ul/li[1]/a'
# 注册人姓名
yy_yhgl_zcyh_name = By.XPATH, 'html/body/div[1]/form/div[1]/input'
# 注册人电话
yy_yhgl_zcyh_phone = By.XPATH, 'html/body/div[1]/form/div[2]/input'
# 推荐人电话
yy_yhgl_zcyh_tjr_phone = By.XPATH, 'html/body/div[1]/form/div[3]/input'
# 推荐人姓名
yy_yhgl_zcyh_tjr_name = By.XPATH, 'html/body/div[1]/form/div[4]/input'
# 注册来源
yy_yhgl_zcyh_zcly = By.XPATH, 'html/body/div[1]/form/div[5]/div/a'
# 选择贷福手机端
yy_yhgl_zcyh_zcly_xz = By.XPATH, 'html/body/div[5]/ul/li[2]/div'
# 是否扣量
yy_yhgl_zcyh_iskz = By.XPATH, 'html/body/div[1]/form/div[6]/div/a'
# 选择正常
yy_yhgl_zcyh_zc = By.XPATH, 'html/body/div[6]/ul/li[2]/div'
# 查询
yy_yhgl_zcyh_cx = By.XPATH, 'html/body/div[1]/form/div[8]/input[1]'
# 导出
yy_yhgl_zcyh_dc = By.XPATH, 'html/body/div[1]/form/div[8]/input[2]'
# 详情
yy_yhgl_zcyh_xq = By.XPATH, 'html/body/div[2]/table/tbody/tr[1]/td[11]/a'

# 用户监控
yy_yhgl_yhjk = By.XPATH, 'html/body/div[1]/div[2]/div[2]/div/ul/li[2]/a'
# 选择按时间查询
# 查询
yy_yhgl_yhjk_cx = By.XPATH, 'html/body/div[2]/div/div[3]/button'

# 渠道统计
yy_qdtj = By.XPATH, 'html/body/div[1]/div[3]/div[1]/a'
# 渠道统计
yy_qdtj_baby = By.XPATH, 'html/body/div[1]/div[3]/div[2]/div/ul/li/a'
# 渠道
yy_qdtj_baby_qd = By.XPATH, 'html/body/div[2]/div[1]/div[2]/span/span[1]/span/span[1]'
# 选择渠道
yy_qdtj_baby_qd_zx = By.XPATH, 'html/body/span/span/span[2]/ul/li[2]'
# 查询
yy_qdtj_baby_cx = By.XPATH, 'html/body/div[2]/div[1]/div[4]/button'
# 导出数据
yy_qdtj_baby_dcsj = By.XPATH, 'html/body/div[2]/div[1]/div[4]/a'

# 贷超管理
yy_dcgl = By.XPATH, 'html/body/div[1]/div[4]/div[1]/a'
# 平台管理
yy_dcgl_pt = By.XPATH, 'html/body/div[1]/div[4]/div[2]/div/ul/li[1]/a'
# 贷款超市管理
yy_dcgl_pt_dkcsgl = By.XPATH, 'html/body/div[1]/div/ul/li[1]/a'
# 访问记录
yy_dcgl_pt_fwjl = By.XPATH, 'html/body/div[1]/div/ul/li[2]/a'
# 添加贷款超市
yy_dcgl_pt_tjdkcs = By.XPATH, 'html/body/div[1]/div/ul/li[3]/a'
# 名称
yy_dcgl_pt_mc = By.XPATH, 'html/body/div[1]/form/div[1]/input'
# 超市类型
yy_dcgl_pt_lx = By.XPATH, 'html/body/div[1]/form/div[2]/div/a'
# 选择全新
yy_dcgl_pt_lx_xz = By.XPATH, 'html/body/div[6]/ul/li[2]/div'
# 上下架
yy_dcgl_pt_sxj = By.XPATH, 'html/body/div[1]/form/div[3]/div/a'
# 选择上架
yy_dcgl_pt_sj = By.XPATH, 'html/body/div[7]/ul/li[2]/div'
# 排序方式
yy_dcgl_pt_px = By.XPATH, 'html/body/div[1]/form/div[5]/div/a'
# 选择顺序
yy_dcgl_pt_sx = By.XPATH, 'html/body/div[7]/ul/li[2]/div'
# 查询
yy_dcgl_pt_cx = By.XPATH, 'html/body/div[1]/form/div[6]/input'
# 用户ip
yy_dcgl_pt_ip = By.XPATH, 'html/body/div[1]/form/div[1]/input'
# ip查询
yy_dcgl_pt_ipcx = By.XPATH, 'html/body/div[1]/form/div[3]/input'

# 客户转换情况
yy_dcgl_kh = By.XPATH, 'html/body/div[1]/div[4]/div[2]/div/ul/li[2]/a'
# 选择注册时间
# 查询
yy_dcgl_kh_cx = By.XPATH, 'html/body/div[1]/form/div[2]/input'

# 推广奖励金
yy_tgjlj = By.XPATH, 'html/body/div[1]/div[5]/div[1]/a'
# 奖励金管理
yy_tgjlj_jljgl = By.XPATH, 'html/body/div[1]/div[5]/div[2]/div/ul/li[1]/a'
# 奖励金类型
yy_tgjlj_jljgl_lx = By.XPATH, 'html/body/div[1]/form/div[2]/div/a'
# 选择拉新：注册
yy_tgjlj_jljgl_zc = By.XPATH, 'html/body/div[6]/ul/li[2]/div'
# 查询
yy_tgjlj_jljgl_cx = By.XPATH, 'html/body/div[1]/form/div[3]/input'
# 提现审核
yy_tgjlj_txsh = By.XPATH, 'html/body/div[1]/div[5]/div[2]/div/ul/li[2]/a'
# 提现转账
yy_tgjlj_txzz = By.XPATH, 'html/body/div[1]/div[5]/div[2]/div/ul/li[3]/a'
# 提现已转账
yy_tgjlj_txyzz = By.XPATH, 'html/body/div[1]/div[5]/div[2]/div/ul/li[4]/a'
# 提现已拒绝
yy_tgjlj_txyjj = By.XPATH, 'html/body/div[1]/div[5]/div[2]/div/ul/li[5]/a'

# 业务数据统计
yy_ywsjtj = By.XPATH, 'html/body/div[1]/div[6]/div[1]/a'
# 业务数据统计
yy_ywsjtj_baby = By.XPATH, 'html/body/div[1]/div[6]/div[2]/div/ul/li/a'
# 导出
yy_ywsjtj_baby_dc = By.XPATH, 'html/body/div[1]/div[1]/a'

"""
财务管理页面元素
"""
# 代付管理
cw_dfgl = By.XPATH, 'html/body/div[1]/div[1]/div[1]/a'
# 代付交易管理
cw_dfgl_jygl = By.XPATH, 'html/body/div[1]/div[1]/div[2]/div/ul/li[1]/a'
# 订单编号
cw_dfgl_jygl_ddbh = By.XPATH, 'html/body/div[1]/form/div[1]/input'
# 客户姓名
cw_dfgl_jygl_name = By.XPATH, 'html/body/div[1]/form/div[2]/input'
# 客户电话
cw_dfgl_jygl_phone = By.XPATH, 'html/body/div[1]/form/div[3]/input'
# 交易单号
cw_dfgl_jygl_jydh = By.XPATH, 'html/body/div[1]/form/div[4]/input'
# 出款账号
cw_dfgl_jygl_ckzh = By.XPATH, 'html/body/div[1]/form/div[5]/div/a'
# 选择账号
cw_dfgl_jygl_xzzh = By.XPATH, 'html/body/div[7]/ul/li[2]/div'
# 财务类型
cw_dfgl_jygl_cwlx = By.XPATH, 'html/body/div[1]/form/div[6]/div/a'
# 选择财务类型
cw_dfgl_jygl_xzlx = By.XPATH, 'html/body/div[8]/ul/li[2]/div'
# 交易时间
# 查询
cw_dfgl_jygl_cx = By.XPATH, 'html/body/div[1]/form/div[8]/input[1]'
# 导出数据
cw_dfgl_jygl_dcsj = By.XPATH, 'html/body/div[1]/form/div[8]/input[2]'

# 资金账户管理
cw_dfgl_zjzhgl = By.XPATH, 'html/body/div[1]/div[1]/div[2]/div/ul/li[2]/a'
# 资金账户
cw_dfgl_zjzhgl_zjzh = By.XPATH, 'html/body/div[1]/form[1]/div[1]/div/a'
# 选择资金账户
cw_dfgl_zjzhgl_xzzjzh = By.XPATH, 'html/body/div[11]/ul/li[2]/div'
# 财务类型
cw_dfgl_zjzhgl_cwlx = By.XPATH, 'html/body/div[1]/form[1]/div[2]/div/a'
# 选择财务类型
cw_dfgl_zjzhgl_xzcwlx = By.XPATH, 'html/body/div[12]/ul/li[2]/div'
# 交易单号
cw_dfgl_zjzhgl_jydh = By.XPATH, 'html/body/div[1]/form[1]/div[3]/input'
# 收支类型
cw_dfgl_zjzhgl_sr = By.XPATH, 'html/body/div[1]/form[1]/div[4]/input[1]'
# 支出
cw_dfgl_zjzhgl_zc = By.XPATH, 'html/body/div[1]/form[1]/div[4]/input[3]'
# 交易时间
# 添加交易
cw_dfgl_zjzhgl_tjjy = By.XPATH, 'html/body/div[1]/form[1]/div[6]/input[1]'
# 新增账户
cw_dfgl_zjzhgl_xzzh = By.XPATH, 'html/body/div[1]/form[1]/div[6]/input[2]'
# 查询
cw_dfgl_zjzhgl_cx = By.XPATH, 'html/body/div[1]/form[1]/div[6]/input[3]'
# 导出数据
cw_dfgl_zjzhgl_dcsj = By.XPATH, 'html/body/div[1]/form[1]/div[6]/input[4]'
# 查看
cw_dfgl_zjzhgl_ck = By.XPATH, 'html/body/div[3]/table/tbody/tr[1]/td[8]/a'
# 关闭
cw_dfgl_zjzhglc_gb = By.XPATH, 'html/body/div[7]/div[3]/button'

# 还款交易管理
cw_dfgl_hkjygl = By.XPATH, 'html/body/div[1]/div[1]/div[2]/div/ul/li[3]/a'
# 订单编号
cw_dfgl_hkjygl_ddbh = By.XPATH, 'html/body/div[1]/form/div[1]/input'
# 交易单号
cw_dfgl_hkjygl_jydh = By.XPATH, 'html/body/div[1]/form/div[2]/input'
# 用户名称
cw_dfgl_hkjygl_yhmc = By.XPATH, 'html/body/div[1]/form/div[3]/input'
# 用户电话
cw_dfgl_hkjygl_yhdh = By.XPATH, 'html/body/div[1]/form/div[4]/input'
# 所属省份
cw_dfgl_hkjygl_sssf = By.XPATH, 'html/body/div[1]/form/div[5]/div[1]/a'
# 选择省份
cw_dfgl_hkjygl_xzsf = By.XPATH, 'html/body/div[6]/ul/li[4]/div'
# 所属城市
cw_dfgl_hkjygl_sscs = By.XPATH, 'html/body/div[1]/form/div[5]/div[2]/a'
# 选择城市
cw_dfgl_hkjygl_xzcs = By.XPATH, 'html/body/div[7]/ul/li[3]/div'
# 时间类型
cw_dfgl_hkjygl_sjlx = By.XPATH, 'html/body/div[1]/form/div[6]/div/a'
# 选择类型
cw_dfgl_hkjygl_xzlx = By.XPATH, 'html/body/div[8]/ul/li[2]/div'
# 查询
cw_dfgl_hkjygl_cx = By.XPATH, 'html/body/div[1]/form/div[7]/input[1]'
# 重置
cw_dfgl_hkjygl_cz = By.XPATH, 'html/body/div[1]/form/div[7]/input[2]'
# 导出数据
cw_dfgl_hkjygl_dcsj = By.XPATH, 'html/body/div[1]/form/div[7]/input[3]'

# 代扣管理
cw_daikgl = By.XPATH, 'html/body/div[1]/div[2]/div[1]/a'
# 代扣交易记录
cw_daikgl_jyjl = By.XPATH, 'html/body/div[1]/div[2]/div[2]/div/ul/li/a'
# 订单编号
cw_daikgl_jyjl_ddbh = By.XPATH, 'html/body/div[1]/form/div[1]/input'
# 用户名
cw_daikgl_jyjl_yhm = By.XPATH, 'html/body/div[1]/form/div[2]/input'
# 开户行
cw_daikgl_jyjl_khh = By.XPATH, 'html/body/div[1]/form/div[3]/input'
# 银行卡号
cw_daikgl_jyjl_yhkh = By.XPATH, 'html/body/div[1]/form/div[4]/input'
# 代扣状态
cw_daikgl_jyjl_dkzt = By.XPATH, 'html/body/div[1]/form/div[5]/div/a'
# 选择代扣状态
cw_daikgl_jyjl_xzdkzt = By.XPATH, 'html/body/div[6]/ul/li[3]/div'
# 代扣时间
# 查询
cw_daikgl_jyjl_cx = By.XPATH, 'html/body/div[1]/form/div[7]/input[1]'
# 导出数据
cw_daikgl_jyjl_dcsj = By.XPATH, 'html/body/div[1]/form/div[7]/input[2]'

# 还款管理
cw_hkgl = By.XPATH, 'html/body/div[1]/div[3]/div[1]/a'
# 待还账单管理
cw_hkgl_dhzdgl = By.XPATH, 'html/body/div[1]/div[3]/div[2]/div/ul/li[1]/a'
# 订单编号
cw_hkgl_dhzdgl_ddbh = By.XPATH, 'html/body/div[1]/form/div[1]/input'
# 客户姓名
cw_hkgl_dhzdgl_name = By.XPATH, 'html/body/div[1]/form/div[2]/input'
# 客户电话
cw_hkgl_dhzdgl_phone = By.XPATH, 'html/body/div[1]/form/div[3]/input'
# 业务类型
cw_hkgl_dhzdgl_ywlx = By.XPATH, 'html/body/div[1]/form/div[4]/div/a'
# 选择业务类型
cw_hkgl_dhzdgl_ywlx_xz = By.XPATH, 'html/body/div[7]/ul/li[3]/div'
# 账单日
# 查询
cw_hkgl_dhzdgl_cx = By.XPATH, 'html/body/div[1]/form/div[6]/input[1]'
# 导出数据
cw_hkgl_dhzdgl_dcsj = By.XPATH, 'html/body/div[1]/form/div[6]/input[2]'
# 销账
cw_hkgl_dhzdgl_xz = By.XPATH, 'html/body/div[3]/table/tbody/tr[1]/td[11]/button[1]'
# 减免
cw_hkgl_dhzdgl_jm = By.XPATH, 'html/body/div[3]/table/tbody/tr[1]/td[11]/button[2]'

# 账单管理
cw_hkgl_zdgl = By.XPATH, 'html/body/div[1]/div[3]/div[2]/div/ul/li[2]/a'
# 用户名称
cw_hkgl_zdgl_yhmc = By.XPATH, 'html/body/div[1]/form/div[1]/input'
# 用户电话
cw_hkgl_zdgl_yhdh = By.XPATH, 'html/body/div[1]/form/div[2]/input'
# 订单编号
cw_hkgl_zdgl_ddbh = By.XPATH, 'html/body/div[1]/form/div[3]/input'
# 查询
cw_hkgl_zdgl_cx = By.XPATH, 'html/body/div[1]/form/div[4]/input'
# 剩余期数
cw_hkgl_zdgl_syqs = By.XPATH, 'html/body/div[2]/table/tbody/tr[1]/td[4]/a'
# 已还期数
cw_hkgl_zdgl_yhqs = By.XPATH, 'html/body/div[2]/table/tbody/tr[1]/td[6]/a'
# 逾期未还期数
cw_hkgl_zdgl_yqwhqs = By.XPATH, 'html/body/div[2]/table/tbody/tr[1]/td[8]/a'
# 逾期已还期数
cw_hkgl_zdgl_yqyhqs = By.XPATH, 'html/body/div[2]/table/tbody/tr[1]/td[10]/a'
# 逾期总期数
cw_hkgl_zdgl_yqzqs = By.XPATH, 'html/body/div[2]/table/tbody/tr[1]/td[12]/a'
# 总期数
cw_hkgl_zdgl_zqs = By.XPATH, 'html/body/div[2]/table/tbody/tr[1]/td[14]/a'

# 待还账单
cw_hkgl_dhzd = By.XPATH, 'html/body/div[1]/div[3]/div[2]/div/ul/li[3]/a'
# 订单编号
cw_hkgl_dhzd_ddbh = By.XPATH, 'html/body/div[1]/form/div[1]/input'
# 用户名称
cw_hkgl_dhzd_yhmc = By.XPATH, 'html/body/div[1]/form/div[2]/input'
# 用户电话
cw_hkgl_dhzd_yhdh = By.XPATH, 'html/body/div[1]/form/div[3]/input'
# 账单日

# 所属省份
cw_hkgl_dhzd_sssf = By.XPATH, 'html/body/div[1]/form/div[5]/div[1]/a'
# 选择省份
cw_hkgl_dhzd_sssf_xz = By.XPATH, 'html/body/div[7]/ul/li[4]/div'
# 所属城市
cw_hkgl_dhzd_sscs = By.XPATH, 'html/body/div[1]/form/div[5]/div[2]/a'
# 选择城市
cw_hkgl_dhzd_sscs_xz = By.XPATH, 'html/body/div[8]/ul/li[3]/div'
# 查询
cw_hkgl_dhzd_cx = By.XPATH, 'html/body/div[1]/form/div[6]/input[1]'
# 重置
cw_hkgl_dhzd_cz = By.XPATH, 'html/body/div[1]/form/div[6]/input[2]'

# 资金账户管理
cw_zjzhgl = By.XPATH, 'html/body/div[1]/div[4]/div[1]/a'
# 资金账户管理
cw_zjzhgl_baby = By.XPATH, 'html/body/div[1]/div[4]/div[2]/div/ul/li/a'
# 账户资金
cw_zjzhgl_baby_zjzh = By.XPATH, 'html/body/div[1]/form[1]/div[1]/div/a'
# 账户资金选择
cw_zjzhgl_baby_zjzh_xz = By.XPATH, 'html/body/div[11]/ul/li[2]/div'
# 财务类型
cw_zjzhgl_baby_cwlx = By.XPATH, 'html/body/div[1]/form[1]/div[2]/div/a'
# 财务类型选择
cw_zjzhgl_baby_cwlx_xz = By.XPATH, 'html/body/div[12]/ul/li[2]/div'
# 交易单号
cw_zjzhgl_baby_jydh = By.XPATH, 'html/body/div[1]/form[1]/div[3]/input'
# 收支类型
# 收入
cw_zjzhgl_baby_sr = By.XPATH, 'html/body/div[1]/form[1]/div[4]/input[1]'
# 支出
cw_zjzhgl_baby_zc = By.XPATH, 'html/body/div[1]/form[1]/div[4]/input[3]'
# 交易时间
# 添加交易
cw_zjzhgl_baby_tjjy = By.XPATH, 'html/body/div[1]/form[1]/div[6]/input[1]'
# 新增账户
cw_zjzhgl_baby_xzzh = By.XPATH, 'html/body/div[1]/form[1]/div[6]/input[2]'
# 查询
cw_zjzhgl_baby_cx = By.XPATH, 'html/body/div[1]/form[1]/div[6]/input[3]'
# 导出数据
cw_zjzhgl_baby_dcsj = By.XPATH, 'html/body/div[1]/form[1]/div[6]/input[4]'
# 查看
cw_zjzhgl_baby_ck = By.XPATH, 'html/body/div[3]/table/tbody/tr[1]/td[8]/a'

# 资金管理
cw_zjgl = By.XPATH, 'html/body/div[1]/div[5]/div[1]/a'
# 待上标订单
cw_zjgl_dsbdb = By.XPATH, 'html/body/div[1]/div[5]/div[2]/div/ul/li[1]/a'
# 订单编号
cw_zjgl_dsbdb_ddbh = By.XPATH, 'html/body/div[1]/form/div[1]/input'
# 客户姓名
cw_zjgl_dsbdb_name = By.XPATH, 'html/body/div[1]/form/div[2]/input'
# 产品类型
cw_zjgl_dsbdb_cplx = By.XPATH, 'html/body/div[1]/form/div[3]/div/a'
# 选择产品类型
cw_zjgl_dsbdb_cplx_xz = By.XPATH, 'html/body/div[5]/ul/li[2]/div'
# 分期数
cw_zjgl_dsbdb_fqs = By.XPATH, 'html/body/div[1]/form/div[4]/div/a'
# 选择分期数
cw_zjgl_dsbdb_fqs_xz = By.XPATH, 'html/body/div[6]/ul/li[3]/div'
# 排序方式
cw_zjgl_dsbdb_pxfs = By.XPATH, 'html/body/div[1]/form/div[5]/div/a'
# 选择排序方式
cw_zjgl_dsbdb_pxfs_xz = By.XPATH, 'html/body/div[7]/ul/li[2]/div'
# 审核通过日期
# 查询
cw_zjgl_dsbdb_cx = By.XPATH, 'html/body/div[1]/form/div[7]/input'
# 查看详情
cw_zjgl_dsbdb_ckxq = By.XPATH, 'html/body/div[2]/table/tbody/tr[1]/td[15]/a'

# 已上标订单
cw_zjgl_ysbdb = By.XPATH, 'html/body/div[1]/div[5]/div[2]/div/ul/li[2]/a'
# 订单编号
cw_zjgl_ysbdb_ddbh = By.XPATH, 'html/body/div[1]/form/div[1]/input'
# 客户姓名
cw_zjgl_ysbdb_name = By.XPATH, 'html/body/div[1]/form/div[2]/input'
# 产品类型
cw_zjgl_ysbdb_cplx = By.XPATH, 'html/body/div[1]/form/div[3]/div/a'
# 选择产品类型
cw_zjgl_ysbdb_cplx_xz = By.XPATH, 'html/body/div[7]/ul/li[2]/div'
# 上标平台
cw_zjgl_ysbdb_sbpt = By.XPATH, 'html/body/div[1]/form/div[4]/div/a'
# 选择上标平台\
cw_zjgl_ysbdb_sbpt_xz = By.XPATH, 'html/body/div[8]/ul/li[2]/div'
# 是否打款
cw_zjgl_ysbdb_sfdk = By.XPATH, 'html/body/div[1]/form/div[5]/div/a'
# 选择是否打款
cw_zjgl_ysbdb_sfdk_xz = By.XPATH, 'html/body/div[9]/ul/li[2]/div'
# 排序方式
cw_zjgl_ysbdb_pxfs = By.XPATH, 'html/body/div[1]/form/div[6]/div/a'
# 选择排序方式
cw_zjgl_ysbdb_pxfs_xz = By.XPATH, 'html/body/div[10]/ul/li[2]/div'
# 分期数
cw_zjgl_ysbdb_fqs = By.XPATH, 'html/body/div[1]/form/div[7]/div/a'
# 选择分期数
cw_zjgl_ysbdb_fqs_xz = By.XPATH, 'html/body/div[11]/ul/li[3]/div'
# 是否已导出
cw_zjgl_ysbdb_sfydc = By.XPATH, 'html/body/div[1]/form/div[8]/div/a'
# 选择是否已导出
cw_zjgl_ysbdb_sfydc_xz = By.XPATH, 'html/body/div[12]/ul/li[1]/div'
# 上标日期
# 查询
cw_zjgl_ysbdb_cx = By.XPATH, 'html/body/div[1]/form/div[10]/input'
# 查看详情
cw_zjgl_ysbdb_ckxq = By.XPATH, 'html/body/div[2]/table/tbody/tr[1]/td[16]/a'
# 返回
cw_zjgl_ysbdb_back = By.XPATH, 'html/body/div[8]/div/input[2]'

# 实际上标
cw_zjgl_sjsb = By.XPATH, 'html/body/div[1]/div[5]/div[2]/div/ul/li[3]/a'
# 项目名称
cw_zjgl_sjsb_xmmc = By.XPATH, 'html/body/div[1]/form/div[1]/input'
# 上标日期
# 页码
cw_zjgl_sjsb_ym = By.XPATH, 'html/body/div[1]/form/div[3]/input'
# 每页数据
cw_zjgl_sjsb_mysj = By.XPATH, 'html/body/div[1]/form/div[4]/input'
# 查询
cw_zjgl_sjsb_cx = By.XPATH, 'html/body/div[1]/form/div[5]/input'

# 已结清订单
cw_zjgl_yjqdb = By.XPATH, 'html/body/div[1]/div[5]/div[2]/div/ul/li[4]/a'
# 筛选时间类型
cw_zjgl_yjqdb_sxsjlx = By.XPATH, 'html/body/div[1]/form/div[1]/div[1]/a'
# 选择筛选时间类型
cw_zjgl_yjqdb_sxsjlx_xz = By.XPATH, 'html/body/div[6]/ul/li[2]/div'
# 点击回款来源
cw_zjgl_yjqdb_hkly = By.XPATH, 'html/body/div[1]/form/div[2]/div/a'
# 选择回款来源
cw_zjgl_yjqdb_hkly_xz = By.XPATH, 'html/body/div[7]/ul/li[2]/div'
# 关键字
cw_zjgl_yjqdb_gjz = By.XPATH, 'html/body/div[1]/form/div[3]/input'
# 查询
cw_zjgl_yjqdb_cx = By.XPATH, 'html/body/div[1]/form/div[4]/input'

# 打款管理
cw_dkgl = By.XPATH, 'html/body/div[1]/div[6]/div[1]/a'
# 未打款
cw_dkgl_wdk = By.XPATH, 'html/body/div[1]/div[6]/div[2]/div/ul/li[1]/a'
# 现金借贷
cw_dkgl_wdk_xjjd = By.XPATH, 'html/body/div[1]/div/ul/li[1]/a'
# 订单编号
cw_dkgl_wdk_ddbh = By.XPATH, 'html/body/div[1]/form/div[1]/input'
# 客户姓名
cw_dkgl_wdk_name = By.XPATH, 'html/body/div[1]/form/div[2]/input'
# 审核通过日期
# 查询
cw_dkgl_wdk_cx = By.XPATH, 'html/body/div[1]/form/div[4]/input[1]'
# 导出数据
cw_dkgl_wdk_dcsj = By.XPATH, 'html/body/div[1]/form/div[4]/input[2]'
# 设置收款账号
cw_dkgl_wdk_szskzh = By.XPATH, 'html/body/div[3]/table/tbody/tr[1]/td[11]/a'

# 商户销售
cw_dkgl_wdk_shxs = By.XPATH, 'html/body/div[1]/div/ul/li[2]/a'
# 分期购物
cw_dkgl_wdk_fqgw = By.XPATH, 'html/body/div[1]/div/ul/li[3]/a'

# 已打款
cw_dkgl_ydk = By.XPATH, 'html/body/div[1]/div[6]/div[2]/div/ul/li[2]/a'
# 现金借贷
cw_dkgl_ydk_xjjd = By.XPATH, 'html/body/div[1]/div/ul/li[1]/a'
# 订单编号
cw_dkgl_ydk_ddbh = By.XPATH, 'html/body/div[1]/form/div[1]/input'
# 客户姓名
cw_dkgl_ydk_name = By.XPATH, 'html/body/div[1]/form/div[2]/input'
# 审核通过日期
# 查询
cw_dkgl_ydk_cx = By.XPATH, 'html/body/div[1]/form/div[4]/input[1]'
# 导出数据
cw_dkgl_ydk_dcsj = By.XPATH, 'html/body/div[1]/form/div[4]/input[2]'
# 上传打款凭证
cw_dkgl_ydk_szskzh = By.XPATH, 'html/body/div[3]/table/tbody/tr[1]/td[11]/a'

# 商户销售
cw_dkgl_ydk_shxs = By.XPATH, 'html/body/div[1]/div/ul/li[2]/a'
# 分期购物
cw_dkgl_ydk_fqgw = By.XPATH, 'html/body/div[1]/div/ul/li[3]/a'

# 打款统计
cw_dkgl_dktj = By.XPATH, 'html/body/div[1]/div[6]/div[2]/div/ul/li[3]/a'
# 日
cw_dkgl_dktj_ri = By.XPATH, 'html/body/div[1]/div/ul/li[1]'
# 周
cw_dkgl_dktj_zhou = By.XPATH, 'html/body/div[1]/div/ul/li[2]'
# 月
cw_dkgl_dktj_yue = By.XPATH, 'html/body/div[1]/div/ul/li[3]'
# 打款日期

# 打款账号
cw_dkgl_dktj_dkzh = By.XPATH, 'html/body/div[1]/form/div[2]/input'
# 查询
cw_dkgl_dktj_cx = By.XPATH, 'html/body/div[1]/form/div[3]/input'

# 还款交易
cw_hkjy = By.XPATH, 'html/body/div[1]/div[7]/div[1]/a'
# 还款交易
cw_hkjy_baby = By.XPATH, 'html/body/div[1]/div[7]/div[2]/div/ul/li/a'
# 用户名称
cw_hkjy_baby_name = By.XPATH, 'html/body/div[1]/form/div[1]/input'
# 时间
# 商户交易号
cw_hkjy_baby_shjyh = By.XPATH, 'html/body/div[1]/form/div[3]/input'
# 支付渠道
cw_hkjy_baby_zfqd = By.XPATH, 'html/body/div[1]/form/div[4]/div/a'
# 选择支付渠道
cw_hkjy_baby_zfqd_xz = By.XPATH, 'html/body/div[5]/ul/li[2]/div'
# 查询
cw_hkjy_baby_cx = By.XPATH, 'html/body/div[1]/form/div[5]/input[1]'
# 导出
cw_hkjy_baby_dc = By.XPATH, 'html/body/div[1]/form/div[5]/input[2]'

# 账单明细
cw_zdmx = By.XPATH, 'html/body/div[1]/div[8]/div[1]/a'
# 逾期管理
cw_zdmx_yqgl = By.XPATH, 'html/body/div[1]/div[8]/div[2]/div/ul/li[1]/a'
# 用户名单
cw_zdmx_yqgl_yhmc = By.XPATH, 'html/body/div[1]/form/div[1]/input'
# 还款日
# 订单编号
cw_zdmx_yqgl_ddbh = By.XPATH, 'html/body/div[1]/form/div[3]/input'
# 查询
cw_zdmx_yqgl_cx = By.XPATH, 'html/body/div[1]/form/div[4]/input[1]'
# 导出
cw_zdmx_yqgl_dc = By.XPATH, 'html/body/div[1]/form/div[4]/input[2]'
# 查看
cw_zdmx_yqgl_ck = By.XPATH, 'html/body/table/tbody/tr[1]/td[3]/input[2]'
# 点击订单
cw_zdmx_yqgl_djdb = By.XPATH, 'html/body/table/tbody/tr[1]/td[3]/a'

# 账单明细
cw_zdmx_baby_zdmx = By.XPATH, 'html/body/div[1]/div[8]/div[2]/div/ul/li[2]/a'
# 用户名称
cw_zdmx_baby_yhmc = By.XPATH, 'html/body/div[1]/form/div[1]/input'
# 还款日
cw_zdmx_baby_hkr = By.XPATH, 'html/body/div[1]/form/div[3]/div/a'
# 选择还款日
cw_zdmx_baby_hkr_xz = By.XPATH, 'html/body/div[6]/ul/li[1]/div'
# 订单编号
cw_zdmx_baby_ddbh = By.XPATH, 'html/body/div[1]/form/div[4]/input'
# 查询
cw_zdmx_baby_cx = By.XPATH, 'html/body/div[1]/form/div[5]/input[1]'
# 重置
cw_zdmx_baby_cz = By.XPATH, 'html/body/div[1]/form/div[5]/input[2]'
# 返回
cw_zdmx_baby_fh = By.XPATH, 'html/body/div[1]/form/div[5]/input[3]'
# 导出
cw_zdmx_baby_dc = By.XPATH, 'html/body/div[1]/form/div[5]/input[4]'

# 账单管理
cw_zdmx_zdgl = By.XPATH, 'html/body/div[1]/div[8]/div[2]/div/ul/li[3]/a'
# 用户名称
cw_zdmx_zdgl_name = By.XPATH, 'html/body/div[1]/form/div[1]/input'
# 用户电话
cw_zdmx_zdgl_phone = By.XPATH, 'html/body/div[1]/form/div[2]/input'
# 订单编号
cw_zdmx_zdgl_ddbh = By.XPATH, 'html/body/div[1]/form/div[3]/input'
# 查询
cw_zdmx_zdgl_cx = By.XPATH, 'html/body/div[1]/form/div[4]/input'

# 待还明细
cw_zdmx_dhmx = By.XPATH, 'html/body/div[1]/div[8]/div[2]/div/ul/li[4]/a'
# 用户名称
cw_zdmx_dhmx_yhmc = By.XPATH, 'html/body/div[1]/form/div[1]/input'
# 还款日
cw_zdmx_dhmx_hkr = By.XPATH, 'html/body/div[1]/form/div[3]/div/a'
# 选择还款日
cw_zdmx_dhmx_hkr_xz = By.XPATH, 'html/body/div[6]/ul/li[1]/div'
# 订单编号
cw_zdmx_dhmx_ddbh = By.XPATH, 'html/body/div[1]/form/div[4]/input'
# 查询
cw_zdmx_dhmx_cx = By.XPATH, 'html/body/div[1]/form/div[5]/input[1]'
# 重置
cw_zdmx_dhmx_cz = By.XPATH, 'html/body/div[1]/form/div[5]/input[2]'
# 返回
cw_zdmx_dhmx_fh = By.XPATH, 'html/body/div[1]/form/div[5]/input[3]'
# 导出
cw_zdmx_dhmx_dc = By.XPATH, 'html/body/div[1]/form/div[5]/input[4]'

# 还款明细
cw_zdmx_hkmx = By.XPATH, 'html/body/div[1]/div[8]/div[2]/div/ul/li[5]/a'
# 用户名称
cw_zdmx_hkmx_yhmc = By.XPATH, 'html/body/div[1]/form/div[1]/input'
# 还款日
cw_zdmx_hkmx_hkr = By.XPATH, 'html/body/div[1]/form/div[3]/div/a'
# 选择还款日
cw_zdmx_hkmx_hkr_xz = By.XPATH, 'html/body/div[6]/ul/li[1]/div'
# 订单编号
cw_zdmx_hkmx_ddbh = By.XPATH, 'html/body/div[1]/form/div[4]/input'
# 查询
cw_zdmx_hkmx_cx = By.XPATH, 'html/body/div[1]/form/div[5]/input[1]'
# 重置
cw_zdmx_hkmx_cz = By.XPATH, 'html/body/div[1]/form/div[5]/input[2]'
# 返回
cw_zdmx_hkmx_fh = By.XPATH, 'html/body/div[1]/form/div[5]/input[3]'
# 导出
cw_zdmx_hkmx_dc = By.XPATH, 'html/body/div[1]/form/div[5]/input[4]'

# 逾期明细
cw_zdmx_yqmx = By.XPATH, 'html/body/div[1]/div[8]/div[2]/div/ul/li[6]/a'
# 用户名称
cw_zdmx_yqmx_yhmc = By.XPATH, 'html/body/div[1]/form/div[1]/input'
# 还款日
cw_zdmx_yqmx_hkr = By.XPATH, 'html/body/div[1]/form/div[3]/div/a'
# 选择还款日
cw_zdmx_yqmx_hkr_xz = By.XPATH, 'html/body/div[6]/ul/li[1]/div'
# 订单编号
cw_zdmx_yqmx_ddbh = By.XPATH, 'html/body/div[1]/form/div[4]/input'
# 查询
cw_zdmx_yqmx_cx = By.XPATH, 'html/body/div[1]/form/div[5]/input[1]'
# 逾期未还
cw_zdmx_yqmx_yqwh = By.XPATH, 'html/body/div[1]/form/div[5]/input[2]'
# 逾期已还
cw_zdmx_yqmx_yqyh = By.XPATH, 'html/body/div[1]/form/div[5]/input[3]'
# 重置
cw_zdmx_yqmx_cz = By.XPATH, 'html/body/div[1]/form/div[5]/input[4]'
# 返回
cw_zdmx_yqmx_fh = By.XPATH, 'html/body/div[1]/form/div[5]/input[5]'
# 导出
cw_zdmx_yqmx_dc = By.XPATH, 'html/body/div[1]/form/div[5]/input[6]'

# 还款对账
cw_zdmx_hkdz = By.XPATH, 'html/body/div[1]/div[8]/div[2]/div/ul/li[7]/a'
# 订单编号
cw_zdmx_hkdz_ddbh = By.XPATH, 'html/body/div[1]/form/div[1]/input'
# 交易单号
cw_zdmx_hkdz_jydh = By.XPATH, 'html/body/div[1]/form/div[2]/input'
# 用户名称
cw_zdmx_hkdz_name = By.XPATH, 'html/body/div[1]/form/div[3]/input'
# 用户电话
cw_zdmx_hkdz_phone = By.XPATH, 'html/body/div[1]/form/div[4]/input'
# 所属省份
cw_zdmx_hkdz_sssf = By.XPATH, 'html/body/div[1]/form/div[5]/div[1]/a'
# 选择省份
cw_zdmx_hkdz_sssf_xz = By.XPATH, 'html/body/div[6]/ul/li[4]/div'
# 所属城市
cw_zdmx_hkdz_sscs = By.XPATH, 'html/body/div[1]/form/div[5]/div[2]/a'
# 选择城市
cw_zdmx_hkdz_sscs_xz = By.XPATH, 'html/body/div[7]/ul/li[3]/div'
# 时间类型
cw_zdmx_hkdz_sjlx = By.XPATH, 'html/body/div[1]/form/div[6]/div/a'
# 选择时间类型
cw_zdmx_hkdz_sjlx_xz = By.XPATH, 'html/body/div[8]/ul/li[2]/div'
# 查询
cw_zdmx_hkdz_cx = By.XPATH, 'html/body/div[1]/form/div[7]/input[1]'
# 重置
cw_zdmx_hkdz_cz = By.XPATH, 'html/body/div[1]/form/div[7]/input[2]'
# 导出数据
cw_zdmx_hkdz_dcsj = By.XPATH, 'html/body/div[1]/form/div[7]/input[3]'

# 待还账单
cw_zdmx_dhzd = By.XPATH, 'html/body/div[1]/div[8]/div[2]/div/ul/li[8]/a'
# 订单编号
cw_zdmx_dhzd_ddbh = By.XPATH, 'html/body/div[1]/form/div[1]/input'
# 用户名称
cw_zdmx_dhzd_yhmc = By.XPATH, 'html/body/div[1]/form/div[2]/input'
# 用户电话
cw_zdmx_dhzd_yhdh = By.XPATH, 'html/body/div[1]/form/div[3]/input'
# 所属省份
cw_zdmx_dhzd_sssf = By.XPATH, 'html/body/div[1]/form/div[5]/div[1]/a'
# 选择省份
cw_zdmx_dhzd_sssf_xz = By.XPATH, 'html/body/div[7]/ul/li[4]/div'
# 所属城市
cw_zdmx_dhzd_sscs = By.XPATH, 'html/body/div[1]/form/div[5]/div[2]/a'
# 选择城市
cw_zdmx_dhzd_sscs_xz = By.XPATH, 'html/body/div[8]/ul/li[3]/div'
# 查询
cw_zdmx_dhzd_cx = By.XPATH, 'html/body/div[1]/form/div[6]/input[1]'
# 重置
cw_zdmx_dhzd_cz = By.XPATH, 'html/body/div[1]/form/div[6]/input[2]'

# 债权对账
cw_zqdz = By.XPATH, 'html/body/div[1]/div[9]/div[1]/a'
# 满标项目
cw_zqdz_mbxm = By.XPATH, 'html/body/div[1]/div[9]/div[2]/div/ul/li[1]/a'
# 项目名称
cw_zqdz_mbxm_name = By.XPATH, 'html/body/div[1]/form/div[1]/input'
# 状态
cw_zqdz_mbxm_zt = By.XPATH, 'html/body/div[1]/form/div[2]/div/a'
# 选择状态
cw_zqdz_mbxm_xzzt = By.XPATH, 'html/body/div[6]/ul/li[4]/div'
# 满标日期
# 查询
cw_zqdz_mbxm_cx = By.XPATH, 'html/body/div[1]/form/div[4]/input'

# 满标还款中
cw_zqdz_mbhkz = By.XPATH, 'html/body/div[1]/div[9]/div[2]/div/ul/li[2]/a'
# 项目名称
cw_zqdz_mbhkz_name = By.XPATH, 'html/body/div[1]/form/div[1]/input'
# 借款状态
cw_zqdz_mbhkz_jkzt = By.XPATH, 'html/body/div[1]/form/div[2]/div/a'
# 选择借款状态
cw_zqdz_mbhkz_jkzt_xz = By.XPATH, 'html/body/div[7]/ul/li[2]/div'
# 满标日期
# 查询
cw_zqdz_mbhkz_cx = By.XPATH, 'html/body/div[1]/form/div[4]/input'

# 满标还款完成
cw_zqdz_mbhkwc = By.XPATH, 'html/body/div[1]/div[9]/div[2]/div/ul/li[3]/a'
# 项目名称
cw_zqdz_mbhkwc_name = By.XPATH, 'html/body/div[1]/form/div[1]/input'
# 保证金状态
cw_zqdz_mbhkwc_bzjzt = By.XPATH, 'html/body/div[1]/form/div[2]/div/a'
# 选择保证金状态
cw_zqdz_mbhkwc_bzjzt_xz = By.XPATH, 'html/body/div[6]/ul/li[2]/div'
# 满标日期
# 查询
cw_zqdz_mbhkwc_cx = By.XPATH, 'html/body/div[1]/form/div[4]/input'
# 账单明细
cw_zqdz_mbhkwc_zdmx = By.XPATH, 'html/body/div[2]/table/tbody/tr[1]/td[13]/a[1]'
# 返回
cw_zqdz_mbhkwc_zdmx_back = By.XPATH, 'html/body/div[1]/input'
# 保证金返还
cw_zqdz_mbhkwc_bzjfh = By.XPATH, 'html/body/div[2]/table/tbody/tr[1]/td[13]/a[2]'

# 还款对账账单
cw_zqdz_hkdzzd = By.XPATH, 'html/body/div[1]/div[9]/div[2]/div/ul/li[4]/a'
# 项目名称
cw_zqdz_hkdzzd_name = By.XPATH, 'html/body/div[1]/form/div[1]/input'
# 账单状态
cw_zqdz_hkdzzd_zdzt = By.XPATH, 'html/body/div[1]/form/div[2]/div/a'
# 选择账单状态
cw_zqdz_hkdzzd_zdzt_xz = By.XPATH, 'html/body/div[7]/ul/li[3]/div'
# 账单日
cw_zqdz_hkdzzd_zdr = By.XPATH, 'html/body/div[1]/form/div[3]/div/a'
# 选择账单日
cw_zqdz_hkdzzd_zdr_xz = By.XPATH, 'html/body/div[8]/ul/li[2]/div'
# 查询
cw_zqdz_hkdzzd_cx = By.XPATH, 'html/body/div[1]/form/div[4]/input'

# 借款到账
cw_zqdz_jkdz = By.XPATH, 'html/body/div[1]/div[9]/div[2]/div/ul/li[5]/a'
# 项目名称
cw_zqdz_jkdz_name = By.XPATH, 'html/body/div[1]/form/div[1]/input'
# 到账日期
cw_zqdz_jkdz_dzrq = By.XPATH, 'html/body/div[1]/form/div[2]/div/a'
# 选择到账日期
cw_zqdz_jkdz_dzrq_xz = By.XPATH, 'html/body/div[4]/ul/li[2]/div'
# 查询
cw_zqdz_jkdz_cx = By.XPATH, 'html/body/div[1]/form/div[3]/input'

# 提现记录
cw_zqdz_txjl = By.XPATH, 'html/body/div[1]/div[9]/div[2]/div/ul/li[6]/a'
# 查看明细
cw_zqdz_txjl_ckmx = By.XPATH, 'html/body/div[1]/div[2]/span[2]'
# 新增提现记录
cw_zqdz_txjl_xztxjl = By.XPATH, 'html/body/div[1]/div[2]/input'
# 转入银行卡
cw_zqdz_txjl_zryhk = By.XPATH, 'html/body/div[1]/form/div[1]/div/a'
# 选择银行卡
cw_zqdz_txjl_zryhk_xz = By.XPATH, 'html/body/div[6]/ul/li[2]/div'
# 交易时间
# 查询
cw_zqdz_txjl_cx = By.XPATH, 'html/body/div[1]/form/div[3]/input'

# 充值记录
cw_zqdz_czjl = By.XPATH, 'html/body/div[1]/div[9]/div[2]/div/ul/li[7]/a'
# 查看明细
cw_zqdz_czjl_ckmx = By.XPATH, 'html/body/div[1]/div/div/span[3]'
# 新增充值记录
cw_zqdz_czjl_xzczjl = By.XPATH, 'html/body/div[1]/div/div/input'
# 充值方式
cw_zqdz_czjl_czfs = By.XPATH, 'html/body/div[1]/form/div[1]/div/a'
# 选择充值方式
cw_zqdz_czjl_czfs_xz = By.XPATH, 'html/body/div[6]/ul/li[2]/div'
# 交易时间
# 查询
cw_zqdz_czjl_cx = By.XPATH, 'html/body/div[1]/form/div[3]/input'

# 保证金返还
cw_zqdz_bzjfh = By.XPATH, 'html/body/div[1]/div[9]/div[2]/div/ul/li[8]/a'
# 项目名称
cw_zqdz_bzjfh_name = By.XPATH, 'html/body/div[1]/form/div[1]/input'
# 返还日期
cw_zqdz_bzjfh_fhrq = By.XPATH, 'html/body/div[1]/form/div[2]/div/a'
# 选择返还日期
cw_zqdz_bzjfh_fhrq_xz = By.XPATH, 'html/body/div[5]/ul/li[2]/div'
# 查询
cw_zqdz_bzjfh_cx = By.XPATH, 'html/body/div[1]/form/div[3]/input'

# 交易往来记录
cw_zqdz_jywljl = By.XPATH, 'html/body/div[1]/div[9]/div[2]/div/ul/li[9]/a'
# 交易类型
cw_zqdz_jywljl_jylx = By.XPATH, 'html/body/div[1]/form/div[1]/div/a'
# 选择交易类型
cw_zqdz_jywljl_jylx_xz = By.XPATH, 'html/body/div[5]/ul/li[2]/div'
# 流水号
cw_zqdz_jywljl_lsh = By.XPATH, 'html/body/div[1]/form/div[2]/input'
# 交易时间
# 查询
cw_zqdz_jywljl_cx = By.XPATH, 'html/body/div[1]/form/div[4]/input'

# 营业报表
cw_yybb = By.XPATH, 'html/body/div[1]/div[10]/div[1]/a'
# 日报表
cw_yybb_rbb = By.XPATH, 'html/body/div[1]/div[10]/div[2]/div/ul/li[1]/a'
# 月报表
cw_yybb_ybb = By.XPATH, 'html/body/div[1]/div[10]/div[2]/div/ul/li[2]/a'

# 累计报表
cw_yybb_ljbb = By.XPATH, 'html/body/div[1]/div[10]/div[2]/div/ul/li[3]/a'
# 累计订单
cw_yybb_ljbb_ljdd = By.XPATH, 'html/body/div[1]/div/ul/li[1]'
# 合计金额 债权总额
cw_yybb_ljbb_hjzq = By.XPATH, 'html/body/div[1]/div/ul/li[2]'
# 时间范围
# 查询
cw_yybb_ljbb_cx = By.XPATH, 'html/body/div[1]/form/div/div[2]/input'

# 对比报表
cw_yybb_dbbb = By.XPATH, 'html/body/div[1]/div[10]/div[2]/div/ul/li[4]/a'
# A月
cw_yybb_dbbb_ay = By.XPATH, 'html/body/div[1]/form/div[1]/input'
# B月
cw_yybb_dbbb_by = By.XPATH, 'html/body/div[1]/form/div[2]/input'
# 查询
cw_yybb_dbbb_cx = By.XPATH, 'html/body/div[1]/form/div[3]/input'

"""
系统设置页面元素
"""
# 权限管理
xt_qxgl = By.XPATH, 'html/body/div[1]/div[1]/div[1]/a'
# 菜单管理
xt_qxgl_cdgl = By.XPATH, 'html/body/div[1]/div[1]/div[2]/div/ul/li[1]/a'
# 菜单列表页面
xt_qxgl_cdgl_lb = By.XPATH, 'html/body/div[1]/div/ul/li[1]/a'
# 修改
xt_qxgl_cdgl_lb_xg = By.XPATH, 'html/body/form/table/tbody/tr[2]/td[6]/a[1]'
# 删除
xt_qxgl_cdgl_sc = By.XPATH, 'html/body/form/table/tbody/tr[2]/td[6]/a[2]'
# 添加下级菜单
xt_qxgl_cdgl_tjxjcd = By.XPATH, 'html/body/form/table/tbody/tr[2]/td[6]/a[3]'
# 保存排序
xt_qxgl_cdgl_save = By.XPATH, 'html/body/form/div/input'
# 同步工作流权限
xt_qxgl_cdgl_tb = By.XPATH, 'html/body/form/div/div/a'

# 菜单添加页面
xt_qxgl_cdgl_tj = By.XPATH, 'html/body/div[1]/div/ul/li[2]/a'
# 上级菜单
# 名称
xt_qxgl_cdgl_tj_mc = By.XPATH, 'html/body/form/div[2]/div/input'
# 链接
xt_qxgl_cdgl_tj_lj = By.XPATH, 'html/body/form/div[3]/div/input'
# 目标
xt_qxgl_cdgl_tj_mb = By.XPATH, 'html/body/form/div[4]/div/input'
# 选择
xt_qxgl_cdgl_tj_xz = By.XPATH, 'html/body/form/div[5]/div/a'
# 排序
xt_qxgl_cdgl_tj_px = By.XPATH, 'html/body/form/div[6]/div/input'
# 可见
xt_qxgl_cdgl_tj_kj = By.XPATH, 'html/body/form/div[7]/div/span[1]/input'
# 同步到工作流
xt_qxgl_cdgl_tj_tb = By.XPATH, 'html/body/form/div[8]/div/span[1]/input'
# 权限标识
xt_qxgl_cdgl_tj_qxbs = By.XPATH, 'html/body/form/div[9]/div/input'
# 保存
xt_qxgl_cdgl_tj_save = By.XPATH, 'html/body/form/div[10]/input[1]'
# 返回
xt_qxgl_cdgl_tj_back = By.XPATH, 'html/body/form/div[10]/input[2]'

# 菜单修改页面
xt_qxgl_cdgl_xg = By.XPATH, 'html/body/div[1]/div/ul/li[2]/a'
# 上级菜单
# 名称
xt_qxgl_cdgl_xg_mc = By.XPATH, 'html/body/form/div[2]/div/input'
# 链接
xt_qxgl_cdgl_xg_lj = By.XPATH, 'html/body/form/div[3]/div/input'
# 目标
xt_qxgl_cdgl_xg_mb = By.XPATH, 'html/body/form/div[4]/div/input'
# 选择
xt_qxgl_cdgl_xg_xz = By.XPATH, 'html/body/form/div[5]/div/a'
# 排序
xt_qxgl_cdgl_xg_px = By.XPATH, 'html/body/form/div[6]/div/input'
# 可见
xt_qxgl_cdgl_xg_kj = By.XPATH, 'html/body/form/div[7]/div/span[1]/input'
# 同步到工作流
xt_qxgl_cdgl_xg_tb = By.XPATH, 'html/body/form/div[8]/div/span[1]/input'
# 权限标识
xt_qxgl_cdgl_xg_qxbs = By.XPATH, 'html/body/form/div[9]/div/input'
# 保存
xt_qxgl_cdgl_xg_save = By.XPATH, 'html/body/form/div[10]/input[1]'
# 返回
xt_qxgl_cdgl_xg_back = By.XPATH, 'html/body/form/div[10]/input[2]'

# 角色管理
xt_qxgl_jsgl = By.XPATH, 'html/body/div[1]/div[1]/div[2]/div/ul/li[2]/a'
# 人员管理
xt_qxgl_rygl = By.XPATH, 'html/body/div[1]/div[1]/div[2]/div/ul/li[3]/a'
# 用户列表
xt_qxgl_rygl_lb = By.XPATH, 'html/body/div[2]/div/ul/li[1]/a'
# 登录名
xt_qxgl_rygl_dlm = By.XPATH, 'html/body/div[2]/form/div[1]/input'
# 姓名
xt_qxgl_rygl_name = By.XPATH, 'html/body/div[2]/form/div[2]/input'
# 角色
xt_qxgl_rygl_js = By.XPATH, 'html/body/div[2]/form/div[3]/div/a'
# 选择角色
xt_qxgl_rygl_xzjs = By.XPATH, 'html/body/div[5]/ul/li[4]/div'
# 查询
xt_qxgl_rygl_cx = By.XPATH, 'html/body/div[2]/form/div[5]/input[1]'
# 导出
xt_qxgl_rygl_dc = By.XPATH, 'html/body/div[2]/form/div[5]/input[2]'

# 离职管理
xt_qxgl_lzgl = By.XPATH, 'html/body/div[1]/div[1]/div[2]/div/ul/li[4]/a'
# 登录名
xt_qxgl_lzgl_dlm = By.XPATH, 'html/body/div[2]/form/div[1]/input'
# 姓名
xt_qxgl_lzgl_name = By.XPATH, 'html/body/div[2]/form/div[2]/input'
# 角色
xt_qxgl_lzgl_js = By.XPATH, 'html/body/div[2]/form/div[3]/div/a'
# 选择角色
xt_qxgl_lzgl_xzjs = By.XPATH, 'html/body/div[5]/ul/li[2]/div'
# 查询
xt_qxgl_lzgl_cx = By.XPATH, 'html/body/div[2]/form/div[5]/input[1]'
# 导出
xt_qxgl_lzgl_dc = By.XPATH, 'html/body/div[2]/form/div[5]/input[2]'

# 系统日志
xt_xtrz = By.XPATH, 'html/body/div[1]/div[2]/div[1]/a'
# 操作日志
xt_xtrz_czrz = By.XPATH, 'html/body/div[1]/div[2]/div[2]/div/ul/li[1]/a'
# 用户id
xt_xtrz_yhid = By.XPATH, 'html/body/div[1]/form/div[1]/input'
# url
xt_xtrz_url = By.XPATH, 'html/body/div[1]/form/div[2]/input'
# 开始日期
xt_xtrz_ksrq = By.CSS_SELECTOR, '#beginDate'
# 结束日期
xt_xtrz_jsrq = By.CSS_SELECTOR, '#endDate'
# 异常信息
xt_xtrz_ycxx = By.CSS_SELECTOR, '#exception'
# 查询
xt_xtrz_cx = By.CSS_SELECTOR, '#btnSubmit'

# 短信日志
xt_xtrz_dxrz = By.XPATH, 'html/body/div[1]/div[2]/div[2]/div/ul/li[2]/a'
# 手机号码
xt_xtrz_dxrz_phone = By.CSS_SELECTOR, '#mobile'
# 短信内容
xt_xtrz_dxrz_dxnr = By.CSS_SELECTOR, '#content'
# 短信id
xt_xtrz_dxrz_id = By.CSS_SELECTOR, '#sendid'
# ip地址
xt_xtrz_dxrz_ip = By.CSS_SELECTOR, '#reqIpaddr'
# 回执状态
xt_xtrz_dxrz_hzzt = By.XPATH, 'html/body/div[2]/form/div[5]/div/a'
# 选择回执状态
xt_xtrz_dxrz_xzzt = By.XPATH, 'html/body/div[6]/ul/li[3]/div'
# 查询
xt_xtrz_dxrz_cx = By.CSS_SELECTOR, '#btnSubmit'
# 催收短信发送
xt_xtrz_dxrz_csdx = By.XPATH, 'html/body/div[2]/div/button'
# 学生电话
xt_xtrz_dxrz_xsdh = By.XPATH, 'html/body/div[1]/div[2]/div[1]/div/input[1]'
# 查询
xt_xtrz_dxrz_csdx_cx = By.XPATH, 'html/body/div[1]/div[2]/div[1]/div/input[2]'
# 取消
xt_xtrz_dxrz_csdx_qx = By.XPATH, 'html/body/div[1]/div[3]/button[2]'

# 接收客户短信
xt_xtrz_jskhdx = By.XPATH, 'html/body/div[1]/div[2]/div[2]/div/ul/li[3]/a'
# 手机号码
xt_xtrz_jskhdx_phone = By.CSS_SELECTOR, '#mobile'
# 请求ip
xt_xtrz_jskhdx_ip = By.CSS_SELECTOR, '#reqIpaddr'
# 状态
xt_xtrz_jskhdx_zt = By.CSS_SELECTOR, '.select2-choice'
# 选择状态
xt_xtrz_jskhdx_xzzt = By.CSS_SELECTOR, '.select2-result-label'
# 查询
xt_xtrz_jskhdx_cx = By.CSS_SELECTOR, '#btnSubmit'
# 阅读
xt_xtrz_jskhdx_yd = By.XPATH, 'html/body/div[2]/table/tbody/tr[1]/td[7]/a'

# 定时任务日志
xt_xtrz_dsrwrz = By.XPATH, 'html/body/div[1]/div[2]/div[2]/div/ul/li[4]/a'
# 任务描述
xt_xtrz_dsrwrz_rwms = By.XPATH, 'html/body/div[2]/div[1]/div[2]/div/span/span[1]/span/span[1]'
# 选择任务描述
xt_xtrz_dsrwrz_rwms_xz = By.XPATH, 'html/body/span/span/span[2]/ul/li[2]'
# 时间
# 查询
xt_xtrz_dsrwrz_cx = By.XPATH, 'html/body/div[2]/div[1]/div[4]/button'

# 数据字典
xt_sjzd = By.XPATH, 'html/body/div[1]/div[3]/div[1]/a'
# 字典管理
xt_sjzd_zdgl = By.XPATH, 'html/body/div[1]/div[3]/div[2]/div/ul/li[1]/a'
# 字典列表页面
xt_sjzd_zdgl_lb = By.XPATH, 'html/body/div[1]/div/ul/li[1]/a'
# 类型
xt_sjzd_zdgl_lx = By.XPATH, 'html/body/div[1]/form/div[1]/div/a'
# 选择类型
xt_sjzd_zdgl_xzlx = By.XPATH, 'html/body/div[5]/ul/li[4]/div'
# 描述
xt_sjzd_zdgl_ms = By.XPATH, 'html/body/div[1]/form/div[2]/input'
# 查询
xt_sjzd_zdgl_cx = By.XPATH, 'html/body/div[1]/form/div[3]/input'
# 发布
xt_sjzd_zdgl_fb = By.XPATH, 'html/body/div[2]/table/tbody/tr[4]/td[2]/a'
# 点击类型（archives_gdflag）
xt_sjzd_zdgl_zm = By.XPATH, 'html/body/div[2]/table/tbody/tr[1]/td[3]/a'
# 修改
xt_sjzd_zdgl_lb_xg = By.XPATH, 'html/body/div[2]/table/tbody/tr[1]/td[6]/a[1]'
# 删除
xt_sjzd_zdgl_sc = By.XPATH, 'html/body/div[2]/table/tbody/tr[1]/td[6]/a[2]'
# 添加键值
xt_sjzd_zdgl_tjjz = By.XPATH, 'html/body/div[2]/table/tbody/tr[1]/td[6]/a[3]'

# 字典添加页面
xt_sjzd_zdgl_tj = By.XPATH, 'html/body/div[1]/div/ul/li[2]/a'
# 键值
xt_sjzd_zdgl_tj_jz = By.XPATH, 'html/body/form/div[1]/div/input'
# 标签
xt_sjzd_zdgl_tj_bq = By.XPATH, 'html/body/form/div[2]/div/input'
# 类型
xt_sjzd_zdgl_tj_lx = By.XPATH, 'html/body/form/div[3]/div/input'
# 描述
xt_sjzd_zdgl_tj_ms = By.XPATH, 'html/body/form/div[4]/div/input'
# 排序
xt_sjzd_zdgl_tj_px = By.XPATH, 'html/body/form/div[5]/div/input'
# 保存
xt_sjzd_zdgl_tj_save = By.XPATH, 'html/body/form/div[6]/input[1]'
# 返回
xt_sjzd_zdgl_tj_back = By.XPATH, 'html/body/form/div[6]/input[2]'

# 字典修改页面
xt_sjzd_zdgl_xg = By.XPATH, 'html/body/div[1]/div/ul/li[2]/a'
# 键值
xt_sjzd_zdgl_xg_jz = By.XPATH, 'html/body/form/div[1]/div/input'
# 标签
xt_sjzd_zdgl_xg_bq = By.XPATH, 'html/body/form/div[2]/div/input'
# 类型
xt_sjzd_zdgl_xg_lx = By.XPATH, 'html/body/form/div[3]/div/input'
# 描述
xt_sjzd_zdgl_xg_ms = By.XPATH, 'html/body/form/div[4]/div/input'
# 排序
xt_sjzd_zdgl_xg_px = By.XPATH, 'html/body/form/div[5]/div/input'
# 保存
xt_sjzd_zdgl_xg_save = By.XPATH, 'html/body/form/div[6]/input[1]'
# 返回
xt_sjzd_zdgl_xg_back = By.XPATH, 'html/body/form/div[6]/input[2]'

# 电话库管理
xt_sjzd_dhkgl = By.XPATH, 'html/body/div[1]/div[3]/div[2]/div/ul/li[2]/a'
# 电话库列表页面
xt_sjzd_dhkgl_lb = By.XPATH, 'html/body/div[1]/div/ul/li[1]/a'
# 归属平台
xt_sjzd_dhkgl_lb_gspt = By.XPATH, 'html/body/div[1]/form/div[1]/input'
# 归属类型
xt_sjzd_dhkgl_lb_gslx = By.XPATH, 'html/body/div[1]/form/div[2]/div/a'
# 选择归属类型
xt_sjzd_dhkgl_lb_xzlx = By.XPATH, 'html/body/div[5]/ul/li[3]/div'
# 电话号码
xt_sjzd_dhkgl_lb_phone = By.XPATH, 'html/body/div[1]/form/div[3]/input'
# 查询
xt_sjzd_dhkgl_lb_cx = By.XPATH, 'html/body/div[1]/form/div[4]/input'
# 修改
xt_sjzd_dhkgl_lb_xg = By.XPATH, 'html/body/div[2]/table/tbody/tr[1]/td[5]/a[1]'
# 删除
xt_sjzd_dhkgl_lb_sc = By.XPATH, 'html/body/div[2]/table/tbody/tr[1]/td[5]/a[2]'

# 电话添加页面
xt_sjzd_dhkgl_tj = By.XPATH, 'html/body/div[1]/div/ul/li[2]/a'
# 号码
xt_sjzd_dhkgl_tj_num = By.XPATH, 'html/body/form/div[1]/div/input'
# 归属平台
xt_sjzd_dhkgl_tj_gspt = By.XPATH, 'html/body/form/div[2]/div/input'
# 归属类型
xt_sjzd_dhkgl_tj_gslx = By.XPATH, 'html/body/form/div[3]/div/div/a'
# 选择归属类型
xt_sjzd_dhkgl_tj_lx = By.XPATH, 'html/body/div[3]/ul/li[3]/div'
# 保存
xt_sjzd_dhkgl_tj_save = By.XPATH, 'html/body/form/div[4]/input[1]'
# 返回
xt_sjzd_dhkgl_tj_back = By.XPATH, 'html/body/form/div[4]/input[2]'

# 电话修改页面
# 号码
xt_sjzd_dhkgl_xg_num = By.XPATH, 'html/body/form/div[1]/div/input'
# 归属平台
xt_sjzd_dhkgl_xg_gspt = By.XPATH, 'html/body/form/div[2]/div/input'
# 归属类型
xt_sjzd_dhkgl_xg_gslx = By.XPATH, 'html/body/form/div[3]/div/div/a'
# 选择归属类型
xt_sjzd_dhkgl_xg_lx = By.XPATH, 'html/body/div[3]/ul/li[3]/div'
# 保存
xt_sjzd_dhkgl_xg_save = By.XPATH, 'html/body/form/div[4]/input[1]'
# 返回
xt_sjzd_dhkgl_xg_back = By.XPATH, 'html/body/form/div[4]/input[2]'

# 机构管理
xt_sjzd_jggl = By.XPATH, 'html/body/div[1]/div[3]/div[2]/div/ul/li[3]/a'
# 机构列表页面
xt_sjzd_jggl_lb = By.XPATH, 'html/body/div[1]/div/ul/li[1]/a'
# 选择机构名称
xt_sjzd_jggl_lb_jgmc = By.XPATH, 'html/body/table/tbody/tr[2]/td[1]/a'
# 修改
xt_sjzd_jggl_lb_xg = By.XPATH, 'html/body/table/tbody/tr[2]/td[6]/a[1]'
# 删除
xt_sjzd_jggl_lb_sc = By.XPATH, 'html/body/table/tbody/tr[2]/td[6]/a[2]'
# 添加下级机构
xt_sjzd_jggl_lb_tlxj = By.XPATH, 'html/body/table/tbody/tr[2]/td[6]/a[3]'

# 机构添加
xt_sjzd_jggl_tj = By.XPATH, 'html/body/div[1]/div/ul/li[2]/a'
# 上级机构
# 归属区域
# 机构名称
xt_sjzd_jggl_tj_mc = By.XPATH, 'html/body/form/div[3]/div/input'
# 机构编码
xt_sjzd_jggl_tj_bm = By.XPATH, 'html/body/form/div[4]/div/input'
# 机构类型
# 机构级别
# 联系地址
xt_sjzd_jggl_tj_dz = By.XPATH, 'html/body/form/div[7]/div/input'
# 邮政编码
xt_sjzd_jggl_tj_yzbm = By.XPATH, 'html/body/form/div[8]/div/input'
# 负责人
xt_sjzd_jggl_tj_fzr = By.XPATH, 'html/body/form/div[9]/div/input'
# 电话
xt_sjzd_jggl_tj_phone = By.XPATH, 'html/body/form/div[10]/div/input'
# 传真
xt_sjzd_jggl_tj_cz = By.XPATH, 'html/body/form/div[11]/div/input'
# 邮箱
xt_sjzd_jggl_tj_yx = By.XPATH, 'html/body/form/div[12]/div/input'
# 备注
xt_sjzd_jggl_tj_bz = By.XPATH, 'html/body/form/div[13]/div/textarea'
# 保存
xt_sjzd_jggl_tj_save = By.XPATH, 'html/body/form/div[14]/input[1]'
# 返回
xt_sjzd_jggl_tj_back = By.XPATH, 'html/body/form/div[14]/input[2]'

# 机构修改
xt_sjzd_jggl_xg = By.XPATH, 'html/body/div[1]/div/ul/li[2]/a'
# 上级机构
# 归属区域
# 机构名称
xt_sjzd_jggl_xg_mc = By.XPATH, 'html/body/form/div[3]/div/input'
# 机构编码
xt_sjzd_jggl_xg_bm = By.XPATH, 'html/body/form/div[4]/div/input'
# 机构类型
# 机构级别
# 联系地址
xt_sjzd_jggl_xg_dz = By.XPATH, 'html/body/form/div[7]/div/input'
# 邮政编码
xt_sjzd_jggl_xg_yzbm = By.XPATH, 'html/body/form/div[8]/div/input'
# 负责人
xt_sjzd_jggl_xg_fzr = By.XPATH, 'html/body/form/div[9]/div/input'
# 电话
xt_sjzd_jggl_xg_phone = By.XPATH, 'html/body/form/div[10]/div/input'
# 传真
xt_sjzd_jggl_xg_cz = By.XPATH, 'html/body/form/div[11]/div/input'
# 邮箱
xt_sjzd_jggl_xg_yx = By.XPATH, 'html/body/form/div[12]/div/input'
# 备注
xt_sjzd_jggl_xg_bz = By.XPATH, 'html/body/form/div[13]/div/textarea'
# 保存
xt_sjzd_jggl_xg_save = By.XPATH, 'html/body/form/div[14]/input[1]'
# 返回
xt_sjzd_jggl_xg_back = By.XPATH, 'html/body/form/div[14]/input[2]'

# 区域管理
xt_sjzd_qygl = By.XPATH, 'html/body/div[1]/div[3]/div[2]/div/ul/li[4]/a'
# 区域列表页面
xt_sjzd_qygl_lb = By.XPATH, 'html/body/div[1]/div/ul/li[1]/a'
# 区域名称
xt_sjzd_qygl_lb_qymc = By.XPATH, 'html/body/table/tbody/tr[2]/td[1]/a'
# 修改
xt_sjzd_qygl_lb_xg = By.XPATH, 'html/body/table/tbody/tr[2]/td[5]/a[1]'
# 删除
xt_sjzd_qygl_lb_sc = By.XPATH, 'html/body/table/tbody/tr[2]/td[5]/a[2]'
# 添加下级区域
xt_sjzd_qygl_lb_tjxjqy = By.XPATH, 'html/body/table/tbody/tr[2]/td[5]/a[3]'

# 区域添加页面
xt_sjzd_qygl_tj = By.XPATH, 'html/body/div[1]/div/ul/li[2]/a'
# 上级区域
# 区域名称
xt_sjzd_qygl_tj_mc = By.XPATH, 'html/body/form/div[2]/div/input'
# 区域编码
xt_sjzd_qygl_tj_bm = By.XPATH, 'html/body/form/div[3]/div/input'
# 区域类型
# 城市等级
# 备注
xt_sjzd_qygl_tj_bz = By.XPATH, 'html/body/form/div[6]/div/textarea'
# 保存
xt_sjzd_qygl_tj_save = By.XPATH, 'html/body/form/div[7]/input[1]'
# 返回
xt_sjzd_qygl_tj_fh = By.XPATH, 'html/body/form/div[7]/input[2]'

# 区域修改页面
xt_sjzd_qygl_xg = By.XPATH, 'html/body/div[1]/div/ul/li[2]/a'
# 上级区域
# 区域名称
xt_sjzd_qygl_xg_mc = By.XPATH, 'html/body/form/div[2]/div/input'
# 区域编码
xt_sjzd_qygl_xg_bm = By.XPATH, 'html/body/form/div[3]/div/input'
# 区域类型
# 城市等级
# 备注
xt_sjzd_qygl_xg_bz = By.XPATH, 'html/body/form/div[6]/div/textarea'
# 保存
xt_sjzd_qygl_xg_save = By.XPATH, 'html/body/form/div[7]/input[1]'
# 返回
xt_sjzd_qygl_xg_fh = By.XPATH, 'html/body/form/div[7]/input[2]'

# 学校管理
xt_sjzd_xxgl = By.XPATH, 'html/body/div[1]/div[3]/div[2]/div/ul/li[5]/a'
# 学校列表页面
xt_sjzd_xxgl_lb = By.XPATH, 'html/body/ul/li[1]/a'
# 所属区域
# 学校名称
xt_sjzd_xxgl_lb_xxmc = By.XPATH, 'html/body/form/input[2]'
# 学校简称
xt_sjzd_xxgl_lb_xxjc = By.XPATH, 'html/body/form/input[3]'
# 学校性质
xt_sjzd_xxgl_lb_xxxz = By.XPATH, 'html/body/form/div[2]/a'
# 选择学校性质
xt_sjzd_xxgl_lb_xzxz = By.XPATH, 'html/body/div[4]/ul/li[2]/div'
# 每页显示条数
xt_sjzd_xxgl_lb_myts = By.XPATH, 'html/body/form/div[3]/a'
# 选择每页显示条数
xt_sjzd_xxgl_lb_xzmys = By.XPATH, 'html/body/div[4]/ul/li[1]/div'
# 查询
xt_sjzd_xxgl_lb_cx = By.XPATH, 'html/body/form/input[4]'
# 生成js文件
xt_sjzd_xxgl_lb_scjs = By.XPATH, 'html/body/form/input[5]'

# 学校添加页面
xt_sjzd_xxgl_tj = By.XPATH, 'html/body/ul/li[2]/a'
# 定位到该城市
xt_sjzd_xxgl_tj_qy_dw = By.XPATH, 'html/body/form/div[1]/div/input'
# 学校名称
# 定位到该学校
# 学校简称
# 学校性质
# 选择学校性质
# 在校人数
# 学校地址
# 定位
# 官方电话
# 邮政编码
# 官网地址
# 学校简历
# x坐标
# y坐标
# 保存
# 返回



# 定时任务管理
xt_dsrwgl = By.XPATH, 'html/body/div[1]/div[4]/div[1]/a'
# 任务管理
xt_dsrwgl_rwgl = By.XPATH, 'html/body/div[1]/div[4]/div[2]/div/ul/li/a'
# 添加任务
xt_dsrwgl_rwgl_tjrw = By.XPATH, 'html/body/div[2]/div[1]/div[2]/button'
# 运行
xt_dsrwgl_rwgl_yx = By.XPATH, 'html/body/div[2]/table/tbody/tr[1]/td[9]/button[1]'
# 编辑
xt_dsrwgl_rwgl_bj = By.XPATH, 'html/body/div[2]/table/tbody/tr[1]/td[9]/button[2]'
# 删除
xt_dsrwgl_rwgl_sc = By.XPATH, 'html/body/div[2]/table/tbody/tr[1]/td[9]/button[3]'

# 利率管理
xt_llgl = By.XPATH, 'html/body/div[1]/div[5]/div[1]/a'
# 地区利率
xt_llgl_dq = By.XPATH, 'html/body/div[1]/div[5]/div[2]/div/ul/li[1]/a'
# 地区利率列表
xt_llgl_dq_lb = By.XPATH, 'html/body/div[1]/div/ul/li[1]/a'
# 状态
xt_llgl_dq_lb_zt = By.XPATH, 'html/body/div[1]/form/div[2]/div/a'
# 选择正常
xt_llgl_dq_lb_zc = By.XPATH, 'html/body/div[6]/ul/li[2]/div'
# 查询
xt_llgl_dq_lb_cx = By.XPATH, 'html/body/div[1]/form/div[3]/input[1]'
# 更新缓存中
xt_llgl_dq_lb_gx = By.XPATH, 'html/body/div[1]/form/div[3]/input[2]'
# 点击x
xt_llgl_dq_lb_x = By.XPATH, 'html/body/div[2]/button'
# 设置利率
xt_llgl_dq_lb_szll = By.XPATH, 'html/body/div[2]/table/tbody/tr[1]/td[6]/a[1]'
# 输入期数
xt_llgl_dq_lb_szll_qs = By.XPATH, 'html/body/form[2]/div[1]/div/input'
# 点击利率类型
xt_llgl_dq_lb_szll_lllx = By.XPATH, 'html/body/form[2]/div[2]/div/div/a'
# 选择利率类型
xt_llgl_dq_lb_szll_lllx_xz = By.XPATH, 'html/body/div[3]/ul/li[2]/div'
# 输入利率
xt_llgl_dq_lb_szll_ll = By.XPATH, 'html/body/form[2]/div[3]/div/input'
# 点击保存
xt_llgl_dq_lb_szll_save = By.XPATH, 'html/body/form[2]/div[4]/input[1]'
# 点击返回
xt_llgl_dq_lb_szll_back = By.XPATH, 'html/body/form[2]/div[4]/input[2]'
# 查看利率
xt_llgl_dq_lb_ckll = By.XPATH, 'html/body/div[2]/table/tbody/tr[1]/td[6]/a[2]'
# 返回
xt_llgl_dq_lb_ckll_back = By.XPATH, 'html/body/form[2]/div/input[1]'
# 删除
xt_llgl_dq_lb_sc = By.XPATH, 'html/body/div[2]/table/tbody/tr[1]/td[6]/a[3]'

# 地区利率添加
xt_llgl_dq_tj = By.XPATH, 'html/body/div[1]/div/ul/li[2]/a'
# 利率名称
xt_llgl_dq_tj_llmc = By.XPATH, 'html/body/form/div[2]/div/input'
# 保存
xt_llgl_dq_tj_save = By.XPATH, 'html/body/form/div[3]/input[1]'
# 返回
xt_llgl_dq_tj_back = By.XPATH, 'html/body/form/div[3]/input[2]'

# 期利率
xt_llgl_qll = By.XPATH, 'html/body/div[1]/div[5]/div[2]/div/ul/li[2]/a'
# 期利率列表
xt_llgl_qll_lb = By.XPATH, 'html/body/div[1]/div/ul/li[1]/a'
# 期数
xt_llgl_qll_lb_qs = By.XPATH, 'html/body/div[1]/form/div[1]/input'
# 利率类型
xt_llgl_qll_lb_lx = By.XPATH, 'html/body/div[1]/form/div[2]/div/a'
# 选择零花钱
xt_llgl_qll_lb_lhq = By.XPATH, 'html/body/div[4]/ul/li[2]/div'
# 状态
xt_llgl_qll_lb_zt = By.XPATH, 'html/body/div[1]/form/div[3]/div/a'
# 选择正常
xt_llgl_qll_lb_zc = By.XPATH, 'html/body/div[5]/ul/li[2]/div'
# 查询
xt_llgl_qll_lb_cx = By.XPATH, 'html/body/div[1]/form/div[4]/input'
# 修改
xt_llgl_qll_lb_xg = By.XPATH, 'html/body/table/tbody/tr[1]/td[7]/a[1]'

# 修改页面
# 期数
xt_llgl_qll_xg_qs = By.XPATH, 'html/body/form/div[1]/div/input'
# 利率
xt_llgl_qll_xg_ll = By.XPATH, 'html/body/form/div[3]/div/input'
# 保存
xt_llgl_qll_xg_save = By.XPATH, 'html/body/form/div[4]/input[1]'
# 返回
xt_llgl_qll_xg_back = By.XPATH, 'html/body/form/div[4]/input[2]'

# 期利率添加页面
xt_llgl_qll_tj = By.XPATH, 'html/body/div[1]/div/ul/li[2]/a'
# 期数
xt_llgl_qll_tj_qs = By.XPATH, 'html/body/form/div[1]/div/input'
# 利率类型
xt_llgl_qll_tj_lx = By.XPATH, 'html/body/form/div[2]/div/div/a'
# 选择零花钱
xt_llgl_qll_tj_lhq = By.XPATH, 'html/body/div[3]/ul/li[1]/div'
# 利率
xt_llgl_qll_tj_ll = By.XPATH, 'html/body/form/div[3]/div/input'
# 保存
xt_llgl_qll_tj_save = By.XPATH, 'html/body/form/div[4]/input[1]'
# 返回
xt_llgl_qll_tj_back = By.XPATH, 'html/body/form/div[4]/input[2]'

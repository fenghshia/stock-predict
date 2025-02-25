# --*-- Coding : UTF-8     --*--
# @Project     : stock-predict
# @File        : __init__.py.py
# @Time        : 2025/2/25 下午4:32
# @IDE         : PyCharm
# @Description : Input Here
# --*-- Author : FengHShia --*--
# Log类: 规范日志操作, 包含 执行ID, 日志等级, 生成时间, 日志内容, 重写str函数
# Logger类: 包含 日志队列: 存储待写入loki的日志,
#               主队列: 存储Log实例,
#               字典缓存: 根据执行ID划分日志队列,
#               主队列处理函数: 根据Log实例处理日志, 新增或删除字典缓存,
#               日志队列处理函数: 将日志队列中数据写入loki,
#               监听器: 监听apscheduler事件, 控制字典缓存

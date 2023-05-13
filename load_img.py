import base64
import datetime


def image_to_base64(image_path):
    with open(image_path, "rb") as f:
        encoded_image = base64.b64encode(f.read()).decode('utf-8')
    return encoded_image

# 获取当前时间
now = datetime.datetime.now()
# 指定日期
target_date = datetime.datetime(2023, 4, 18)
# 计算时间差
time_diff = now - target_date

wechat_image_text = "如需帮助可以加入群聊讨论：" + '<img src="data:image/png;base64,' + image_to_base64("img/wechatgroup.png") + '"/>'
wepay_image_text = "本项目目前上线运行{0}天已经消耗chatgpt-api超过{1}刀，需要您的赞助：".format(time_diff.days, 3*time_diff.days + 9) \
                   + '<img src="data:image/png;base64,' + image_to_base64("img/wepay.png") + '"/>'
mywechat_image_text = "如需定制私人人工智能方案 或 进行论文python数据分析 可以加微信详谈需求" + '<img src="data:image/png;base64,' +\
                      image_to_base64("img/wechat.png") + '"/>'

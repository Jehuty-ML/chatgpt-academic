import os

from toolbox import CatchException, update_ui, report_execption
from .crazy_utils import request_gpt_model_in_new_thread_with_ui_alive
import datetime

from .加群 import wechat_image_text


def check_code_has_list(gpt_say):
    # 检验输入区是否包含代码块
    if gpt_say.count("`") < 1:
        not_code = True
    else:
        not_code = False
    if not_code:
        i_say = 'ppt的内容要代码块输出'
    else:
        i_say = ''
    return i_say


@CatchException
def 一键生成PPT_mindshow(txt, llm_kwargs, plugin_kwargs, chatbot, history, system_prompt, web_port):
    """
    txt             输入栏用户输入的文本，例如需要翻译的一段话，再例如一个包含了待处理文件的路径
    llm_kwargs      gpt模型参数，如温度和top_p等，一般原样传递下去就行
    plugin_kwargs   插件模型的参数，暂时没有用武之地
    chatbot         聊天显示框的句柄，用于显示给用户
    history         聊天历史，前情提要
    system_prompt   给gpt的静默提醒
    web_port        当前软件运行的端口号

    update_ui必须在这个函数，不能在下一级函数，否则返回值会不匹配

    """

    # 清空历史，以免输入溢出
    history = []
    # 检测输入参数，如没有给定输入参数，直接退出
    if txt.strip() == "":
        txt = '请在输入区输入ppt的主题和要求'
        report_execption(chatbot, history, a="", b=txt)
        yield from update_ui(chatbot=chatbot, history=history)  # 刷新界面
        return

    i_say = '''帮我生成一篇主题为《{0}》的PPT，要求包含五部分内容，每部分需要包含3-4个要点，一定要用markdown源代码输出ppt内容。
    '''.format(txt)
#     i_say = '''帮我生成一篇主题为《{0}》的PPT
#     '''.format(txt)
    origin_i_say = i_say
    gpt_say = yield from request_gpt_model_in_new_thread_with_ui_alive(
        inputs=i_say, inputs_show_user=i_say,
        llm_kwargs=llm_kwargs, chatbot=chatbot, history=[],
        sys_prompt="你是一个ppt设计师，一定要用markdown源代码回复你生成的ppt内容，标题要用#号，副标题要用##号"
    )
    chatbot[-1] = (i_say, gpt_say)
    history.append(i_say);history.append(gpt_say)
    yield from update_ui(chatbot=chatbot, history=history)  # 刷新界面

    i_say = check_code_has_list(gpt_say=gpt_say)
    for i in range(3):
        if i_say == '':
            break
        elif i_say == 'ppt的内容要代码块输出':
            i_say = origin_i_say
            gpt_say = '```\n' + gpt_say + '\n```'
            chatbot[-1] = (i_say, gpt_say)
            history.append(i_say)
            history.append(gpt_say)
            yield from update_ui(chatbot=chatbot, history=history)  # 刷新界面
            i_say = check_code_has_list(gpt_say=gpt_say)
        else:
            gpt_say = yield from request_gpt_model_in_new_thread_with_ui_alive(
                inputs=i_say, inputs_show_user=i_say,
                llm_kwargs=llm_kwargs, chatbot=chatbot, history=[],
                sys_prompt="你是一个ppt设计师，一定要用markdown源代码回复你生成的ppt内容，标题要用#号，副标题要用##号"
            )
            chatbot[-1] = (i_say, gpt_say)
            history.append(i_say)
            history.append(gpt_say)
            yield from update_ui(chatbot=chatbot, history=history)  # 刷新界面
            i_say = check_code_has_list(gpt_say=gpt_say)

    chatbot.append(('chatgpt+mindshow 1分钟制作ppt教程：', '''[local message]<br>
    1.打开mindshow网址：[点我跳转地址🚀](https://mindshow.fun/#/folder/import)
    或复制链接打开：https://mindshow.fun/#/folder/import （第一次使用要先注册）<br>
    2.将刚刚上面生成的代码块内容复制到左侧文本框区域<br>
    3.点击“导入创建”按钮<br>
    4.检查ppt生成是否正常，如果太短或者排版不对请检查生成内容是否符合markdown格式的要求，作适当修改。<br>{}
    <br>其他更多精彩功能请自行探索'''.format(wechat_image_text)))
    yield from update_ui(chatbot=chatbot, history=history)  # 刷新界面

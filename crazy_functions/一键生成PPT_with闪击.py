import os

from toolbox import CatchException, update_ui, report_execption
from .crazy_utils import request_gpt_model_in_new_thread_with_ui_alive
import datetime


def check_code_has_list(gpt_say):
    # 检验输入区是否包含代码块
    if gpt_say.count("`") < 1:
        not_code = True
    else:
        not_code = False
    # 检验输入区是否包含多个 =======列表=======
    if gpt_say.count("=列表=") + gpt_say.count('= 列表页 =') <= 1:
        not_enough_list = True
    else:
        not_enough_list = False

    if not_enough_list and not_code:
        i_say = 'ppt的每个列表页都要使用======列表======开头，还有ppt内容要代码块输出'
    elif not_enough_list:
        i_say = 'ppt的每个列表页都要使用======列表======开头'
    elif not_code:
        i_say = 'ppt的内容要代码块输出'
    else:
        i_say = ''
    return i_say



@CatchException
def 一键生成PPT_with闪击(txt, llm_kwargs, plugin_kwargs, chatbot, history, system_prompt, web_port):
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

    i_say = '''帮我生成一篇主题为《{0}》的PPT，要求如下:
第一、一定要使用中文。
第二、页面形式有3种，封面、目录、列表。
第三、目录页要列出内容大纲，目录需要有5大块。
第四、根据内容大纲，生成对应的PPT列表页，每一页PPT列表页使用=====列表=====开头。
第五、封面页格式如下:======封面=====
#主标题
##副标题
演讲人:我的名字
第六、目录页格式如下:=====目录=====
#目录
##CONTENT
1、内容
2、内容
第七、列表页格式如下:=====列表===== 每个列表页要有3-4个要点
#页面主标题
1、要点
要点描述内容
第八、列表页里的要点描述内容是对要点的详细描述，10个字以上，50个字以内。
第九、一定要用代码块输出ppt内容
    '''.format(txt)
#     i_say = '''帮我生成一篇主题为《{0}》的PPT
#     '''.format(txt)
    gpt_say = yield from request_gpt_model_in_new_thread_with_ui_alive(
        inputs=i_say, inputs_show_user=i_say,
        llm_kwargs=llm_kwargs, chatbot=chatbot, history=[],
        sys_prompt="你是一个ppt大纲设计师，一定要用代码块回复你生成的ppt部分内容，标题要用#号，副标题要用##号标识，每一页PPT列表页使用=====列表=====开头"
    )
    chatbot[-1] = (i_say, gpt_say)
    history.append(i_say);history.append(gpt_say)
    yield from update_ui(chatbot=chatbot, history=history)  # 刷新界面

    i_say = check_code_has_list(gpt_say=gpt_say)
    for i in range(3):
        if i_say == '':
            break
        elif i_say == 'ppt的内容要代码块输出':
            i_say = chatbot[-1][0]
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
                sys_prompt="你是一个ppt大纲设计师，一定要用代码块回复你生成的ppt部分内容，标题要用#号，副标题要用##号标识，每一页PPT列表页使用=====列表=====开头"
            )
            chatbot[-1] = (i_say, gpt_say)
            history.append(i_say)
            history.append(gpt_say)
            yield from update_ui(chatbot=chatbot, history=history)  # 刷新界面
            i_say = check_code_has_list(gpt_say=gpt_say)

    chatbot.append(('chatgpt+闪击ppt 1分钟制作ppt教程：', '''[local message]<br>
    1.打开闪闪击ppt在线版网址：[点我跳转地址🚀](https://ppt.sankki.com/editor?mode=demo)
    或复制链接打开：https://ppt.sankki.com/editor?mode=demo <br>
    2.将上面的代码块内容复制到左侧草稿区域<br>
    3.把复制的内容中演讲人：[我的名字]修改成您的实际名字，或者根据需要做其他内容上的修改<br>
    4.点击“文本转PPT”按钮<br>
    5.检查ppt生成是否正常，如果太短或者排版不对请检查生成内容是否符合闪击ppt的要求，作适当修改。如果需要帮助可以进群。
    其他更多精彩功能请自行探索'''))
    yield from update_ui(chatbot=chatbot, history=history)  # 刷新界面

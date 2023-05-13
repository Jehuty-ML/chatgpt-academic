from load_img import wechat_image_text, wepay_image_text, mywechat_image_text
from toolbox import CatchException, update_ui, report_execption


@CatchException
def 加群(txt, llm_kwargs, plugin_kwargs, chatbot, history, system_prompt, web_port):
    chatbot.append(('怎么加入微信讨论群', '[local message]'+wechat_image_text))
    yield from update_ui(chatbot=chatbot, history=[])  # 刷新界面


@CatchException
def 赞助(txt, llm_kwargs, plugin_kwargs, chatbot, history, system_prompt, web_port):
    chatbot.append(('怎么帮助网站开发者', '[local message]'+wepay_image_text))
    yield from update_ui(chatbot=chatbot, history=[])  # 刷新界面


@CatchException
def 开发程序(txt, llm_kwargs, plugin_kwargs, chatbot, history, system_prompt, web_port):
    chatbot.append(('需要定制私人人工智能方案或进行论文python数据分析', '[local message]'+mywechat_image_text))
    yield from update_ui(chatbot=chatbot, history=[])  # 刷新界面



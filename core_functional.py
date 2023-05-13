# 'primary' 颜色对应 theme.py 中的 primary_hue
# 'secondary' 颜色对应 theme.py 中的 neutral_hue
# 'stop' 颜色对应 theme.py 中的 color_er
# 默认按钮颜色是 secondary
from toolbox import clear_line_break


def get_core_functions():
    return {
        "英语学术润色": {
            # 前言
            "Prefix":   r"Below is a paragraph from an academic paper. Polish the writing to meet the academic style, " +
                        r"improve the spelling, grammar, clarity, concision and overall readability. When necessary, rewrite the whole sentence. " +
                        r"Furthermore, list all modification and explain the reasons to do so in markdown table." + "\n\n",
            # 后语
            "Suffix":   r"",
            "Color":    r"stop",    # 按钮颜色
        },
        "中文学术润色": {
            "Prefix":   r"作为一名中文学术论文写作改进助理，你的任务是改进所提供文本的拼写、语法、清晰、简洁和整体可读性，" +
                        r"同时分解长句，并提供改进建议。请只提供文本的更正版本，避免包括解释。请编辑以下文本" + "\n\n",
            "Suffix":   r"",
        },
        "查找英语语法错误": {
            "Prefix":   r"Can you help me ensure that the grammar and the spelling is correct? " +
                        r"Do not try to polish the text, if no mistake is found, tell me that this paragraph is good." +
                        r"If you find grammar or spelling mistakes, please list mistakes you find in a two-column markdown table, " +
                        r"put the original text the first column, " +
                        r"put the corrected text in the second column and highlight the key words you fixed.""\n"
                        r"Example:""\n"
                        r"Paragraph: How is you? Do you knows what is it?""\n"
                        r"| Original sentence | Corrected sentence |""\n"
                        r"| :--- | :--- |""\n"
                        r"| How **is** you? | How **are** you? |""\n"
                        r"| Do you **knows** what **is** **it**? | Do you **know** what **it** **is** ? |""\n"
                        r"Below is a paragraph from an academic paper. "
                        r"You need to report all grammar and spelling mistakes as the example before."
                        + "\n\n",
            "Suffix":   r"",
            "PreProcess": clear_line_break,    # 预处理：清除换行符
        },
        "中译英": {
            "Prefix":   r"Please translate following sentence to English:" + "\n\n",
            "Suffix":   r"",
        },
        "学术中英互译": {
            "Prefix":   r"I want you to act as a scientific English-Chinese translator, " +
                        r"I will provide you with some paragraphs in one language " +
                        r"and your task is to accurately and academically translate the paragraphs only into the other language. " +
                        r"Do not repeat the original provided paragraphs after translation. " +
                        r"You should use artificial intelligence tools, " +
                        r"such as natural language processing, and rhetorical knowledge " +
                        r"and experience about effective writing techniques to reply. " +
                        r"I'll give you my paragraphs as follows, tell me what language it is written in, and then translate:" + "\n\n",
            "Suffix": "",
            "Color": "secondary",
        },
        "英译中": {
            "Prefix":   r"翻译成地道的中文：" + "\n\n",
            "Suffix":   r"",
        },
        "中文降重+润色": {
            "Prefix": r"作为一名中文学术论文写作改进助手，您的任务是改进所提供的文本的拼写、语法、清晰度、简洁性和整体易读性，同时分解冗长的句子，"
                      r" 减少重复，并提供改进建议。请仅提供已更正的文本版本。请编辑以下文本：" + "\n\n",
            "Suffix": r"",
            "Color":    r"stop"
        },
        "英语降重+润色": {
            "Prefix": r"As a English academic paper writing improvement assistant, your task is toimprove thespelling, grammar, clarity,"
                      r" conciseness and overall readability ofthe text provided, whilebreaking down long sentences, reducing repetition,"
                      r"and providing improvementsuggestions. Please provide only the correctedversion of the text."
                      r" Please edit the followina text：" + "\n\n",
            "Suffix": r"",
            "Color":    r"stop"
        },
        "根据论文摘要写题目（中英双语）": {
            "Prefix": r"帮我根据论文摘要写题目，要求只要输出题目的中文和英文版本。以下是论文摘要内容：" + "\n\n",
            "Suffix": r"",
        },
    }

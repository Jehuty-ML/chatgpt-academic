from toolbox import HotReload  # HotReload 的意思是热更新，修改函数插件后，不需要重启程序，代码直接生效

# TODO 载入对话历史，联网问题chatgpt
def get_crazy_functions():
    ###################### 第一组插件 ###########################
    # [第一组插件]: 最早期编写的项目插件和一些demo
    from crazy_functions.读文章写摘要 import 读文章写摘要
    from crazy_functions.批量总结PDF文档 import 批量总结PDF文档
    from crazy_functions.批量总结PDF文档pdfminer import 批量总结PDF文档pdfminer
    from crazy_functions.总结word文档 import 总结word文档
    from crazy_functions.批量翻译PDF文档_多线程 import 批量翻译PDF文档
    from crazy_functions.谷歌检索小助手 import 谷歌检索小助手
    from crazy_functions.理解PDF文档内容 import 理解PDF文档内容标准文件输入
    from crazy_functions.对话历史存档 import 对话历史存档, 载入对话历史存档

    function_plugins = {
        "保存当前的对话并下载": {
            "Color": "primary",
            "AsButton": True,
            "Function": HotReload(对话历史存档)
        },
        "上传并载入历史对话存档": {
            "Color": "primary",
            "AsButton": True,
            "Function": HotReload(载入对话历史存档)
        },
        "批量总结论文（Tex格式）": {
            # "Color": "stop",    # 按钮颜色
            "Function": HotReload(读文章写摘要)
        },
        "批量翻译英语论文（PDF格式）": {
            # "Color": "stop",
            "AsButton": True,  # 加入下拉菜单中
            "Function": HotReload(批量翻译PDF文档)
        },
        "批量总结论文（PDF格式）[测试功能]": {
            "Color": "stop",
            "AsButton": True,  # 加入下拉菜单中
            # HotReload 的意思是热更新，修改函数插件代码后，不需要重启程序，代码直接生效
            "Function": HotReload(批量总结PDF文档)
        },
        "批量总结论文PDF格式带约简功能版（适合长论文）[测试功能]": {
            # "Color": "stop",
            "AsButton": True,  # 加入下拉菜单中
            "Function": HotReload(批量总结PDF文档pdfminer)
        },
        "批量总结论文（word格式）": {
            "Color": "stop",
            "Function": HotReload(总结word文档)
        },
        "理解PDF文档内容并通过对话交流(chatpdf)": {
            # HotReload 的意思是热更新，修改函数插件代码后，不需要重启程序，代码直接生效
            "Color": "stop",
            "AsButton": True,  # 加入下拉菜单中
            "Function": HotReload(理解PDF文档内容标准文件输入)
        },
        "谷歌学术检索助手（输入谷歌学术搜索页url）": {
            # "Color": "stop",
            "AsButton": True,  # 加入下拉菜单中
            "Function": HotReload(谷歌检索小助手)
        },
    }
    ###################### 第二组插件 ###########################
    # [第二组插件]: 经过充分测试，但功能上距离达到完美状态还差一点点
    from crazy_functions.Latex全文润色 import Latex中文润色
    from crazy_functions.Latex全文润色 import Latex英文润色
    from crazy_functions.Latex全文翻译 import Latex中译英
    from crazy_functions.Latex全文翻译 import Latex英译中
    from crazy_functions.批量Markdown翻译 import Markdown中译英
    from crazy_functions.批量Markdown翻译 import Markdown英译中


    function_plugins.update({
        "[测试功能] 英文Latex项目全文润色（输入路径或上传压缩包）": {
            # HotReload 的意思是热更新，修改函数插件代码后，不需要重启程序，代码直接生效
            # "Color": "stop",
            "AsButton": True,  # 加入下拉菜单中
            "Function": HotReload(Latex英文润色)
        },
        "[测试功能] 中文Latex项目全文润色（输入路径或上传压缩包）": {
            # HotReload 的意思是热更新，修改函数插件代码后，不需要重启程序，代码直接生效
            # "Color": "stop",
            "AsButton": False,  # 加入下拉菜单中
            "Function": HotReload(Latex中文润色)
        },
        "[测试功能] Latex项目全文中译英（输入路径或上传压缩包）": {
            # HotReload 的意思是热更新，修改函数插件代码后，不需要重启程序，代码直接生效
            # "Color": "stop",
            "AsButton": False,  # 加入下拉菜单中
            "Function": HotReload(Latex中译英)
        },
        "[测试功能] Latex项目全文英译中（输入路径或上传压缩包）": {
            # HotReload 的意思是热更新，修改函数插件代码后，不需要重启程序，代码直接生效
            # "Color": "stop",
            "AsButton": True,  # 加入下拉菜单中
            "Function": HotReload(Latex英译中)
        },
        "[测试功能] 批量Markdown中译英（输入路径或上传压缩包）": {
            # HotReload 的意思是热更新，修改函数插件代码后，不需要重启程序，代码直接生效
            # "Color": "stop",
            "AsButton": False,  # 加入下拉菜单中
            "Function": HotReload(Markdown中译英)
        },
        "[测试功能] 批量Markdown英译中（输入路径或上传压缩包）": {
            # HotReload 的意思是热更新，修改函数插件代码后，不需要重启程序，代码直接生效
            # "Color": "stop",
            "AsButton": True,  # 加入下拉菜单中
            "Function": HotReload(Markdown英译中)
        },
        
    })

    ###################### 第三组插件 ###########################
    # [第三组插件]: 尚未充分测试的函数插件，放在这里
    try:
        from crazy_functions.下载arxiv论文翻译摘要 import 下载arxiv论文并翻译摘要
        function_plugins.update({
            "一键下载arxiv论文并翻译摘要（先在input输入编号，如1812.10695）": {
                # "Color": "stop",
                "AsButton": False,  # 加入下拉菜单中
                "Function": HotReload(下载arxiv论文并翻译摘要)
            }
        })

    except Exception as err:
        print(f'[下载arxiv论文并翻译摘要] 插件导入失败 {str(err)}')

    try:
        from crazy_functions.一键生成PPT_mindshow import 一键生成PPT_mindshow
        function_plugins.update({
            "一键生成PPT(结合mindshow)": {
                "Color": "primary",
                "AsButton": True,  # 加入下拉菜单中
                "Function": HotReload(一键生成PPT_mindshow)
            }
        })
    except Exception as err:
        print(f'[一键生成PPT_mindshow] 插件导入失败 {str(err)}')

    try:
        from crazy_functions.加群 import 加群, 赞助, 开发程序
        function_plugins.update({
            "需要使用帮助/讨论使用技巧": {
                "Color": "primary",
                "AsButton": True,  # 加入下拉菜单中
                "Function": HotReload(加群)
            },
            "赞助": {
                "Color": "primary",
                "AsButton": True,  # 加入下拉菜单中
                "Function": HotReload(赞助)
            },
            "定制私人人工智能方案/论文数据python程序分析": {
                "Color": "primary",
                "AsButton": True,  # 加入下拉菜单中
                "Function": HotReload(开发程序)
            },
        })
    except Exception as err:
        print(f'[加群赞助开发程序] 插件导入失败 {str(err)}')

    ###################### 第n组插件 ###########################
    return function_plugins

# 放在yaml文件根目录
# 封装setting
# python中的settings使用绝对路径
# setting使用了的 Python 内部变量 file ，该变量被自动设置为代码所在的 Python 模块文件名。
# os.path.dirname(file) 将会获取自身所在的文件，即settings.py 所在的目录，然后由os.path.join 这个方法将这目录与 templates 进行连接。
# 原文链接：https://blog.csdn.net/weixin_42684559/article/details/118693045
# -*- coding: utf-8 -*-
import os
import yaml

DIR_NAME = os.path.dirname(os.path.abspath(__file__))
print("当前路径是：", DIR_NAME)    # 获取到yamlfiles文件夹所在的路径


# 读取测试用例yaml文件
def readYamlCase(yamlFileName):
    # DIR_NAME是识别yamlfiles文件夹下面的路径
    # yamlFileName是yaml文件名字
    # 解决支持win和linux调试问题
    with open(DIR_NAME+"/"+yamlFileName,mode="r",encoding='utf-8') as f:
    # with open(yamlFileName, mode="r", encoding='utf-8') as f: 也可直接传yaml文件的路径，调用时地址为“../testcases/yamlfiles.test01.yaml”
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        print(value, type(value))  # 打印value是什么类型格式
        return value
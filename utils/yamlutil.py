import os
import yaml
import re
from utils.logutils import log

# 读取数据
def read_yaml(key):
        with open(os.getcwd()+'/Global.yaml',mode='r',encoding='utf-8') as f:
            value = yaml.load(stream=f,Loader=yaml.FullLoader)
            #log.info("读取Global全局变量数据完毕")
            return value[key]


# 写入数据
def write_yaml(data):
    with open(os.getcwd()+'/Global.yaml',mode='a',encoding='utf-8') as f:
        yaml.dump(data,stream=f,allow_unicode=True)
        #log.info("写入Global全局变量数据完毕")

# 清空数据
def clear_yaml():
    with open(os.getcwd()+'/Global.yaml',mode='w',encoding='utf-8') as f:
        f.truncate()
    #log.info("清空Global文件数据完毕")


# 先读取文件再删除
# 删除yaml文件匹配字符串的行；有包含字符串+多行一样的串的都会删除
# 调用方法：strName为自定义变量
def del_yamlKey(strName):
    list = []
    matchPattern = re.compile(strName)
    file= open(os.getcwd() + '/Global.yaml','r')
    while 1:
        line = file.readline()
        if not line:
            logger.info("Read file End or Error")
            break
        elif matchPattern.search(line):
            pass
        else:
            list.append(line)
    file.close()
    file = open(os.getcwd() + '/Global.yaml','w')
    for i in list:
        file.write(i)
    file.close()


#!/usr/bin/env python -u
# 我在python脚本的顶部设置了此选项，然后输出开始显示在Jenkins控制台上.
from utils.yamlutil import *
import pytest, allure
# 导入RequestSend类
from utils.requestutils import *
from Config.host import HOST
from utils.logutils import log

#############################################################
# 公共调用 yaml方法，在test_xx.py执行test_casesXX中调用
# 实例如下：
# @pytest.mark.parametrize('caseInfo',readYamlCase("demo1.yaml"))
# def test_demo1(caseInfo):
#     run_yaml(caseInfo)
#############################################################
# 调用，请遵循yaml文件取值和名字，写法规则
# read yaml files
def run_yaml(caseInfo):
    allure.dynamic.story(caseInfo["case_story"])  # 动态取模块名字to allure
    allure.dynamic.title(caseInfo["case_title"])  # 动态标题to allure
    case_title = caseInfo["case_title"]  # 用例标题

    url = f'{HOST}'+caseInfo["url"]  # 接口地址
    method = caseInfo["method"]      # 请求方法
    # 读取全局变量accessToken
    # headers = {'Content-Type': 'application/x-www-form-urlencoded', 'clientType': 'IOS',"Authorization": "Bearer "+read_yaml("accessToken")}
    headers = caseInfo["headers"]
    data = caseInfo["data"]   # 请求参数传值
    res_data = None

    # 异常处理
    try:
        # 打印日志
        log.info("正在执行用例:"+case_title)
        # 执行测试用例，发送http请求
        res_data = request_send(url, method, data, headers)
        # 打印日志
        log.info("用例执行成功，请求的结果为{}".format(res_data))
    # 异常捕获
    except:
        # 打印日志
        log.info("用例执行失败，请查看日志找原因。")
        # 断言结果为失败
        assert False
    # 结果进行验证
    assert_respoes(caseInfo, res_data)
    # 返回res_data信息
    return res_data

#################
    # 结果验证方法
def assert_respoes(caseInfo, res_data):
    # 变量初始化为False
    is_pass = False
    # 异常处理，捕获assert抛出的异常，不直接抛出
    # 根据项目情况定制断言规则，有返回断言errorCode和无返回断言状态码code
    try:
        # 有返回，断言返回里面的errorCode
        if "errorCode" in str(res_data['body']):
            assert str(res_data['body']['errorCode']) == str(caseInfo["api_validate"]["errorCode"])
            print("返回的code和errorCode是:", res_data['code'], res_data['body']['errorCode'])
            print("预期errorCode是:", caseInfo["api_validate"]["errorCode"])
            # 打印信息
            log.info("有返回，用例断言成功")
            # 设置变量为True
            is_pass = True

        # 无返回，断言状态码code
        else:
            assert str(res_data['code']) == str(caseInfo["api_validate"]["code"])  # 请求成功200，判断预期为200
            print("实际状态码是:", res_data['code'])
            print("预期状态码是:", caseInfo["api_validate"]["code"])
            # 打印信息
            log.info("无返回，用例断言成功")
            # 设置变量为True
            is_pass = True

    # 捕获异常
    except:
    # 设置变量为False
        is_pass = False
    # 打印日志
        log.info("用例断言失败,请确认是否为bug",is_pass)
    # 无论是否出现异常，都执行下面内容代码
    finally:
        # 根据变量结果是True/False，进行断言验证，成功则通过，失败则未通过
        assert is_pass
    # 返回该变量结果
    return is_pass


if __name__ == '__main__':
    pytest.main()


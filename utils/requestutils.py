import requests
from utils.logutils import log


# 封装requests请求函数
def request_send(url, method, data, headers):
    # 打印日志
    log.info("请求的url为{}".format(url))
    # 打印日志
    log.info("请求的method为{}".format(method))
    # 打印日志
    log.info("请求的data为{}".format(data))
    # 打印日志
    log.info("请求的headers为{}".format(headers))
    if method == "get":
        res = requests.get(url, params=data, headers=headers)
    elif method == "post":
        if headers["Content-Type"] == "application/json":
            res = requests.post(url, json=data, headers=headers)
        else:
            res = requests.post(url, data=data, headers=headers)
    code = res.status_code
    log.info("返回的status_code为{}".format(code))
    log.info("返回的response为{}".format(res.text))
    dict1 = dict()
    try:
        body = res.json()
    except:
        body = res.text
    dict1["code"] = code
    dict1["body"] = body
    return dict1




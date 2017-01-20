
cases = [
    {
        "jsonContent": {
            "agentName": "北京"
        },
        "httpStatus": 200,
        "path": "result",
        "method": "POST",
        "jsonStatus": 200,
        "desc": "登录成功"
    },
    {
        "jsonContent": {
            "result": null
        },
        "httpStatus": 200,
        "path": "result",
        "method": "POST",
        "jsonStatus": 4511,
        "desc": "登录密码错误"
    },
    {
        "jsonContent": {
            "result": null
        },
        "httpStatus": 200,
        "path": "result",
        "method": "POST",
        "jsonStatus": 4514,
        "desc": "登录-参数校验失败"
    }
];

module.exports = cases;

cases = [
    {
        "desc": "登录成功",
        "httpStatus": 200,
        "jsonContent": {
            "agentName": "北京"
        },
        "jsonStatus": 200,
        "method": "POST",
        "path": "result"
    },
    {
        "desc": "登录密码错误",
        "httpStatus": 200,
        "jsonContent": {
            "result": null
        },
        "jsonStatus": 4511,
        "method": "POST",
        "path": "result"
    },
    {
        "desc": "登录-参数校验失败",
        "httpStatus": 200,
        "jsonContent": {
            "result": null
        },
        "jsonStatus": 4514,
        "method": "POST",
        "path": "result"
    }
];

module.exports = cases;
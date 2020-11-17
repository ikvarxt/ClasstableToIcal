# ClasstableToIcal
项目基于 [SunsetYe66/ClasstableToIcal](https://github.com/SunsetYe66/ClasstableToIcal) ，增加从 [LNTU-API](https://github.com/LiaoGuoYin/LNTU-API) 获取到辽宁工程技术大学课程表数据。

## Usage

教程请访问 

> 原项目详细教程请参看[少数派](https://sspai.com/post/59694)。

先安装依赖：

```shell
pip3 install uuid xlrd requests
```

然后执行 `getClassData.py` ：
```shell
python3 getClassDate.py
```

根据提示输入教务在线账号、密码。如果出现报错，可试着**再运行一次**，可能就会好。建议**晚上 11 点前运行**脚本，大佬的 API 服务器晚上好像会关机。

然后执行 `ical_generator.py` :
```shell
python3 ical_generator.py
```
生成 ics 文件即为日程时间安排文件。

测试环境：Python 3.8.5，macOS 10.15.7。

## 一些设置

### 课程开始结束时间

在 conf_ClassTime.json 中，修改 `startTime`、`endTime` 字段即可。

```json
"1": {
    "name": "第一大节", 
    "startTime": "080000",
    "endTime": "093500"
}
```

`startTime` 与 `endTime` 采用 `%H%M%S` 格式。

## Credits

[SunsetYe66/ClasstableToIcal](https://github.com/SunsetYe66/ClasstableToIcal) 

## License
 
LGPLv3

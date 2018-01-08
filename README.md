## 自动登录京东，打卡领钢镚，签到领京豆

[![Python](https://img.shields.io/badge/Python-3.5%2B-blue.svg)](https://www.python.org)


### 使用方法：

1. 安装`Python` (3.5 或更高版本）

2. 建立虚拟运行环境（可选）

3. 下载代码

4. 安装依赖：`pip install -r requirements.txt`

5. 创建配置文件（可选）

6. 运行：`python app/main.py`（默认使用`conf/config.ini`登陆）

<br>


## 说明

直接登录京东较复杂，不易实现，因此采用了[三种方式(参见Wiki)](https://github.com/vc5/JD-Coin/wiki/%E7%99%BB%E5%BD%95%E6%96%B9%E5%BC%8F))进行登录：

#### 默认登录方式：使用selenium调用chrome进行登陆,请确认您已经安装了Chrome

##### 需要手动安装的依赖
1. Chrome
2. ChromeDriver(目前已经实现无需用户安装，默认支持Win、Linux-X64、Mac，请自行测试)
请下载[ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)后，确保该可执行文件可以在`PATH`中被找到




## 最近一次更新说明
1.支持了京东店铺签到，取消了京东股票翻牌（尚未解决自动签到）
2.采用`requestium` (requests+selenium)重写了Job基类
3.现在您只需要了解requests，就可以轻松的编写新的签到任务了,参见[Wiki/如何编写新的签到任务](https://github.com/vc5/JD-Coin/wiki/%E5%A6%82%E4%BD%95%E7%BC%96%E5%86%99%E6%96%B0%E7%9A%84%E7%AD%BE%E5%88%B0%E4%BB%BB%E5%8A%A1)
4.内置了chromedriver，目前支持Win、Linux64、Mac，用户只需要安装Chrome就可以了

## 其他

### 配置文件说明(大小写敏感)
`DEFAULT`下的配置会作为默认值，用户自定义的值会覆盖DEFAULT所指定的值，添加多用户，只需要按照格式添加新的Section就好了


`config.ini`
```ini
[DEFAULT]
Debug = yes
Headless = no
;跳过任务的格式“Bean|SignJR”
Jobs_skip  = no
Enable = yes

按以下格式填写用户名和密码
[vincent]
Username = adqwes123as
Password = asd123zcasd
```

#### 帐号/密码：

可以将帐号/密码保存到配置文件中（若使用浏览器方式，可以只保存帐号），这样就不用在每次登录时手动输入了（虽然使用了 cookie 保存登录状态，但京东还是会每隔几天就让你重新登录的...）。

将默认配置文件复制为`config.ini`，然后使用 [Base85](https://en.wikipedia.org/wiki/Ascii85) 方式将对应的帐号、密码编码后填入配置文件中即可，完成后是这样子的：


编码示例（Python）：

```python
>>> import base64
>>> base64.b85encode(b'username').decode()
'b#rBMZeeX@'
```

#### 我没有小白卡/我想跳过某些任务：

将想要跳过的任务填写到配置文件中的 `jobs_skip` 中即可。比如想跳过「小白卡钢镚打卡」任务，填写 `Daka` 即可：

```ini
Jobs_skip = Daka
```

跳过多个任务:

```ini
Jobs_skip=DataStation|Daka
```

任务列表:

| 任务 | 描述 |
| --- | --- |
| DaKa | 小白卡钢镚打卡（已下线） |
| DakaApp | 京东客户端钢镚打卡 |
| BeanApp | 京东客户端签到领京豆 |
| Bean | 京东会员页签到领京豆 |
| SignJR | 京东金融签到领奖励 |
| DataStation | 流量加油站签到领流量 |
| RedPacket | 京东小金库现金红包（已下线） |
|DoubleSign_JR|京东金融双签（已下线）|
|ShopSign|京东店铺签到|

### 设置网络代理

设置环境变量 `HTTP_PROXY` / `HTTPS_PROXY` 即可。



2. 运行:
```
python app/main.py -c config.ini

```

## Example

```log
2017-03-15 10:38:48,711 root[config] INFO: 使用配置文件 "config.ini".
2017-03-15 10:38:48,745 root[main] INFO: # 从文件加载 cookies 成功.
2017-03-15 10:38:48,745 jobs[daka] INFO: Job Start: 小白卡钢镚打卡
2017-03-15 10:38:49,734 jobs[daka] INFO: 登录状态: True
2017-03-15 10:38:50,642 jobs[daka] INFO: 今日已打卡: False; 打卡天数: 2
2017-03-15 10:38:50,742 jobs[daka] INFO: 打卡成功: True; Message: 打卡成功
2017-03-15 10:38:50,743 jobs[daka] INFO: Job End.
2017-03-15 10:38:50,743 jobs[daka] INFO: Job Start: 京东客户端钢镚打卡
2017-03-15 10:38:50,843 jobs[daka] INFO: 登录状态: True
2017-03-15 10:38:50,923 jobs[daka_app] INFO: 今日已打卡: False; 打卡天数: 2
2017-03-15 10:38:51,105 jobs[daka_app] INFO: 打卡成功: True; Message: 打卡成功,成功领取了0.1个钢镚！
2017-03-15 10:38:51,105 jobs[daka] INFO: Job End.
2017-03-15 10:38:51,105 jobs[daka] INFO: Job Start: 京东客户端签到领京豆
2017-03-15 10:38:51,249 jobs[daka] INFO: 登录状态: True
2017-03-15 10:38:51,344 jobs[bean_app] INFO: 今日已签到: False; 签到天数: 2
2017-03-15 10:38:51,452 jobs[bean_app] INFO: 签到成功; 获得 2 个京豆.
2017-03-15 10:38:51,452 jobs[daka] INFO: Job End.
2017-03-15 10:38:51,452 jobs[daka] INFO: Job Start: 京东会员页签到领京豆
2017-03-15 10:38:51,967 jobs[daka] INFO: 登录状态: True
2017-03-15 10:38:52,472 jobs[bean] INFO: 今日已签到: False; 现在有 1087 个京豆.
2017-03-15 10:38:52,922 jobs[bean] INFO: 签到成功，获得 20 个京豆.
2017-03-15 10:38:52,923 jobs[daka] INFO: Job End.
2017-03-15 10:38:52,923 jobs[daka] INFO: Job Start: 京东金融签到领京豆
2017-03-15 10:38:53,514 jobs[daka] INFO: 登录状态: True
2017-03-15 10:38:53,582 jobs[bean_jr] INFO: 今天已签到: False; 签到天数: 2
2017-03-15 10:38:53,681 jobs[bean_jr] INFO: 签到成功，获得 5 个京豆.
2017-03-15 10:38:53,681 jobs[daka] INFO: Job End.
=================================
= 任务数: 5; 失败数: 0
= 全部成功 ~
=================================
```

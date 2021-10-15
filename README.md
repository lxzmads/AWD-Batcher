# AWD-Batcher

Attack With Defense比赛中的exploit快速集成小脚本。

## 依赖

- python 3.7.1
- see in requirements.txt

## 目标

- exp解耦，即exp可以单独使用，也可以配合此脚本使用，这样可以更快的将现有exp集成进来。
- exp快速生成（待开发），目前可以配合burp的`Copy AS Python-Requests`扩展或者Postman的代码生成功能食用
- 攻击流量快速exp化（待开发），AWD每一轮时间都很宝贵，希望可以更快的将别人攻击我们的流量快速复现成exp
- 总之就是要快（不是

## 功能

- [x] 根据IP段生成队伍IP与每个队伍的随机密码
- [x] 批量化exp利用核心功能,实现的方式是动态加载所有可用exp，逐个尝试直到成功获取flag
- [x] flag定时提交
- [ ] 根据pcap流量生成exp
- [ ] 根据监测到的HTTP Request生成exp

## Usage

1. 创建teams.conf，存放每个队伍这个题目对应的IP地址和随机密码，可以借助teams.py生成，注意剔除自己队伍的IP
2. 在exps目录放入写好的exp，exp的例子可以在`exp-examples`目录找到。注意exp文件内的实际利用函数名要和exp文件名相同
3. 运行batcher.py即可批量获取flag

## Contact

lxzmads#gmail.com

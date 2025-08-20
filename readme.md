# 方舟字节码变异Fuzz
运行环境：wsl2 + Ubuntu(24.04)

## QuickStart
1. 参考[下载和变异运行ArkTS演进版代码](https://wiki.huawei.com/domains/1048/wiki/8/WIKI202307131553293)官方文档，在本项目根目录下创建arkcompiler文件夹，并下载完整的ArkTS运行平台（该文档需要申请权限，并在华为内网访问）
2. 在``arkcompiler/runtime_core/static_core/``路径下创建``test.ets``，作为源代码文件
3. 运行``bash compile_run.sh``来编译并运行test.ets，验证环境配置的正确性
4. 运行``python fuzz.py``进行变异fuzz实验，结果将以jsonl格式保存在项目根目录


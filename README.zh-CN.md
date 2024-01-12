# GithubDNSUpdate
一个可以将Github DNS获取到系统hosts文件的程序。

## 背景
当我想在Github上更改用户头像时，我的Github打不开，所以在网上寻找教程。我找到了[host.txt](https://hosts.gitcdn.top/hosts.txt)，可每次需要自己更改，于是我便萌生了写一个自动将文件添加到系统hosts文件的程序。

## 安装
这个项目使用了[python3](https://python.org)和[wget](https://www.gnu.org/software/wget/)。请确保你本地安装了它们。
 
```sh
$ git clone https://github.com/ZhangDongzai/GithubDNSUpdate.git
```

## 使用说明
这是一个python3文件，你应该使用python3去运行它。

```sh
$ python3 ./main.py
```

## 维护者
@ZhangDongzai

## 开源许可
[MIT](LICENSE) © Richard Littauer
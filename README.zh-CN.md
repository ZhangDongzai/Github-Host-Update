# GithubHostUpdate

[English](README.md)  
一个可以将Github host获取到系统hosts文件的程序。

## 背景

当我想在Github上更改用户头像时，我的Github打不开，所以在网上寻找教程。我找到了更新Github host的网站，可每次需要自己更改，于是我便萌生了写一个自动将文件添加到系统hosts文件的程序。

## 安装

这个项目使用了[python3](https://python.org), [python3](https://python.org)使用的模块有[os](https://docs.python.org/3/library/os.html)和[requests](https://requests.readthedocs.io/)。请确保你本地安装了它们。
 
```sh
git clone https://github.com/ZhangDongzai/GithubHostUpdate.git
```

## 使用说明

### 命令行版本

这是一个[python3](https://python.org)文件，你应该使用[python3](https://python.org)去运行它。

```sh
python3 main.py
```

或者你可以使用[pyinstaller](http://www.pyinstaller.org/)来创建二进制文件。

```sh
pyinstaller -F -c -i GithubHostUpdate.ico -n GithubHostUpdate_command main.py
```

然后在./dist下找到二进制可执行文件并执行。

### 图形界面版本

这是一个[python3](https://python.org)文件，你应该使用[python3](https://python.org)去运行它。

```sh
python3 gui.py
```

或者你可以使用[pyinstaller](http://www.pyinstaller.org/)来创建二进制文件。

```sh
pyinstaller -F -i GithubHostUpdate.ico -n GithubHostUpdate_GUI gui.py
```

然后在./dist下找到二进制可执行文件并执行。

## 维护者

@[ZhangDongzai](https://github.com/ZhangDongzai)

## 开源许可

[MIT](LICENSE) © Richard Littauer
# GithubHostUpdate

[Chinese](README.zh-CN.md)  
A program that fetches Github host to the system hosts file

## Background

When I want to change my Hostuser avatar on Github, my Github won't open, so look for tutorials online. I found the site to update the Github host, but every time I needed to change it myself, I came up with the idea of writing a program that automatically added files to the system hosts file.

## Install

This project uses [python3](https://python.org), [python3](https://python.org) using modules are [os](https://docs.python.org/3/library/os.html) and [requests](https://requests.readthedocs.io/). Make sure you have them installed locally.
 
```sh
git clone https://github.com/ZhangDongzai/GithubHostUpdate.git
```

## Usage

### Command Version

This is a [python3](https://python.org) file, and you should use [python3](https://python.org) to run it.

```sh
python3 main.py
```

Or you can use [pyinstaller](http://www.pyinstaller.org/) to create a binary executable.

```sh
pyinstaller -F -c -i GithubHostUpdate.ico -n GithubHostUpdate_command main.py
```

Then find the binary executable under ./dist and execute it.

### GUI Version

This is a [python3](https://python.org) file, and you should use [python3](https://python.org) to run it.

```sh
python3 gui.py
```

Or you can use [pyinstaller](http://www.pyinstaller.org/) to create a binary executable.

```sh
pyinstaller -F -w -i GithubHostUpdate.ico -n GithubHostUpdate_GUI gui.py
```

Then find the binary executable under ./dist and execute it.

## Maintainers

@[ZhangDongzai](https://github.com/ZhangDongzai)

## License

[MIT](LICENSE) © Richard Littauer

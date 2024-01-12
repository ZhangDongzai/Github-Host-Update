# GithubDNSUpdate
A program that fetches Github DNS to the system hosts file

## Background
When I want to change my user avatar on Github, my Github won't open, so look for tutorials online. I found [host.txt](https://hosts.gitcdn.top/hosts.txt), but every time I needed to change it myself, I came up with the idea of writing a program that automatically added files to the system hosts file.

## Install
This project uses [python3](https://python.org) and [wget](https://www.gnu.org/software/wget/). Make sure you have them installed locally.
 
```sh
git clone https://github.com/ZhangDongzai/GithubDNSUpdate.git
```

## Usage
This is a python3 file, and you should use [python3](https://python.org) to run it.

```sh
python3 main.py
```

Or you can use [pyinstaller](http://www.pyinstaller.org/) to create a binary executable.

```sh
pyinstaller -F -c -i ./GithubDNSUpdate.ico -n GithubDNSUpdate main.py
```

Then find the binary executable under ./dist and execute it.

```sh
cd dist
GithubDNSUpdate
```

## Maintainers
@[ZhangDongzai](https://github.com/ZhangDongzai)

## License
[MIT](LICENSE) © Richard Littauer

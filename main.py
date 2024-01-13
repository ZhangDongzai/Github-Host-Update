# GithubHostsUpdate

from os import name, system


file_number = 2

file = {1: ["https://hosts.gitcdn.top/hosts.txt",
            "# fetch-github-hosts begin\n",
            "# fetch-github-hosts end\n",
            "hosts.txt"],
        2: ["https://gitlab.com/ineo6/hosts/-/raw/master/next-hosts",
            "# 地址可能会变动，请务必关注GitHub、Gitlab获取最新消息",
            "# GitHub Host End",
            "next-hosts"]}

file_url = file[file_number][0]
file_begin = file[file_number][1]
file_end = file[file_number][2]
file_name = file[file_number][3]


def download() -> None:
    """download the file"""  
    system("wget "+file_url)

def writeToHostsFile() -> None:
    # read the file and copy its content
    with open(file=file_name, mode="r", encoding="utf-8") as file:
        download_file_content = file.readlines()

    # read hosts file
    if name == "nt":
        # Windows
        file_location = "C:\\Windows\\System32\\drivers\\etc\\hosts"
    elif name == "posix":
        # Linux or MacOS
        file_location = "/etc/hosts"

    with open(file=file_location, mode="r", encoding="utf-8") as file:
        hosts_file_content = file.readlines()

    # find hosts begin and end
    begin, end = None, None

    for i in range(len(hosts_file_content)):
        if hosts_file_content[i] == file_begin:
            begin = i
        elif hosts_file_content[i] == file_end:
            end = i

    with open(file=file_location, mode="w", encoding="utf-8") as file:
        if (begin == None) and (end == None):
            # the file didn't write hosts before
            file.writelines(hosts_file_content + download_file_content)
        elif (type(begin) == int) and (type(end) == int):
            # the file wrote hosts before
            file.writelines(hosts_file_content[0: begin-1] + download_file_content + hosts_file_content[end+1: -1])

def deleteFile() -> None:
    """delete the download file"""
    if name == "nt":
        # Windows
        system("del "+file_name)
    elif name == "posix":
        # Linux or MacOS
        system("rm "+file_name)


if __name__ == "__main__":
    download()
    writeToHostsFile()
    deleteFile()
    
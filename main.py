# GithubHostsUpdate

import wget
import os


def download() -> str:
    """download the file and return the name of the file"""
    
    # set the url of the hosts file
    file_url = "https://hosts.gitcdn.top/hosts.txt"

    # download file
    os.system("wget "+file_url)


def writeToHostsFile() -> None:
    # read the file and copy its content
    with open(file="hosts.txt", mode="r", encoding="utf-8") as file:
        download_file_content = file.readlines()

    # read hosts file
    if os.name == "nt":
        # Windows
        file_location = "C:\\Windows\\System32\\drivers\\etc\\hosts"
    elif os.name == "posix":
        # Linux or MacOS
        file_location = "/etc/hosts"

    with open(file=file_location, mode="r", encoding="utf-8") as file:
        hosts_file_content = file.readlines()

    # find hosts begin and end
    begin, end = None, None

    for i in range(len(hosts_file_content)):
        if hosts_file_content[i] == "# fetch-github-hosts begin\n":
            begin = i
        elif hosts_file_content[i] == "# fetch-github-hosts end\n":
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
    if os.name == "nt":
        # Windows
        os.system("del hosts.txt")
    elif os.name == "posix":
        # Linux or MacOS
        os.system("rm hosts.txt")


if __name__ == "__main__":
    download()
    writeToHostsFile()
    deleteFile()
    
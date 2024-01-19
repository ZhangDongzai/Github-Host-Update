# GithubHostsUpdate

from os import name
from sys import argv
from requests import get, Response


file = {1: "https://hosts.gitcdn.top/hosts.txt",
        2: "https://gitlab.com/ineo6/hosts/-/raw/master/next-hosts"}

file_number = 2
file_encoding = "utf-8"

if name == "nt":
    # Windows
    file_location = "C:\\Windows\\System32\\drivers\\etc\\hosts"
elif name == "posix":
    # Linux or MacOS
    file_location = "/etc/hosts"

def UpdateFile(file_number: int=file_number):
    global file_url, file_location

    if len(argv) == 0:
        # No entrys
        file_url = file[file_number][0]
    elif len(argv) == 1:
        # 1 entry
        try:
            # Is file_number
            file_url = file[int(argv[0])][0]
        except ValueError:
            # Is url
            file_url = argv[0]
    else:
        # More then 1 entry
        raise ValueError("Too much entrys")

def download(file_url: str) -> Response:
    """Download the file"""
    global download_content, download_begin, download_end

    # Download file
    
    # requests.get(file_url) -> requests.Response
    # requests.Response.content -> bytes
    # str(bytes, encoding="utf-8") -> str
    # str.split('\n') -> list
    download_content = str(get(file_url).content, encoding="utf-8").split('\n')

    download_begin = download_content[0]
    download_end = download_content[-1]

def writeToHostsFile() -> None:
    # Read hosts file
    with open(file=file_location, mode="r", encoding=file_encoding) as file:
        hosts_content = file.readlines()

    # Find hosts begin and end
    begin, end = None, None

    for i in range(len(hosts_content)):
        if hosts_content[i] == download_begin:
            begin = i
        elif hosts_content[i] == download_end:
            end = i

    with open(file=file_location, mode="w", encoding=file_encoding) as file:
        if (begin == None) and (end == None):
            # The file didn't write hosts before
            file.writelines(hosts_content + download_content)
        elif (type(begin) == int) and (type(end) == int):
            # The file wrote hosts before
            file.writelines(hosts_content[0: begin-1] + download_content + hosts_content[end+1: -1])


if __name__ == "__main__":
    UpdateFile(file_number)
    download(file_url)
    writeToHostsFile()
    
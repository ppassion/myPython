import os


def getFolderSize(path):
    totalSize = 0

    if not os.path.exists(path):
        print("===PATH " + path.name + " does not exist===")
        return totalSize

    if os.path.isfile(path):
        totalSize = os.path.getsize(path)
        return totalSize

    if os.path.isdir(path):
        with os.scandir(path) as nextDir:
            for subDir in nextDir:
                subDirFullPath = os.path.join(path, subDir.name)
                if subDir.is_dir():
                    try:
                        subDirSize = getFolderSize(subDir)
                        totalSize += subDirSize
                    except WindowsError:
                        print
                        "Error: 没有找到文件或读取文件失败"
                    else:
                        print
                        "内容写入文件成功"
                elif subDir.is_file():
                    subDirSize = os.path.getsize(subDir)
                    totalSize += subDirSize

            return totalSize


def calBytes(todoBytes):
    if todoBytes < 1024:  # 比特
        todoBytes = str(round(todoBytes, 2)) + ' B'  # 字节
    elif 1024 <= todoBytes < 1024 * 1024:
        todoBytes = str(round(todoBytes / 1024, 2)) + ' KB'  # 千字节
    elif 1024 * 1024 <= todoBytes < 1024 * 1024 * 1024:
        todoBytes = str(round(todoBytes / 1024 / 1024, 2)) + ' MB'  # 兆字节
    elif 1024 * 1024 * 1024 <= todoBytes < 1024 * 1024 * 1024 * 1024:
        todoBytes = str(round(todoBytes / 1024 / 1024 / 1024, 2)) + ' GB'  # 千兆字节
    elif 1024 * 1024 * 1024 * 1024 <= todoBytes < 1024 * 1024 * 1024 * 1024 * 1024:
        todoBytes = str(round(todoBytes / 1024 / 1024 / 1024 / 1024, 2)) + ' TB'  # 太字节
    elif 1024 * 1024 * 1024 * 1024 * 1024 <= todoBytes < 1024 * 1024 * 1024 * 1024 * 1024 * 1024:
        todoBytes = str(round(todoBytes / 1024 / 1024 / 1024 / 1024 / 1024, 2)) + ' PB'  # 拍字节
    elif 1024 * 1024 * 1024 * 1024 * 1024 * 1024 <= todoBytes < 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024:
        todoBytes = str(round(todoBytes / 1024 / 1024 / 1024 / 1024 / 1024 / 1024, 2)) + ' EB'  # 艾字节
    return todoBytes


# 获取path下直属目录和文件的大小，类似Linux中 du -sh *
def getDirectSubSize(path):
    print('total size is ' + calBytes(getFolderSize(path)))
    with os.scandir(path) as nextDir:
        for subDir in nextDir:
            size = getFolderSize(subDir)
            print('%-30s%-20s' % (calBytes(size),subDir.name))


userFolder = "D:\\software\\VMware\\Virtual Machines\\hadoop1"
getDirectSubSize(userFolder)

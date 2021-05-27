# Coding : utf-8
# Author : chyh
# Date   : 2021/5/1 16:10

import subprocess
import threading
import sys


# 每一个线程只能完成对于一台机器的一个操作
class operateVMThread(threading.Thread):
    # WM WARE提供的命令行工具
    vmrun = r'D:\\software\\VMware\\VMware Workstation\\vmrun.exe'

    # 命令行工具是对虚拟机的vmx文件进行操作，所以需要维护一套主机名与vmx文件路径的映射关系
    vmx_map = {'hadoop1': r'"D:\\software\\VMware\\Virtual Machines\\hadoop1\\hadoop1.vmx"',
               'hadoop2': r'"D:\\software\\VMware\\Virtual Machines\\hadoop2\\hadoop1.vmx"',
               'hadoop3': r'"D:\\software\\VMware\\Virtual Machines\\hadoop3\\hadoop1.vmx"',
               'm01': r'F:\\VM\\m01\\m01.vmx',
               'm02': r'F:\\VM\\m02\\m02.vmx',
               'm03': r'F:\\VM\\m03\\m03.vmx'}

    # 4种操作，启、停、重启、挂起，注意每个value的前后都有空格，命令中需要的空格写在这里了
    operation_map = {'start': r' -T ws start ',
                     'stop': r' -T ws stop ',
                     'suspend': r' -T ws suspend ',
                     'rest': r' -T ws rest '}

    def __init__(self, hostname, operation):
        if not self.vmx_map.__contains__(hostname):
            print(hostname + "主机不存在")
            sys.exit()
        if not self.operation_map.__contains__(operation):
            print(operation + "操作不合法")
            sys.exit()
        threading.Thread.__init__(self)
        self.threadName = "Thread  ==  " + operation + ' ' + hostname
        self.hostname = hostname
        self.operation = operation

    def run(self) -> None:
        cmd = self.vmrun + self.operation_map[self.operation] + self.vmx_map[self.hostname]
        subprocess.Popen(cmd)


'''
host_list:需要操作的主机名list
operation:需要执行的操作
'''


def operate(host_list: list, operation: str):
    threads = []
    for host in host_list:
        thread = operateVMThread(host, operation)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


if __name__ == '__main__':
    hosts = ('m01', 'm02', 'm03')
    # operate(hosts, 'start')
    operate(hosts, 'suspend')
    # operate(hosts, 'stop')

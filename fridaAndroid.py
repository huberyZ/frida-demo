#!/usr/bin/env python3
import frida
import sys

def on_message(message, data):
    if message['type'] == 'error':
        print(message['stack'])
    else:
        print(message)

def startHook(packageName, jsCode):
    rdev = frida.get_remote_device()
    #脚本控制app启动 
#    pid = rdev.spawn(packageName)
#    session = rdev.attach(pid)
#    rdev.resume(pid)
    session = rdev.attach(packageName)
    script = session.create_script(jsCode)
    script.on('message', on_message)
    print(' Start attach')
    script.load()
    sys.stdin.read()
  #  session.detach()

if __name__ == "__main__":
    if (len(sys.argv) < 3):
        print("please enter package name and jscode...")
        exit(0)

    packageName = sys.argv[1]
    jsCodeName = sys.argv[2]
    with open(jsCodeName, 'r') as fp:
        jscode = fp.read()

    startHook(packageName, jscode)
    print("frida hook ok.");

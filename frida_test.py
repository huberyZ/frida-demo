#!/usr/bin/env python3
import frida
import sys

jscode = """
if(Java.available){
    Java.perform(function(){
        var MainActivity = Java.use("com.test.myimei.MainActivity");
        MainActivity.check.overload("int").implementation=function(math){
            console.log("[javascript] check be called.");
            send("check be called.");
            return this.check(95);      
        }
    });
}
"""

def on_message(message, data):
    if message['type'] == 'send':
        print(" {0}".format(message['payload']))
    else:
        print(message)

rdev = frida.get_remote_device()
session = rdev.attach("com.test.myimei")
script = session.create_script(jscode)
script.on('message', on_message)
print(' Start attach')
script.load()
sys.stdin.read()


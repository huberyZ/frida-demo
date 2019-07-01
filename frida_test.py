#!/usr/bin/env python3
import frida
import sys

javaFuncJsCode = """
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


privateNativeFuncJsCode = """
var nativePointer = new NativePointer(0x111111); // 此处参数为私有函数地址
send("native pointers:" + nativePointer);
var resultPointer;

Interceptor.attach(nativePointer, {
    onEnter: function(args) {
    
    },

    onLeave: function(retval) {
    
    }
});
"""

exportNativeFuncJsCode = """
var nativePointer = Module.findExportByName("libjniFunc.so", "Java_com_test_myimei_MainActivity_encryption");
send("native func encrytion() pointers:" + nativePointer);
Interceptor.attach(nativePointer, {
    onEnter: function(args) {
        send("encrytion() args: " + args[0])
    },
    onLeave: function(retval) {
        send("encrytion result value:" + retval);
    }
});
"""

def on_message(message, data):
    if message['type'] == 'send':
        print(" {0}".format(message['payload']))
    else:
        print(message)

def startHook(packageName, jsCode):
    rdev = frida.get_remote_device()
    session = rdev.attach(packageName)
    script = session.create_script(jsCode)
    script.on('message', on_message)
    print(' Start attach')
    script.load()
    sys.stdin.read()

if __name__ == "__main__":
#    startHook("com.test.myimei", javaFuncJsCode)
    startHook("com.test.myimei", exportNativeFuncJsCode)
   

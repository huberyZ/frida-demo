#!/usr/bin/env python3
import frida
import sys

javaFuncJsCode = """
if(Java.available){
    Java.perform(function(){
        console.log("[javascript] check be called.");
        var a = Java.use("com.ta.utdid2.device.a");
        a.getUtdid.overload().implementation=function(){
            send("c.getValue be called.");
            var str = this.getUtdid();
            send("getUtdid:" + str);
            return str;
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
//        send("encrytion() args: " + "len: " + parseInt(args[2]))
        send("encrytion() args: " + Memory.readCString(args[0], parseInt(args[1])) + "len: " + parseInt(args[1]))
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
    startHook("com.MobileTicket", javaFuncJsCode)
#    startHook("com.test.myimei", exportNativeFuncJsCode)
   

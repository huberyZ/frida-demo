//function hook1() {
//    if(Java.available){
//        Java.perform(function() {
//            console.log("[javascript] check be called.");
////            var settings = Java.use("android.provider.Settings");
//            ettings.System.putString.overload("android.content.ContentResolver", "java.lang.String", "java.lang.String").implementation=function(content, str1, str2){
//                send("c.getValue be called.");
//                send("src str1:" + str1);
//                send("src str2:" + str2);
//                return this.putString(content, str1, str2);
//            }
//        });
//    }
//}

//function hook1() {
//    if(Java.available){
//        Java.perform(function() {
//            console.log("[javascript] check be called.");
//            var adler32 = Java.use("java.util.zip.Adler32");
//            adler32.update.overload('[B').implementation=function(bytearray){
//                send("Adler32.update be called.");
//       //         send("num:" + num);
//                return this.update(bytearray);
//            }
//        });
//    }
//}



function hook1() {
    if(Java.available){
        Java.perform(function() {
            console.log("[javascript] check be called.");
            var ut = Java.use("com.ta.utdid2.device.UTDevice");
            ut.getUtdid.overload("android.content.Context").implementation=function(context){
                send("ut.getUtdid be called.");
                var str = this.getUtdid(context);
                send("ut.getUtdid:" + str);
                return str;
            }
        });
    }
}



setTimeout(hook1, 0);

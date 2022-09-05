//2021/12/25

app.startActivity({
  extras: {
    "android.intent.extra.TEXT": getClip(),
  },
  action: "android.intent.action.SEND",
  type: "text/*",
  packageName: "com.mojitec.mojidict",
  className: "com.mojitec.mojidict.ui.SearchActivityV2",
});

/* 
请注意，该Intent会被被拒绝访问，具体原因不明

Intent来自MOJi官网博客：
https://www.shareintelli.com/710/?platform=Android


下面为源代码 
public void startShow(View view) {
Intent intent = new Intent(Intent.ACTION_VIEW);
intent.putExtra(Intent.EXTRA_TEXT, “Dog”);//根据 静读天下的支持来看，二者的intent结构应该一致
intent.setType(“text/*”);
startActivity(intent);
}

Intent { 
    act=android.intent.action.SEND 
    cat=[android.intent.category.DEFAULT,android.intent.category.BROWSABLE] 
    flg=0x14000040 
    cmp=com.mmjang.ankihelper/.ui.popup.PopupActivity 
    
}
*/

/*
URL来自来自MOJi官网博客
https://www.shareintelli.com/710/?platform=Android
*/

launchApp("com.mojitec.mojidict");
app.startActivity({
  action: "android.intent.action.VIEW",
  data: "mojisho://?search=" + getClip(),
  packageName: "com.mojitec.mojidict",
});

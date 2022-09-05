/*
注意由于Android10 隐私政策调整，
当Auto.js不处于前台时
无法向剪贴板写入内容。
可以借助分屏实现。

另外，由于setClip()和getClip()
实际获取的是脚本启动时的的内容，
中途写入和赋值都会失败。

*/

console.show(); //注意实际使用时不需要弹窗，只需要记录
var start = Date.now();
var IndexText = files.read("v3_index.txt", (encoding = "utf-8")); //注意对象类型

function SearchIndex(SearchText) {
  if (IndexText.match(SearchText + "\r\n") != null) {
    //IndexText.search(InputText)找不到时不会返回null，另外，这里的匹配不是完全一致，需要用"\r\n"防止部分匹配
    ProcessTexts.push(SearchText);
    log("在索引中找到并返回结果：" + SearchText);
    //exit();
  } else {
    log("索引中找不到" + SearchText);
  }
}

var NoNeedProcess = "ぐつぶむる";

var NeedOnceProcess_itidann = "、ずよぬ";
var NeedOnceProcess_godann = "わえおがきぎげこごしせにねのばびべぼめもり";
var NeedOnceProcess_adj = "くうす";

var NeedTwiceProcess_adj_godann = "かけみそ"; //这几个词尾来源： 形容词 / 五段

var NeedTwiceProcess_itidann_godann = "たちてとなまられろ"; // 这些只可能来自一段 / 五段

function Process(InputText) {
  if (InputText === "行っ") {
    var ProcessText = InputText.slice(0, InputTextLength - 1) + "う"; //考虑到行く的结果比较简单，这里优先返回行う
    SearchIndex(ProcessText);
    var ProcessText = InputText.slice(0, InputTextLength - 1) + "く"; //考虑到行く的结果比较简单，这里优先返回行う
    SearchIndex(ProcessText);
  } else if (NoNeedProcess.match(LastLetter) != null) {
    log("now");
  } else if (NeedOnceProcess_itidann.match(LastLetter) != null) {
    log("词尾假名是" + LastLetter + "有可能是一段");
    ProcessText = InputText.slice(0, InputTextLength - 1) + "る";
    SearchIndex(ProcessText);
  } else if (NeedOnceProcess_godann.match(LastLetter) != null) {
    log("词尾假名是" + LastLetter + "有可能是五段");
    if ("わえお".match(LastLetter) != null) {
      ProcessText = InputText.slice(0, InputTextLength - 1) + "う";
      SearchIndex(ProcessText);
    } else if ("きこ".match(LastLetter) != null) {
      ProcessText = InputText.slice(0, InputTextLength - 1) + "く";
      SearchIndex(ProcessText);
    } else if ("しせ".match(LastLetter) != null) {
      ProcessText = InputText.slice(0, InputTextLength - 1) + "す";
      SearchIndex(ProcessText);
    } else if ("にねの".match(LastLetter) != null) {
      ProcessText = InputText.slice(0, InputTextLength - 1) + "ぬ";
      SearchIndex(ProcessText);
    } else if ("ばびべぼ".match(LastLetter) != null) {
      ProcessText = InputText.slice(0, InputTextLength - 1) + "ぶ";
      SearchIndex(ProcessText);
    } else if ("めも".match(LastLetter) != null) {
      ProcessText = InputText.slice(0, InputTextLength - 1) + "む";
      SearchIndex(ProcessText);
    } else if ("り".match(LastLetter) != null) {
      ProcessText = InputText.slice(0, InputTextLength - 1) + "る";
      SearchIndex(ProcessText);
    }
  } else if (NeedOnceProcess_adj.match(LastLetter) != null) {
    log("词尾假名是" + LastLetter + "有可能是形容词");
    ProcessText = InputText.slice(0, InputTextLength - 1) + "い";
    SearchIndex(ProcessText);
  } else if (NeedTwiceProcess_adj_godann.match(LastLetter) != null) {
    log("词尾假名是" + LastLetter + "有可能是形容词，也有可能是五段");
    ProcessText = InputText.slice(0, InputTextLength - 1) + "い";
    SearchIndex(ProcessText);
    if ("かけ".match(LastLetter) != null) {
      log("不是形容词，有可能是五段");
      ProcessText = InputText.slice(0, InputTextLength - 1) + "く";
      SearchIndex(ProcessText);
    } else if ("み".match(LastLetter) != null) {
      ProcessText = InputText.slice(0, InputTextLength - 1) + "む";
      SearchIndex(ProcessText);
    } else if ("そ".match(LastLetter) != null) {
      ProcessText = InputText.slice(0, InputTextLength - 1) + "す";
      SearchIndex(ProcessText);
    }
  } else if (NeedTwiceProcess_itidann_godann.match(LastLetter) != null) {
    log("词尾假名是" + LastLetter + "有可能是一段，也有可能是五段");
    ProcessText = InputText.slice(0, InputTextLength - 1) + "る";
    SearchIndex(ProcessText);
    if ("たちてと".match(LastLetter) != null) {
      log("不是一段，有可能是五段");
      ProcessText = InputText.slice(0, InputTextLength - 1) + "つ";
      SearchIndex(ProcessText);
    } else if ("な".match(LastLetter) != null) {
      ProcessText = InputText.slice(0, InputTextLength - 1) + "ぬ";
      SearchIndex(ProcessText);
    } else if ("ま".match(LastLetter) != null) {
      ProcessText = InputText.slice(0, InputTextLength - 1) + "む";
      SearchIndex(ProcessText);
    } else if ("られろ".match(LastLetter) != null) {
      ProcessText = InputText.slice(0, InputTextLength - 1) + "る";
      SearchIndex(ProcessText);
    }
  } else if (LastLetter === "っ") {
    ProcessText = InputText.slice(0, InputTextLength - 1) + "る";
    SearchIndex(ProcessText);
    ProcessText = InputText.slice(0, InputTextLength - 1) + "つ";
    SearchIndex(ProcessText);
  } else if (LastLetter === "さ") {
    ProcessText = InputText.slice(0, InputTextLength - 1) + "い"; //部分形容词的名词
    SearchIndex(ProcessText);
    ProcessText = InputText.slice(0, InputTextLength - 1) + "す"; //す结尾的五段动词未然形
    SearchIndex(ProcessText);
    ProcessText = InputText.slice(0, InputTextLength - 1) + "る"; //使役态
    SearchIndex(ProcessText);
  } else if (LastLetter === "ん") {
    ProcessText = InputText.slice(0, InputTextLength - 1) + "む";
    SearchIndex(ProcessText);
    ProcessText = InputText.slice(0, InputTextLength - 1) + "ぬ";
    SearchIndex(ProcessText);
    ProcessText = InputText.slice(0, InputTextLength - 1) + "ぶ";
    SearchIndex(ProcessText);
  } else if (LastLetter === "い") {
    log("词尾假名是" + LastLetter + "但不是形容词");
    ProcessText = InputText.slice(0, InputTextLength - 1) + "う"; //五段连一
    SearchIndex(ProcessText);
    ProcessText = InputText.slice(0, InputTextLength - 1) + "く"; //五段连一
    SearchIndex(ProcessText);
    ProcessText = InputText.slice(0, InputTextLength - 1) + "ぐ"; //五段连一
    SearchIndex(ProcessText);
  } else if (LastLetter === "ゃ") {
    log("一段动词てしまう的口语表达");
    ProcessText = InputText.slice(0, InputTextLength - 2) + "る"; //注意ちゃう是3个假名
    SearchIndex(ProcessText);
  }
}

var InputText = getClip();
console.log(InputText);

var ProcessTexts = [];
SearchIndex(InputText); //首先查找一次索引，有结果直接返回

SearchIndex(InputText + "る"); //一段动词特殊处理

var InputTextLength = InputText.length; //注意不是length()
var LastLetter = InputText[InputTextLength - 1]; //JS不支持反向索引
Process(InputText);
ProcessTexts.push(InputText);

//去掉重复值,优先保留第一次出现
function delete_duplicate_item(arr) {
  return Array.from(new Set(arr));
}

ProcessTexts = delete_duplicate_item(ProcessTexts);

var SelectedText = ""; //保存最终结果
var SelectedItem = dialogs.select("请选择一个推导结果：", ProcessTexts);
if (SelectedItem >= 0) {
  SelectedText = ProcessTexts[SelectedItem];
  var ClipBroadOutputText = setClip(SelectedText);
  var script = engines.execScriptFile("sendclip_url.js");
  var end = Date.now();
  log(end - start);
} else {
  toast("您取消了选择");
}

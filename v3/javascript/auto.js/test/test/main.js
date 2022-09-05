/*
本脚本主要用于验证算法准确度，需要在手机上花费较长的时间进行测试，考虑到只有最新版的Auto.js Pro 才支持node.js，后续有空再尝试将test.js使用node.js重构方便进行集成测试。有兴趣的话，可以自行探索，也欢迎提交PR:)
*/

//console.show()
var start = Date.now();

var IndexText = files.read("v3_index.txt", (encoding = "utf-8")); //注意对象类型
function SearchIndex(SearchText) {
  if (IndexText.match(SearchText + "\r\n") != null) {
    //IndexText.search(InputText)找不到时不会返回null，另外，这里的匹配不是完全一致，需要用"\r\n"防止部分匹配
    ProcessTexts.push(SearchText);
    //console.log("在索引中找到并返回结果：" + SearchText);
    //exit();
  } else {
    //console.log("索引中找不到" + SearchText);
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
    //看看到底有没必
  } else if (NeedOnceProcess_itidann.match(LastLetter) != null) {
    //console.log("词尾假名是" + LastLetter + "有可能是一段");
    ProcessText = InputText.slice(0, InputTextLength - 1) + "る";
    SearchIndex(ProcessText);
  } else if (NeedOnceProcess_godann.match(LastLetter) != null) {
    //console.log("词尾假名是" + LastLetter + "有可能是五段");
    if ("わえお".match(LastLetter) != null) {
      ProcessText = InputText.slice(0, InputTextLength - 1) + "う";
      SearchIndex(ProcessText);
    } else if ("きこ".match(LastLetter) != null) {
      ProcessText = InputText.slice(0, InputTextLength - 1) + "く";
      SearchIndex(ProcessText);
    } else if ("がぎげご".match(LastLetter) != null) {
      ProcessText = InputText.slice(0, InputTextLength - 1) + "ぐ";
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
    //console.log("词尾假名是" + LastLetter + "有可能是形容词");
    ProcessText = InputText.slice(0, InputTextLength - 1) + "い";
    SearchIndex(ProcessText);
  } else if (NeedTwiceProcess_adj_godann.match(LastLetter) != null) {
    //console.log("词尾假名是" + LastLetter + "有可能是形容词，也有可能是五段");
    ProcessText = InputText.slice(0, InputTextLength - 1) + "い";
    SearchIndex(ProcessText);
    if ("かけ".match(LastLetter) != null) {
      //console.log("不是形容词，有可能是五段");
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
    //console.log("词尾假名是" + LastLetter + "有可能是一段，也有可能是五段");
    ProcessText = InputText.slice(0, InputTextLength - 1) + "る";
    SearchIndex(ProcessText);
    if ("たちてと".match(LastLetter) != null) {
      //console.log("不是一段，有可能是五段");
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
    ProcessText = InputText.slice(0, InputTextLength - 1) + "う";
    SearchIndex(ProcessText);
  } else if (LastLetter === "さ") {
    ProcessText = InputText.slice(0, InputTextLength - 1) + "い"; //部分形容词的名词
    SearchIndex(ProcessText);
    ProcessText = InputText.slice(0, InputTextLength - 1) + "す"; //す结尾的五段动词未然形
    SearchIndex(ProcessText);
    ProcessText = InputText.slice(0, InputTextLength - 1) + "る"; //使役态
    SearchIndex(ProcessText);
  } else if (LastLetter === "ん") {
    ProcessText = InputText.slice(0, InputTextLength - 1) + "む";//五段动词连2
    SearchIndex(ProcessText);
    ProcessText = InputText.slice(0, InputTextLength - 1) + "る";//一段动词口语否定
    SearchIndex(ProcessText);
    ProcessText = InputText.slice(0, InputTextLength - 1) + "ぬ";//五段动词连2
    SearchIndex(ProcessText);
    ProcessText = InputText.slice(0, InputTextLength - 1) + "ぶ";//五段动词连2
    SearchIndex(ProcessText);
  } else if (LastLetter === "い") {
    //console.log("词尾假名是" + LastLetter + "但不是形容词");
    ProcessText = InputText.slice(0, InputTextLength - 1) + "う"; //五段连1
    SearchIndex(ProcessText);
    ProcessText = InputText.slice(0, InputTextLength - 1) + "く"; //五段连2
    SearchIndex(ProcessText);
    ProcessText = InputText.slice(0, InputTextLength - 1) + "ぐ"; //五段连2
    SearchIndex(ProcessText);
  } else if (LastLetter === "ゃ") {
    //console.log("一段动词てしまう的口语表达");
    ProcessText = InputText.slice(0, InputTextLength - 2) + "る"; //注意,ちゃう是3个假名
    SearchIndex(ProcessText);
  }
}

//去掉重复值,优先保留第一次出现
function delete_duplicate_item(arr) {
  return Array.from(new Set(arr));
}

var FileContext = files.read("temp.txt", (encoding = "utf-8")); //注意对象类型
var FileContextList = FileContext.split("\n");

for (var line in FileContextList) {
  var InputText = FileContextList[line].split("\t")[0];
  //log("划词部分是："+InputText)
  var ProcessTexts = []; //保存推导的结果
  //console.log(InputText);

  SearchIndex(InputText); //首先查找一次索引，有结果直接返回
  SearchIndex(InputText + "る"); //一段动词特殊处理

  var InputTextLength = InputText.length; //注意不是length()
  var LastLetter = InputText[InputTextLength - 1]; //JS不支持反向索引
  Process(InputText);
  ProcessTexts.push(InputText); //保存初始值，便于脚本出错时修改
  ProcessTexts = delete_duplicate_item(ProcessTexts);
  files.append(
    "save.txt",
    ProcessTexts + "\t" + FileContextList[line]  + "\n"
  );
  var percent = 0;
  log((line * 100) / FileContextList.length + "%");
  if ((line / FileContextList.length) * 100 + "%" > percent) {
    percent = 1 + percent;
    log(percent);
  }
}

var end = Date.now();
log(end - start);

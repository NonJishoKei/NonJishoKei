/*
本脚本用于调试
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
    var ProcessText = InputText.slice(0, InputTextLength - 1) + "く";
    SearchIndex(ProcessText);
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

    /*按照假名所在的行进行分类*/
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

function DelOCRError(ProcessText) {
  ProcessText = ProcessText.replace(" ", "");
  ProcessText = ProcessText.replace("\n", "");
  return ProcessText.replace(" ", "");
}

function ConverHina2kata(ProcessText) {
  return ProcessText.replace(/[\u30a1-\u30f6]/g, function (match) {
    var chr = match.charCodeAt(0) - 0x60;
    return String.fromCharCode(chr);
  });
}

function DelWordRuby(ProcessText) {
  var reg = /\([\u3040-\u309f]*?\)/g;
  OutputText = ProcessText.replace(reg, "");
}

function ConverRepeSingleSign(ProcessText) {
  //这些符号只代表一个假名或者汉字，注意ゝヽ不一定出现在单词的结尾部分，例如：やがて再び唇をわなゝかした
  return ProcessText.replace(/([^\n]{1})(々|〻|ゝ|ヽ)/g, "$1$1");
}

function ConverRepeSingleDakuSign(ProcessText) {
  return ProcessText.replace(/([^\n]{1})(ヾ|ゞ)/g, function (match, $1) {
    var chr = $1.charCodeAt(0) + 0x1;
    return $1 + String.fromCharCode(chr);
  });
}

function ConverRepeDoubleSign(ProcessText) {
  //这些符号代表2个假名或者汉字
  return ProcessText.replace(/([^\n]{2})(〳〵|／＼)/g, "$1$1");
}

function ConverRepeDoubleDakuSign(ProcessText) {
  ProcessText = /^([^\n]*?)(〴〵|／″＼)(.*?)$/.exec(InputText);
  if (ProcessText[1].match(/[^\u3040-\u30ff]/) != null) {
    log(ProcessText[1] + ProcessText[1]);
    return ProcessText[1] + ProcessText[1];
  } else {
    return (
      ProcessText[1] +
      ProcessText[0].replace(
        /([^\n]{1})([^\n]{1})(〴〵|／″＼)/g,
        function (match, $1, $2) {
          var chr = $1.charCodeAt(0) + 0x1;
          return String.fromCharCode(chr) + $2;
        }
      )
    );
  }
}

var InputText = getClip();
console.log(InputText);

//预处理

InputText = DelOCRError(InputText);
if (InputText.search(/^([\u30a1-\u30f6]*?)$/) != -1) {
  //暂时不处理タピる这种特殊的外来语单词
  ConverHina2kata(InputText);
}

if (InputText.search(/\(/) != -1) {
  InputText = DelWordRuby(InputText);
}

if (InputText.search(/([^\n]{1})(々|〻|ゝ|ヽ)/) != -1) {
  InputText = ConverRepeSingleSign(InputText);
}

if (InputText.search(/([^\n]{1})(ヾ|ゞ)/) != -1) {
  InputText = ConverRepeSingleDakuSign(InputText);
}

if (InputText.search(/([^\n]{2})(〳〵|／＼)/) != -1) {
  InputText = ConverRepeDoubleSign(InputText);
}

if (InputText.search(/^([^\n]*?)(〴〵|／″＼)(.*?)$/) != -1) {
  InputText = ConverRepeDoubleDakuSign(InputText);
}

var ProcessTexts = []; //记录所有推导的结果
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
  log('选择的推到结果是：'+SelectedText)
  //var script = engines.execScriptFile("sendclip_url.js");测试时不用唤起MOJi，观察控制台即可
  var end = Date.now();
  log(end - start);
} else {
  toast("您取消了选择");
}

/*
自动转换那些日语独有的标记，本项目参考了一份来自日本文化厅的文件
々〻（汉字重复标记，后者主要用于手写，但考虑到OCR等场景，算作一类）例子：度々、度〻、明々白々
ゝゞヽヾ（假名的重复标记，多见于比较老的文章）例子：こゝろ、ほヾ
〳〵／＼（前者是Unicode编码，后者来自青空文库）例子：いよ〳〵、しげ／＼（注意这种字符串的\通过pyperclip传递时不会被转义）
〴〵／″＼（前者是Unicode编码，后者来自青空文库）例子：しみ〴〵、しみ／″＼
*/

console.show(); //注意实际使用时不需要弹窗，只需要记录
var start = Date.now();
var InputText = "しげ／＼";


function ConverRepeSingleSign(ProcessText) {//这些符号只代表一个假名或者汉字，注意ゝヽ不一定出现在单词的结尾部分，例如：やがて再び唇をわなゝかした
    return ProcessText.replace(/([^\n]{1})(々|〻|ゝ|ヽ)/g, "$1$1");
}

function ConverRepeSingleDakuSign(ProcessText) {
    return ProcessText.replace(/([^\n]{1})(ヾ|ゞ)/g,function(match,$1){
        var chr = $1.charCodeAt(0) +0x1;
        return $1+String.fromCharCode(chr);
})}

function ConverRepeDoubleSign(ProcessText) {//这些符号代表2个假名或者汉字
    return ProcessText.replace(/([^\n]{2})(〳〵|／＼)/g,"$1$1")
}


function ConverRepeDoubleDakuSign(ProcessText) { 
    ProcessText = /^([^\n]*?)(〴〵|／″＼)(.*?)$/.exec(InputText)
    if (ProcessText[1].match(/[^\u3040-\u30ff]/) != null) {
        log(ProcessText[1] + ProcessText[1])
        return ProcessText[1] + ProcessText[1]
    } else {
        return ProcessText[1] + ProcessText[0].replace(/([^\n]{1})([^\n]{1})(〴〵|／″＼)/g, function(match, $1,$2) {
            var chr = $1.charCodeAt(0) + 0x1;
            return String.fromCharCode(chr)+$2;
        })
    }
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

  log(InputText)

var end = Date.now();
log(end - start);
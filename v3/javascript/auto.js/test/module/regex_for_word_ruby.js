/*

检查输入的内容中是否有假名注音的语法()，通过正则提取真正需要查找的部分
测试用例
食(た)べる
魂(こん)不(ふ)守(しゅ)舎(しゃ)
*/

console.show(); //注意实际使用时不需要弹窗，只需要记录
var start = Date.now();
var InputText = "魂(こん)不(ふ)守(しゅ)舎(しゃ)";

function DelWordRuby(ProcessText) {
  var reg = /\([\u3040-\u309f]*?\)/g;
  OutputText = ProcessText.replace(reg, "");
  log(OutputText);
}

if (InputText.search(/\(/) != -1) {
  InputText = DelWordRuby(InputText);
}

var end = Date.now();
log(end - start);

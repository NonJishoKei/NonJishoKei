/*

计算输入值的Unicode码，并尝试将其转为平假名后在词典中进行查找
需要匹配的示例：
チョコチョコ（当有拗音时，单词长度就不是4了）
ヒト（不止有拟声拟态词会写假名）
不能匹配的：
タピる（部分合成的外来语，往往是固定说法，不要随意拆分不全是片假名的单词，因为权威的词典很可能不会收录转换后的写法）
*/

console.show(); //注意实际使用时不需要弹窗，只需要记录
var start = Date.now();
var InputText = "";

function ConverHina2kata(ProcessText) {
    return ProcessText.replace(/[\u30a1-\u30f6]/g, function(match) {
        var chr = match.charCodeAt(0) - 0x60;
        return String.fromCharCode(chr);
    });
}

if (InputText.search(/^([\u30a1-\u30f6]*?)$/) != -1) {//暂时不处理タピる这种特殊的外来语单词
    ConverHina2kata(InputText);
}

var end = Date.now();
log(end - start);
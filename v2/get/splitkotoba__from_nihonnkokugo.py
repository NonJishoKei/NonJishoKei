import os
import re
'''
本脚本尝试分离、提取下列词条：（不完整，待补充）
と‐・す 【賭】賭す
たいくつ‐が・る 【退屈─】  退屈がる  
そり‐こく・る 【剃─】  剃こくる  
あい‐くろし・い 【愛─】  愛くろしい  
あい‐ぐ・す 【相具】  相具す  
たか‐ぶ・る【高─・昂】品词  高ぶる和昂る
あが・る【上・揚・挙・騰】上る、揚る……
そり‐かえ・る 【反返】  反返る 这个可能是编纂者失误
'''

ProessPath = os.getcwd()

InputFile = r'temp.txt'
OutpurFile = r'save.txt'

with open(InputFile, encoding="UTF-8") as f, open(OutpurFile, 'w', encoding='UTF-8') as s:
    for line in f:
        # あ	【足】    	名
        if '【' in line:
            regex = r'^(?P<hiragara>(.*?))\t【(?P<kakikata>(.*?))】\t(?P<hinnsi>(.*?))$'
            splitline = re.search(regex, line)
            EditLines = []
            # 判断是否需要补充
            if splitline != None:
                HiragaraText = splitline.group("hiragara")
                KakikataText = splitline.group("kakikata")
                HinsiText = splitline.group("hinnsi")
                
                # 观察是否需要替换动词 あいいど・む	【相挑】   替换为 相挑む 和あいいどむ
                if '・' in HiragaraText:
                    
                    if '・' in KakikataText:
                        AllKakikataText = []
                        KakikataText = KakikataText.split('・') #あが・る【上・揚・挙・騰】 〔ラ四〕
                        for i in KakikataText:
                            AllKakikataText.append(i) # 上、揚挙、騰
                        for i in AllKakikataText:
                            EditLine = HiragaraText+'\t'+i+'\t'+HinsiText  #列表： あが・る   上  〔ラ四〕
                            EditLines.append(EditLine) #

                        
                        for i in EditLines:
                            regex = r'^(.*?)・(.*?)\t(.*?)\t(.*?)'#あが・る\t上\t〔ラ四〕
                            replacement = r"\3\2\t\4"#上る\t〔ラ四〕
                            outputline = re.sub(regex, replacement, i)
                            s.write(outputline+'\n')
                        s.write(HiragaraText.replace(
                            '・', '')+'\t'+HinsiText+'\n')#あがる\t〔ラ四〕
                    elif '・' not in KakikataText: #あいあた・る	【相当】    〔自ラ四〕
                        s.write(HiragaraText.replace(
                            '・', '')+'\t'+HinsiText+'\n') # 保存あいあたる 〔自ラ四〕
                        HiragaraText = re.sub("^(.*?)・(.*?)", r"\2",HiragaraText) #提取あいあた
                        s.write(KakikataText+HiragaraText+'\t'+HinsiText+'\n') # 保存 相当る〔自ラ四〕
                # 不需要拆分动词：たほう	【多方】	名
                elif '・'not in HiragaraText:
                    
                    if '・' in KakikataText:# 需要拆分假名书写：たべん	【多弁・多辯】	名
                        AllKakikataText = []
                        KakikataText = KakikataText.split('・')
                        for i in KakikataText:
                            AllKakikataText.append(i) # 提取多弁、多辯
                        for i in AllKakikataText:
                            EditLine = i+'\t'+HinsiText
                            EditLines.append(EditLine) # 提取：多弁\t名,多辯\t名
                        # 保存每一行的结果
                        for i in EditLines:
                            s.write(i+'\n') # 保存：多弁\t名、多辯\t名
                        s.write(HiragaraText+'\t'+HinsiText+'\n') #保存たべん\t名
                        
                    elif '・' not in KakikataText: # おしごろう	【唖五郎】	名
                        s.write(HiragaraText+'\n'+HinsiText+'\n')#おしごろう\t名
                        s.write(KakikataText+'\n'+HinsiText+'\n')#唖五郎\t名
                else:
                    print(line)
        else:
            s.write(line)

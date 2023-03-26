#!/usr/bin/env python3
import time

ch_list = ['']

#replace_with_backtick('啊', s)

pstring1 = ''
pstring2 = ''
with open('flypy.dict.yaml', encoding='utf-8') as f:
    for line in f: 
        if not '\t' in line:
            continue
        string1, string2 = line.strip().split('\t')
        if (len(string1) == 1 and len(string2) == 4):
            if (pstring2 == string2):
                ch_list.append(pstring1 + '\t' + pstring2)
                ch_list.append(string1 + '\t' + pstring2)     
        pstring1 = string1
        pstring2 = string2
        
for string in ch_list:
    print(string)
    
   
dict_head = '''---
name: flypywc
version: "{}"
sort: original
wildcard: "`~"
columns:
  - text
  - code
  - weight
  - stem
encoder:
  rules:
    - lengh_equal: 1
      formula: "AaAz"
    - length_equal: 2
      formula: "AaAbBaBb"
    - length_equal: 3
      formula: "AaAbBaCa"
    - length_in_range: [4, 10]
      formula: "AaBaCaZa"
...
'''

dict_head = dict_head.format(time.time())
    
#with open('flypywc.dict.yaml', "w", encoding='utf-8') as f:
#    f.write(dict_head)
#    for string in ch_list:
#        f.write(string)
#        f.write('\n')
        


#!/usr/bin/env python3

ch_list = ['']

def replace_with_backtick(w, s):
    for i in range(len(s)+1):
        for j in range(i+1, len(s)+1):
            new_s = w + '\t' + s[:i] + '`'*(j-i) + s[j:]
            print(new_s)
            
def rep1(t, w, s):
    for i in range(len(s)):
        ns = t + w + s[:i] + '`' + s[i + 1:]
        print (ns)
        
def rep2(t, w, s):
    if (len(s) < 2):
        return
    for i in range(len(s)):
        rep1(t, w + s[:i] + '`', s[i + 1:])
        

def rep3(t, w, s):
    for i in range(len(s)):
        rep2(t, s[:i] + '`', s[i + 1:])
        
def repx(t, w, s, x):
    if (x == 1):
        for i in range(len(s) + 1):
            for j in range(i + 1, len(s) + 1):
                ns = t + '\t' + w + s[:i] + '`' + s[i + 1:]
                ch_list.append(ns)
    else:
        for i in range(len(s)):
            repx(t, w + s[:i] + '`', s[i + 1:], x - 1)
            
            
def repTo4(w, s):
    rep1(w, '', s)
    rep2(w, '', s)
    rep3(w, '', s)

def rep(w, s):
    for i in range(1, len(s)):
        repx(w, '', s, i)

#replace_with_backtick('啊', s)

with open('wc.txt', encoding='utf-8') as f:
    for line in f:
        string1, string2 = line.strip().split('\t')
        rep(string1, string2)
        
for string in ch_list:
    print(string)
    
   
dict_head = '''---
name: flypywc
version: "1.02"
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
    
with open('flypywc.dict.yaml', "w", encoding='utf-8') as f:
    f.write(dict_head)
    for string in ch_list:
        f.write(string)
        f.write('\n')
        


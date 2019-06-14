# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 14:01:26 2018

@author: Jiastin
"""
import re
f=open("C:\\Users\\Jiastin\\Documents\\病历示例文本\\结肠直肠肿瘤病房\\ZY010000487429\\病程记录.txt",'r',encoding='utf-8')
s=f.read()
print(s.splitlines())
u=s.split('\n\n') 
#print(u)
w1 = '查体：'
w2 = '：' 
pat = re.compile(w1+'(.*?)'+w2,re.S) #把各段病程记录与研究生之间的内容都摘出来
result = pat.findall(s)
print(result)
#print(len(result))
punctuation = "[\n]" #去掉相应的标点符号和空格
u_pure =[re.sub(punctuation, "",x) for x in u]
#print(u_pure)


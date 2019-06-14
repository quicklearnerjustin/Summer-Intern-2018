 # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import re
f=open("C:\\Users\\Jiastin\\Documents\\病历示例文本\\结肠直肠肿瘤病房\\ZY010000487429\\病程记录.txt",'r',encoding='utf-8')
s=f.read()
#print(type(s))
#print(s)
w1 = '病程记录'
w2 = '研究生'
pat = re.compile(w1+'(.*?)'+w2,re.S) #把各段病程记录与研究生之间的内容都摘出来
result = pat.findall(s)
punctuation = "[\，+\,+\.+\n]" #去掉相应的标点符号和空格
result_pure =[re.sub(punctuation, "",x) for x in result]
#print(result_pure)
Useless=["0","1","2","3","4","5","6","7","8","9"] #去掉所有数字
def remove_uselss(str1,str2):
    for item in str2:
        str1=str1.replace(item,"")
    return str1    
result_pure1=[remove_uselss(x,Useless) for x in result_pure]
#print(result_pure1)
counts = {} #生成一个空字典
for item in result_pure1:			
    counts[item] = counts.get(item,0) + 1 #计算每个字符串出现的次数，把相应的键和值放到字典里
items = list(counts.items()) #转换成列表
items.sort(key=lambda x:x[1], reverse=True) #把列表中的每对元素按出现的次数由大到小排列 
print(items)
"""a="".join([str(result_pure1[i])+str(result_pure1[i+1]) for i in range(0, len(result_pure1),2)]) #把列表转换为字符串
print(a)
print(type(a))
a=a.splitlines()"""

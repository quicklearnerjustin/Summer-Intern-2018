# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 15:57:48 2018

@author: Jiastin
"""
import os  
import time  
import re 
import jieba

'''---------------读取摘取数据--------------------'''
time_start=time.time()
path = 'C:\\Users\\Jiastin\\Documents\\病历示例文本'  
a=''  
for fpathe,dirs,fs in os.walk(path):  #先读取文件名
    for f in fs:    
        a=a+os.path.join(fpathe,f)
#print(a)
b=a.split('txt') #用’txt‘split每个文件路径形成列表
#print(b)
for i in range(len(b)): #把文件路径补全
    b[i]=b[i]+'txt'
    c=b[0:-1]
    #print(c)
s=''
for j in range(len(c)):    #依次读取每个文件文本
    filePath = c[j]
    datan = open(filePath,'r',encoding='utf-8')
    s=s+datan.read()
'''诊断'''
w1 = '初步诊断：'
w2 = '诊断依据' 
pat = re.compile(w1+'(.*?)'+w2,re.S) #把各初步诊断的内容都摘出来
result = pat.findall(s)
#print(result)
'''主诉'''
z1='患者以“'
z2='为主诉'
pat1 = re.compile(z1+'(.*?)'+z2,re.S) #把各主诉的内容都摘出来
result1 = pat1.findall(s)
print(result1)
'''---------------清理数据--------------------'''

punctuation = "[\，+\, +\n +\。]" #去掉相应的标点符号和空格
result_pure =[re.sub(punctuation, "",x) for x in result]
#print(result_pure)
for i in range(len(result_pure)):
    if '1.' in result_pure[i]:
        result_pure[i]=result_pure[i].strip('1.')
#print(result_pure)
k=[]
'''去掉序号'''
for i in range(len(result_pure)):#先按'.'split
    k+=result_pure[i].split('.')
num=['2','3','4','5','6']    
for i in range(len(k)): #若split之后的字符串最后一个字符是数字，就把该数字去掉
    if k[i][-1] in num:
        k[i]=k[i][0:-1]
print(k)

'''---------------分词 筛选 查找--------------------'''

for i in range(len(k)): #拓展词库
    jieba.add_word(k[i])
'''file=docx.Document()
file.add_paragraph(k)
file.save('C:\\Users\\Jiastin\\Documents\\病历示例文本')'''

'''分词试验'''
e='孕1产0妊娠38周3ROA单胎冠心病高血压病3级'
print(jieba.lcut(e))

empty=[]
for i in range(len(result1)):   #分词主诉
    empty+=jieba.lcut(result1[i])
final=[]
for i in range(len(empty)): #查找主诉与诊断的重合
    for j in range(len(k)):
        if empty[i]==k[j]:
            final.append(k[j])
if len(final)>=1: #final里面有东西
    print(final)
else: #final为空
    print('没有医生把诊断写进主诉里面')   
time_end=time.time()         
print('time cost:',time_end-time_start,'s')
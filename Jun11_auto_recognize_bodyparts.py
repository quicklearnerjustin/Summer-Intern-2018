# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 14:01:26 2018

@author: Jiastin
"""
import re
f=open("C:\\Users\\Jiastin\\Documents\\病历示例文本\\结肠直肠肿瘤病房\\ZY010000487429\\病程记录.txt",'r',encoding='utf-8')
s=f.read()
w1 = '查体：'
w2 = '：' 
pat = re.compile(w1+'(.*?)'+w2,re.S) #把各段查体与查体下一项之间的内容都摘出来
result = pat.findall(s)
#print(result)
punctuation = '\n' #去掉元素之间的换行符
#result_pure =[re.sub(punctuation, '',x) for x in result]
result_pure =[re.sub(punctuation, "",x) for x in result]
Useless=['查房意见','处置','专科检查','辅助检查'] #去掉查体后一项的专业名称（只剩查体的内容）
def remove_uselss(str1,str2):
    for item in str2:
        str1=str1.replace(item,"")
    return str1    
result_pure1=[remove_uselss(x,Useless) for x in result_pure]
#print(result_pure1)
b=[]
for i in range(len(result_pure1)):
    a=re.split('[，。,]',result_pure1[i])#按逗号句号断句 split sentences with commas or periods
    b+=a
for y in b:#清理多余信息
    if '' in b:
        b.remove('')
    elif '3、' in b:
        b.remove('3、')
print(b)
#print(type(b))
def same(list1,str1):#找两个列表的交叉重复项 find the same elements 
    c = []
    for m in range(len(str1)): 
        for n in range(len(list1)):
          for p in range(0,3):
               if str1[m:(m+p)] == list1[n]:
                   c=c+list(str1[m:(m+p)])#提取重复项 filter the repeated elements
                   c=list(set(c)) #列表去重 delete the repeated elements
    return c  

k=['T','P','R']#体温心率血压 body temperature and blood pressure
l=['心','肺','肝','脾','胃','结膜','巩膜','口','腹','肾','下肢','肛门'] #器官 organs

for j in range(len(b)):
    if same(k,b[j]) != []: #要是测体温心率血压的就输出none print none when the sentence is describing body temperatures or blood pressure
        print('none',b[j])
    else:
        for z in range(10): #在当句或者往前找找到最近的是什么器官就打印什么器官 
            if same(l,b[j-z]) != []:
                print(''.join(same(l,b[j-z])[::-1]),b[j])
                break #找到了就停止循环 if we find it, we stop the current loop 
        

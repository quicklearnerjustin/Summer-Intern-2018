jie# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 14:01:19 2018

@author: Jiastin
"""
import os  
  
import re 
path = 'C:\\Users\\Jiastin\\Documents\\病历示例文本\\第二呼吸内科病房'  
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

print(s)
w1 = '初步诊断：'
w2 = '鉴别诊断' 
pat = re.compile(w1+'(.*?)'+w2,re.S) #筛选出'初步诊断'和'诊断依据' 
result = pat.findall(s)
print(result)
x1 = '初步诊断：'
x2 = '诊断依据' 
pat1 = re.compile(x1+'(.*?)'+x2,re.S) #只筛选出'初步诊断'
result1 = pat1.findall(s)
#print(result1)
print(len(result))
print(len(result1))
p=[]
r=[]
q=[]
for i in range(len(result)):
    p=p+result[i].split('\n')
#print(p)    
#print(len(p))
def removSpace(list1):           
    for i in range(len(p)): 
        p[i]=p[i].replace(' ','')
    return p
#print(removSpace(p))
aa=[]
bb={}
for i in range(len(result)):
    aa=result[i].split('诊断依据') #把每个字符串以“诊断依据”为界，split分成前后两个部分（疾病诊断和依据）（列表）
    aa0=aa[0].split()#split第一个部分<疾病诊断>成列表
    aa1=aa[1].split()#split第二个部分<依据>成列表
    aa0=aa0[0:len(aa1)]#按<依据>个数截取等长<疾病诊断>
    yay=dict(zip(aa1,aa0))#把<依据>和<疾病诊断>一一对应组成字典 注：依据在前是因为诊断可能会重复，而不同病人的诊断依据重复的可能性极低
    bb=dict(bb,**yay)#依次放到空字典里形成新字典
print(bb)
p1=[]
r1=[]
q1=[]
for i in range(len(result1)):
    p1=p1+result1[i].split('\n')
#print(p)    
#print(len(p))
def get_keys(d,value):#字典通过值返回键
    return [k for k,v in d.items() if v[2:] == value or v == value]
def removSpace(list1):           
    for i in range(len(p1)):
        p1[i]=p1[i].replace(' ','')
    return p1
#print(removSpace(p))
r1=removSpace(p1)    
for i in range(len(r1)):    
    q1=q1+r1[i].split()
print(q1)    
print(len(q1))
#print(result1[0].split('\n')+result1[1].split('\n')+result1[2].split('\n'))
num=['1','2','3','4','5','6','7','8','9']
def addNum(list1):
    for i in range(len(q1)):
        for j in range(len(num)):
            if q1[i][0] not in num:
                q1[i]='1、'+q1[i]
            else:
                q1[i]=q1[i]
    return q1
#print(addNum(q)) 
def substt(list1):
    for i in range(len(q1)):
        if '.' in q1[i]:
            q1[i]=q1[i].replace('.','、')
        else:
            q1[i]=q1[i]
    return q1
#print(substt(q))
counts = {} #生成一个空字典
for item in q1:			
    counts[item[2:]] = counts.get(item[2:],0) + 1 #计算每个字符串出现的次数，把相应的键和值放到字典里
items = list(counts.items()) #转换成列表
items.sort(key=lambda x:x[1], reverse=True) #把列表中的每对元素按出现的次数由大到小排列 
print(items)
print(items[0][0])
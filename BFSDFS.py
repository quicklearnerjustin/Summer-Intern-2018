# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 17:07:57 2018

@author: Jiastin
"""


time_start=time.time()
import os, re




def BFS_Dir(path, dirCallback = None, fileCallback = None):
    queue = []
    ret = []
    queue.append(path);
    while len(queue) > 0:
        tmp = queue.pop(0)
        if(os.path.isdir(tmp)):
            ret.append(tmp)
            for item in os.listdir(tmp):
                queue.append(os.path.join(tmp, item))
            if dirCallback:
                dirCallback(tmp)
        elif(os.path.isfile(tmp)):
            ret.append(tmp)
            print(tmp)
            f=open(tmp,'r',encoding='utf-8')
            s=f.read()
            z1='岁，以“'
            z2='”为主诉'
            pat1 = re.compile(z1+'(.*?)'+z2,re.S) #把各主诉的内容都摘出来
            result1 = pat1.findall(s)
            print(result1)
            if fileCallback:
                fileCallback(tmp)        
    return ret
BFS_Dir('C:\\Users\\Jiastin\\Documents\\病历示例文本')
        
time_end=time.time() 
print('time cost:',time_end-time_start,'s')

time_start=time.time()
def DFS_Dir(path, dirCallback = None, fileCallback = None):
    stack = []
    ret = []
    stack.append(path);
    while len(stack) > 0:
        tmp = stack.pop(len(stack) - 1)
        if(os.path.isdir(tmp)):
            ret.append(tmp)
            for item in os.listdir(tmp):
                stack.append(os.path.join(tmp, item))
            if dirCallback:
                dirCallback(tmp)
        elif(os.path.isfile(tmp)):
            ret.append(tmp)
            print(tmp)
            f=open(tmp,'r',encoding='utf-8')
            s=f.read()
            z1='患者以“'
            z2='为主诉'
            pat1 = re.compile(z1+'(.*?)'+z2,re.S) #把各主诉的内容都摘出来
            result1 = pat1.findall(s)
            print(result1)
            if fileCallback:
                fileCallback(tmp)
    return ret
DFS_Dir('C:\\Users\\Jiastin\\Documents\\病历示例文本')
time_end=time.time()         

print('time cost:',time_end-time_start,'s')


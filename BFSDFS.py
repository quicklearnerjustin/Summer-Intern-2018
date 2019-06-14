# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 17:07:57 2018

@author: Jiastin
"""

import os, fnmatch, time
# 检查一个目录，后者某个包含子目录的目录树，并根据某种模式迭代所有文件
# patterns如：*.html,若大小写敏感可写*.[Hh][Tt][Mm][Ll] 
# single_level 为True表示只检查第一层 
# yield_folders 表示是否显示子目录，为False只遍历子目录中的文件，
# 但不返回字母名 
'''def all_files(root, patterns='*', single_level=False, yield_folders=False): 
  # 将模式从字符串中取出放入列表中 
  patterns = patterns.split(';') 
  for path, subdirs, files in os.walk(root): 
    if yield_folders: 
      files.extend(subdirs) 
    files.sort() 
    for name in files: 
      for pattern in patterns: 
        if fnmatch.fnmatch(name, pattern): 
          yield os.path.join(path, name) 
          break
    if single_level: 
      break
for file in all_files('C:\\Users\\Jiastin\\Documents\\病历示例文本', '*.s;*.c', False, False):
  print(file)

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
print(s)'''


'''time_start=time.time()

#import os
class ShenDu:
    def __init__(self,path):
        "初始化函数，遍历的根目录"
        self.path = path
        self.MyList =[]#创建一个文件夹列表
        self.MyList.append(self.path)#把根目录加入列表中

    def BianLi(self):
        "对于遍历的具体实现"
        while len(self.MyList) !=0:
            path =self.MyList.pop()#弹出一个路径
            if os.path.isdir(path):#对弹出的路径进行判断是否为文件夹
                #print("文件夹",path)
                myFileList =os.listdir(path)#如果是文件夹，就把文件夹中所有东西加入列表
                for line in myFileList:#循环列表（过滤文件）
                    myPath =path+"\\"+line#形成绝对路径
                    if os.path.isdir(myPath):#如果是文件夹就把这个文件夹添加到文件夹列表中
                        self.MyList.append(myPath)
                    else:#如果不是则输出
                        print("文件",myPath)
                        f=open(myPath,'r',encoding='utf-8')
                        s=f.read()
                        print(s)

    def __del__(self):
        "最终会执行的操作"
        pass
path ="C:\\Users\\Jiastin\\Documents\\病历示例文本"#根目录
file =ShenDu(path)#实例化对象
file.BianLi()#







time_end=time.time()         
print('time cost:',time_end-time_start,'s')'''


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

'''time_start=time.time()
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

print('time cost:',time_end-time_start,'s')'''


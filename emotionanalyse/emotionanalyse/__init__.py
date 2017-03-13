#coding:utf8
import sys
import codecs
import jieba

f = codecs.open("D:\\emotion-analysis\\data\\pnn_annotated.txt",'r',encoding='utf-8')
data = f.readlines()
newdata = []
segmenttest = []
newsegmenttest = []
for line in data:
    newdata.append(line.strip('\r\n'))
for line in newdata:
    segmenttest.append(line.replace('\t',''))
    
classpositive = []
classnegative = []
classneutral = []

temp1 = []
temp2 = []
temp3 = []

for line in segmenttest:
    if line[0] == '1':
        classpositive.append(line[1:])
    if line[0] == '0':
        classneutral.append(line[1:])
    if line[0] == '-':
        classnegative.append(line[2:])
        
splitpositive = []
splitnegative = []
splitneutral = []
        
for line in classpositive:
    temp1.append(jieba.cut(line))
for line in classneutral:
    temp2.append(jieba.cut(line))
for line in classnegative:
    temp3.append(jieba.cut(line))
    
i1 = 0
i2 = 0
i3 = 0
for line in temp1:
    splitpositive.append([])
    for seg in line:
        if seg != '\r\n':
            splitpositive[i1].append(seg)
    i1 += 1      
for line in temp2:
    splitneutral.append([])
    for seg in line:
        if seg != '\r\n':
            splitneutral[i2].append(seg)
    i2 += 1
for line in temp3:
    splitnegative.append([])
    for seg in line:
        if seg != '\r\n':
            splitnegative[i3].append(seg)
    i3 += 1


f1 = codecs.open("D:\\textpredition\\emotionanalyse\\positive.txt",'r',encoding='utf-8')
data1 = f1.readlines()
newdata1 = data1[1:]

f2 = codecs.open("D:\\textpredition\\emotionanalyse\\negative.txt",'r',encoding='utf-8')
data2 = f2.readlines()

newdata2 = data2[1:]

segment1 = []
segment2 = []
segment = []

for line in newdata1:
    segment1.append(line.strip(' \r\n'))
for line in newdata2:
    segment2.append(line.strip(' \r\n'))

positive = 0
negative = 0
classpreditpositive = []
classpreditneutral = []
classpreditnegative = []
for line in splitpositive:
    for word in line:
        if word in segment1:
            positive += 1
        if word in segment2:
            negative += 1
    if positive > negative:
        classpreditpositive.append(1)
    positive = 0
    negative = 0
for line in splitneutral:
    for word in line:
        if word in segment1:
            positive += 1
        if word in segment2:
            negative += 1
    if positive == negative:
        classpreditneutral.append(1)
    positive = 0
    negative = 0
for line in splitnegative:
    for word in line:
        if word in segment1:
            positive += 1
        if word in segment2:
            negative += 1
    if positive < negative:
        classpreditnegative.append(1)
    positive = 0
    negative = 0
    
print('rate of positive:',len(classpreditpositive)/len(classpositive))   
print('rate of neutral:',len(classpreditneutral)/len(classneutral))
print('rate of negative:',len(classpreditnegative)/len(classnegative))  


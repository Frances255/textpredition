## 基于词典的中文情感分类
- 工具：PyDev+Anaconda3+jieba
- 准确率：对消极、积极语料的预测准确率约为50%，中性语料准确率为80%
- 所使用的语料来自github，目测是别人爬的微薄评论
- 所使用的词典来自知网的情感词典</br>

### 代码说明</br>
1.导入语料文件并对文本进行处理，去掉换行符和空格
<pre><code>
f = codecs.open("D:\\emotion-analysis\\data\\pnn_annotated.txt",'r',encoding='utf-8')
data = f.readlines()
newdata = []
segmenttest = []
newsegmenttest = []
for line in data:
    newdata.append(line.strip('\r\n'))
for line in newdata:
    segmenttest.append(line.replace('\t',''))
</pre></code>
2. 对语料的语句进行分类，语料中每句开头为1的为积极语句，为0的是中性语句，为-1的是消极语句
<pre><code>
classpositive = []
classnegative = []
classneutral = []
for line in segmenttest:
    if line[0] == '1':
        classpositive.append(line[1:])
    if line[0] == '0':
        classneutral.append(line[1:])
    if line[0] == '-':
        classnegative.append(line[2:])
</pre></code>
3.使用jieba进行分词和一些处理
<pre><code>
temp1 = []
temp2 = []
temp3 = []
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
</pre></code>
4.导入情感词典
<pre><code>
f1 = codecs.open("D:\\textpredition\\emotionanalyse\\positive.txt",'r',encoding='utf-8')
data1 = f1.readlines()
newdata1 = data1[1:]

f2 = codecs.open("D:\\textpredition\\emotionanalyse\\negative.txt",'r',encoding='utf-8')
data2 = f2.readlines()

newdata2 = data2[1:]
</pre></code> 
5.去掉词典文件中的换行符
<pre><code>
segment1 = []
segment2 = []
segment = []

for line in newdata1:
    segment1.append(line.strip(' \r\n'))
for line in newdata2:
    segment2.append(line.strip(' \r\n'))
</pre></code>
6.将分词后的语料中的词和情感词典中的进行对比，判断语句中消极和积极的词个数，相等预测为中性，小于预测为积极，大于预测为消极
<pre><code>
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
</pre></code>
7.计算准确率
<pre><code>
print('rate of positive:',len(classpreditpositive)/len(classpositive))   
print('rate of neutral:',len(classpreditneutral)/len(classneutral))
print('rate of negative:',len(classpreditnegative)/len(classnegative))  
</pre></code>


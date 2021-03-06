# 变位词问题
# 1. 问题描述
变位词是指两个词存在组成字母的重新排列问题。
例如：heart 和 earth、python和typhon
为简化问题，假设两个字符串的长度相同，均为小写。

# 2. 解题目标
写一个bool函数，以两个词为参数，返回这两个词是否为变位词。
$f(S_1,S_2)$ >>> True或False
可以展现同一个问题的不同数量级解法。

# 3.解法比较
## 3.1 解法一：逐字检查
### 3.1.1 解题思路
将字符串 $S_1$ 中的每个字符逐一到 $S_2$ 中寻找相同的字符，如果能找到，就对 $S_2$ 中的该字符进行打钩(避免重复检查)。如果每个字符都能找到对应的字符，则二者是变位词；如果有一个字符没有找到对应字符，则不是变位词。

### 3.1.2 程序技巧
1. 实现打钩标记：将 $S_2$ 中找到的字符设置为**None**
2. 由于字符串为不可变类型，因此将初始的字符串转化为列表

### 3.1.3 算法分析
1. 问题规模：词中包含的字符个数 $n$
2. 主要部分：在于两重循环
外层循环遍历 $S_1$ 的每个字符，将内层循环执行 $n$ 次；
内层循环在$S_2$中寻找字符，每个字符遍历的次数分别为$1，2，…，n$ 中的一次，且各不相同。

总执行次数为 $\sum_{i=1}^ni=1+2+…+n=\frac{n(n+1)}{2}=\frac{n^2}{2}+\frac{n}{2}$
可知数量级为 $O(n^2)$

### 3.1.4 代码
```
def anagram1(s1,s2):
    pos1 = 0
    list2 = list(s2)
    stillOK = True
    while pos1 < len(s1) and stillOK :
        pos2 = 0
        found = False
        while pos2 < len(list2) and not found:  
            if s1[pos1] == list2[pos2]:
                found = True
            else:
                pos2 = pos2 + 1
        if found == True:
            list2[pos2] = None
        else :
            stillOK = False
        pos1 = pos1 + 1
    return stillOK
```



## 3.2 解法二：排序比较
### 3.2.1 解题思路
将两个字符串的每个字母都按照字母顺序进行排序，再比较逐个字符是否相同，如果每个字符都能对应，则为变位词，如果有一个不是则不是。
python → hnopy
hyphon → hnopy

### 3.2.2 算法分析
在排序中使用
```
list1.sort()
```
算法粗看上去，只用到排序后逐一比较字符的一层循环，最多执行$n$次，数量级为$O(n)$。但是sort函数不是没有代价的，如果排序算法采用不同的方式，则运行时间的数量级为$O(n^2)$或$O(nlog(n))$，大于单重循环的$O(n)$
所以在排序比较中，主导算法时间的是排序步骤。因此，本算法的运行数量级为$O(n^2)$或$O(nlog(n))$。

### 3.2.3 代码
```

def anagram2(s1,s2):
  list1 = list(s1)
  list2 = list(s2)
  list1.sort()
  list2.sort()
  stillOK = True
  for i in range(len(s1)):
    if list1[i] != list2[i]:
        stillOK = False
        break
  return stillOK
```

## 3.3 解法三：暴力求解
暴力算法是指穷尽所有可能的组合。
### 3.3.1 解题思路
将$S_1$的所有字符进行全排列，再查看$S_2$是否出现在全排列中。

### 3.3.2 算法分析
1. 困难：产生$S_1$的所有字符的全排列。
$n$个字符进行全排列，根据组合数学的知识，所有可能的结果一共有$n!$个，而$n!$的增长速度比$2^n$还快。
例如，对于20个字符的字符串而言，将会产生$20!=2,432,902,008,176,640,000$ 个结果，即使每微妙处理一个字符串，需要接近8万年的时间去完成。
2. 结论：暴力算法不可行



## 3.4 解法四：计数比较
### 3.4.1 解题思路
对比两个字符串中每个字母出现的频率，如果26个字母每个字母出现的频率都相同，则为变位词。
### 3.4.2 具体做法
1. 为每个词设置一个26个位的计数器，检查每个词，计数器中设定好每个字母出现的次数
2. 比较两个字符串的计数器是否相同，如果都相同则为变位词。
### 3.4.3 算法分析
计数比较中出现了3个循环，但没有嵌套结构。前两个循环用于字符串计数，操作长度等于字符串长度$n$，第3个循环用于计数器比较，操作总次数为26次。所以总操作次数为$2n+26$次，其数量级为$O(n)$。这是一个线性数量级的算法，是4个变位词中性能最优的。

*注：本算法依赖于两个长度为26的计数器，需占用更多的存储空间。牺牲存储空间来换取运行时间，或反之，在选择问题解法的过程中经常出现。需在二者之间进行权衡。

### 3.4.3 代码
## using counting list
```
def anagram4(s1,s2):
  count1 = [0]*26
  count2 = [0]*26
  stillOK = True
  for i in range(len(s1)):
    pos = ord(s1[i]) - ord("a")
    count1[pos] = count1[pos] + 1
  for i in range(len(s2)):
    pos = ord(s2[i]) - ord("a")
    count2[pos] = count2[pos] + 1
  for i in range(len(count1)):
      if count1[i] != count2[i]:
          stillOK = False
  return stillOK
```
## using dictionary
```
def anagram4(s1,s2):
    dict1 = dict()
    dict2 = dict()
    for c in s1:
        if c not in dict1:
            dict1[c] = 1
        else:
            dict1[c] += 1
    for c in s2:
        if c not in dict2:
            dict2[c] = 1
        else:
            dict2[c] += 1
    return dict1 == dict2
            
```


---
layout:     post
title:      剑指offer 41-end
subtitle:   
date:       2020-01-28
author:     WY
header-img: img/post-bg-ios9-web.jpg
catalog: true
tags:
    - 剑指offer
---

#### 41.和为S的连续正数序列
输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序。
题目：小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。但是他并不满足于此,
他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。没多久,他就得到另一组连续正数和为100的序列:18,19,20,
21,22。现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? 
- 滑动窗口
```
def findcountinouss(tsum):
    if target<3:
        return []

    small =1
    big =2
    mid = (tsum+1)//2
    cursum = big+small
    res= []
    while small<mid:
        if cursum == tsum:
            res.append(list(range(small,big+1)))
        while cursum>tsum:
            cursum-=small
            small+=1
            if cursum==tsum:
                res.append(list(range(small,big+1)))
        big+=1
        cursum+=big
```

#### 和为S的两个数字
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。

```
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        if len(array)<2:
            return []
        i,j = 0 ,len(array)-1
        while i<j:
            if tsum == (array[i]+array[j]):
                return [array[i],array[j]]
            elif tsum>(array[i]+array[j]):
                i+=1
            else:
                j-=1
        return []  
```

#### 43.左旋转字符串
对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。
```
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        
        res1 = s[n:]
        xun =s[:n]
        return res1+xun
```
#### 44.翻转单词顺序列
例如，“student. a am I”翻转为“I am a student.”。

思路：按空格切分为数组，依次入栈，再出栈(用空格连接)
```
class Solution:
    def ReverseSentence(self, s):
        # write code here
        a = s.split(' ')
        res = []
        for i in a:
            res.append(i)
        out = []
        for j in range(len(res)):
            out.append(res.pop()+' ')
        
        return ''.join(x for x in out)[:-1]
```

#### 45.扑克牌顺子
一副扑克牌,里面有2个大王，2个小王，从中随机抽出5张牌，如果牌能组成顺子就输出true，否则就输出false。为了方便起见，大小王是0，大小王可以当作任何数字。

```
def isContuin(number):
    if not number:
        return False
    number.sort()
    zerC = number.count(0)
    for i,val in enumerate(nums[:-1]):
        if val!=0:
            if number[i+1]==val:return False
            zerC=zerC-(number[i+1]-val)+1
            if zerC<0:
                return False
    return True

```

#### 46.孩子们的游戏（圆圈中最后剩下的数）
游戏是这样的：首先，让小朋友们围成一个大圈。然后，他随机指定一个数m，让编号为0的小朋友开始报数。
每次喊到m-1的那个小朋友要出列，不再回到圈中，从他的下一个小朋友开始，
继续0...m-1报数....这样下去....直到剩下最后一个小朋友获胜，获胜的小朋友编号多少？(注：小朋友的编号是从0到n-1)

- 递推公式 反推 x' = (x+m)%(cur_n)
```
def lastchild(n,m):
    if n < 1 or m <1:
        return -1
    value =0
    for index in range(2,n+1):
        value
        value = preV
    return value
```

#### 47.求1+2+3+...+n
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

```
class Solution:
    def Sum_Solution(self, n):
        # write code here
        if n<1:
            return 0
        else:
            return n + self.Sum_Solution(n-1)
```
#### 48.不用加减乘除做加法
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
- 虽然知道用位运算，但是python写着实很难受。。。

```
class Solution:
    def Add(self,n1,n2):
        while n2!=0:
            tmp=n1^n2
            n2 = (n1&n2)<<1
            n1 = tmp&0xFFFFFFFF
        return num1 if num1<0xFFFFFFFF else ~(num1^0xFFFFFFFF)

```

#### 49.把字符串转换成整数
将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)

```
class Solution:
    def StrToInt(self, s):
        # write code here
        s = s.strip()
        number ,flag= 0,1
        if not s:
            return 0
        if s[0]=='-':
            s=s[1:]
            flag=-1
        elif s[0]=='+':
            s=s[1:]
            flag=1
        for i in s:
            if i>=0 and i<='9':
                number = 10*number+int(i)
            else:
                return 0
        number = flag*number
        return number
```

#### 50.数组中重复的数字
在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。
```
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        dic ={}
        for i in numbers:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for i in dic:
            if dic[i]>1:
                duplication[0]=i
                return True
        return False
```

#### 51.x
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。

```
class Solution:
    def multiply(self, A):
        # write code here

       # head = [1]
       # tail = [1]
       # for i in range(len(A)-1):
       #     head.append(A[i]*head[i])
        #    tail.append(A[-i-1]*tail[i])
       # return [head[j]*tail[-j-1] for j in range(len(head))]
        n =len(A)
        L = [1]*n
        for i in range(1,n):
            L[i] = L[i-1]*A[i-1]
              
        R = [1]*n
        for j in range(n-2,-1,-1):
            R[j] = R[j+1]*A[j+1]
        B = []
        for i in range(len(A)):
            B.append(L[i]*R[i])
        return B

```

#### 52.正则表达式匹配
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素

- 动态规划dp[i][j]

```
class Solution:
    def match(self,s,p):
        n,m = len(s),len(p)
        dp = [[Flase for i in range(m+1)]for j in range(n+1)]
        dp[0][0]=True

        for c in range(1,m+1):
            if p[c-1]=='*' and c>1:
                dp[0][c]=dp[0][c-2]
        for r in range(1,n+1):
            for c in range(1,m+1):
                if p[c-1]=='.' or p[c-1]==s[r-1]:
                    dp[r][c] =dp[r-1][c-1]
                elif p[c-1]=='*' and c>1:
                    if p[c-2]=='.' or p[c-2]==s[r-1]:
                        dp[r][c] =dp[r][c-2] or dp[r-1][c]
                    else：
                        dp[r][c]=dp[r][c-2]

        return dp[-1][-1]
```

#### 55.链表中环的入口节点
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。

```
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        slow, fast = pHead,pHead
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast==slow:
                fast = pHead
                while fast!=slow:
                    slow=slow.next
                    fast=fast.next
                return fast
        return None
```

#### 56.删除链表中重复的结点
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
```
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        dummy = ListNode(0)
        dummy.next = pHead
        pre = dummy
        cur = pHead
        while cur:
            while cur.next and cur.val==cur.next.val:
                cur=cur.next
            if pre.next == cur:
                pre = pre.next
            else:
                pre.next=cur.next
                
            cur = cur.next
        return dummy.next
```


#### 57.二叉树的下一个结点
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
1、如果该节点有右子树，那么它的下一个节点就是它的右子树的最左侧子节点；

2、如果该节点没有右子树且是父节点的左子树，那么下一节点就是父节点；

3、如果该节点没有右子树且是父节点的右子树，比如i节点，那么我们往上找父节点，找到一个节点满足： 它是它的父节点的左子树的节点。
```
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
def GetNext(node):
    if not node:
        return None
    if node.right:
        res = node.right
        while res.left:
            res=res.left
        return res
    while node.next:
        tmp = node.next
        if tmp.left = node:
            return tmp
        node =tmp
    return None
```

#### 58.对称的二叉树
请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。（leetcode101题）

```
def issy(root):
    def dfs(left,right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val!=right.val:
            return False
        return dfs(left.right,right.left) and dfs(left.left,right.right)
    return dfs(root.left,root.right) if root else True 
```

#### 59.把二叉树打印成多行
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。（leetcode102题）
```
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        res = []
        def dfs(node,index):
            if not node: return
            if len(res)==index:
                res.append([])
            res[index].append(node.val)
            dfs(node.left,index+1)
            dfs(node.right,index+1)
        dfs(pRoot,0)
        return res
```

#### 60.按之字形顺序打印二叉树
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。


```
class Solution:
    def Print(self, pRoot):
        # write code here
        
        # write code here
        res = []
        def dfs(node,index):
            if not node: return
            if len(res)==index:
                res.append([])
            res[index].append(node.val)
            dfs(node.left,index+1)
            dfs(node.right,index+1)
        dfs(pRoot,0)
        out =[]
        for i in range(len(res)):
            if i %2==1:
                out.append(res[i][::-1])
            else:
                out.append(res[i])
        return out
```

#### 61.二叉搜索树的第K个节点
给定一棵二叉搜索树，请找出其中的第k小的结点。例如，（5，3，7，2，4，6，8）中，按结点数值大小顺序第三小结点的值为4。
- 中序遍历

```
class Solution:
    def KthNode(self,root,k):
        if not root or not k:
            return 
        res=[]
        def help(node):
            if len(res)>=k or not node:
                return 
            help(node.left)
            res.append(node.val)
            help(node.right)
        help(root)
        if len(res)<k:
            return 
        return res[k-1]
```

#### 62.滑动窗口的最大值
给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。
```
def maxWin(num,size):
    res = []
    i = 0
    while size>0 and i+size-1<len(num):
        res.append(max(num[i:i+size]))
        i+=1
    return res
```

#### 64.矩阵中的路径
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。 例如，在下面的3 X 4 矩阵中包含一条字符串"bfce"的路径，但是矩阵中不包含"abfb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，
路径不能再次进入该格子。

```
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        judge =[True]*rows*cols
        for i in range(rows):
            for j in range(cols):
                if self.check(matrix,rows,cols,i,j,path,judge):
                    return True
        return False
    
    def check(self,matrix,row,col,i,j,path,jud):
        index = i*col+j
        if not path:
            return True
        if i< 0 or i>=row or j<0 or j >=col or matrix[index]!=path[0] or jud[index]==False:
            return False
        jud[index]=False
        if (self.check(matrix,row,col,i+1,j,path[1:],jud) or 
        self.check(matrix,row,col,i-1,j,path[1:],jud) or 
        self.check(matrix,row,col,i,j+1,path[1:],jud) or 
        self.check(matrix,row,col,i,j-1,path[1:],jud)):
            return True
        jud[index]=True
        return False
``` 
#### 65.机器人的运动范围
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？

```
class Solution:
    def movingCount(self,threshold,rows,cols):
        if rows<1 or cols<1 or threshold<0:
            return 0
        visited = [False] * (rows*cols)
        return self.moving(threshold,rows,cols,0,0,visited)
    def moving(self,threshold,rows,cols,x,y,visited):
        cnt = 0
        if 0<=x<rows and 0<=y<cols and not visited[x*cols+y]:
            if self.calsum(x)+self.calsum(y)<=threshold:
                visited[x*cols+y]=True

                cnt =1 + self.moving(threshold,rows,cols,x+1,y,visited)
                + self.moving(threshold,rows,cols,x-1,y,visited)
                + self.moving(threshold,rows,cols,x,y+1,visited)
                + self.moving(threshold,rows,cols,x,y-1,visited)
        return cnt
    def calsum(self,x):
        ressum=0
        while x!=0:
            while x!=0:
                ressum+=x%10
                x/=10
        return ressum
```
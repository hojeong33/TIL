## 배열 1

### 알고리즘

유한한 단계를 통해 문제를 해결하기 위한 절차나 방법

슈더코드와 순서도로 알고리즘 표현

정확성, 작업량(시간 복잡도 빅-오 표기법 : 실제 걸리는 시간 측정), 메모리 사용량, 단순성, 최적성

### 배열

일정한 자료형의 변수들을 하나의 이름으로 열거하여 사용하는 자료구조

### 정렬

#### 버블 정렬

```python
def BubbleSort(a):
    for i in range(len(a)-1,0,-1):
        for j in ragne(0,i):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
```

[55,7,78,12,43] -> [7,55,12,43,78] ->[7,12,43,55,78]->[7,12,43,55,78]->[7,12,43,55,78]

O(n^2)

#### 카운팅 정렬

```python
def CountingSort(A,B,k):#A: 입력 배열(1 to k) B: 정렬된 배열 #C: 카운트배열
    C=[0]*k
    for i in range(0,len(B)):
        C[A[i]]+=C[i-1]
    for i in range(1,len(C)):
        C[i]+=C[i-1]
    for i in range(len(B)-1,-1,-1):
        B[C[A[i]]-1]=A[i]
        C[A[i]]-=-1
     
```

O(n+k)

#### Baby-gin Game-탐욕

```python
num=456789
c=[0]*12
for i in range(6):
    c[num%10]+=1
    num//=10
i=0
tri=run=0
while i<10:
    if c[i]>=3:
        c[i]-=3
        tri+=1
        continue;
    if c[i]>=1 and c[i+1]>=1 and c[i+2]>=1:
        c[i]-=1
        c[i+1]-=1
        c[i+2]-=1
        run+=1
        continue
    i+=1
if run + tri ==2:print("Baby Gin")
else: print("lose")
```

#### 완전 검색

```python
for i in range(1,4):
    for j in range(1,4):
        if i!=j:
            for k in range(1,4):
                if i!=k and j!=k:
                    print(i,j,k)
                    
```

## 배열 2

2차원 배열 선언

nXm 배열

순회

```python
#행우선
for i in range(len(Array)):
    for j in range(len(Array[i])):
        Array[i][j]
#열우선
for j in range(len(Array[0])):
    for i in range(len(Array)):
        Array[i][j]
#지그재그
for i in range(len(Array)):
    for j in range(len(Array[0])):
        Array[i][j+(m-1-2*j)*(i%2)]
```

#### 델타를 이용한 2차 배열 탐색

```python
dr[-1,1,0,0]
dc[0,0,-1,1]

for r in range(len(ary)):
    for c in range(len(ary[r])):
        for i in range(4):
            testR=r+dr[i]
            testC=c+dc[i]
            test(ary[testR][testC])
```

#### 전치행렬

```python
arr=[[1,2,3][4,5,6][7,8,9]]
for i in range(3):
    for j in range(3):
        if i<j:
            arr[i][j],arr[j][i]=arr[j][i],arr[i][j]
            
```

#### 부분집합 생성하기

```python
bit=[0,0,0,0]
for i in range(2):
    bit[0]=i
    for j in range(2):
        bit[1]=j
        for k in range(2):
            bit[2]=k
            for l in range(2):
                bit[3]=1
                print(bit)
```

```python
arr=[3,6,7,1,5,4]
n=len(arr)
for i in range(1<<n):
    for j in range(n+1):
        if i&(1<<j):
            print(arr[j],end=", ")
    print()
print()
```

#### 순차 검색-정렬되어 있지 않은 경우 O(n)

```python
def sequentialSearch(a,n,key):
    i=0
    while i<n and a[i]!=key:
        i=i+1
    it i<n: return i
    else: return -1
```

#### 순차 검색-정렬되어 있는 경우 O(n) : 실패 반환하는 경우 평균 비교 회수 반으로

```python
def sequentialSearch(a,n,key):
    i=0
    i=i+1
    while i<n and a[i]<key:
        i=i+1
    if i<n and a[i]=key:return i
    else: return -1
    
```



#### 이진 검색(정렬된 상태!!)

 ```python
 def binarySearch(a,key):
     start=0
     end=len(a)-1
     while start<=end:
         middle=(start+end)//2
         if a[middle]==key:
             return True
         elif a[middle]>key:
             end=middle-1
         else:
             start=middle+1
     return false
 ```

#### 재귀 함수 이용

```python
def binarySearch(a,low,high,key):
    if low>high:
        return False
   	else:
        middle=(low+high)//2
        if key==a[middle]:
            return True
        elif key<a[middle]:
            return binarySearch(a,low,middle-1,key)
        else:
            return binarySearch(a,middle+1,high,key)
```



#### 선택 정렬 O(n^2)

```python
def selectionSort(a):
    for i in range(0,len(a)-1):
        min=i
        for j in range(i+1,len(a)):
            if a[min]>a[j]:
                min=j
        a[i],a[min]=a[min],a[i]
```



## string

```python
def atoi(str_input:str)->int:
    ans=0
    for i in range(len(str_input)):
        ans*=10
        ans+=ord(str_input[i])-ord('0')
    return ans
def itoa(int_input:int)->str:
    ans=''
    tmp=int_input
    
    while tmp>0:
        num=tmp%10
        ans+=chr(num+48)
        tmp//=10
    retun ans
```










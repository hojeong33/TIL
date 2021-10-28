## ECMAScript6

### INTRO

#### 세미클론

​	선택적으로 사용가능

#### 코딩 스타일 가이드

​	airbandb

### 변수와 식별자

#### 식별자

​	문자, 달러($), 밑줄(_) 로 시작 , 대소문자 구분,클래스명 외 모두 소문자, 예약어 사용 불가능

​	스타일

		- 카멜 케이스 (camelCase) : 변수, 객체 , 함수에 사용
		- 파스칼 케이스 (PascalCase) : 클래스, 생성자에 사용
		- 대문자 스네이크 케이스 (SNAKE_CASE) : 상수 ( 변경될 가능성이 없는 값을 말함)

#### 변수

​	const : 재할당 할 수 없음, 재선언 불가능, 블록 스코프

​	let : 재할당 할 수 있음, 재선언 불가능, 블록 스코프

​	var : 재할당 & 재선언 가능 ,호이스팅, 함수 스코프



### 타입과 연산자

#### 데이터 타입

 - 원시 타입(Primitive type)
    - 객체가 아닌 기본 타입
    - 변수에 해당 타입의 값이 담김
    - 다른 변수에 복사할 때 실제 값이 복사됨
    - 숫자(Number) 타입 
       - 정수, 실수 구분 없는 하나의 숫자 타입
       - 부동소수점 형식을 따름 (실수 연산 시 오차 발생 가능성 있음)
       - NaN(NOT-A-NUMBER) : 계산 불가능한 경우 반환값
   - 문자열(String) 타입
     - 텍스트 데이터 나타내는 타입
     - "",''는 파이썬과 동일
     - 템플릿 리터럴(Template Literal)
       -  따음표 대신 `(백키) 사용 가능
       - `${}` 형태로 사용 가능
   - undefined 
     - 값이 없음을 나타냄 
     - 자동
   - null
     - 값이 없음을 나타냄
     - 의도적 표현
     - typeof null -> object
   - Boolean Type
     - true,false 소문자 표현( 파이썬과 다름 )
     - false: undefined,null,-0,0,NaN, 빈 문자열
 - 참조 타입(Reference type)
   	- 객체 타입의 자료형
      	- 변수에 해당 객체의 참조 값이 담김
   	- 다른 변수에 복사할 때 참조 값이 복사됨
   	- 함수, 배열, 객체

#### 연산자

- 할당 연산자
  - 파이썬과 동일 + (++,--)
- 비교 연산자
  - 결과값을 boolean으로 반환
- 동등 비교 연산자(==)
  - '1004'==1004 ->true
  - 1==true -> true
- 일차 비교 연산자(===)
  - 타입과 값이 모두 일치하는 지 엄격한 비교
- 논리 연산자
  - and : &&
  - or : ||
  - not : !
  - 단축 평가 지원
    - false&&true=>false
    - true||false=>true
- 삼항 연산자(Ternary Operator)
  - 조건 ? 참 :거짓 ( 파이썬: 참 if 조건 else 거짓)

### 조건문과 반복문

#### 조건문

- if

  - if,else if,else

- switch

  - case

  - ```js
    switch(month){
        case 3:
        case 4:
        case 5: {
            console.log('봄')
            break
        } 
        case 6: 
        case 7:
        case 8:{
            console.log('여름')
            break
        }
         case 9:
        case 10:
        case 11:{
            console.log('가을')
            break
        }
        default : {
            console.log('겨울')
        }
      }
    ```

  - break가 없으면 default만날때가지 실행한다

#### 반복문

- while

  - ```js
    while(condition){
        //do something
    }
    ```

- for

  - ```js
    for (initialization;condition;expression;){
        //do something
    }
    ```

- for ~ in

  - ```js
    for (variable in object){
        //do something
    }
    ```

  - 객체 속성을 순회할 때

- for~ of

  - ```js
    for(variable of iterables){
        //do something
    } 
    ```

  - 반복 가능한 객체를 순회할 때 

### 함수

#### 함수

- 함수 선언식

  - ```js
    function name(args){
        //do something
    }
    ```

  - 익명 함수 불가능

  - 호이스팅 가능

- 함수 표현식

  - ```js
    const myFunction =function(args){
        //do something
    }
    ```

  - 익명 함수 가능

  - 호이스팅 불가능

- 기본 인자 

  - 인자 작성 시 '='문자 뒤 기본 인자 선언 가능
  - 누락시 undefined

#### 화살표 함수

- function 키워드 생략 가능

- 함수의 매개변수가 단 하나라면 '()' 생략 가능

- 함수의 몸통인 표현식이 한 줄이라면 '{}' 생략 가능

- ```js
  const arrow = name=> `hello ${name}`
  ```

  

### 배열과 객체

#### 배열

- 참조 타입

- 배열의 길이 array.length

- 메소드
  - reverse : 원본 배열 반대로 정렬
  - push& pop : 마지막 추가, 마지막 뽑기
  - unshift &shift: 가장 앞에 추가 , 가장 앞 뽑기
  - includes: 있으면 참 없으면 거짓
  - indexOf : 처음으로 찾은 인덱스 , 없을 시 -1
  - join([separator]) : 생략 시 , 로 구분
  
- callback 함수 : 어떤 함수의 내부에서 실행될 목적으로 인자로 넘겨받는 함수를 말함

  - element: 배열의 요소, index : 배열 요소의 인덱스, array: 배열 자체

  - forEach : 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행 

    - ```js
      array.forEach((element,index,array) => {
          //do something
      })
      ```

  - map :  콜백 함수의 반환 값을 요소로 하는 새로운 배열 반환

    - ```js
      array.map((element,inex,array) => {
          //do something
      })
      ```

  - filter : 콜백 함수의 반환 값이 참인 요소들만모아서 새로운 배열을 반환

    - ```js
      array.filter((element,inex,array) => {
          //do something
      })
      ```

  - reduce :콜백 함수의 반환 값들을 하나의 값(acc)에 누적 후 반환

    - ```js
      array.reduce((acc,element,index,array)=>{
          //do something
      }, initialValue)
      ```

  - find : 콜백 함수의 반환 값이 참이면 해당 요소를 반환 

    - 찾는 값이 없으면 undefined 반환

      ```js
      array.find((element,inex,array) => {
          //do something
      })
      ```

  - some : 배열의 요소 중 하나라도 판별 함수를 통과하면 참을 반환

    - ```js
      array.some((element,inex,array) => {
          //do something
      })
      ```

  - every : 배열의 모든 요소가 판별 함수를 통과하면참을 반환

    - ```js
      array.every((element,inex,array) => {
          //do something
      })
      ```

#### 객체

 - 속성의 집합
 - key
   	-  문자열 타입만 가능
      	- 이름에 띄어쓰기 ㄱ등의 구분자가 있으면 따음표 묶어서 표현 -> 하나면 '' 생략 가능
- value
  - 모든 타입 가능
- 객체 관련 ES6 문법
  - 속석명 축약
    - key와 할당할 변수가 같으면 생략 가능
  - 메서드명 축약
  - 계산된 속성
  - 구조 분해 할당
- JSON 
  - 문자열
  - JSON.parse() : 자바스크립트 객체로
  - JSON.stringify() : JSON 형태로


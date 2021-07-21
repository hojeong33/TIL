## 함수

높은 재사용성 + 유지보수 용이

- pow(a,b) : a의 b제곱

- import statistics #수학통계함수

  statistics.pstdev(values) --표준편차 구하는 함수

- 하나의 객체만 리턴함!

  복수 return?-->튜플형태로 하나의 객체 리턴 

  return 없이?-->Nonetype 객체 반환

- argument(인자)  vs parameter(매개변수)

  parameter : 함수에 입력으로 전달된 값을 받는 변수 ex) def my_func(a,b):

  argument : 함수 호출시 전달되는 입력값 ex) my_func(1,2)

- 기본 인자 : def add(a,b=0)

- 키워드 인자 : add(x=2,y=5)--> 위치가 달라도 키워드를 읽기 때문에 상관 x

- *objects : 정해지지 않은 여러 개의 인자 처리

- 가변 인자 리스트 : def add(*args)---> 인자들이 튜플로 묶여 처리됨

- 가변 키워드 인자 : def family(**kwargs)--->키워드 인자들을 딕셔너리로 묶여 처리됨 

  

- 함수 스코프 :  전역(global): 코드 어디서든 , 지역(local): 함수 내에서

- 이름 검색 : 작은거-->큰거 순 (Local > Enclosed > Global > Built-in)

- global 변수 : local에서 global 변수 접근해서 수정 가능

  global에 나열된 이름은 global 앞에 등장 안됨, 매개변수, for루프 대상 , 함 수 정의에 사용 x

  (global은 선언되지 않은 변수를 만들 수 있음 그러나 nonlocal은 안됨)

- nonlocal 변수 : 전역을 제외한 자기 상위 스코프의 변수에 접근

- 함수로 값을 바꾸고자 한다면 항상 인자로 넘기고 리턴 값을 사용하는것을 추천

- unpacking

  ```python
  def get_numbers(a,*args):
      return a, args
  
  print(get_numbers(1))
  #(1,())
  print(get_numbers(1,2,3))
  #(1,(2,3))
  x=[1,2,3]
  print(get_numbers(x))
  #([1,2,3],())
  print(get_numbers(*x)) #인자로 들어갈때 *를 쓰면 언패킹
  #(1,(2,3))
  print(get_numbers(*[1,2,3]))
  ```

- 함수 정의 주의 사항

  올바른 순서: my_info(x,y,*args,**kwargs)

  ## 재귀함수

  - 팩토리얼 함수
  - 피보나치 함수 

  ## 예외와 예외처리

  - 문법 에러(Syntax Error)

  예외(exception): 실행 도중 예상치 못한 상황을 맞이하면 프로그램 실행이 멈춤 

  ​                             즉 실행준 감지되는 에러를 예외, 문법적으로 틀리지 않음

  - ZeroDivisionError : 0으로 나누고자 할 때
  - NameError : namespace 이름이 없음
  - TypeError : Type 불일치, argument 누락, argument 개수 초과, argument type 불일치
  - ValueError : 타입은 올바르나 값이 적절하지 않거나 없는 경우
  - IndexError : 인덱스가 존재하지 않거나 범위를 벗어난 경우
  - KeyError : 해당 키가 존재하지 않는 경우
  - ModuleNotFoundError : 존재하지 않는 module
  - ImportError :  모듈은 있으나 존재하지않는 클래스/함수를 가져오는 경우
  - KeyboardInterrupt : 임의로 프로그램을 종료하였을 때
  - Indentation Error : 들여쓰기 에러

  ### 예외처리

  try:

  except (에러종류):

  복수예외처리

  try:

  except(에러종류,에러종류):

  또는

  except에러:
  except에러:

  except Exception: (모든 에러를 잡음)

  

  else

  - try 문에서 예외가 발생하지 않으면 실행

  finally

  - 예외 여부와 상관없이 실행

  

  except 에러 as 변수명:

  print(f'{변수명}, 오류가 발생함')

  

  ### 예외 발생시키기

  raise <표현식>(메세지)

  assert <표현식>,<메세지> false인경우  AsserrionError가 발생 ----> -O 디버깅 코드 지워짐

  

  EAFP : 허락보다 용서가 쉽다 ( 예외 처리를 활용하여 검사 수행하지 않고 일단 실행하고 예외처리를 진행하는 스타일)--> 파이썬 코드가 문제없이 실행될 것을 전제로 코드를 실행

  LBYL : 도약하기 전에 봐라(어떤 것이 실행하기전에 에러가 날만한 요소들을 조건문으로 검사하고 수행)

  


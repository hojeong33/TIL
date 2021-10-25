HTTP

HyperText Transfer Protocol 

웹 상에서 컨텐츠를 전송하기 위한 약속

웹에서 이루어지는 모든 데이터 교환의 기초

request(요청)

response(응답)



Stateless : 상태가 없음

Connectless : 연결이 없음(서버와의 연결 x)

 쿠키와 세션을 통해 서버 상태를 요청과 연결하도록 함



#### 요청

- HTTP request methods

  GET, POST, PUT DELETE

- HTTP request status codes

1. informational

2. successful
3. redirection
4. client error
5. server error

- 웹에서 리소스 식별

​	HTTP 요청의 대상을 리소스



#### URI(통합자원식별자)	

- URL(Uniform Resource Locator) 

​		통합 자원 위치

​		네트워크 상에 자원이 어디 있는지 알려주기 위한 약속

​		과거에는 실제 자원의 위치를 나타냈지만 현재는 추상화된 의미론적인 구성

​		'웹 주소', '링크' 라고도 불림

- URN(Uniform Resource Name)

​		통합 자원 이름

​		url과 달리 자원의 위치에 영향을 받지않는 유일한 이름 역할을 함

- URI의 구조

  - Scheme(protocol) ex) https

  - Host(Domain name) ex) www.example.com

    IP address 직접 사용 가능 ex) 구글 142.251.42.142

  - Port

    웹 서버 상의 리소스에 접근하는데 사용되는 기술적인 문

    HTTP 80, HTTP 443

  - Path

    웹 서버 상의 리소스 경로

    옛날에는 물리적인 실제 위치를 나타냄 -> 추상화 형태의 구조 표현

  - Query(Identifier)

    Query String Parameters

    웹 서버에 제공되는 추가적인 매개 변수

    & 로 구분되는 key- value

  - Fragment(Anchor)

    브라우저에게만 알려주고 서버로 요청이 보내지지는 않음

    

#### API (Application Programming Interface)

​	프로그래밍 언어가 제공하는 기능을 수행할 수 있게 만든 인터페이스

​	CLI,GUI,API..

​	Web API

​		웹 애플리케이션 개발에서 다른 서비스에 요청을 보내고 응답을 받기 위해 정의된 명세

​		OPEN API

​	응답 데이터 타입

​		HTML, XML, JSON



#### REST

REpresentational State Transfer

네트워크 구조 원리의 모음( 자원을 정의하고 자원에 대한 주소를 지정하는 전반적인 방법)

REST 원리를 따르는 시스템을 RESTful이랑 용어로 지칭함

자원을 정의하는 방법에서 고안

방법

- 자원 
  - URI
- 행위 
  - HTTP method
- 표현 
  - 자원과 행위를 통해 궁극적으로 표현되는 결과물
  - JSON으로 표현된 데이터를 제공

#### JSON

- JavaScript Object Notation
- 단순 문자열
- 사람이 읽거나 쓰기 쉽고 기계가 파싱(해석, 분석)하고 만들어내기 쉬움
- 파이썬의 dictionary 자바스크립의 object처럼 C계열의 언어가 갖고 있는 자료구조로 쉽게 변화할 수 있는 key- value 형태의 구조를 갖고 있음
- 규칙
  1. 정보는 URI 로 표현
  2.  자원에 대한 행위는 http method로 표현
-  지키지 않더라도 동작 여부에 큰 영향을 미치지는 않음



더미 데이터 

python manage.py seed articles --number=20



#### Serialization

직렬화

####  Django Rest Framework(DRF)

Web API 구축을 위한 강력한 Toolkit을 제공하는 라이브러리


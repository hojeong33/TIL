## HTML & CSS

### HTML

Hyper Text : 텍스트의 정보가 다중으로 연결 

​                       하이퍼링크를 통해 한 문서에서 다른 문서로 즉시 접근 가능

Markup : 텍스트에 역할을 부여함(의미 부여)

Language :데이터의 구조를 명시, 단순하게 데이터 표현(저장x, 조건x, 반복 x)

웹 컨텐츠의 '의미'와 '구조' 부여

 #### HTML 기본 구조 -html

<head> 정보를 담고 있으며 브라우저에 나타나지 않는다

<body> 브라우저 화면에 나타나는 정보로 실제 내용에 해당

메타데이터 - 문서 정보를 먼저 전달해줌 ( 링크 보낼 시 밑에 해당 Open Graph를 보여줌)

DOM트리 - 객체 지향 표현

요소 : 태그 & 내용 <h1>(여는 태그)contents</h1>(닫는 태그)

속성 : (태그안에 사용하는 속성) <a 속성="값"></ 공백 x 쌍따음표 사용!

MDN Web Doc

<!-- 주석 -->

/* */

Non semantic 요소 div,span 의미x는 태그  -> 시멘틱 태그  header(의미 부여)

#### HTML 문서 구조화

그룹 컨텐츠 

텍스트 관련 요소 

form 태그 : 서버에서 처리될 데이터 제공하는 역할

- action 어디로 보낼지
- method  

input 태그 : form 안에 들어감/ 

### CSS

Cascading Style Sheets

인라인/내부참조/외부참조

#### CSS Selector(선택자)

#id 선택

.클래스 선택

#### CSS 적용 우선순위

!important

인라인>id선택자>class선택자>요소선택자

#### css 상속

자식:직계만 div > span

자손: 전부 div span

#### css 크기 단위

- px(픽셀) : 고정적임
- % : 가변적임

- em : 바로 위 부모 요소에 대한 상속 , 배수 단위 상대적인 사이즈
- rem : 최상위 요소의 사이즈를 기준으로 배수 단위 (html)
- viewport : 화면 비율에 따라 사이즈 결정

### css 선택자 심화

일반 형제 결합자 : p ~ span 

- P태그 뒤에 존재하는 span태그 

인접 형제 결합자 : p + span

- p태그 뒤에 바로 존재하는 span태그만 

## Box Model

- Margin : 테두리 바깥 여백 (top,right,bottom,left) (상화/좌우, 상/좌우/하,상/우/하/좌)
- Border : 테두리 (width,style,color) ex) 2px dashed black(순서 상관 x)
- Padding : 테두리 안쪽 여백
- Content : 글이나 이미지 등의 내용 

* box-sizing : border-box;  보더박스로 설정 해야함
* 마진 상쇄 : 큰 마진 값으로 겹치게 되는 현상
* 모든 요소는 네모!!!!!!!!



### css display

- 블록
  - div / ul, ol li/ p/ hr/ form
  - margin -right:auto -> 좌측정렬, left:auto -> 우측정렬 둘다시 :중간 정렬
- 인라인
  - 줄바꿈일어나지 않음 , width, height,마진 탑, 마진 바틈 지정 x line-height 지정
  - span/a/img/input,label/b,em
  - text-align:left-> 좌측 정렬, text-align:right->우측정렬 center-> 가운데 정렬

- display : inline-block
- display : none 차지하던 공간이 사라진다 vs hidden (보이지 않지만 공간은 있다)



### css position

- static : 좌측상단부터 시작
- relative : 상대적
  - 자기 자신의 static 위치를 기준으로 이동, 다른것들이 자기 위치로 이동x
- absolute : 절대적
  - 집 나간 자식!! 레이아웃에서 공간을 차지하지 않음 -> 다른 것들이 위치로 이동 o
  - 새로운 부모/조상 요소를 기준으로 (없으면 body(문서의 좌측 끝) )
- fixed : 고정적
  - 우리가 보는 viewport를 기준으로 이동
  - 스크롤 시에도 항상 같은 곳에 위치

top:50, -> 위에서 아래로 50

left:50 -> 왼쪽에서 오른쪽으로 50


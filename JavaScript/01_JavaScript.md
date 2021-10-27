## JavaScript 

브라우저 화면을 동적으로 만들기 위함

브라우저를 조작할 수 있는 유일한 언어

팀 버너스리 : www,url...

브랜던 아이크 : javascript...

크롬 압도적인 속도, 강력한 개발자 도구, 웹 표준 

#### DOM(Document Object Model)

- 해석 - pashing
- 조작 -document
- 조작 순서- 선택-> 변경
- 보이는 화면
- 상속 구조 
  - EventTartget
  - Node
  - Element
  - Document
  - HTMLElement
- 선택
  - Document.querySelector(selector) : css 선택자
  - Document.querySelectorAll(selector) : 여러개 선택 css선택자를 문자열로 받음 -> Nodelist 반환
- 변경
  - Document.createElement()
  - Element.append() : 특정 부모 자식 마지막 자식으로 추가, 여러개 추가, 반환값 없음
  - Node.appendChild() : 특정 부모 자식 마지막으로 추가, 한번에 하나, Node만 추가 가능, 추가된  Node 객체 반환
  - Node.innerText : tag 인식 안됨 ,raw text
  - Element.innerHTML : tag 인식 됨

#### BOM(Browser Object Model)

- 조작-window

#### EVENT

- Event handler 
  - target.addEventListener(type, listener[,options])
- 취소
  - preventDefault()
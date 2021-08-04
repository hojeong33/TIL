# 02 Web-CSS Layout&Bootstrap

## Float

- 정상 흐름으로부터 빠져 **텍스트 및 인라인 요소**가 즈 주위를 감싸 요소의 좌,우측을 따라 배치하는 것 
- none :기본값
- left: 요소를 왼쪽
- right: 요소를 오른쪽

## Flexbox

- 공간배분, 정렬 기능을 제공하기 위한 1차원(단방향) 레이아웃 모델 설계
- 요소
  - Flex Container(부모요소) : 대상을 담고있는 레이아웃
    - display : flex or inline-flex
    - 정렬될 것들을 컨트롤함
  - Flex item(자식요소) : 정렬 대상 (컨텐츠) 
- 축
  - main axis(메인축) 기본값: x축 왼쪽->오른쪽
  - cross axis(교차축) : 메인축을 수직으로 지나는 축 기본값:위에서 아래
- 속성
  - 배치 방향 설정 flex-direction (메인축)
    - row(default), row-reverse, column(위에서 아래), column-reverse
  - 메인축 방향 정렬 justify-content
  - 교차축 방향 정렬 align-items , align-self, align-content
    - content : 여러줄
    - items : 한줄
    - self : flex item 개별 요소
  - flex-wrap : 넘치면 다음줄

div.container>div.item.item${$} * 10

## Bootstrap

- spacing  
  	-  mt-1 (margin-top) rem 0.25 ,4px---> mt-5 rem 3, 48px
  	- mx-0( x 축 margin 0) mx-auto( 수평중앙정렬)
  	- p~(padding) s(left), e(right), x(right left), y(top bottom)
- Flexbox in Bootstrap
  	- class d-flex 로 정의되어있음

## Grid system

- flexbox 로 제작됨
- container, rows, column
- 12개의 column
- 6개의 grid breakpoints

### Grid options

- xs  : col-
- sm : col-sm-
- md
- lg
- xl
- xxl



​	

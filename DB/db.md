## db

relational database : key와 value 들의 간단한 관계를 표 형태로 정리한 데이터베이스

스키마: 데이터베이스에서 자료의 구조, 표현방법, 관계 등 전반적인 명세를 기술한 것

테이블: 열(컬럼/필드)과 행(레코드/값)의 모델을 사용해 조직된 데이터 요소들의 집합

기본키: 각 행의 고유한 값-> 반드시 설정해야 한다



relational database management system

mysql,sqlite,postgresql,oracle,ms sql



sql (structured query language): 데이터 관리를 위해 설계된 특수 목적으로 프로그래밍 언어

ddl: (definition) :관계형 데이터베이스 구조를 정의하기 위한 명령어 create,drop,alter

dml:(manipulation) : 데이터를 저장,조회,수정,삭제 위한 명령어 insert,select,delete,update

dcl: (control): 사용자의 권한 제어 명령어 grant,revoke,commit,rollback



sqlite 켜는 법: sqlite3 tutorial.squlite3

AUTOINCREMENT -> 재사용 방지
/*
[DB 3일차(3/7) 학습내용]

DML : 데이터조작언어
데이터 삽입 / 갱신 / 삭제 / 조회

테이블 = 관계/개체 (원자형태 => 정규화)
행(row) : 레코드, 튜플, 카디널리티
열(column) : 속성, 필드, 차수
키(key) : 주키(PK), 후보키, 대체키, 외래키(FK), 슈퍼키(복합키)

1. 데이터 삽입
INSERT INTO 테이블명 (열이름리스트)  VALUES (값리스트);

INSERT INTO 테이블명 (열이름리스트)
	 VALUES (값리스트),
	 VALUES (값리스트),
	 VALUES (값리스트);

2. 데이터 갱신
UPDATE 테이블명 SET 열=값 WHERE 조건;

3. 데이터 삭제
DELETE FROM 테이블명 WHERE 조건;

4. 데이터 조회
SELECT [ALL | DISTINCT] 열이름 리스트  (5)
	FROM 테이블명   (1)
	WHERE 검색조건(들)  (2)
	GROUP BY 열이름     (3)
	HAVING 검색조건(들) (4)
	ORDER BY 열이름1 [ASC┃ | DESC], 열이름2 [ASC┃ | DESC]  (6)

검색조건에서 사용되는 연산자
 (1) 비교 : = != > < >= <=
 (2) 범위 : between A and B, not between A and B
 (3) 멤버 :  in (  ), not in( )
 (4) NULL :  is NULL , is not NULL
 (5) 논리 :  and, or, xor
 (6) 패턴매칭 : LIKE '패턴'  => 와일드카드 _  %
*/


/*
-- 데이터베이스 삭제
drop database IF exists shopdb;
drop database if exists testdb1;
drop database if exists testdb2;
drop database if exists testdb;
-- 또는 drop schema testdb;

-- DB 스키마 생성
create schema bookshopdb default character set utf8mb4;


-- 생성되는 위치 지정 (혹은 bookshopdb.publisher)
use bookshopdb;

-- 테이블 생성 : publisher
create table publisher(
	pubNo varchar(10) not null,
    pubName varchar(30) not null,
	primary key (pubNo)
);

-- 테이블 생성 : book - 도서(book), 출판사(publisher), 회원(memeber), 주문(order)
create table book (
	bookNo varchar(10) not null primary key,
	bookName varchar(30) not null,
    bookPrice int default 10000 check(bookPrice > 1000),
    bookDate date,
    pubNo varchar(10) not null,
    foreign key (pubNo) references publisher(pubNo)
);

-- describe publisher;
-- describe book;

drop table book;

create table book (
	bookNo varchar(10) not null primary key,
	bookName varchar(30) not null,
    bookPrice int default 10000 check(bookPrice > 1000),
    bookDate date,
    pubNo varchar(10) not null,
    constraint FK_book_publisher foreign key (pubNo) references publisher(pubNo)
);

-- 학사관리시스템 DB: schooldb 만들기
create schema schooldb default character set utf8mb4;

use schooldb;

-- 테이블 생성, student, department, professor, course, scores
create table department(
	depCode char(10) not null primary key,
    depName varchar(15) not null,
    depTel varchar(15)
);

create table student(
	stdId varchar(10) not null primary key,
    stdName varchar(15) not null,
    stdYear int default 1 check(stdYear >= 1 and stdYear <=4),
    stdAddr varchar(40),
    stdBirth date,
    depCode char(10) not null,
    constraint FK_std_depart foreign key(depCode) 
				references department(depCode)
);

create table professor(
	proNo char(10) not null primary key,
    proName varchar(30) not null,
    proPhone char(20),
    depCode char(10) not null,
	constraint FK_pro_depart foreign key(depCode) 
			references department(depCode)
);

create table course(
	courseCode char(10) not null primary key,
    courseName varchar(30) not null,
    courseCredit int default 3 check(courseCredit >= 1 and courseCredit <= 6),
    proNo char(10) not null,
    constraint FK_course_professor foreign key(proNo)
			references professor (proNo)
);

-- 주키가 복합키(슈퍼키)로 설정
create table scores(
	stdId varchar(10) not null,
    courseCode char(10) not null,
    score int default 0 not null check(score>=0 and score<=100),
    grade char(10) not null, 
    constraint PK_scores_std_course primary key (stdId, courseCode),
    constraint FK_scores_student foreign key (stdId) references student(stdId),
    constraint FK_scores_course foreign key(courseCode) references course(courseCode)
);
*/

create table board(
	boardNo int auto_increment not null primary key,
    # auto_increment 하나씩 증가시킬 때
    boardTitle varchar(30) not null,
    boardAuthor varchar(20) not null,
    boardContent varchar(100) not null
);

-- 테이블 변경(alter)
-- alter table board auto_increment = 100;
-- set @auto_increment_increment = 2;

-- set @count = 0;
-- update board set boardNo = @count:=@count+1
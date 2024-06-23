use bookshopdb;

/*
-- select * from book;

alter table book 
	add column bookAuthor varchar(30);

describe book;

-- update book SET bookAuthor = '홍길동' where (`bookNo` = '1');

-- <테이블의 모든 행(레코드)의 모든 컬럼을 조회>
-- select * from book;

-- <테이블의 지정한 컬럼들을 조회>
-- 원하는 필드명만 확인
-- select bookName, bookAuthor, bookPrice from book;
select bookAuthor from book;

-- <distict 키워드 사용시 중복된 행을 하나만 제시> / 중복된 내용은 제거함 (성춘향 1번 나옴)
select distinct bookAuthor from book;

-- <조건에 맞는 검색>
-- select [all | distict] 필드명1, 필드명2 ... from 테이블명 where 조건식;

-- where 조건식 
-- 1) 비교 : =, <=>, <, >, <=, >=, !=
-- 2) 범위 : between
-- 3) 리스트에 포함 여부 : in, not in 
-- 4) NULL : is null, is not null
-- 5) 논리 : and, or, xor
-- 6) 패턴매칭 : like  예)%프린터% 앞뒤에 뭐가 있든 상관없이 프린터가 들어있으면 인식

-- 1) 비교 :  =, <=>, <, >, <=, >=, !=
-- 저자가 홍길동인 도서의 도서명, 저자 조회
select bookName, bookAuthor from book
		where bookAuthor = '홍길동';  

-- 가격이 20000 이상인 도서명, 가격, 저자 조회
select bookName, bookPrice, bookAuthor from book
		where bookPrice >= 20000;

-- 가격이 20000이상 25000 이하인 도서명, 가격, 저자 조회
select bookName, bookPrice, bookAuthor from book
		where bookPrice >= 20000 and bookPrice <= 25000;
        
-- 가격이 20000이상 25000 이하인 도서명, 가격, 저자 조회
select bookName, bookPrice, bookAuthor from book
		where 20000 <= bookPrice <= 25000;

-- 출판일이 2022년 1월 1일 이후인 도서명, 출간일 조회
select bookName, bookDate from book
		where bookDate >= '2022-01-01';


-- 2) 범위 : between and | not between and
-- 가격이 20000이상 25000 이하인 도서명, 가격, 저자 조회
select bookName, bookPrice, bookAuthor from book
		where bookPrice between 20000 and 25000;
        
        
-- 출판일이 2023년도에 출간한 도서명, 출간일 조회
select bookName, bookDate from book
		where bookDate between '2023-01-01' and '2023-12-31';


-- 3) 리스트에 포함 여부 : in, not in

-- 출판사 번호가 1과 2인 도서의 정보 조회
select * from book
	where pubNo in (1,2);
    
select * from book
	where pubNo not in (3);
    

-- 4) NULL : is null, is not null

update bookshopdb.book
	set bookAuthor = '' #null이 아닌 공백문자
    where (`bookNo`=1); 

select * from book
 	where bookAuthor = ''; #null ''공백문자

-- 저자가 null인 레코드 조회
update bookshopdb.book
	set bookAuthor = null
    where (`bookNo`=1); 

select * from book
	where bookAuthor is null;
    
-- 저자가 null이 아닌 레코드 조회
update bookshopdb.book
	set bookAuthor = null
    where (`bookNo`=5); 

select * from book
	where bookAuthor is not null;
*/


-- 5) 논리 : and, or, xor, not
-- 저자가 성춘향이고 가격이 20000원 이상인 도서 도회
select * from book
	where bookAuthor = '성춘향' and bookPrice >= 20000;
    
-- 저자가 성춘향 또는 가격이 20000원 이상인 도서 도회 (공통된 조건 포함)
select * from book
	where bookAuthor = '성춘향' or bookPrice >= 20000;

-- 저자가 성춘향이거나 가격이 20000 이상인 도서 조회 (공통된 조건 미포함)
-- xor 둘다 포함하지 않는 경우 
select * from book
	where bookAuthor = '성춘향' xor bookPrice >= 20000; 


-- 6) 패턴매칭 : like '패턴' 
-- 예) %프린터% 앞뒤에 뭐가 있든 상관없이 프린터가 들어있으면 인식

/* 
[와일드 카드 문자] :
			% : 0개 이상의 문자를 가진 문자열
            _ : 단일문자 ('_'의 개수 만큼의 문자로 구성)

문자열 연산 예.
			'홍%' : '홍'으로 시작하는 문자열 검색
			'%길%' : '길'을 포함하는 문자열 검색 ('길' 앞과 뒤에 아무 문자열이나 포함 가능)
            '%동' : '동'으로 끝나는 문자열 검색
            '___' : 3개의 문자로 구성된 문자열
*/

-- 도서 테이블에서 '길동'이라는 이름을 가진 도서 검색 ('%길동')
select * from book
		where bookAuthor like '%길동';
        
-- product 테이블에서 제품명이 6글자인 모든 행 조회
select * from product
		where prdName like '______';

-- product 테이블에서 제품명에 'TV'가 들어있는 제품 조회
select * from product 
		where prdName like '%TV%';

-- book 테이블에서 도서명에 '데이터'가 들어있는 도서 조회
select * from book
		where bookName like '%데이터%';
        
-- book 테이블에서 도서명에 '데이터'로 시작하는 도서 조회
select * from book
		where bookName like '데이터%';

-- book 테이블에서 도서명에 '데이터'로 끝나는 도서 조회
select * from book
		where bookName like '%데이터';

-- book 테이블에서 도서명에 '데이터'가 들어있지 않은 도서 조회
select * from book
		where bookName not like '%데이터%';

/*
-- DML : Data Manipulation Language 
-- bookshopdb 사용: 데이터 삽입
use bookshopdb;

-- publisher 테이블에 데이터 삽입
-- insert into 테이블명(필드이름1, 필드2, ...) values (값1, 값2 ..);

insert into publisher (pubNo, pubName) values('1', '강남출판사');
insert into publisher (pubNo, pubName) values('2', '강북출판사');
insert into publisher (pubNo, pubName) values('3', '서초출판사');

-- 테이블 조회 : select문
select * from publisher;
*/

use bookshopdb;
insert into book (bookNo, bookName, bookPrice, bookDate, pubNo)
		values ('1', '자바', 20000, '2020-12-12', '1');
        
insert into book (bookNo, bookName, bookPrice, bookDate, pubNo)
		values ('2', '자바스크립트', 15000, '2020-1-12', '2');
        
insert into book (bookNo, bookName, bookPrice, bookDate, pubNo)
		values ('3', '통계학개론', 30000, '2021-2-2', '2'),
			   ('4', '알고리즘', 25000, '2023-5-30', '3'),
			   ('5', '데이터분석', 35000, '2023-11-20', '2'),
			   ('6', '웹프로그래밍', 18000, '2019-09-15', '1');
               
insert into book
		values ('7', '데이터베이스', 35000, '2021-7-10', '1'),
			   ('8', '알고리즘', 30000, '2020-01-30', '3'),
			   ('9', '데이터전처리', 25000, '2024-1-10', '2'),
			   ('10', '머신러닝', 38000, '2023-12-15', '1');
               
select * from book;




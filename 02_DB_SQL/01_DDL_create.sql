# 한줄 주석
-- 한줄 주석 : -- / #
-- workbench에서 주석을 위한 단축키 ctr + \


-- 스키마 생성 & 삭제 
-- drop schema testdb1;
-- drop database testdb2;

-- create schema testdb1 default character set utf8mb4;
-- create database testdb2 default character set utf8mb4;


-- 상품 테이블 생성 : 필드명 - 제품아이디, 제품명, 제품가격, 제조사 
-- 제약 조건 : 기본키 - 제품 아이디 NotNull

use testdb1;

/* -- 여러줄 주석
create table product(
	prdID varchar(10) not null primary key,
    prdName varchar(30) not null FK_book_publisher,
    prdPrice int,
    prdCompany varchar(30)
    );


create table product1(
	prdID varchar(10) not null,
    prdName varchar(30) not null,
    prdPrice int,
    prdCompany varchar(30),
    primary key(prdID)
    );
    
create table product2(
	prdID varchar(10) not null,
    prdName varchar(30) not null,
    prdPrice int,
    prdCompany varchar(30),
    constraint PK_product2_prdID primary key(prdID)
    );
    
    
    create table testdb1.publisher(
		pubNo varchar(10) not null primary key,
        pubName varchar(30) not null
	);
    
    
    
    -- 외래키 (foreign key) 생성 및 제약 조건 설정
    create table book(
		bookNo varchar(10) not null primary key,
        bookName varchar(30) not null,
        bookPrice int default 10000 check(bookprice > 1000),
        # 제약 조건 최소 1000원 이상
        bookDate date,
        pubNo varchar(10) not null,
        constraint FK_book_publisher foreign key (pubNo) references publisher (pubNo)
    );
    */
    
   --  describe book; 
  --  describe publisher;
  
  /*
  [참조 무결성 제약 조건]
  외래키를 기존 테이블에 값을 삽입, 삭제, 수정시  실행 불가
  => 외래키를 갖는 값이 수정 불가하도록 지정되어 있음
  => onUpdate이 Restrict로 지정되어 있어서
  
  외래키를 주키로 하는 테이블에서 수정해야 함
  
  외래키를 이용하는 테이블 삭제 시:
  => 외래키를 사용하는 테이블을 먼저 삭제하고, 
	외래키를 주키로 하는 테이블을 그 다음에 삭제
  */
  
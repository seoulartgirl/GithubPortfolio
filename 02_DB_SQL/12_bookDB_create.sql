/*
1. bookdb 생성
2. Table Data Import Wizard를 이용하여 테이블 생성
     : publisher, book, booClient, bookSale
3. 테이블 변경 : 데이터 형식, 제약조건(PK, FK)
*/
/*
-- 1. bookdb 생성
drop database if exists bookdb;
create schema bookdb character set utf8mb4;

-- 2. Table Data Import Wizard를 이용하여 테이블 생성

-- 3. 테이블 변경 :publisher 데이터 형식, 제약조건(PK, FK)
*/
use bookdb;
alter table publisher
	modify pubNo varchar(10) not null,
    modify pubName varchar(20),    
    add constraint PK_publisher_pubNo 
		primary key (pubNo);

desc publisher;

alter table book
	modify bookNo varchar(10) not null,
    modify bookName varchar(20),
    modify bookAuthor varchar(30),
    modify bookDate date,
    modify bookStock int,
    modify pubNo varchar(10) not null,
    add constraint PK_book_bookNo 
		primary key (bookNo),
    add constraint FK_book_publisher
		foreign key (pubNo) references publisher (pubNo);
        
desc book;

alter table bookClient
	modify clientNo varchar(10) not null,
    modify clientName varchar(30),
    modify clientPhone varchar(13),
    modify clientAddress varchar(50),
    modify clientBirth date,
    modify clientHobby varchar(30),
    modify clientGender varchar(1),
    add constraint PK_bookClient_clientNo 
		primary key (clientNo);

desc bookClient;
        
alter table bookSale
	modify bsNo varchar(10) not null,
    modify bsDate date,
    modify clientNo varchar(10) not null,
    modify bookNo varchar(10) not null,
    add constraint PK_bookSale_bsNo 
		primary key (bsNo),
    add constraint FK_bookSale_client
		foreign key (clientNo) references bookClient (clientNo),
	add constraint FK_bookSale_book
		foreign key (bookNo) references book (bookNo);
        
desc bookSale;
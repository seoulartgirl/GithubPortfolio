#1. DB 생성
-- drop database if exists bookdb;
-- create schema bookdb default character set utf8mb4;
/*
#2. 
use bookdb;
alter table publisher
	modify pubNo varchar(10) not null primary key,
    modify pubName varchar(20);

use bookdb;
alter table book
	modify bookNo varchar(10) not null,
    modify bookName varchar(20),
    modify bookAuthor varchar(30),
	modify bookPrice int,
    modify bookDate varchar(10),
    modify bookstock int,
    modify pubNo varchar(10) not null,
	add constraint PK_book_bookNo primary key(bookNo),
	add constraint PK_book_pubNo foreign key(pubNo) 
			references publisher(pubNo);
        
-- desc book;
-- select * from book;
            
            
alter table bookClient
	modify clientNo varchar(10) primary key not null,
    modify clientName varchar(30),
    modify clientPhone varchar(13),
    modify clientAddress varchar(50),
    modify clientBirth varchar(10),
    modify clientHobby varchar(30),
    modify clientGender varchar(1);

alter table bookSale
	modify bsNo varchar(10) not null primary key,
    modify bsDate date,
    modify bsQty int,
    modify clientNo varchar(10) not null,
    modify bookNo varchar(10) not null,
	add constraint PK_bookSale_clientNo foreign key(clientNo) 
			references bookClient(ClientNo),
	add constraint PK_bookSale_bookNo foreign key(bookNo) 
			references book(bookNo);
            
desc bookSale;
*/

//*
alter table publisher 
		add constraint primary key(pubNo),
		modify column pubNo varchar(10) not null,
        modify column pubname varchar(20);
*/
/*
alter table book
		modify bookNo varchar(10) not null primary key,
		modify bookName varchar(20),
        modify bookAuthor varchar(30),
        modify bookDate Date,
        modify pubNo varchar(10) not null,
        add constraint FK_book_publisher foreign key(pubNo) references publisher(pubNo);
*/
/*
alter table bookclient
		modify clientNo varchar(10) not null primary key,
        modify clientName varchar(30),
        modify clientPhone varchar(13),
        modify clientAddress varchar(50),
        modify clientBirth date,
        modify clientHobby varchar(30),
        modify clientGender varchar(1);
*/
/*
alter table booksale
		modify bsNo varchar(10) not null primary key,
        modify bsDate date,
        modify clientNo varchar(10) not null,
        modify bookNo varchar(10) not null,
        add constraint FK_sale_client foreign key(clientNo) references bookclient(clientNo),
        add constraint FK_sale_book foreign key(bookNo) references book(bookNo);
*/		
-- -3-
-- 1
select bookNo, bookName, pubname
		from book
        join publisher on book.pubNo = publisher.pubNo;
        
-- 2
select bookName, bookAuthor, pubName
		from book
		join publisher on book.pubNo = publisher.pubNo
        where pubName = '서울 출판사';
        
 -- 3       
select distinct book.bookname 
		from book
		join publisher on book.pubNo = publisher.pubNo
        join booksale on book.bookNo = booksale.bookNo
        where pubName = '정보출판사' and booksale.bsQty >= 1;
        
-- 4        
select clientName, bookName, bookPrice, bsQty
		from bookclient
        join booksale on booksale.clientNo = bookclient.clientNo
        join book on book.bookNo = booksale.bookNo
        where book.bookPrice >= 30000;
        
 -- 5
 select bookName, clientName, clientGender, clientAddress
		from book
        join booksale on book.bookNo = booksale.bookNo
        join bookclient on bookclient.clientNo = booksale.clientNo
        where bookName = '안드로이드 프로그래밍'
        order by clientName;
        
-- 6	
select sum(BK.bookPrice * BS.bsQty) as '총 매출액'
		from book BK
        join booksale BS on BK.bookNo = BS.bookNo
        join publisher on BK.pubNo = publisher.pubNo
        where pubName = '도서출판 강남';
        
-- 7        
select bsDate, pubName, bookName, bookPrice, bsQty, bsQty * bookPrice as 주문액
		from book B
        join booksale BS on B.bookNo = BS.bookNo
        join publisher on B.pubNo = publisher.pubNo
        where pubName = '서울 출판사';
        
-- 8
select B.bookNo, B.bookName, sum(bsQty) as '총 주문수량'
		from book B
        join booksale BS on B.bookNo = BS.bookNo
        group by bookNo;
        
-- 9
select BC.clientName, sum(BS.bsQty * B.bookPrice) as '총구매액'
		from bookclient BC
        join booksale BS on BS.clientNo = BC.clientNo
		join book B on B.bookNo = BS.bookNo
        group by BC.clientName
		having sum(BS.bsQty * B.bookPrice) >= 100000;
        
-- 10
select BC.clientName, BS.bsDate, B.bookName, BS.bsQty, P.pubName
		from book B
		join booksale BS on BS.bookNo = B.bookNo
        join publisher P on B.pubNo = P.pubNo
        join bookclient BC on BC.clientNo = BS.clientNo
        where P.pubName = '도서출판 강남'
        order by BC.clientName;

-- -4-
-- 1
#join문 사용
select sum(BS.bsQty) as '총구매량'
	from bookClient BC
    join bookSale Bs
    on BC.clientNo = BS.clientNo
    where BC.clientName = '호날두';

#서브쿼리문 사용
select sum(BS.bsQty) as '총구매량'
		from booksale BS
        where clientNo = (select clientNo from bookclient BC
						where BC.clientName = '호날두');
        
-- 2
select clientName
		from bookclient
        where clientNo in (select clientNo from booksale
                        where bookNo in (select bookNo from book
                                        where pubNo = (select pubNo from publisher
                                                        where pubName = '정보출판사')));
        
-- 3
select clientName
	from bookclient
	join booksale BS on BS.clientNo = BC.clientNo
    group by BC.clientName
    having max(BS.bsQty) > (select max(BS.bsQty)
			from booksale
			where clientNo = (select clientNo from bookclient 
								where clientName='베컴'));

-- 4 
select sum(bsQty) as '총판매량'
	from booksale
    where clientNo in (
		select clientNo
			from bookclient
            where clientAddress = '서울');
    
-- 5
select clientName from bookclient where clientNo in 
	(select clientNo from booksale where bookNo in 
		(select bookNo from book where pubNo in
			(select pubNo from publisher where pubName='정보출판사')));
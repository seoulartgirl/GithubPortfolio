/*
	테이블 결합 :  UNION | UNION ALL | INNER JOIN | OUTER JOIN
*/

use bookshopdb;
/*
select * from book
	where pubNo = '1'
union
select * from book
	where pubNo = '2';

-- 내부조인(inner join)
-- 형식1 : select ~ from 테이블1, 테이블2 where 테이블1.컬러명 = 테이블2.컬럼명

select book.pubNo, pubName, bookName, bookAuthor, bookPrice
	from book, publisher
    where book.pubNo = publisher.pubNo
    
*/

/*
-- 형식2: join
-- from 테이블1 [inner] join 테이블2 on 테이블1. 컬럼명 = 테이블2.컬럼명
-- bookClient와 bookSale을 조인하여 clientName 제시

select bookClient.clientNo, bookClient.clientName, bookSale.bsQty
	from bookClient
    join bookSale
    on bookClient.clientNo = bookSale.clientNo;

use bookdb;
select BC.clientNo, BC.clientName, BS.bsQty
	from bookClient BC
    join bookSale BS
    on BC.clientNo = BS.clientNo;
  
select *
	from bookClient BC
    inner join bookSale BS
    on BC.clientNo = BS.clientNo;

select distinct BC.clientNo, BC.clientName
	from bookClient BC
    inner join bookSale BS
    on BC.clientNo = BS.clientNo
    order by BC.clientName;
    
-- 고객별로 총주문수량을 계산하여 총주문수량의 내림차순으로 고객번호, 고객이름, 총주문수량 조회
select distinct BC.clientNo, BC.clientName, sum(BS.bsQty) as '총주문수량'
	from bookClient BC
    inner join bookSale BS
    on BC.clientNo = BS.clientNo
    group by BC.clientNo
    order by 총주문수량 desc;

-- 주문한 도서(bookSale)의 고객명(bookClient)과 도서명(book) 출력
select BC.clientName, B.bookName
	from bookSale BS
    inner join bookClient BC on BS.clientNo = BC.clientNo
    inner join book B on BS.bookNo = B.bookNo;

-- 주문한 도서(bookSale)의 고객명(bookClient)과 도서명(book), 도서가격, 주문량 출력
select BS.bsNo, BS.bsDate, BC.clientNo, BC.clientName, B.bookName, B.bookPrice, BS.bsQty
	from bookSale BS
    inner join bookClient BC on BS.clientNo = BC.clientNo
    inner join book B on BS.bookNo = B.bookNo;
 
-- 주문한 도서(bookSale)의 고객명(bookClient)과 도서명(book), 도서가격, 주문량 출력
select BS.bsNo, BS.bsDate, BC.clientNo, BC.clientName, 
		B.bookName, B.bookPrice, BS.bsQty, 
        B.bookPrice * BS.bsQty as 주문액
	from bookSale BS
    inner join bookClient BC on BS.clientNo = BC.clientNo
    inner join book B on BS.bookNo = B.bookNo;

-- 주문한 도서(bookSale)의 고객명(bookClient)과 도서명(book), 도서가격, 주문량 출력
-- 주문액 내림차순으로 정렬 후 Top3 조회
select BS.bsNo, BS.bsDate, BC.clientNo, BC.clientName, 
		B.bookName, B.bookPrice, BS.bsQty, 
        B.bookPrice * BS.bsQty as 주문액
	from bookSale BS
    inner join bookClient BC on BS.clientNo = BC.clientNo
    inner join book B on BS.bookNo = B.bookNo
    order by 주문액 desc
    limit 3;


-- 주문한 도서(bookSale)의 고객명(bookClient)과 도서명(book), 도서가격, 주문량 출력
-- 2019년 이후 주문한 내역 조회
select BS.bsNo, BS.bsDate, BC.clientNo, BC.clientName, 
		B.bookName, B.bookPrice, BS.bsQty, 
        B.bookPrice * BS.bsQty as 주문액
	from bookSale BS
    inner join bookClient BC on BS.clientNo = BC.clientNo
    inner join book B on BS.bookNo = B.bookNo
    where BS.bsDate >= '2019-01-01'
    order by 주문액 desc;
	*/
    
   -- 외부조인(outer join) :
--  공통된 속성을 매개로 결합하되 정보가 없는 레코드도 추가
-- 1) 좌측 외부조인(left outer join) : 좌측의 테이블 정보 유지

select *
	from bookClient BC
		left outer join bookSale BS
        on BS.clientNo = BC.clientNo;

-- 2) 우측 외부조인(right outer join) : 우측의 테이블 정보 유지

select *
	from bookClient BC
		right outer join bookSale BS
        on BS.clientNo = BC.clientNo;

-- 3) 완전 외부조인(full outer join) : 두 테이블 정보 유지

select *
	from bookClient BC
		left outer join bookSale BS
        on BS.clientNo = BC.clientNo
union
select *
	from bookClient BC
		right outer join bookSale BS
        on BS.clientNo = BC.clientNo;        
	

-- 구매이력이 없는 회원의 정보 조회
select *
	from bookClient BC
		left outer join bookSale BS
        on BS.clientNo = BC.clientNo
	where BS.clientNo is null
    order by BC.clientBirth;
*/    
-- 도서 중 한번도 판매된 적 없는 도서 출력
select *
	from book B
		left outer join bookSale BS
        on B.bookNo = BS.bookNo
	where BS.clientNo is null;
	
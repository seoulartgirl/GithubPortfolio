/*
집계함수 : max(필드명), min(), sum(), avg(), round(), count(), count(*)
*/

use bookshopdb;

select count(prdPrice) as '총 제품수',
	sum(prdPrice) as 가격총액,
	round(avg(prdPrice),1) as 평균가격,
    #round 소수점 한자리까지 보여주기
    min(prdPrice) as 최저가,
    max(prdPrice) as 최고가
	from product;
    
select count(bookAuthor) as '총 저자명',
	count(*) as '총 도서수', #전체 행의 수
	min(bookPrice) as 최저가,
    max(bookPrice) as 최고가
    from book;
    
-- 노트북이 들어있는 단어 개수 세기
select count(prdName) from product
    where prdName like '%노트북%';
    
select prdName from product
    where prdName like '%노트북%';
    
/*
	그룹별 집계 : group by / having
    select 집약키필드명, 집계함수적용, ... 
		from where 조건
		group by 집약키필드명;
    
    group by에 사용하는 필드 => 집계를 위한 키, 집약키
*/

select * from book
	order by pubNo;

select pubNo, count(pubNo), sum(bookPrice) 
	from book
	group by pubNo;
    
select * from productorder;

-- productorder 테이블에서 고객별 주문 총액과 평균 주문액 출력
select customer_id, 
	count(quantity) as 주문횟수, 
    sum(quantity) as 주문총액,
    avg(quantity) as 평균주문
    
	from productorder
	group by customer_id
    with rollup;
    -- order by 주문총액;
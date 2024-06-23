use bookshopdb;

-- having절은 group by의 조건

select pubNo, count(*) as '도서 수 합계'
		from book
        where bookPrice >= 25000
        group by pubNo
        having count(*) >= 2
        order by pubNo desc;
        #또는 order by '도서 수 합계' desc;
        

/* 참고: 위 group by를 따로 따로 했을 때 
select count(*) from book
	where pubNo = '1';
select count(*) from book
	where pubNo = '2';
select count(*) from book
	where pubNo = '3';
*/

/*
# 연습문제
#1. 도서 테이블에서 가격순으로 내림차순 정렬, 
#도서명, 저자, 가격 출력 (가격이 같으면 저자 순으로 오름차순 정렬)
select bookName, bookAuthor, bookPrice 
			from book
            order by bookPrice desc, bookAuthor;
            
#2. 도서 테이블에서 저자에 '길동'이 들어가는 도서의 총 재고 수 계산하여 출력
select count(*) from book 
	where bookAuthor like '%길동';
    
#2-1. 도서 테이블에서 저자에 '길동'이 들어가는 도서의 가격 총액 계산하여 출력
select sum(bookPrice) as '가격합계' from book 
	where bookAuthor like '%길동%';

#3. 도서 테이블에서 '서울출판사' 도서 중 최고가와 최저가 출력
alter table book add(bookPub varchar(30));

update book
			set bookPub = '서울출판사'
            where bookNo in (1,2,3);

select bookName, bookPub, bookPrice from book
	where bookPub like '%서울출판사';
    
#3. 도서 테이블에서 '서초출판사' 도서 중 최고가와 최저가 출력
select bookName, bookPub, bookPrice from book
	where pubNo = '3';
    
select max(bookPrice) as '최고가', min(bookPrice) as'최저가 '
	from book
    where pubNo = '3';
*/

#4. 도서 테이블에서 출판사별로 총 재고 수량과 평균 재고수량 계산하여 출력
# 총 재고수량으로 내림차순 정렬
select count(*) as '총 재고수량', avg(count(*)) as '평균 재고수량'
		from book
        group by bookPub
        order by count(*) desc; 
        
#4-1. 제품 주문 테이블에서 고객별로 총주문량과 평균 주문량을 계산하여 고객 번호 순으로 출력
select customer_id, sum(quantity) as '총주문수량', round(avg(quantity)) as '평균주문량'
	from productorder
    group by customer_id
    having 평균주문량 >= 3
    order by 평균주문량 desc;


#5. 도서판매 테이블에서 고객별로 총 주문 수량과 총 주문 건수 출력. 
# 단 주문건수가 2 이상인 고객만 해당
select customer_id, sum(quantity) as '총주문수량', count(*) as '총주문건수'
		from productorder
        where quantity >=2
        group by customer_id;

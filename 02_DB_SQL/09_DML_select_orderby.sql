/*
정렬(sort): 
	select from where order by 필드명 [asc|desc];
    asc가 디폴트 (입력 안하면)

use bookshopdb;

select * from book
	order by bookName;
    
select * from book
	order by bookPrice;

select * from book
	order by bookDate desc;
    
select * from book
	order by bookAuthor desc;

-- ascii : 48 ~ 57 => 숫자
-- ascii : 65 ~ 90 => 알파벳 대문자
-- ascii : 97 ~ 122 => 알파벳 소문자

-- select * from book order by bookName;


select * from book
	order by (case when ascii(substring(bookName, 1)) between 48 and 57 then 3
				when ascii(substring(bookName, 1)) < 122 then 2
                else 1
                end);
         
-- 정렬 기준 : 두 가지 이상인 경우
select * from book
	order by (case when ascii(substring(bookName, 1)) between 48 and 57 then 3
				when ascii(substring(bookName, 1)) < 122 then 2
                else 1
                end), bookName;

-- 조회 개수 제한 : limit n(숫자) | 숫자 2개 줄 경우 - limit 시작인덱스, 개수
select * from book
	order by bookName
    limit 3;
    
select * from book
	order by bookName
    limit 3, 5;


-- 정렬 기준 : 여러개
select bookName as '도서명', bookAuthor as '저자' , bookPrice as '가격', pubNo as '출판사' from book
		order by pubNo, bookPrice desc;
*/
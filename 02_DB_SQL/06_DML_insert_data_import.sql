-- table data import wizard를 이용하여 테이블 생성

-- 1. Navigator에서 DB 선택하고 우클릭하여 [Table Data import wizard 선택]
-- 2. 임포트 하려는 데이터 경로 선택
-- 3. 테이블 이름과 피드명, 데이터 형식 수정 선택
-- 4. 데이터 임포트 실행
-- 5. 테이블 생성 확인

-- desc bookshopdb.product;
-- 파일을 임포트 하면 제약 조건이 없

use bookshopdb;

alter table product
	modify prdNo varchar(10) not null;
    
alter table product 
	add constraint PK_product_prdNo primary key(prdNo);
    
alter table product
	modify prdName varchar(20),
    modify prdMaker varchar(30),
    modify prdColor varchar(10),
    modify ctgNo varchar(10);
desc product;

/*
연습문제. productorder.csv 파일을 임포트하여
productOrder 테이블을 생성하고,
데이터 형식을 변경하시오.
- pk는 order_id, 데이터 형식은 int
- FK는 product_id (product table의 prdNo)
*/    
 
 alter table productorder 
	modify order_id int not null,
	modify customer_id varchar(10) not null,
    modify product_id varchar(10) not null,
    modify quantity int not null,
    modify price int not null,
    modify order_time datetime not null;

alter table productorder
	add constraint PK_prdOrder_orderid primary key (order_id),
    add constraint FK_prdOrder_product foreign key (product_id)
		references product (prdNo);
    
desc productorder;

select * from productorder;
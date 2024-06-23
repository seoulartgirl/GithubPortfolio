#1. 데이터 베이스를 생성하시오
-- drop database if exists marketdb;
-- create schema marketdb default character set utf8mb4;

#2. 테이블 정의 및 생성, 데이터 입력시 insert문 활용
/*
use marketdb;
create table memberType(
	membertype_id int not null primary key,
    membertype varchar(5) not null
);

use marketdb;
insert into memberType
		values('1', '보통 회원'),
			  ('2', '할인 회원');
              

create table customer(
	customer_id int not null primary key,
    customer_name varchar(45) not null,
	birthday date,
    membertype_id int not null,
    constraint FK_customer_membertype_id foreign key (membertype_id) references memberType (membertype_id)
);

use marketdb;
insert into customer
		values('1', '김바람', '1984-06-24', '2'),
			  ('2', '이구름', '1990-07-16', '1'),	
              ('3', '박하늘', '1976-03-09', '2'),
		      ('4', '강산', '1991-05-04', '1'),
			  ('5', '유바다', '1993-04-21', '2');

create table product (
	product_id int not null primary key,
    product_name varchar(20) not null,
    stock int default 0 check(stock>=0),
    price int default 0 check(price>=0)
);

insert into product
		values('1', '약용 입욕제', '100', '70'),
			  ('2', '약용 핸드솝', '23', '700'),	
              ('3', '천연 아로마 입욕제', '4', '120'),
		      ('4', '거품 목욕제', '23', '120');


create table productOrder(
	order_id int not null primary key,
    customer_id int not null,
    product_id int not null,
    quantity int not null,
    price int not null,
    order_time datetime,
    constraint FK_productOrder_customer_id foreign key(customer_id) references customer(customer_id),
    constraint FK_productOrder_product_id foreign key(product_id) references product(product_id)
);

insert into productOrder
		values('1', '4', '1', '12', '840', '2019-10-13 12:01:34'),
			  ('2', '5', '3', '5', '600', '2019-10-13 18:11:05'),
			  ('3', '2', '2', '2', '1400', '2019-10-14 10:43:54'),
			  ('4', '3', '2', '1', '700', '2019-10-15 23:15:09'),
			  ('5', '1', '4', '3', '360', '2019-10-15 23:37:11'),
			  ('6', '5', '2', '1', '700', '2019-10-16 01:23:28'),
			  ('7', '1', '4', '2', '300', '2019-10-18 12:42:50');


select * from memberType;
select * from customer;
select * from product;
select * from productOrder;


-- alter table productOrder.order_id auto_increment=1;

#3-1. 고객 테이블에 성별, 나이, 전화번호 컬럼 추가, 성별은 F/M 형식 입력되게 하고 나이는 0 이상이 입력되도록
alter table marketdb.customer 
		add (cus_gen varchar(3) check(cus_gen = 'F' or cus_gen='M'), cus_age int check(cus_age>=0), cus_tel varchar(20));

#3-2. 고객 테이블에 데이터 3개 정도 삽입
use marketdb;
insert into customer (customer_id, customer_name, birthday, membertype_id, cus_gen, cus_age)
		values('6', '김바람', '1984-06-24', '2', 'M', 20),
			  ('7', '이구름', '1990-07-16', '1', 'F', 23),	
              ('8', '박하늘', '1976-03-09', '2', 'F', 18);

#3-3 고객명이 홍길동인 고객의 전화번호 수정, 값은 임의의 번호로
update customer set cus_tel = '010-1111-1111' where customer_name ='홍길동';

#3-4 나이가 20살 미만인 고객 삭제
delete from customer where cus_age < 20;

#3-5 고객 테이블에서 고객명, 생년월일, 성별 조회
select customer_name, birthday, cus_gen from customer;

#3-6 고객 테이블에서 주소만 검색하여 조회 (중복되는 주소는 한번만 출력)
select distinct customer_address from customer;

#3-7 고객 테이블에서 취미가 '축구'이거나 '등산'인 고객의 고객명, 취미 조회
select customer_name, customer_hobby from customer
	where customer_hobby='축구' or customer_hobby='등산';
*/